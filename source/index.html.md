---
title: Open Data Product Vocab (ODPV) version DRAFT | Linux Foundation 

language_tabs: # must be one of https://git.io/vQNgJ
- yaml

toc_footers:
  - License <a href='https://www.apache.org/licenses/LICENSE-2.0'>Apache 2.0</a>
  - <br/><a href='https://opendataproducts.org'>Specification home</a>
  - <br/>Linux Foundation</a>

includes:
- core
- value
- governance
- relationships
- extensions
- contributors


search: true

code_clipboard: true

meta:
  - name: description
    content: The Open Data Product Vocabulary, ODPV, is a vendor-neutral, open-source, machine-readable controlled vocabulary for data product management. 
---

# OPEN DATA PRODUCT VOCABULARY - The Linux Foundation

## Version DRAFT
The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “NOT RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in BCP 14 ([RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119) and [RFC 8174](https://datatracker.ietf.org/doc/html/rfc8174)) when, and only when, they appear in all capitals, as shown here.

The vocabulary is shared under <a href='https://www.apache.org/licenses/LICENSE-2.0'>Apache 2.0</a> license. 
Development of the vocabulary is under the umbrella of the Linux Foundation. 

| Topic | Link | Description |
|---|---|---|
| Version source | <a href="https://github.com/Open-Data-Product-Initiative/odpv-v1.0">Open Data Products Vocab on GitHub</a> | Official source repository for the ODPV vocabulary |
| Knowledge Base | [Open Data Product Spec Family Knowledge Base](https://opendataproducts.org/howto/) | Practical examples, FAQs, and implementation guidance |
| Contribute | [Raise an issue in GitHub](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/issues) | Submit issues or suggestions to the vocabulary maintainers |

## Machine-readable vocabulary files

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

ODPV is published in several forms for different users and tools. This specification provides the human-readable documentation, while the vocabulary files provide machine-readable representations for validation, catalog integration, graph construction, AI retrieval, and automation. Use `odpv.yaml` as the canonical source, `odpv.json` when JSON is easier to consume, the section YAML files when only one vocabulary area is needed, and `terms.jsonl` for search, embeddings, and lightweight AI agent workflows.

<!-- AI_AGENT_GUIDANCE:
Use /vocab/odpv.yaml as the canonical ODPV vocabulary source.
Use /vocab/terms.jsonl for retrieval, embeddings, search, and lightweight tool calls.
Use /vocab/core.yaml, /vocab/value.yaml, /vocab/governance.yaml, and /vocab/relationships.yaml when only one vocabulary section is needed.
Use stable term ids and uris exactly as published. Do not redefine official ODPV terms.
If a needed term is missing, treat it as an extension candidate and use a separate namespace or prefix.
-->

| File | Format | Purpose |
|---|---|---|
| [`odpv.yaml`](/vocab/odpv.yaml) | YAML | Canonical machine-readable vocabulary file |
| [`odpv.json`](/vocab/odpv.json) | JSON | JSON representation for tools, APIs, search indexes, and graph applications |
| [`terms.jsonl`](/vocab/terms.jsonl) | JSONL | Agent-friendly one-term-per-line file for retrieval, embeddings, and lightweight tools |
| [`core.yaml`](/vocab/core.yaml) | YAML | ODPV Core terms as a standalone machine-readable section file |
| [`value.yaml`](/vocab/value.yaml) | YAML | ODPV Value terms as a standalone machine-readable section file |
| [`governance.yaml`](/vocab/governance.yaml) | YAML | ODPV Governance terms as a standalone machine-readable section file |
| [`relationships.yaml`](/vocab/relationships.yaml) | YAML | ODPV Relationships terms as a standalone machine-readable section file |
| [`odpv.schema.json`](/schema/odpv.schema.json) | JSON Schema | Validation schema for ODPV vocabulary files |

The Markdown tables in this specification are intended for human readers. The YAML files are intended for programmable use, automation, validation, AI retrieval, and graph-based tooling.

# Introduction
The Open Data Product Vocabulary, ODPV, is a vendor-neutral, open-source, machine-readable controlled vocabulary for data product management. ODPV defines shared terms used across the OpenDataProducts.org standards family, including data products, catalogs, graphs, value concepts, governance concepts, and relationship terms. It is designed to help organizations use consistent language across specifications, catalogs, graph implementations, AI assistants, and GraphRAG-ready data product portfolios.

<img src="/images/specs-with-vocab.png" width="750px">

## What ODPV Defines

ODPV defines the shared vocabulary layer for the OpenDataProducts.org standards family. The first version focuses on four concept groups:

**ODPV Core**: [ODPV Core](#odpv-core) defines foundational terms used across the standards family.These terms describe the basic objects and roles needed to manage data products, catalogs, and graphs.

**ODPV Value**: [ODPV Value](#odpv-value) defines terms that connect data products to business demand, objectives, outcomes, and prioritization. These terms help connect data products to measurable value and portfolio-level decision-making.

**ODPV Governance**: [ODPV Governance](#odpv-governance) defines terms for quality, access, legal, operational, and compliance context.These terms help describe how data products are governed, accessed, controlled, and trusted.

**ODPV Relationships**: [ODPV Relationships](#odpv-relationships) defines reusable relationship terms for graph implementation and portfolio analysis. These relationship terms help connect data products, use cases, objectives, KPIs, signals, providers, consumers, policies, and catalogs in a consistent way.

These groups create a common language for describing, connecting, validating, and reasoning over data product portfolios.


| Section | Purpose | Term count |
|---|---|---:|
| ODPV Core | Foundational objects, roles, classifications, and references | 13 |
| ODPV Value | Business value, demand, outcomes, gaps, and priorities | 15 |
| ODPV Governance | Quality, access, licensing, agreements, policy, and compliance | 15 |
| ODPV Relationships | Relationship terms for graphs and portfolio analysis | 16 |
| Total | Shared vocabulary terms | 59 |

[Suggest addition to the vocabulary](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/issues) 

## Companion Vocabulary, Not a Heavy Ontology

ODPV is not intended to be a heavy ontology. It is a practical controlled vocabulary that gives stable reference terms to the OpenDataProducts.org standards family. Each specification can reference ODPV terms instead of redefining shared concepts locally. Shared terms belong in ODPV. Spec-specific terms stay in the relevant specification. Extensions can define additional domain-specific or organization-specific terms.

## Relationship to ODPS, ODPC, and ODPG

* ODPS defines one data product.
* ODPC defines reusable catalog and portfolio objects.
* ODPG defines relationships between data products, use cases, objectives, KPIs, signals, and other portfolio objects.
* ODPV defines the shared language used by all of them.

Used together, ODPS, ODPC, ODPG, and ODPV create a machine-readable operating model for data product management.

## Why ODPV Matters

ODPV helps prevent terminology drift across the standards family. Without a shared vocabulary, each specification may define terms such as Data Product, Use Case, Objective, KPI, Signal, Owner, SLA, License, or Relationship slightly differently. ODPV gives these terms one stable reference point. This improves:

* Specification alignment
* Graph implementation
* Metadata validation
* Catalog interoperability
* AI-assisted discovery
* GraphRAG context
* Portfolio analysis
* Tool development

## Example Use

* A data product in ODPS can reference ODPV terms for concepts such as DataProduct, Owner, SLA, DataQuality, License, and AccessMethod.
* A catalog in ODPC can reference ODPV terms for concepts such as DataProductCatalog, UseCase, BusinessObjective, KPI, Signal, Gap, and Priority.
* A graph in ODPG can reference ODPV terms for node types and relationship types such as supports, requires, contributesTo, measures, belongsTo, dependsOn, governedBy, providedBy, consumedBy, and indicates.

## Specification Aims

* Define shared terms for data product management.
* Reduce duplicate term definitions across ODPS, ODPC, and ODPG.
* Prevent terminology drift across the standards family.
* Support consistent graph node and relationship naming.
* Support AI-assisted discovery, metadata generation, and GraphRAG.
* Improve interoperability between catalogs, platforms, marketplaces, and tools.
* Provide a lightweight path toward semantic knowledge graph implementation.
* Keep formal ontology work optional.
