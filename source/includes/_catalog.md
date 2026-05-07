# Catalog

The `Catalog` object defines a reusable ODPC catalog. It provides the top-level structure for organizing product references, use cases, business objectives, signals, tags, ownership, scope, lifecycle status, and graph location.

In ODPC, the `Catalog` object acts as the portfolio container. It helps organizations group related data products and demand-side objects around a domain, organization, geography, audience, or strategic theme.

The `Catalog` object can include product references, use cases, business objectives, and signals directly as reusable catalog objects. It can also point to an ODPG graph through the `graph` attribute. The graph defines the relationships between catalog objects, such as which products support which use cases, which use cases contribute to which objectives, and where gaps exist.

The `Catalog` object should remain focused on catalog structure and portfolio organization. It should not define detailed product metadata, relationship semantics, or graph edges. Detailed product definitions belong to product models such as ODPS. Relationship modeling belongs to ODPG.

By defining catalogs as reusable objects, ODPC supports discovery, portfolio browsing, governance review, prioritization, filtering, AI-assisted portfolio analysis, and reporting across data product ecosystems.

## Mandatory attributes and options

> Example of catalog object usage:

```yml
catalog:
  id: CAT-001
  name:
    en: Urban Mobility Data Product Catalog
  description:
    en: Catalog of data products, use cases, objectives, and signals related to urban mobility.
```


| Attribute | Type | Required | Description |
|---|---|---:|---|
| `catalog` | object | ✓ | Top-level object that defines an ODPC catalog. |
| `id` | string | ✓ | Stable identifier for the catalog. |
| `name` | object | ✓ | Human-readable catalog name using language-tagged strings. |
| `name.en` | string | ✓ | English catalog name. |
| `description` | object | ✓ | Short explanation of the catalog purpose and scope using language-tagged strings. |
| `description.en` | string | ✓ | English catalog description. |


## Optional attributes and options

> Example of catalog object usage:

```yml
catalog:
  id: CAT-001
  name:
    en: Urban Mobility Data Product Catalog
  description:
    en: Catalog of data products, use cases, objectives, and signals related to urban mobility.

  owner:
    organization: Example Transport Authority
    team: Business Analytics
    role: Data Product Portfolio Manager

  scope:
    domains:
      - smart-city
      - mobility
      - transport
    geography: Abu Dhabi
    audience:
      - internal
      - public

  version: "1.0.0"
  status: active

  graph:
    standard: ODPG
    version: "1.0"
    uri: https://example.org/graphs/urban-mobility.graph.yaml

  productReferences:
    - id: DP-001
      productID: urbanpulse-events
      productVersion: "1.0.0"
      name:
        en: UrbanPulse Events Data Product
      description:
        en: Data product providing event information for urban analytics and citizen services.
      productModel:
        standard: ODPS
        version: "4.1"
        format: yaml
        uri: https://example.org/products/urbanpulse-events/odps.yaml

  useCases:
    - id: UC-001
      name:
        en: Event Demand Forecasting
      description:
        en: Forecast event-related demand to improve mobility planning and citizen services.

  businessObjectives:
    - id: BO-001
      name:
        en: Improve Urban Mobility Efficiency
      description:
        en: Reduce travel delays and improve movement across the city through better data-driven planning and operations.

  signals:
    - id: SIG-001
      name:
        en: Increasing Event Demand
      description:
        en: Indicates rising demand for event-related mobility and public service planning.

  tags:
    - smart-city
    - mobility
    - events
```

| Attribute | Type | Required | Description |
|---|---|---:|---|
| `owner` | object |  | Ownership information for the catalog. |
| `owner.organization` | string |  | Organization responsible for the catalog. |
| `owner.team` | string |  | Team responsible for the catalog. |
| `owner.role` | string |  | Responsible role, such as `Data Product Portfolio Manager`. |
| `scope` | object |  | Business, organizational, geographic, or audience scope of the catalog. |
| `scope.domains` | array of strings |  | Domains covered by the catalog. |
| `scope.geography` | string |  | Geographic scope of the catalog, if relevant. |
| `scope.audience` | array of strings |  | Intended audience for catalog use, such as `internal`, `partner`, `public`, or `commercial`. |
| `version` | string |  | Catalog version. |
| `status` | string |  | Lifecycle status of the catalog, such as `draft`, `active`, `deprecated`, or `retired`. |
| `graph` | object |  | Defines the graph specification used to describe relationships between catalog objects. |
| `graph.standard` | string |  | Graph standard used for the catalog graph. Default is `ODPG` for Open Data Product Graphs. Other options: `RDF` for semantic web graphs, `JSON-LD` for linked data in JSON, `GraphML` for graph exchange, `openCypher` for property graph scripts, `GQL` for ISO property graph queries, `Gremlin` for graph traversal, `GraphSON` for TinkerPop-style graph JSON, or `GeoSPARQL` for geospatial RDF graphs. |
| `graph.version` | string | ✓ when `graph` is used | Version of the graph standard. |
| `graph.uri` | string | ✓ when `graph` is used | URI pointing to the graph definition. |
| `productReferences` | array of objects |  | List of data product references included in the catalog. Each item follows the `ProductReference` object schema. |
| `useCases` | array of objects |  | List of use cases included in the catalog. Each item follows the `UseCase` object schema. |
| `businessObjectives` | array of objects |  | List of business objectives included in the catalog. Each item follows the `BusinessObjective` object schema. |
| `signals` | array of objects |  | List of signals included in the catalog. Each item follows the `Signal` object schema. |
| `tags` | array of strings |  | Keywords used for search, grouping, filtering, and portfolio analysis. |
