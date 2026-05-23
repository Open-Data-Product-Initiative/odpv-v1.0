---
title: Open Data Product Vocab (ODPV) version RC | Linux Foundation 

language_tabs: # must be one of https://git.io/vQNgJ
- yaml

toc_footers:
  - License <a href='https://www.apache.org/licenses/LICENSE-2.0'>Apache 2.0</a>
  - <br/><a href='https://opendataproducts.org'>Specification home</a>
  - <br/>Linux Foundation</a>

includes:
- toolkit
- agent_usage
- term_governance
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
  - name: llms
    content: /llms.txt
  - name: ai-agent-guidance
    content: Use /llms.txt for agent guidance, /vocab/terms.jsonl for retrieval-friendly vocabulary terms, /vocab/odpv.jsonld or /vocab/odpv.skos.ttl for linked-data tooling, and source helper scripts for local agent workflows.
---

# OPEN DATA PRODUCT VOCABULARY - The Linux Foundation

## Version RELEASE CANDIDATE
The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “NOT RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in BCP 14 ([RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119) and [RFC 8174](https://datatracker.ietf.org/doc/html/rfc8174)) when, and only when, they appear in all capitals, as shown here.

The vocabulary is shared under <a href='https://www.apache.org/licenses/LICENSE-2.0'>Apache 2.0</a> license. 
Development of the vocabulary is under the umbrella of the Linux Foundation. 

| Topic | Link | Description |
|---|---|---|
| Version source | <a href="https://github.com/Open-Data-Product-Initiative/odpv-v1.0">Open Data Products Vocab on GitHub</a> | Official source repository for the ODPV vocabulary |
| Knowledge Base | [Open Data Product Spec Family Knowledge Base](https://opendataproducts.org/howto/) | Practical examples, FAQs, and implementation guidance |
| Contribute | [Raise an issue in GitHub](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/issues) | Submit issues or suggestions to the vocabulary maintainers |

# Introduction
The Open Data Product Vocabulary, ODPV, is a vendor-neutral, open-source, machine-readable controlled vocabulary for data product management. ODPV defines shared terms used across the OpenDataProducts.org standards family, including data products, catalogs, graphs, value concepts, governance concepts, and relationship terms. It is designed to help organizations use consistent language across specifications, catalogs, graph implementations, AI assistants, and GraphRAG-ready data product portfolios.

<img src="/images/odpv.png" width="750px">

## What ODPV Defines

ODPV defines the shared vocabulary layer for the OpenDataProducts.org standards family. The current vocabulary contains 78 terms across four concept groups:

**ODPV Core**: [ODPV Core](#odpv-core) defines foundational terms used across the standards family. These terms describe the basic objects, roles, classifications, and references needed to manage data products, catalogs, graphs, and agent workflows.

**ODPV Value**: [ODPV Value](#odpv-value) defines terms that connect data products to business demand, objectives, strategy, outcomes, and prioritization. These terms help connect data products to measurable value and portfolio-level decision-making.

**ODPV Governance**: [ODPV Governance](#odpv-governance) defines terms for quality, access, licensing, pricing, support, legal, operational, and compliance context. These terms help describe how data products are governed, accessed, controlled, and trusted.

**ODPV Relationships**: [ODPV Relationships](#odpv-relationships) defines reusable relationship terms for graph implementation, portfolio analysis, and cross-spec linking. These relationship terms help connect data products, use cases, objectives, KPIs, signals, providers, consumers, policies, catalogs, workflows, agents, and services in a consistent way.

These groups create a common language for describing, connecting, validating, and reasoning over data product portfolios.


| Section | Purpose | Term count |
|---|---|---:|
| ODPV Core | Foundational objects, roles, classifications, and references | 18 |
| ODPV Value | Business value, strategy, demand, outcomes, gaps, and priorities | 17 |
| ODPV Governance | Quality, access, licensing, pricing, support, agreements, policy, and compliance | 19 |
| ODPV Relationships | Relationship terms for graphs, portfolio analysis, and cross-spec linking | 24 |
| Total | Shared vocabulary terms | 78 |

[Suggest addition to the vocabulary](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/issues) 

## Machine-Readable Vocabulary Resources

ODPV is published in multiple machine-readable forms for tools, AI agents, catalogs, graph workflows, and semantic tooling.

| Resource | Format | Purpose |
|---|---|---|
| [`odpv.yaml`](/vocab/odpv.yaml) | YAML | Canonical machine-readable vocabulary source |
| [`odpv.json`](/vocab/odpv.json) | JSON | JSON representation for tools, APIs, search indexes, and graph applications |
| [`odpv.jsonld`](/vocab/odpv.jsonld) | JSON-LD | Linked-data representation for semantic tooling and graph workflows |
| [`odpv.skos.ttl`](/vocab/odpv.skos.ttl) | Turtle | SKOS representation with labels, definitions, related terms, and external mappings |
| [`terms.jsonl`](/vocab/terms.jsonl) | JSONL | Agent-friendly one-term-per-line file for retrieval, embeddings, and lightweight tools |
| [`llms.txt`](/llms.txt) | Text | AI agent guidance for discovering and using ODPV resources |

## Agent Helper Commands

ODPV includes source helper scripts for repeatable local vocabulary lookup, relationship checking, and context engineering workflows.

| Command | Purpose |
|---|---|
| `python3 scripts/agent_vocab_helper.py resolve <text>` | Resolve source language, aliases, or user phrases to a canonical ODPV term |
| `python3 scripts/agent_vocab_helper.py explain <term-id>` | Return a compact JSON explanation of a term with definition, aliases, related terms, mappings, and examples |
| `python3 scripts/agent_vocab_helper.py relationship <source> <verb> <target>` | Check whether a relationship exists and whether source and target fit the relationship domain and range hints |
| `python3 scripts/agent_vocab_helper.py context <term-id>` | Produce an agent-ready context packet for retrieval, grounding, and prompt assembly |
| `python3 scripts/search_vocab.py "<query>" --json` | Search more broadly across labels, aliases, definitions, examples, and related terms |

## Companion Vocabulary, Not a Heavy Ontology

ODPV is not intended to be a heavy ontology. It is a practical controlled vocabulary that gives stable reference terms to the OpenDataProducts.org standards family. Each specification can reference ODPV terms instead of redefining shared concepts locally. Shared terms belong in ODPV. Spec-specific terms stay in the relevant specification. Extensions can define additional domain-specific or organization-specific terms.

## Relationship to ODPS, ODPC, and ODPG

<!-- AI_STANDARDS_FAMILY_GUIDANCE:
ODPV is the shared vocabulary layer for the OpenDataProducts.org standards family.
ODPS is the Open Data Product Specification. Use ODPS when describing one data product and its product metadata.
ODPC is the Open Data Product Catalog specification. Use ODPC when describing catalogs, portfolios, use cases, objectives, KPIs, signals, and related portfolio objects.
ODPG is the Open Data Product Graph specification. Use ODPG when describing graph structures and relationships between data products, use cases, objectives, KPIs, signals, governance objects, providers, and consumers.
ODPV does not replace ODPS, ODPC, or ODPG. It provides stable ids, labels, definitions, and relationship names that those specifications can reference.
ODPG documentation: https://opendataproducts.org/odpg-v1.0/
ODPS homepage: https://opendataproducts.org/
-->

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

## Automated Drift Detection

ODPV includes automated cross-spec drift detection for the Open Data Product standards family. A weekly GitHub Action fetches the published ODPS, ODPC, and ODPG schemas, compares their schema terms against the canonical ODPV vocabulary, and writes a dated report.

Reports are kept in [`cross-spec-drift/`](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/tree/main/cross-spec-drift) so the project can track how alignment changes over time and use the historical reports as input for later analysis.

## Example Use

* A data product in ODPS can reference ODPV terms for concepts such as DataProduct, ProductDetails, ProductStrategy, DataHolder, SLA, DataQuality, License, DataAccess, PricingPlan, PaymentGateway, and Support.
* A catalog in ODPC can reference ODPV terms for concepts such as DataProductCatalog, UseCase, BusinessObjective, KPI, Signal, Gap, Priority, Reference, and Owner.
* A graph in ODPG can reference ODPV terms for node types and relationship types such as Agent, Workflow, Capability, uses, supports, contributesTo, measures, dependsOn, produces, consumes, ownedBy, alignsWith, impacts, exposes, and identifies.

## Specification Aims

* Define shared terms for data product management.
* Reduce duplicate term definitions across ODPS, ODPC, and ODPG.
* Prevent terminology drift across the standards family.
* Support consistent graph node and relationship naming.
* Support AI-assisted discovery, metadata generation, and GraphRAG.
* Improve interoperability between catalogs, platforms, marketplaces, and tools.
* Provide a lightweight path toward semantic knowledge graph implementation.
* Keep formal ontology work optional.
