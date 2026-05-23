#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import ssl
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import urlopen

import yaml

from vocab_utils import ROOT, iter_terms, load_yaml


DEFAULT_ODPG_SCHEMA = "https://opendataproducts.org/odpg-v1.0/schema/odpg.yaml"
DEFAULT_ODPC_SCHEMA = "https://opendataproducts.org/odpc-v1.0/schema/odpc.yaml"
DEFAULT_ODPS_SCHEMA = "https://opendataproducts.org/v4.1/schema/odps.yaml"
DEFAULT_REPORT_DIR = ROOT / "cross-spec-drift"
DEFAULT_REPORT_NAME = "odpv-cross-spec-drift.md"
LEGACY_REPORT = DEFAULT_REPORT_DIR / DEFAULT_REPORT_NAME
RUN_TIMESTAMP_RE = re.compile(r"^(?:- )?Last drift detection run: `([^`]+)`$", re.MULTILINE)
REPORT_IMAGE = "../source/images/odpv-cross-spec-drift.png"
ODPC_HELPER_DEFINITIONS = {"LanguageString", "ExtensionProperties", "CatalogMeta"}
ODPS_COMPONENT_MAPPINGS = {
    "contract": "DataContract",
    "dataQuality": "DataQuality",
}


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


def compare_mapped_terms(
    spec_name: str,
    source: str,
    terms: list[str],
    terms_by_id: dict[str, dict[str, Any]],
    alias_to_id: dict[str, str],
    mappings: dict[str, str],
) -> list[DriftRow]:
    rows: list[DriftRow] = []
    for term in terms:
        mapped = mappings.get(term)
        if mapped and mapped in terms_by_id:
            rows.append(
                DriftRow(
                    source=source,
                    spec_term=term,
                    odpv_match=mapped,
                    status="Alias match",
                    notes=f"{spec_name} term maps through ODPV alias.",
                )
            )
            continue
        rows.extend(compare_terms(spec_name, source, [term], terms_by_id, alias_to_id))
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


def build_odps_rows(odps_schema_source: str) -> list[DriftRow]:
    schema = load_schema(odps_schema_source)
    terms_by_id, alias_to_id = odpv_lookup()
    try:
        product_components = list(schema["properties"]["product"]["properties"])
    except KeyError as exc:
        raise ValueError("Could not find properties.product.properties in ODPS schema") from exc
    return compare_mapped_terms(
        "ODPS",
        "Product component",
        product_components,
        terms_by_id,
        alias_to_id,
        ODPS_COMPONENT_MAPPINGS,
    )


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|")


def bold(value: str) -> str:
    return f"**{value}**" if value else value


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


def current_run_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def dated_report_path(run_timestamp: str) -> Path:
    return DEFAULT_REPORT_DIR / f"{run_timestamp[:10]}-{DEFAULT_REPORT_NAME}"


def existing_run_timestamp(report_path: Path) -> str | None:
    if not report_path.exists():
        return None
    match = RUN_TIMESTAMP_RE.search(report_path.read_text(encoding="utf-8"))
    if not match:
        return None
    return match.group(1)


def remove_legacy_report(report_path: Path) -> None:
    if LEGACY_REPORT.exists() and report_path.resolve() != LEGACY_REPORT.resolve():
        LEGACY_REPORT.unlink()


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
        cells = [
            markdown_escape(row.source),
            f"`{markdown_escape(row.spec_term)}`",
            match,
            markdown_escape(row.status),
            markdown_escape(row.notes),
        ]
        if row.status == "Possible drift":
            cells = [bold(cell) for cell in cells]
        lines.append(
            "| "
            + " | ".join(cells)
            + " |"
        )
    return lines


