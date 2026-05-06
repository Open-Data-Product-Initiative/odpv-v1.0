# UseCase

The `UseCase` object describes a business, operational, analytical, or policy use case that needs data products. It captures why data is needed, who needs it, what decision or process it supports, and what outcome is expected.

In ODPC, a use case is a demand-side portfolio object. It helps organizations understand where data products create value and which business needs the portfolio should support.

A `UseCase` can describe required data through `dataNeeds`, but it should not directly reference data products. Connections between use cases, data products, business objectives, and signal belong to Open Data Product Graphs (ODPG).

ODPG defines graphs and connections between catalog objects. It is used to model relationships such as which data products support a use case, which use cases contribute to a business objective, and where portfolio gaps exist.

The `UseCase` object should remain focused on the use case itself, not on detailed relationship semantics.

By defining use cases as reusable catalog objects, ODPC enables discovery, prioritization, gap analysis, reuse analysis, and AI-assisted planning across data product portfolios.

## Mandatory attributes and options

> Example of BusinessObjective object usage:

```yml
useCase:
  id: UC-001
  name:
    en: Predictive Maintenance for Aircraft Fleet
  description:
    en: Predict maintenance needs earlier by combining 
        aircraft usage, schedules, and maintenance history.
```

| Attribute        | Type   | Options                           | Description                                                         |
| ---------------- | ------ | --------------------------------- | ------------------------------------------------------------------- |
| `useCase`        | object | required                          | Top-level object that defines a use case in ODPC.                   |
| `id`             | string | required                          | Stable identifier for the use case.                                 |
| `name`           | object | required, language-tagged strings | Human-readable use case name.                                       |
| `name.en`        | string | required                          | English name of the use case.                                       |
| `description`    | object | required, language-tagged strings | Short explanation of the use case, its purpose, and expected value. |
| `description.en` | string | required                          | English description of the use case.                                |


## Optional attributes and options

> Example of BusinessObjective object usage:

```yml
useCase:
  id: UC-001
  name:
    en: Predictive Maintenance for Healthcare Revenue Growth

  description:
    en: Predict equipment maintenance needs in healthcare facilities to reduce downtime, improve service reliability, and support revenue growth.

  domains:
    - healthcare
    - operations
    - revenue management

  stakeholders:
    - Healthcare Administrators
    - CFOs
    - Revenue Managers
    - Maintenance Engineers
    - Operations Managers
    - Safety Officers
    - Data Analysts

  businessChallenge:
    en: Healthcare organizations face operational disruptions from equipment failures, leading to service delays, safety risks, and lost revenue.

  decision:
    en: Schedule healthcare equipment maintenance proactively based on equipment usage, failure patterns, and patient service demand.

  expectedOutcome:
    en: Reduce equipment downtime, improve patient service continuity, reduce maintenance costs, and support measurable revenue growth.

  kpis:
    - Revenue growth from improved equipment uptime
    - Equipment downtime reduction
    - Maintenance cost reduction
    - On-time service performance
    - Patient service utilization rate

  impactMetrics:
    - Cost savings from reduced reactive repairs
    - Increased revenue from higher patient service availability
    - Improved on-time service performance
    - Enhanced safety and reduced operational disruption

  dataNeeds:
    summary:
      en: Combines revenue data, equipment sensor readings, maintenance logs, patient utilization metrics, and market trends to forecast failures and optimize service planning.
    items:
      - Historical revenue and cost data by service line
      - Patient visit records and demographics
      - Market competition analysis and pricing benchmarks
      - Service quality feedback and patient satisfaction scores
      - Real-time equipment sensor readings
      - Historical maintenance and failure logs
      - Equipment usage schedules
      - Inventory levels for parts availability

  scoring:
    businessValue: high
    effort: medium
    category: juicyAndWorthIt
    score: 3.0

  status: active
  priority: high

  tags:
    - predictive-maintenance
    - healthcare
    - revenue-growth
    - operations
```

| Attribute               | Type             | Options                           | Description                                                                                          |
| ----------------------- | ---------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `domains`               | array of strings | optional                          | Business, operational, policy, or industry domains related to the use case.                          |
| `stakeholders`          | array of strings | optional                          | People, teams, roles, or groups involved in or affected by the use case.                             |
| `businessChallenge`     | object           | optional, language-tagged strings | Business, operational, policy, or service problem the use case addresses.                            |
| `businessChallenge.en`  | string           | optional                          | English business challenge statement.                                                                |
| `decision`              | object           | optional, language-tagged strings | Decision, action, or operational choice the use case supports.                                       |
| `decision.en`           | string           | optional                          | English decision statement.                                                                          |
| `expectedOutcome`       | object           | optional, language-tagged strings | Expected business, operational, policy, or service outcome.                                          |
| `expectedOutcome.en`    | string           | optional                          | English expected outcome statement.                                                                  |
| `kpis`                  | array of strings | optional                          | KPI or key result labels used to assess the value or success of the use case.                        |
| `impactMetrics`         | array of strings | optional                          | Measurable or observable impact areas expected from the use case.                                    |
| `dataNeeds`             | object           | optional                          | Data required to support the use case.                                                               |
| `dataNeeds.summary`     | object           | optional, language-tagged strings | Short summary of the overall data requirement.                                                       |
| `dataNeeds.summary.en`  | string           | optional                          | English summary of the data requirement.                                                             |
| `dataNeeds.items`       | array of strings | optional                          | Individual data needs, expressed as plain strings.                                                   |
| `scoring`               | object           | optional                          | Evaluation of the use case for prioritization or portfolio review.                                   |
| `scoring.businessValue` | string           | optional                          | Estimated business value, such as `low`, `medium`, `high`, or `critical`.                            |
| `scoring.effort`        | string           | optional                          | Estimated implementation effort, such as `low`, `medium`, or `high`.                                 |
| `scoring.category`      | string           | optional                          | Portfolio scoring category, such as `quickWins`, `juicyAndWorthIt`, `niceToHave`, or `avoidOrDefer`. |
| `scoring.score`         | number           | optional                          | Numeric score used for prioritization, ranking, or portfolio analysis.                               |
| `status`                | string           | optional                          | Lifecycle status of the use case, such as `draft`, `active`, `paused`, `completed`, or `retired`.    |
| `priority`              | string           | optional                          | Relative importance of the use case, such as `low`, `medium`, `high`, or `critical`.                 |
| `tags`                  | array of strings | optional                          | Keywords used to classify, search, or filter the use case.                                           |

