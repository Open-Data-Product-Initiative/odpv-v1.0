# Catalog

The `Catalog` object defines a managed collection of ODPC portfolio objects. It provides the container for product references, use cases, business objectives, KPIs, signals, and catalog items.

In ODPC, a catalog is the portfolio-level structure that allows organizations to organize, publish, govern, and exchange reusable catalog objects. A catalog may represent an enterprise data product catalog, a government portfolio catalog, a domain catalog, a marketplace catalog, or a project-specific catalog.

A `Catalog` should provide identity, ownership, scope, lifecycle status, and references to the objects included in the catalog. The catalog does not define relationship semantics between the objects. That belongs to ODPG.

By defining catalogs as machine-readable objects, ODPC supports interoperability between tools, platforms, marketplaces, AI workflows, and graph-based portfolio analysis.

## Attributes and options

> Example of Catalog object usage:

```yml
catalog:
  id: CAT-001
  name:
    en: Smart City Data Product Portfolio Catalog
  description:
    en: Catalog of reusable data product portfolio objects for smart city planning and operations.
  owner:
    organization: Example Smart City Office
    role: Data Product Portfolio Manager
  scope:
    domain: smart-city
    geography: Example City
    audience:
      - internal
      - partner
  version: 1.0.0
  status: active

  productReferences:
    - id: DP-001
      name:
        en: UrbanPulse Events Data Product
      productModel:
        standard: ODPS
        version: 4.1
        format: yaml
      uri: https://example.org/products/urbanpulse-events/odps.yaml
      status: active

    - id: DP-002
      name:
        en: Traffic Flow Data Product
      productModel:
        standard: ODPS
        version: 4.1
        format: yaml
      uri: https://example.org/products/traffic-flow/odps.yaml
      status: active

    - id: DP-003
      name:
        en: Emergency Incident Data Product
      productModel:
        standard: ODPS
        version: 4.1
        format: yaml
      uri: https://example.org/products/emergency-incidents/odps.yaml
      status: active

  useCases:
    - id: UC-001
      name:
        en: Emergency Response Optimization
      expectedOutcome:
        en: Reduce average emergency response time across the city.
      status: active

    - id: UC-002
      name:
        en: Event-Aware Traffic Planning
      expectedOutcome:
        en: Reduce congestion around major event locations.
      status: active

  businessObjectives:
    - id: BO-001
      name:
        en: Reduce Emergency Response Time
      status: active

    - id: BO-002
      name:
        en: Improve Event Mobility
      status: active

  kpis:
    - id: KPI-001
      name:
        en: City Emergency Response Time
      unit: minutes
      target: 5
      direction: at_most
      status: active

    - id: KPI-002
      name:
        en: Event Area Congestion Index
      unit: percentage
      target: -10
      direction: decrease
      status: active

  signals:
    - id: SIG-001
      name:
        en: Rising Incident Delay Signal
      signalType: risk
      severity: high
      status: active

    - id: SIG-002
      name:
        en: High Event Congestion Signal
      signalType: opportunity
      severity: medium
      status: active

  tags:
    - smart-city
    - portfolio
    - data-products
```

| Element | Type | Options | Description |
|---|---|---|---|
| catalog | object | required | Top-level object that defines an ODPC catalog. |
| id | string | required | Stable identifier for the catalog. |
| name | object | language-tagged strings | Human-readable catalog name. |
| description | object | language-tagged strings | Short explanation of the catalog purpose and scope. |
| owner | object | optional | Ownership information for the catalog. |
| organization | string | optional | Organization responsible for the catalog. |
| role | string | optional | Responsible role, such as Data Product Portfolio Manager. |
| scope | object | optional | Defines the business, organizational, geographic, or audience scope of the catalog. |
| domain | string | optional | Domain covered by the catalog. |
| geography | string | optional | Geographic scope of the catalog, when relevant. |
| audience | array of strings | internal, partner, public, commercial | Intended audience for catalog use. |
| version | string | optional | Catalog version. |
| status | string | draft, active, deprecated, retired | Lifecycle status of the catalog. |
| productReferences | array of objects | optional | List of data product references included in the catalog. Each item follows the productReference object schema. |
| useCases | array of objects | optional | List of use cases included in the catalog. Each item follows the useCase object schema. |
| businessObjectives | array of objects | optional | List of business objectives included in the catalog. Each item follows the businessObjective object schema. |
| kpis | array of objects | optional | List of KPIs included in the catalog. Each item follows the kpi object schema. |
| signals | array of objects | optional | List of signals included in the catalog. Each item follows the signal object schema. |
| tags | array of strings | optional | Keywords used for search, grouping, and portfolio analysis. |analysis.                                                      |

