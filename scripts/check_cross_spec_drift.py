#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ssl
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.request import urlopen

import yaml

from vocab_utils import ROOT, iter_terms, load_yaml


DEFAULT_ODPG_SCHEMA = "https://opendataproducts.org/odpg-v1.0/schema/odpg.yaml"
DEFAULT_ODPC_SCHEMA = "https://opendataproducts.org/odpc-v1.0/schema/odpc.yaml"
DEFAULT_REPORT = ROOT / "cross-spec-drift" / "odpv-cross-spec-drift.md"
ODPC_HELPER_DEFINITIONS = {"LanguageString", "ExtensionProperties"}


@dataclass(frozen=True)
class DriftRow:
    source: str
    spec_term: str
    odpv_match: str
    status: str
    notes: str


def load_schema(source: str) -> dict[str, Any]:
    if source.startswith(("http://", "https://")):
        context = None
        try:
            import certifi

            context = ssl.create_default_context(cafile=certifi.where())
        except ImportError:
            context = ssl.create_default_context()
        with urlopen(source, timeout=30, context=context) as response:  # noqa: S310 - schema URL is user/config controlled.
            text = response.read().decode("utf-8")
    else:
        text = Path(source).read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ValueError(f"{source} did not contain a YAML mapping")
    return data


def schema_examples(schema: dict[str, Any], object_name: str, property_name: str) -> list[str]:
    definitions = schema.get("$defs", schema.get("definitions"))
    if not isinstance(definitions, dict):
        raise ValueError("Could not find $defs or definitions in ODPG schema")
    try:
        examples = definitions[object_name]["properties"][property_name]["examples"]
    except KeyError as exc:
        raise ValueError(f"Could not find $defs.{object_name}.properties.{property_name}.examples") from exc
    if not isinstance(examples, list) or not all(isinstance(item, str) for item in examples):
        raise ValueError(f"{object_name}.{property_name}.examples must be an array of strings")
    return examples


def schema_definitions(schema: dict[str, Any]) -> dict[str, Any]:
    definitions = schema.get("$defs", schema.get("definitions"))
    if not isinstance(definitions, dict):
        raise ValueError("Could not find $defs or definitions in schema")
    return definitions


def odpv_lookup() -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    terms_by_id: dict[str, dict[str, Any]] = {}
    alias_to_id: dict[str, str] = {}
    for _section, term in iter_terms(load_yaml()):
        term_id = term["id"]
        terms_by_id[term_id] = term
        aliases = term.get("alsoKnownAs", {}).get("en", [])
        if isinstance(aliases, list):
            for alias in aliases:
                alias_to_id.setdefault(alias, term_id)
    return terms_by_id, alias_to_id


def compare_terms(
    spec_name: str,
    source: str,
    terms: list[str],
    terms_by_id: dict[str, dict[str, Any]],
    alias_to_id: dict[str, str],
) -> list[DriftRow]:
    rows: list[DriftRow] = []
    for term in terms:
        if term in terms_by_id:
            rows.append(
                DriftRow(
                    source=source,
                    spec_term=term,
                    odpv_match=term,
                    status="Exact match",
                    notes=f"{spec_name} term is an official ODPV id.",
                )
            )
            continue

        alias_match = alias_to_id.get(term)
        if alias_match:
            rows.append(
                DriftRow(
                    source=source,
                    spec_term=term,
                    odpv_match=alias_match,
                    status="Alias match",
                    notes=f"{spec_name} term maps through ODPV alias.",
                )
            )
            continue

        rows.append(
            DriftRow(
                source=source,
                spec_term=term,
                odpv_match="",
                status="Possible drift",
                notes="No exact ODPV id or alias match found.",
            )
        )
    return rows


def build_odpg_rows(odpg_schema_source: str) -> list[DriftRow]:
    schema = load_schema(odpg_schema_source)
    terms_by_id, alias_to_id = odpv_lookup()
    node_terms = schema_examples(schema, "node", "type")
    edge_terms = schema_examples(schema, "edge", "type")
    return [
        *compare_terms("ODPG", "Node type", node_terms, terms_by_id, alias_to_id),
        *compare_terms("ODPG", "Edge type", edge_terms, terms_by_id, alias_to_id),
    ]


