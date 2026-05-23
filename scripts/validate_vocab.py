#!/usr/bin/env python3
from __future__ import annotations

import json
import sys

import yaml

from vocab_utils import (
    CANONICAL_JSON,
    CANONICAL_JSONLD,
    CANONICAL_SKOS_TTL,
    SECTION_IDS,
    TERMS_JSONL,
    VOCAB_DIR,
    build_artifacts,
    iter_terms,
    load_yaml,
    read_text,
    validate_data,
)


def main() -> int:
    data = load_yaml()
    errors = validate_data(data)

    expected_artifacts = build_artifacts(data)
    for path, expected in expected_artifacts.items():
        if not path.exists():
            errors.append(f"Missing derived artifact: {path}")
        elif read_text(path) != expected:
            errors.append(f"Derived artifact is out of sync: {path}")

    try:
        with CANONICAL_JSON.open("r", encoding="utf-8") as handle:
            json_data = json.load(handle)
        if json_data != data:
            errors.append("odpv.json does not match odpv.yaml")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Could not parse odpv.json: {exc}")

    try:
        with CANONICAL_JSONLD.open("r", encoding="utf-8") as handle:
            jsonld_data = json.load(handle)
        if jsonld_data.get("@type") != "skos:ConceptScheme":
            errors.append("odpv.jsonld does not describe a skos:ConceptScheme")
        if len(jsonld_data.get("@graph", [])) != len(iter_terms(data)):
            errors.append("odpv.jsonld graph term count does not match canonical term count")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Could not parse odpv.jsonld: {exc}")

    try:
        skos_text = CANONICAL_SKOS_TTL.read_text(encoding="utf-8")
        if "skos:ConceptScheme" not in skos_text:
            errors.append("odpv.skos.ttl does not contain a skos:ConceptScheme")
        if skos_text.count(" a skos:Concept") != len(iter_terms(data)) + 1:
            errors.append("odpv.skos.ttl concept count does not match canonical term count")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Could not read odpv.skos.ttl: {exc}")

    try:
        lines = TERMS_JSONL.read_text(encoding="utf-8").splitlines()
        jsonl_terms = [json.loads(line) for line in lines if line.strip()]
        if len(jsonl_terms) != len(iter_terms(data)):
            errors.append("terms.jsonl line count does not match canonical term count")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Could not parse terms.jsonl: {exc}")

    sections = {section["id"]: section for section in data["sections"]}
    for section_id in SECTION_IDS:
        path = VOCAB_DIR / f"{section_id}.yaml"
        try:
            with path.open("r", encoding="utf-8") as handle:
                section_doc = yaml.safe_load(handle)
            if section_doc.get("sections") != [sections[section_id]]:
                errors.append(f"{path} does not match canonical {section_id} section")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Could not parse {path}: {exc}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    terms = [term for _, term in iter_terms(data)]
    relationships = [term for term in terms if term.get("type") == "relationship"]
    print(
        "Validation OK "
        f"terms={len(terms)} "
        f"relationships={len(relationships)} "
        f"sections={len(data['sections'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
