from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
VOCAB_DIR = ROOT / "source" / "vocab"
CANONICAL_YAML = VOCAB_DIR / "odpv.yaml"
CANONICAL_JSON = VOCAB_DIR / "odpv.json"
TERMS_JSONL = VOCAB_DIR / "terms.jsonl"
SECTION_IDS = ("core", "value", "governance", "relationships")
REQUIRED_TERM_FIELDS = (
    "id",
    "uri",
    "type",
    "status",
    "introducedIn",
    "preferredLabel",
    "definition",
    "alsoKnownAs",
    "relatedTerms",
    "usedIn",
    "examples",
)


def load_yaml(path: Path = CANONICAL_YAML) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not contain a YAML mapping")
    return data


def dump_yaml(data: dict[str, Any]) -> str:
    return yaml.safe_dump(
        data,
        sort_keys=False,
        allow_unicode=False,
        width=10_000,
    )


def dump_json(data: dict[str, Any]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=True) + "\n"


def iter_sections(data: dict[str, Any]) -> list[dict[str, Any]]:
    sections = data.get("sections")
    if not isinstance(sections, list):
        raise ValueError("ODPV data must contain a sections array")
    return sections


def iter_terms(data: dict[str, Any]) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    terms: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for section in iter_sections(data):
        for term in section.get("terms", []):
            terms.append((section, term))
    return terms


def section_document(data: dict[str, Any], section: dict[str, Any]) -> dict[str, Any]:
    return {**data, "sections": [section]}


def build_terms_jsonl(data: dict[str, Any]) -> str:
    lines = []
    for section, term in iter_terms(data):
        flattened = {
            "vocabulary": data["id"],
            "vocabularyVersion": data["version"],
            "section": section["id"],
            "sectionName": section["name"]["en"],
            **term,
        }
        lines.append(json.dumps(flattened, ensure_ascii=True, separators=(",", ":")))
    return "\n".join(lines) + "\n"


def build_artifacts(data: dict[str, Any]) -> dict[Path, str]:
    artifacts = {
        CANONICAL_JSON: dump_json(data),
        TERMS_JSONL: build_terms_jsonl(data),
    }
    for section in iter_sections(data):
        section_id = section["id"]
        artifacts[VOCAB_DIR / f"{section_id}.yaml"] = dump_yaml(section_document(data, section))
    return artifacts


def validate_data(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    section_ids = [section.get("id") for section in iter_sections(data)]
    if section_ids != list(SECTION_IDS):
        errors.append(f"Expected sections {list(SECTION_IDS)}, found {section_ids}")

    seen_ids: set[str] = set()
    for section, term in iter_terms(data):
        term_id = term.get("id", "<missing id>")
        if term_id in seen_ids:
            errors.append(f"Duplicate term id: {term_id}")
        seen_ids.add(term_id)

        for field in REQUIRED_TERM_FIELDS:
            if field not in term:
                errors.append(f"{term_id}: missing required field {field}")

        examples = term.get("examples", {}).get("en") if isinstance(term.get("examples"), dict) else None
        if not isinstance(examples, list) or not examples:
            errors.append(f"{term_id}: examples.en must be a non-empty array")

        if term.get("type") == "relationship":
            if not term.get("domain"):
                errors.append(f"{term_id}: relationship term must include domain")
            if not term.get("range"):
                errors.append(f"{term_id}: relationship term must include range")

        used_in = term.get("usedIn")
        if not isinstance(used_in, list) or not used_in:
            errors.append(f"{term_id}: usedIn must be a non-empty array")

        if section.get("id") not in SECTION_IDS:
            errors.append(f"{term_id}: unknown section {section.get('id')}")

    return errors


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
