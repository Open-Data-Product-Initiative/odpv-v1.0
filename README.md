# Open Data Products Vocabulary (ODPV)

The Open Data Product Vocabulary, ODPV, is a vendor-neutral, open-source, machine-readable controlled vocabulary for data product management. ODPV defines shared terms used across the OpenDataProducts.org standards family, including data products, catalogs, graphs, value concepts, governance concepts, and relationship terms. It is designed to help organizations use consistent language across specifications, catalogs, graph implementations, AI assistants, and GraphRAG-ready data product portfolios.

# What ODPV Defines

ODPV defines the shared vocabulary layer for the OpenDataProducts.org standards family. The first version focuses on four concept groups:

* ODPV Core
* ODPV Value
* ODPV Governance
* ODPV Relationships

These groups create a common language for describing, connecting, validating, and reasoning over data product portfolios.

# ODPV Core

ODPV Core defines foundational terms used across the standards family.

The first version includes:

* DataProduct
* DataProductCatalog
* DataProductGraph
* Dataset
* Distribution
* DataService
* Provider
* Consumer
* Owner
* Outcome Owner
* System Steward

These terms describe the basic objects and roles needed to manage data products, catalogs, and graphs.

# ODPV Value

ODPV Value defines terms that connect data products to business demand, objectives, outcomes, and prioritization.

The first version includes:

* UseCase
* BusinessObjective
* KPI
* Impact
* Signal
* Gap
* Priority

These terms help connect data products to measurable value and portfolio-level decision-making.

# ODPV Governance

ODPV Governance defines terms for quality, access, legal, operational, and compliance context.

The first version includes:

* DataQuality
* Pricing plan
* SLA
* License
* AccessMethod
* Agreement
* Policy
* ComplianceRule

These terms help describe how data products are governed, accessed, controlled, and trusted.

# ODPV Relationships

ODPV Relationships defines reusable relationship terms for graph implementation and portfolio analysis.

The first version includes:

* supports
* requires
* contributesTo
* measures
* belongsTo
* dependsOn
* governedBy
* providedBy
* consumedBy
* indicates

These relationship terms help connect data products, use cases, objectives, KPIs, signals, providers, consumers, policies, and catalogs in a consistent way.

# Companion Vocabulary, Not a Heavy Ontology

ODPV is not intended to be a heavy ontology.

It is a practical controlled vocabulary that gives stable reference terms to the OpenDataProducts.org standards family. Each specification can reference ODPV terms instead of redefining shared concepts locally. Shared terms belong in ODPV. Spec-specific terms stay in the relevant specification. Extensions can define additional domain-specific or organization-specific terms.

# Relationship to ODPS, ODPC, and ODPG

* ODPS defines one data product.
* ODPC defines reusable catalog and portfolio objects.
* ODPG defines relationships between data products, use cases, objectives, KPIs, signals, and other portfolio objects.
* ODPV defines the shared language used by all of them.

Used together, ODPS, ODPC, ODPG, and ODPV create a machine-readable operating model for data product management.

# Why ODPV Matters

ODPV helps prevent terminology drift across the standards family. Without a shared vocabulary, each specification may define terms such as Data Product, Use Case, Objective, KPI, Signal, Owner, SLA, License, or Relationship slightly differently. ODPV gives these terms one stable reference point. This improves:

* Specification alignment
* Graph implementation
* Metadata validation
* Catalog interoperability
* AI-assisted discovery
* GraphRAG context
* Portfolio analysis
* Tool development

# Example Use

* A data product in ODPS can reference ODPV terms for concepts such as DataProduct, Owner, SLA, DataQuality, License, and AccessMethod.
* A catalog in ODPC can reference ODPV terms for concepts such as DataProductCatalog, UseCase, BusinessObjective, KPI, Signal, Gap, and Priority.
* A graph in ODPG can reference ODPV terms for node types and relationship types such as supports, requires, contributesTo, measures, belongsTo, dependsOn, governedBy, providedBy, consumedBy, and indicates.

# Specification Aims

* Define shared terms for data product management.
* Reduce duplicate term definitions across ODPS, ODPC, and ODPG.
* Prevent terminology drift across the standards family.
* Support consistent graph node and relationship naming.
* Support AI-assisted discovery, metadata generation, and GraphRAG.
* Improve interoperability between catalogs, platforms, marketplaces, and tools.
* Provide a lightweight path toward semantic knowledge graph implementation.
* Keep formal ontology work optional.

# Found a Bug?

Found a bug, question, or improvement idea?

Submit an issue or propose changes with a pull request.

# Contributors

Open Data Product Vocabulary is part of the OpenDataProducts.org standards family under the Open Data Product Initiative.

The project is developed as part of the broader work to expand OpenDataProducts.org from one specification into a modular family of standards for data product management.