def build_odpc_rows(odpc_schema_source: str) -> list[DriftRow]:
    schema = load_schema(odpc_schema_source)
    terms_by_id, alias_to_id = odpv_lookup()
    definitions = schema_definitions(schema)
    terms = [term for term in definitions if term not in ODPC_HELPER_DEFINITIONS]
    return compare_terms("ODPC", "Schema definition", terms, terms_by_id, alias_to_id)


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|")


def display_source(source: str) -> str:
    if source.startswith(("http://", "https://")):
        return source
    resolved = Path(source).resolve()
    try:
        return str(resolved.relative_to(ROOT))
    except ValueError:
        pass
    try:
        return str(Path("..") / resolved.relative_to(ROOT.parent))
    except ValueError:
        return source


def render_rows(spec_name: str, rows: list[DriftRow]) -> list[str]:
    possible_drifts = [row for row in rows if row.status == "Possible drift"]
    lines = [
        f"## {spec_name} to ODPV",
        "",
        f"- Checked terms: {len(rows)}",
        f"- Possible drifts: {len(possible_drifts)}",
        "",
    ]

    if possible_drifts:
        lines.append("Possible drift detected. Review rows marked `Possible drift` and either add an ODPV term, add an ODPV alias, or update the source specification.")
    else:
        lines.append("No unresolved drift detected.")

    lines.extend(
        [
            "",
            f"| {spec_name} source | {spec_name} term | ODPV match | Status | Notes |",
            "|---|---|---|---|---|",
        ]
    )
    for row in rows:
        match = f"`{row.odpv_match}`" if row.odpv_match else ""
        lines.append(
            "| "
            + " | ".join(
                [
                    markdown_escape(row.source),
                    f"`{markdown_escape(row.spec_term)}`",
                    match,
                    markdown_escape(row.status),
                    markdown_escape(row.notes),
                ]
            )
            + " |"
        )
    return lines


def render_report(odpg_rows: list[DriftRow], odpc_rows: list[DriftRow], odpg_schema_source: str, odpc_schema_source: str) -> str:
    rows = [*odpg_rows, *odpc_rows]
    possible_drifts = [row for row in rows if row.status == "Possible drift"]
    lines = [
        "# ODPV Cross-Spec Drift Report",
        "",
        "This report compares published Open Data Product family schemas against the canonical ODPV vocabulary.",
        "",
        f"- ODPG schema: `{display_source(odpg_schema_source)}`",
        f"- ODPC schema: `{display_source(odpc_schema_source)}`",
        "- ODPV source: `source/vocab/odpv.yaml`",
        f"- Checked terms: {len(rows)}",
        f"- Possible drifts: {len(possible_drifts)}",
        "",
    ]

    if possible_drifts:
        lines.append("Possible drift detected. Review rows marked `Possible drift` and either add an ODPV term, add an ODPV alias, or update the source specification.")
    else:
        lines.append("No unresolved drift detected.")

    lines.extend(["", *render_rows("ODPG", odpg_rows), "", *render_rows("ODPC", odpc_rows)])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare published family schema terms against ODPV.")
    parser.add_argument("--odpg-schema", default=DEFAULT_ODPG_SCHEMA, help="URL or path to ODPG YAML schema")
    parser.add_argument("--odpc-schema", default=DEFAULT_ODPC_SCHEMA, help="URL or path to ODPC YAML schema")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT, help="Markdown report path")
    parser.add_argument("--check", action="store_true", help="Fail if the existing report is out of sync")
    args = parser.parse_args()

    odpg_rows = build_odpg_rows(args.odpg_schema)
    odpc_rows = build_odpc_rows(args.odpc_schema)
    report = render_report(odpg_rows, odpc_rows, args.odpg_schema, args.odpc_schema)

    if args.check:
        if not args.report.exists():
            print(f"Missing cross-spec drift report: {args.report}", file=sys.stderr)
            return 1
        current = args.report.read_text(encoding="utf-8")
        if current != report:
            print(f"Cross-spec drift report is out of sync: {args.report}", file=sys.stderr)
            return 1
        print("Cross-spec drift report is in sync")
        return 0

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(report, encoding="utf-8")
    rows = [*odpg_rows, *odpc_rows]
    possible_drifts = sum(1 for row in rows if row.status == "Possible drift")
    print(f"Wrote {args.report} terms={len(rows)} possibleDrifts={possible_drifts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
