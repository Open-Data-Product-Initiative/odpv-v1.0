# Signal

The `Signal` object describes an observed market, operational, user, technology, policy, competitive, quality, usage, risk, or gap indicator that may create demand for new use cases, new data products, or product improvements.

In ODPC, a `Signal` acts as the voice of opportunity. It helps organizations capture what is changing around them or inside their operations, then use that intelligence to guide portfolio planning, prioritization, and product development.

A `Signal` can come from internal sources such as search logs, usage analytics, support tickets, surveys, and operational systems. It can also come from external sources such as AI web crawling, competitor monitoring, market reports, public tenders, policy changes, technology trends, or sector analysis.

The `Signal` object should describe what was observed, where it came from, how strong it is, how confident the organization is, what opportunity it suggests, and what action should be considered.

The `Signal` object should not directly define relationships to products, use cases, business objectives, or other catalog objects. Those connections belong to Open Data Product Graphs (ODPG), which defines the graphs and relationships between catalog objects.

By defining signals as reusable catalog objects, ODPC supports opportunity discovery, market intelligence, gap analysis, portfolio prioritization, AI-assisted planning, and continuous alignment between data products and changing business needs.

## Mandatory attributes and options

> Example of catalog object usage:

```yml
signal:
  id: SIG-001
  name:
    en: Competitors expanding real-time event intelligence
  description:
    en: External market monitoring found that competing smart city platforms are adding real-time event intelligence features.
  type: competitive
  source:
    origin: external
    method: ai_crawl
  observedAt: 2026-04-18T09:30:00Z
```


| Attribute        | Type     | Required | Description                                                                                  |
| ---------------- | -------- | -------: | -------------------------------------------------------------------------------------------- |
| `signal`         | object   |        ✓ | Top-level object that defines an ODPC signal.                                                |
| `id`             | string   |        ✓ | Stable identifier for the signal.                                                            |
| `name`           | object   |        ✓ | Human-readable signal name using language-tagged strings.                                    |
| `name.en`        | string   |        ✓ | English signal name.                                                                         |
| `description`    | object   |        ✓ | Short explanation of what was observed and why it matters, using language-tagged strings.    |
| `description.en` | string   |        ✓ | English signal description.                                                                  |
| `type`           | string   |        ✓ | Signal type. One of: `demand`, `competitive`, `market`, `technology`, `policy`, `operational`, `quality`, `usage`, `risk`, or `gap`.          |
| `source`         | object   |        ✓ | Source information that explains where the signal came from.                                 |
| `source.origin`  | string   |        ✓ | Origin of the signal, such as `internal`, `external`, or `mixed`.                            |
| `source.method`  | string   |        ✓ | Method used to detect the signal, such as `ai_crawl`, `search_analysis`, `usage_analysis`, `survey`, `manual_review`, or `system_monitoring`. |
| `observedAt`     | datetime |        ✓ | Date and time when the signal was observed.                                                  |

## Type explained

| Type          | Meaning                                                                         |
| ------------- | ------------------------------------------------------------------------------- |
| `demand`      | Users, customers, or stakeholders show demand for data, use cases, or products. |
| `competitive` | Competitors or peer organizations are moving in a relevant direction.           |
| `market`      | Market behavior suggests new demand or value potential.                         |
| `technology`  | Technology change creates a new product or use case opportunity.                |
| `policy`      | Regulation, policy, or strategy creates new demand or obligations.              |
| `operational` | Internal operations show need for better data or decisions.                     |
| `quality`     | Quality issues create risk or improvement opportunities.                        |
| `usage`       | Product usage or non-usage reveals demand, friction, or value.                  |
| `risk`        | A risk appears that may affect trust, compliance, delivery, or operations.      |
| `gap`         | A missing product, missing data, or unmet capability is detected.               |


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

| Attribute                | Type             | Required | Description                                                                                                                                                 |
| ------------------------ | ---------------- | -------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source.system`          | string           |          | System, tool, agent, or platform that detected or produced the signal.                                                                                      |
| `source.channel`         | string           |          | Channel where the signal was observed, such as `public_web`, `search_queries`, `usage_logs`, `support_tickets`, `market_report`, or `stakeholder_feedback`. |
| `source.reference`       | string           |          | Source reference, such as a report ID, crawl ID, log reference, URL, or document reference.                                                                 |
| `strength`               | string           |          | Estimated strength of the signal, such as `low`, `medium`, `high`, or `critical`.                                                                           |
| `confidence`             | string           |          | Confidence in the signal, such as `low`, `medium`, or `high`.                                                                                               |
| `opportunity`            | object           |          | Opportunity suggested by the signal, using language-tagged strings.                                                                                         |
| `opportunity.en`         | string           |          | English opportunity statement.                                                                                                                              |
| `impact`                 | object           |          | Expected impact or relevance of the signal.                                                                                                                 |
| `impact.valuePotential`  | string           |          | Estimated value potential, such as `low`, `medium`, `high`, or `critical`.                                                                                  |
| `impact.urgency`         | string           |          | Estimated urgency, such as `low`, `medium`, `high`, or `critical`.                                                                                          |
| `impact.affectedDomains` | array of strings |          | Domains affected by the signal.                                                                                                                             |
| `evidence`               | object           |          | Evidence supporting the signal.                                                                                                                             |
| `evidence.summary`       | object           |          | Short evidence summary using language-tagged strings.                                                                                                       |
| `evidence.summary.en`    | string           |          | English evidence summary.                                                                                                                                   |
| `evidence.examples`      | array of strings |          | Concrete examples that support the signal.                                                                                                                  |
| `recommendedAction`      | object           |          | Recommended action based on the signal, using language-tagged strings.                                                                                      |
| `recommendedAction.en`   | string           |          | English recommended action.                                                                                                                                 |
| `status`                 | string           |          | Signal lifecycle status, such as `new`, `reviewing`, `accepted`, `rejected`, `converted`, or `archived`.                                                    |
| `tags`                   | array of strings |          | Keywords used to classify, search, or filter the signal.                                                                                                    |

