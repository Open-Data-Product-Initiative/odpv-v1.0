# ODPV Relationships

<!-- AI_SECTION_GUIDANCE:
This section defines ODPV relationship term names and meanings.
Use these relationship ids as controlled vocabulary terms for graph edges.
ODPG defines how these relationship types are used in graph structures; ODPV only defines the shared names, labels, and definitions.
ODPG documentation: https://opendataproducts.org/odpg-v1.0/
-->

ODPV defines the names and meanings of relationship types. [ODPG](https://opendataproducts.org/odpg-v1.0/) defines how those relationship types are used in graph structures. In other words, ODPV defines the vocabulary. [ODPG](https://opendataproducts.org/odpg-v1.0/) defines the graph model.

ODPV Relationships defines the terms used to connect data products, catalogs, use cases, objectives, KPIs, signals, governance objects, and related portfolio items.

These terms describe how objects support, require, measure, govern, depend on, replace, or relate to each other. They turn separate vocabulary terms into a connected model that AI tools, catalogs, graph systems, and portfolio applications can understand.

The relationship vocabulary is especially important for [ODPG](https://opendataproducts.org/odpg-v1.0/). It provides the shared relationship types needed to build data product graphs, trace value paths, identify gaps, and connect data products to business outcomes.

Each relationship term has one canonical ODPV name. Also known as terms help users map familiar relationship language to the official vocabulary. Related terms show nearby relationship types that are connected but should not be treated as identical.

> Snippet of YAML version:

```yml
id: supports
uri: https://opendataproducts.org/odpv-v1.0/terms/supports
type: relationship
status: stable
introducedIn: 1.0.0
preferredLabel:
  en: supports
definition:
  en: Indicates that one object helps enable, serve, or 
      make another object possible, such as a data product 
      supporting a use case.
alsoKnownAs:
  en:
    - enables
    - serves
    - helps
    - provides support for
relatedTerms:
  - contributesTo
  - requires
  - relatedTo
usedIn:
  - ODPG
```

| Term            | Type         | Description                                                                                                                                   | Also known as                                                    | Related terms                                      | Used in |
| --------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------- | ------- |
| `supports`      | relationship | Indicates that one object helps enable, serve, or make another object possible, such as a data product supporting a use case.                 | enables, serves, helps, provides support for                     | `contributesTo`, `requires`, `relatedTo`           | ODPG    |
| `requires`      | relationship | Indicates that one object needs another object to be complete, useful, or executable, such as a use case requiring a data product.            | needs, depends on, must have, requires input from                | `dependsOn`, `supports`, `DataNeed`                | ODPG    |
| `contributesTo` | relationship | Indicates that one object helps advance another object, such as a use case contributing to a business objective.                              | advances, helps achieve, adds value to, supports progress toward | `supports`, `measures`, `BusinessObjective`        | ODPG    |
| `measures`      | relationship | Indicates that one object measures another object, such as a KPI measuring a business objective or outcome.                                   | tracks, monitors, evaluates, assesses                            | `KPI`, `Outcome`, `BusinessObjective`              | ODPG    |
| `belongsTo`     | relationship | Indicates that one object is assigned to, grouped under, or included in another object, such as a data product belonging to a catalog.        | assigned to, grouped under, included in, cataloged under         | `partOf`, `hasPart`, `DataProductCatalog`          | ODPG    |
| `dependsOn`     | relationship | Indicates that one object has a dependency on another object, such as a data product depending on another product, service, or dataset.       | relies on, has dependency on, uses dependency, is dependent on   | `requires`, `relatedTo`, `derivedFrom`             | ODPG    |
| `governedBy`    | relationship | Indicates that one object is governed by another object, such as a data product governed by a license, policy, agreement, or compliance rule. | controlled by, regulated by, subject to, under governance of     | `Policy`, `License`, `Agreement`, `ComplianceRule` | ODPG    |
| `providedBy`    | relationship | Indicates that one object is provided, published, or made available by a provider.                                                            | published by, supplied by, made available by, offered by         | `Provider`, `Owner`, `Steward`                     | ODPG    |
| `consumedBy`    | relationship | Indicates that one object is used, accessed, or consumed by a consumer.                                                                       | used by, accessed by, received by, consumed by                   | `Consumer`, `AccessMethod`, `UsageRights`          | ODPG    |
| `indicates`     | relationship | Indicates that one object points to, reveals, or suggests another object, such as a signal indicating a gap, demand, risk, or opportunity.    | points to, suggests, reveals, signals                            | `Signal`, `Gap`, `Demand`, `Risk`, `Opportunity`   | ODPG    |
| `relatedTo`     | relationship | Indicates a general relationship between two objects when a more specific relationship type is not available.                                 | associated with, connected to, linked to, relevant to            | `supports`, `dependsOn`, `partOf`                  | ODPG    |
| `partOf`        | relationship | Indicates that one object is part of a larger object, such as a catalog item being part of a catalog.                                         | component of, included in, member of, belongs within             | `hasPart`, `belongsTo`, `DataProductCatalog`       | ODPG    |
| `hasPart`       | relationship | Indicates that one object contains or includes another object.                                                                                | contains, includes, has component, consists of                   | `partOf`, `belongsTo`, `Dataset`                   | ODPG    |
| `derivedFrom`   | relationship | Indicates that one object is derived from another object, such as an insight, product, dataset, or signal derived from a source.              | based on, sourced from, generated from, created from             | `dependsOn`, `Reference`, `Dataset`                | ODPG    |
| `replaces`      | relationship | Indicates that one object replaces another object, such as a newer data product replacing an older version.                                   | supersedes, succeeds, takes over from, replaces version          | `versionOf`, `derivedFrom`, `relatedTo`            | ODPG    |
| `versionOf`     | relationship | Indicates that one object is a version of another object.                                                                                     | variant of, release of, revision of, versioned form of           | `replaces`, `derivedFrom`, `Identifier`            | ODPG    |

[Suggest addition to the vocabulary](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/issues) 
