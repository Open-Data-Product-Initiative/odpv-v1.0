# AI Agent Usage Patterns

ODPV is designed to be usable by AI agents, catalog tools, retrieval systems, graph systems, and automation workflows. From an agent perspective, ODPV provides the shared terminology layer for data product management: it names stable concepts, labels, definitions, aliases, related terms, and relationship names that other specifications and tools can reference consistently.

ODPS defines one data product. ODPC defines reusable catalog and portfolio objects around data products. [ODPG](https://opendataproducts.org/odpg-v1.0/) defines relationships between those objects. ODPV provides the shared vocabulary terms used across the standards family. This separation helps agents choose the right source before acting.

<!-- AI_AGENT_USAGE_PATTERNS:
Use ODPV as the shared vocabulary and terminology layer, not as the full data product, catalog, or graph definition layer.
Use ODPS or another referenced product model for detailed data product metadata.
Use ODPC for catalog and portfolio objects such as ProductReference, UseCase, BusinessObjective, KPI, Signal, and Catalog.
Use ODPG for graph structures, graph relationships, traversal, and connected portfolio analysis.
Use ODPV term ids and uris for stable shared concepts, labels, definitions, aliases, and relationship names.
-->

## Agent capabilities enabled by ODPV

Agents can use ODPV to:

* select stable term ids and uris for data product management concepts
* map user language, synonyms, and internal terminology to preferred ODPV terms
* retrieve definitions, labels, aliases, related terms, and examples from `terms.jsonl`
* validate vocabulary files against `odpv.schema.json`
* explain distinctions between nearby terms such as `DataProduct`, `Dataset`, `DataService`, and `Distribution`
* choose relationship terms such as `supports`, `requires`, `contributesTo`, `measures`, `dependsOn`, `governedBy`, `providedBy`, and `consumedBy`
* prepare graph-ready relationship names for ODPG or another graph implementation
* support catalog alignment by using the same terms in ODPC catalogs and ODPS product descriptions
* detect terminology drift, duplicate concepts, unclear aliases, or missing shared terms
* suggest extension terms when an organization-specific or domain-specific concept is not part of the official vocabulary

## Common agent workflows

| Workflow | Agent behavior |
|---|---|
| Term lookup | Match a user phrase or internal label to the best ODPV term using preferred labels, aliases, definitions, examples, and related terms. |
| Vocabulary validation | Validate ODPV vocabulary files, check required fields, detect malformed terms, and suggest schema-compliant repairs. |
| Terminology alignment | Compare ODPS, ODPC, ODPG, vendor catalog, or internal model wording against ODPV and recommend stable term ids and uris. |
| Relationship selection | Choose the most specific ODPV relationship term for a graph edge and avoid falling back to `relatedTo` when a better term exists. |
| Retrieval and RAG | Use `llms.txt`, `terms.jsonl`, schema files, section YAML files, and include pages to retrieve the correct term before generating or editing content. |
| Vocabulary extension | Identify missing shared terms and propose extension candidates with an id, label, definition, concept group, related terms, and example usage. |
| Artifact maintenance | Update canonical `odpv.yaml`, regenerate derived JSON, JSONL, and section YAML files, then validate that generated artifacts are in sync. |
| Standards-family guidance | Decide whether a task belongs in ODPS, ODPC, ODPG, or ODPV before generating content or changing files. |

## Agent behavior constraints

Agents using ODPV should keep vocabulary boundaries clear:

* Do not treat ODPV as a replacement for ODPS, ODPC, or ODPG.
* Do not put full product metadata, catalog objects, or graph structures into ODPV terms.
* Do not redefine official ODPV term ids, uris, labels, or meanings locally.
* Do not invent new official terms when an existing ODPV term fits.
* Do not use `relatedTo` when a more specific relationship term such as `supports`, `requires`, `dependsOn`, or `governedBy` applies.
* Do not assume aliases are preferred labels; use them for search, mapping, and onboarding.
* Do not edit generated vocabulary artifacts directly when changing official vocabulary content; update `source/vocab/odpv.yaml` first and regenerate derived files.

## Example prompts ODPV enables

```text
Find the best ODPV term for "data API" and return the stable id and uri.
```

```text
Map these internal catalog labels to ODPV preferred terms and explain uncertain matches.
```

```text
Choose ODPV relationship terms for these graph edges and avoid generic relationships where possible.
```

```text
Validate this ODPV vocabulary file and suggest schema-compliant repairs.
```

```text
Identify terminology drift between this ODPC catalog and the official ODPV terms.
```

```text
Propose an ODPV extension term for a missing domain-specific concept.
```
