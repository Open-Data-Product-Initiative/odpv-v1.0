#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from typing import Any

from vocab_utils import iter_terms, load_yaml


WORD_RE = re.compile(r"[a-z0-9]+")


FIELD_WEIGHTS = {
    "id": 5,
    "preferredLabel": 5,
    "alsoKnownAs": 4,
    "definition": 3,
    "examples": 3,
    "relatedTerms": 2,
    "section": 1,
}


def tokenize(value: str) -> list[str]:
    return WORD_RE.findall(value.lower())


def flatten_language_value(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return " ".join(flatten_language_value(item) for item in value)
    if isinstance(value, dict):
        return " ".join(flatten_language_value(item) for item in value.values())
    return ""


def searchable_fields(section: dict[str, Any], term: dict[str, Any]) -> dict[str, str]:
    return {
        "id": term.get("id", ""),
        "preferredLabel": flatten_language_value(term.get("preferredLabel")),
        "alsoKnownAs": flatten_language_value(term.get("alsoKnownAs")),
        "definition": flatten_language_value(term.get("definition")),
        "examples": flatten_language_value(term.get("examples")),
        "relatedTerms": " ".join(term.get("relatedTerms", [])),
        "section": section.get("id", ""),
    }


def score_term(query_tokens: list[str], fields: dict[str, str]) -> tuple[int, list[str]]:
    score = 0
    matched_fields = []
    for field, text in fields.items():
        field_tokens = set(tokenize(text))
        matches = sum(1 for token in query_tokens if token in field_tokens)
        if matches:
            score += matches * FIELD_WEIGHTS[field]
            matched_fields.append(field)
    return score, matched_fields


def search(query: str, limit: int) -> list[dict[str, Any]]:
    data = load_yaml()
    query_tokens = tokenize(query)
    results = []
    for section, term in iter_terms(data):
        fields = searchable_fields(section, term)
        score, matched_fields = score_term(query_tokens, fields)
        if score == 0:
            continue
        result = {
            "score": score,
            "matchedFields": matched_fields,
            "vocabularyVersion": data["version"],
            "section": section["id"],
            "id": term["id"],
            "uri": term["uri"],
            "preferredLabel": term["preferredLabel"],
            "definition": term["definition"],
            "relatedTerms": term.get("relatedTerms", []),
            "examples": term.get("examples", {}),
        }
        results.append(result)

    grouped = defaultdict(list)
    for result in results:
        grouped[result["score"]].append(result)

    return sorted(results, key=lambda item: (-item["score"], item["id"]))[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(description="Search ODPV vocabulary terms.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=5, help="Maximum number of matches")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    results = search(args.query, args.limit)
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=True))
        return 0

    for result in results:
        label = result["preferredLabel"].get("en", result["id"])
        definition = result["definition"].get("en", "")
        print(f"{result['id']} ({label})")
        print(f"  uri: {result['uri']}")
        print(f"  section: {result['section']}")
        print(f"  score: {result['score']}")
        print(f"  matchedFields: {', '.join(result['matchedFields'])}")
        print(f"  definition: {definition}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