def render_drift_summary(spec_rows: list[tuple[str, list[DriftRow]]]) -> list[str]:
    possible_drifts = [
        (spec_name, row)
        for spec_name, rows in spec_rows
        for row in rows
        if row.status == "Possible drift"
    ]
    lines = [
        "## Possible Drift Summary",
        "",
    ]
    if not possible_drifts:
        lines.append("No unresolved drift detected.")
        return lines

    lines.extend(
        [
            "| Spec | Source | Term | Suggested action |",
            "|---|---|---|---|",
        ]
    )
    action = "Review whether to add an ODPV term, add an alias, or update the source specification."
    for spec_name, row in possible_drifts:
        lines.append(
            "| "
            + " | ".join(
                [
                    markdown_escape(spec_name),
                    markdown_escape(row.source),
                    f"`{markdown_escape(row.spec_term)}`",
                    action,
                ]
            )
            + " |"
        )
    return lines


def render_report(
    odpg_rows: list[DriftRow],
    odpc_rows: list[DriftRow],
    odps_rows: list[DriftRow],
    odpg_schema_source: str,
    odpc_schema_source: str,
    odps_schema_source: str,
    run_timestamp: str,
) -> str:
    rows = [*odpg_rows, *odpc_rows, *odps_rows]
    possible_drifts = [row for row in rows if row.status == "Possible drift"]
    lines = [
        "# ODPV Cross-Spec Drift Report",
        "",
        f"![ODPV cross-spec drift]({REPORT_IMAGE})",
        "",
        "This report compares published Open Data Product family schemas against the canonical ODPV vocabulary.",
        "",
        f"Last drift detection run: `{run_timestamp}`",
        "",
        f"- ODPG schema: `{display_source(odpg_schema_source)}`",
        f"- ODPC schema: `{display_source(odpc_schema_source)}`",
        f"- ODPS schema: `{display_source(odps_schema_source)}`",
        "- ODPV source: `source/vocab/odpv.yaml`",
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
            *render_drift_summary(
                [
                    ("ODPG", odpg_rows),
                    ("ODPC", odpc_rows),
                    ("ODPS", odps_rows),
                ]
            ),
            "",
            *render_rows("ODPG", odpg_rows),
            "",
            *render_rows("ODPC", odpc_rows),
            "",
            *render_rows("ODPS", odps_rows),
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare published family schema terms against ODPV.")
    parser.add_argument("--odpg-schema", default=DEFAULT_ODPG_SCHEMA, help="URL or path to ODPG YAML schema")
    parser.add_argument("--odpc-schema", default=DEFAULT_ODPC_SCHEMA, help="URL or path to ODPC YAML schema")
    parser.add_argument("--odps-schema", default=DEFAULT_ODPS_SCHEMA, help="URL or path to ODPS YAML schema")
    parser.add_argument("--report", type=Path, help="Markdown report path")
    parser.add_argument("--check", action="store_true", help="Fail if the existing report is out of sync")
    args = parser.parse_args()

    odpg_rows = build_odpg_rows(args.odpg_schema)
    odpc_rows = build_odpc_rows(args.odpc_schema)
    odps_rows = build_odps_rows(args.odps_schema)
    run_timestamp = current_run_timestamp()
    report_path = args.report if args.report else dated_report_path(run_timestamp)
    run_timestamp = existing_run_timestamp(report_path) if args.check else run_timestamp
    if not run_timestamp:
        run_timestamp = current_run_timestamp()
    report = render_report(
        odpg_rows,
        odpc_rows,
        odps_rows,
        args.odpg_schema,
        args.odpc_schema,
        args.odps_schema,
        run_timestamp,
    )

    if args.check:
        if not report_path.exists():
            print(f"Missing cross-spec drift report: {report_path}", file=sys.stderr)
            return 1
        current = report_path.read_text(encoding="utf-8")
        if current != report:
            print(f"Cross-spec drift report is out of sync: {report_path}", file=sys.stderr)
            return 1
        print("Cross-spec drift report is in sync")
        return 0

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")
    if not args.report:
        remove_legacy_report(report_path)
    rows = [*odpg_rows, *odpc_rows, *odps_rows]
    possible_drifts = sum(1 for row in rows if row.status == "Possible drift")
    print(f"Wrote {report_path} terms={len(rows)} possibleDrifts={possible_drifts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
