#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from search_vocab import search
from vocab_utils import iter_terms, load_yaml


def term_packet(section: dict[str, Any], term: dict[str, Any]) -> dict[str, Any]:
    packet = {
        "section": section["id"],
        "id": term["id"],
        "uri": term["uri"],
        "type": term["type"],
        "status": term["status"],
        "introducedIn": term.get("introducedIn"),
        "preferredLabel": term["preferredLabel"],
        "definition": term["definition"],
        "alsoKnownAs": term.get("alsoKnownAs", {}),
        "relatedTerms": term.get("relatedTerms", []),
        "usedIn": term.get("usedIn", []),
        "examples": term.get("examples", {}),
    }
    for optional in ("mappings", "domain", "range"):
        if term.get(optional):
            packet[optional] = term[optional]
    return packet


def load_index() -> tuple[dict[str, Any], dict[str, tuple[dict[str, Any], dict[str, Any]]], dict[str, tuple[str, dict[str, Any], dict[str, Any]]]]:
    data = load_yaml()
    terms_by_id: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    aliases: dict[str, tuple[str, dict[str, Any], dict[str, Any]]] = {}
    for section, term in iter_terms(data):
        terms_by_id[term["id"]] = (section, term)
        for alias in term.get("alsoKnownAs", {}).get("en", []):
            aliases.setdefault(alias.casefold(), (alias, section, term))
    return data, terms_by_id, aliases


def resolve(query: str) -> dict[str, Any]:
    data, terms_by_id, aliases = load_index()
    if query in terms_by_id:
        section, term = terms_by_id[query]
        return {
            "query": query,
            "vocabularyVersion": data["version"],
            "match": {
                **term_packet(section, term),
                "matchType": "id",
                "matchedAliases": [],
                "score": 100,
            },
            "candidates": [],
        }

    alias_match = aliases.get(query.casefold())
    if alias_match:
        alias, section, term = alias_match
        return {
            "query": query,
            "vocabularyVersion": data["version"],
            "match": {
                **term_packet(section, term),
                "matchType": "alias",
                "matchedAliases": [alias],
                "score": 95,
            },
            "candidates": [],
        }

    candidates = search(query, 5)
    if not candidates:
        return {"query": query, "vocabularyVersion": data["version"], "match": None, "candidates": []}

    best = candidates[0]
    section, term = terms_by_id[best["id"]]
    return {
        "query": query,
        "vocabularyVersion": data["version"],
        "match": {
            **term_packet(section, term),
            "matchType": "search",
            "matchedAliases": [],
            "score": best["score"],
            "matchedFields": best["matchedFields"],
        },
        "candidates": candidates[1:],
    }


def explain(term_id: str) -> dict[str, Any]:
    data, terms_by_id, _aliases = load_index()
    if term_id not in terms_by_id:
        raise KeyError(f"Unknown ODPV term: {term_id}")
    section, term = terms_by_id[term_id]
    return {"vocabularyVersion": data["version"], **term_packet(section, term)}


def relationship(source: str, verb: str, target: str) -> dict[str, Any]:
    data, terms_by_id, aliases = load_index()
    resolved = resolve(verb)
    match = resolved.get("match")
    if not match or match.get("type") != "relationship":
        alias_match = aliases.get(verb.casefold())
        if alias_match:
            _alias, section, term = alias_match
        else:
            return {
                "vocabularyVersion": data["version"],
                "source": source,
                "verb": verb,
                "target": target,
                "relationship": None,
                "compatible": False,
                "sourceCompatible": False,
                "targetCompatible": False,
                "notes": ["No official ODPV relationship matched the verb."],
            }
    else:
        section, term = terms_by_id[match["id"]]

    domain = term.get("domain", [])
    range_ = term.get("range", [])
    source_compatible = source in domain
    target_compatible = target in range_
    notes = []
    if not source_compatible:
        notes.append(f"{source} is not listed in domain for {term['id']}.")
    if not target_compatible:
        notes.append(f"{target} is not listed in range for {term['id']}.")

    return {
        "vocabularyVersion": data["version"],
        "source": source,
        "verb": verb,
        "target": target,
        "relationship": term_packet(section, term),
        "compatible": source_compatible and target_compatible,
        "sourceCompatible": source_compatible,
        "targetCompatible": target_compatible,
        "notes": notes,
    }


def context(term_id: str) -> dict[str, Any]:
    data, terms_by_id, _aliases = load_index()
    if term_id not in terms_by_id:
        raise KeyError(f"Unknown ODPV term: {term_id}")
    section, term = terms_by_id[term_id]

    incoming = []
    outgoing = []
    for _rel_section, rel in terms_by_id.values():
        if rel.get("type") != "relationship":
            continue
        if term_id in rel.get("domain", []):
            outgoing.append(rel["id"])
        if term_id in rel.get("range", []):
            incoming.append(rel["id"])

    related_packets = []
    for related_id in term.get("relatedTerms", []):
        related = terms_by_id.get(related_id)
        if not related:
            continue
        related_section, related_term = related
        related_packets.append(
            {
                "id": related_term["id"],
                "uri": related_term["uri"],
                "section": related_section["id"],
                "preferredLabel": related_term["preferredLabel"],
                "definition": related_term["definition"],
            }
        )

    return {
        "contextType": "odpv.term",
        "vocabularyVersion": data["version"],
        "term": term_packet(section, term),
        "neighbors": {
            "relatedTerms": term.get("relatedTerms", []),
            "relatedTermPackets": related_packets,
        },
        "relationshipHints": {
            "incoming": sorted(incoming),
            "outgoing": sorted(outgoing),
        },
        "usageGuidance": [
            "Use the stable id and uri in generated outputs.",
            "Prefer aliases only for matching user or source language; emit the canonical id.",
            "Use related terms for retrieval expansion, not as exact synonyms.",
        ],
    }


def print_json(payload: dict[str, Any]) -> int:
    print(json.dumps(payload, indent=2, ensure_ascii=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Agent-oriented ODPV vocabulary helper.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    resolve_parser = subparsers.add_parser("resolve", help="Resolve text to a canonical ODPV term")
    resolve_parser.add_argument("text")

    explain_parser = subparsers.add_parser("explain", help="Explain an ODPV term")
    explain_parser.add_argument("term_id")

    relationship_parser = subparsers.add_parser("relationship", help="Check an ODPV relationship domain/range")
    relationship_parser.add_argument("source")
    relationship_parser.add_argument("verb")
    relationship_parser.add_argument("target")

    context_parser = subparsers.add_parser("context", help="Return an agent-ready term context packet")
    context_parser.add_argument("term_id")

    args = parser.parse_args()
    try:
        if args.command == "resolve":
            return print_json(resolve(args.text))
        if args.command == "explain":
            return print_json(explain(args.term_id))
        if args.command == "relationship":
            return print_json(relationship(args.source, args.verb, args.target))
        if args.command == "context":
            return print_json(context(args.term_id))
    except KeyError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
