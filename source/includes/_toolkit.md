# Vocabulary Toolkit 

> Snippet of YAML version:

```yml
id: DataProduct
uri: https://opendataproducts.org/odpv-v1.0/terms/DataProduct
type: object
status: stable
preferredLabel:
  en: Data Product
definition:
  en: A managed data offering designed for reuse, with 
      defined ownership, access, quality, usage terms, 
      and value context.
alsoKnownAs:
  en:
    - data product
    - data offering
    - reusable data asset
relatedTerms:
  - Dataset
  - DataService
  - Distribution
usedIn:
  - ODPS
  - ODPC
  - ODPG
```

ODPV is published in several forms for different users and tools. This specification provides the human-readable documentation, while the vocabulary files provide machine-readable representations for validation, catalog integration, graph construction, AI retrieval, linked-data tooling, and automation. Use `odpv.yaml` as the canonical source, `odpv.json` when JSON is easier to consume, `odpv.jsonld` or `odpv.skos.ttl` for semantic web and linked-data tooling, the section YAML files when only one vocabulary area is needed, and `terms.jsonl` for search, embeddings, and lightweight AI agent workflows.

The primary implementation toolkit for the whole Open Data Product standards family is the [Open Data Product Agent SDK](https://github.com/Open-Data-Product-Initiative/odp-agent-sdk). Use it when building tools, validators, agent workflows, catalog integrations, graph workflows, or automation that needs to work across ODPS, ODPC, ODPG, and ODPV together.

<!-- AI_AGENT_GUIDANCE:
Use /vocab/odpv.yaml as the canonical ODPV vocabulary source.
Use /vocab/terms.jsonl for retrieval, embeddings, search, and lightweight tool calls.
Use /vocab/odpv.jsonld and /vocab/odpv.skos.ttl for linked-data, semantic web, and SKOS-aware tooling.
Use /vocab/core.yaml, /vocab/value.yaml, /vocab/governance.yaml, and /vocab/relationships.yaml when only one vocabulary section is needed.
Use https://github.com/Open-Data-Product-Initiative/odp-agent-sdk as the main SDK for cross-standard Open Data Product tooling.
Use stable term ids and uris exactly as published. Do not redefine official ODPV terms.
If a needed term is missing, treat it as an extension candidate and use a separate namespace or prefix.
-->

| Resource | Format | Purpose |
|---|---|---|
| [Open Data Product Agent SDK](https://github.com/Open-Data-Product-Initiative/odp-agent-sdk) | SDK | Main toolkit for building tools, validators, agent workflows, catalog integrations, and graph workflows across the Open Data Product standards family |
| [`llms.txt`](/llms.txt) | Text | AI agent guidance for discovering and using the ODPV vocabulary files |
| [`odpv.yaml`](/vocab/odpv.yaml) | YAML | Canonical machine-readable vocabulary file |
| [`odpv.json`](/vocab/odpv.json) | JSON | JSON representation for tools, APIs, search indexes, and graph applications |
| [`odpv.jsonld`](/vocab/odpv.jsonld) | JSON-LD | Linked-data representation for semantic tooling and graph workflows |
| [`odpv.skos.ttl`](/vocab/odpv.skos.ttl) | Turtle | SKOS representation with labels, definitions, related terms, and external mappings |
| [`terms.jsonl`](/vocab/terms.jsonl) | JSONL | Agent-friendly one-term-per-line file for retrieval, embeddings, and lightweight tools |
| [`core.yaml`](/vocab/core.yaml) | YAML | ODPV Core terms as a standalone machine-readable section file |
| [`value.yaml`](/vocab/value.yaml) | YAML | ODPV Value terms as a standalone machine-readable section file |
| [`governance.yaml`](/vocab/governance.yaml) | YAML | ODPV Governance terms as a standalone machine-readable section file |
| [`relationships.yaml`](/vocab/relationships.yaml) | YAML | ODPV Relationships terms as a standalone machine-readable section file |
| [`odpv.schema.json`](/schema/odpv.schema.json) | JSON Schema | Validation schema for ODPV vocabulary files |

Agent-oriented helper scripts are available in the source repository for maintaining and using the vocabulary files.

<!-- AI_AGENT_SCRIPT_GUIDANCE:
When working from the source repository, use scripts/search_vocab.py for repeatable local term lookup.
Use scripts/generate_vocab_artifacts.py after editing source/vocab/odpv.yaml to regenerate derived JSON, JSON-LD, SKOS Turtle, JSONL, and section YAML files.
Use scripts/generate_vocab_artifacts.py --check in CI or review workflows to detect drift between canonical and derived vocabulary artifacts.
Use scripts/validate_vocab.py to validate vocabulary structure, generated artifacts, JSONL output, section files, examples, and relationship guidance.
Use scripts/test_vocab_scripts.py to verify the helper scripts themselves.
Use scripts/check_cross_spec_drift.py to compare published ODPS, ODPC, and ODPG schema terms against ODPV and refresh the dated cross-spec-drift report.
Do not edit generated vocabulary artifacts directly unless intentionally repairing generated output; update source/vocab/odpv.yaml first.
-->

| Script | Purpose |
|---|---|
| [`generate_vocab_artifacts.py`](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/blob/main/scripts/generate_vocab_artifacts.py) | Regenerates derived vocabulary artifacts from canonical `odpv.yaml`, including JSON, JSON-LD, SKOS Turtle, JSONL, and section YAML; use `--check` in CI to detect drift |
| [`validate_vocab.py`](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/blob/main/scripts/validate_vocab.py) | Validates vocabulary structure, required fields, generated artifacts, JSONL, section files, and relationship guidance |
| [`search_vocab.py`](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/blob/main/scripts/search_vocab.py) | Searches ODPV terms using labels, aliases, definitions, examples, and related terms |
| [`check_cross_spec_drift.py`](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/blob/main/scripts/check_cross_spec_drift.py) | Compares published ODPS, ODPC, and ODPG schema terms against ODPV and writes a dated report under `cross-spec-drift/` |

The Markdown tables in this specification are intended for human readers. The YAML files are intended for programmable use, automation, validation, AI retrieval, and graph-based tooling.
