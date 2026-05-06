# BusinessObjective

The `BusinessObjective` object defines a higher-level business, operational, policy, or strategic objective that data products and use cases contribute to. It captures the outcome the organization wants to achieve and provides the portfolio-level anchor for value management.

In ODPC, business objectives help move data product management from asset lists to outcome-driven portfolios. They make it possible to understand which data products support strategic goals, which use cases contribute to measurable outcomes, and where gaps exist.

A `BusinessObjective` can be measured by one or more KPIs. It can also be referenced by use cases, catalog items, or graph relationships. The objective should remain reusable and stable across products and use cases.

By defining objectives as catalog objects, ODPC supports prioritization, investment decisions, governance reviews, AI-assisted portfolio analysis, and reporting on business value.

## Attributes and options

> Example of BusinessObjective object usage:

```yml
businessObjective:
  id: BO-001
  name:
    en: Improve Urban Mobility Efficiency
  description:
    en: Reduce travel delays and improve movement across the city through better data-driven planning and operations.
  strategicAlignment:
    - en: Smart City Vision 2030
    - en: Transport Digital Transformation Program
  owner:
    organization: Example Transport Authority
    team: Business Analytics
    role: Strategy Lead
  expectedOutcomes:
    - en: Shorter average travel times across key corridors.
    - en: Improved public transport reliability.
    - en: Better coordination between road, traffic, and public transport operations.
  kpis:
    - id: KPI-001
      name:
        en: Average Travel Time Reduction
      description:
        en: Measures reduction in average travel time across selected mobility corridors.
      unit: percentage
      baseline:
        value: 0
        date: 2025-10-31
      target:
        value: 10
        date: 2026-12-31
  timeframe:
    startDate: 2026-01-01
    endDate: 2026-12-31
  status: active
  priority: high
```

## Mandatory

| Element             | Type   | Options                           | Description                                                                       |
| ------------------- | ------ | --------------------------------- | --------------------------------------------------------------------------------- |
| `businessObjective` | object | required                          | Top-level object that defines a business objective in ODPC.                       |
| `id`                | string | required                          | Stable identifier for the business objective.                                     |
| `name`              | object | required, language-tagged strings | Human-readable business objective name.                                           |
| `name.en`           | string | required                          | English name of the business objective.                                           |
| `description`       | object | required, language-tagged strings | Short explanation of the business objective, its purpose, and expected direction. |
| `description.en`    | string | required                          | English description of the business objective.                                    |

## Optional 

| Element                | Type             | Options                           | Description                                                                                                                                                     |
| ---------------------- | ---------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `strategicAlignment`   | array of objects | optional                          | Strategic programs, policies, visions, mandates, or transformation initiatives the business objective supports.                                                 |
| `strategicAlignment[]` | object           | language-tagged strings           | One strategic alignment statement.                                                                                                                              |
| `owner`                | object           | optional                          | Ownership information for the business objective.                                                                                                               |
| `owner.organization`   | string           | optional                          | Organization responsible for the business objective.                                                                                                            |
| `owner.team`           | string           | optional                          | Team responsible for the business objective.                                                                                                                    |
| `owner.role`           | string           | optional                          | Responsible role, such as Strategy Lead, Product Owner, or Performance Lead.                                                                                    |
| `expectedOutcomes`     | array of objects | optional                          | Business outcomes expected from achieving the objective.                                                                                                        |
| `expectedOutcomes[]`   | object           | language-tagged strings           | One expected outcome statement.                                                                                                                                 |
| `kpis`                 | array of objects | optional                          | Measurable indicators used to track progress against the business objective. KPIs are nested inside `businessObjective`, not defined as top-level ODPC objects. |
| `kpis.id`              | string           | optional                          | Stable identifier for the KPI within the business objective.                                                                                                    |
| `kpis.name`            | object           | optional, language-tagged strings | Human-readable KPI name.                                                                                                                                        |
| `kpis.description`     | object           | optional, language-tagged strings | Explanation of what the KPI measures.                                                                                                                           |
| `kpis.unit`            | string           | optional                          | Unit used for the KPI value, such as `percentage`, `count`, `days`, `AED`, or `score`.                                                                          |
| `kpis.baseline`        | object           | optional                          | Starting measurement used as the comparison point.                                                                                                              |
| `kpis.baseline.value`  | number           | optional                          | Baseline value.                                                                                                                                                 |
| `kpis.baseline.date`   | date             | optional                          | Date when the baseline value was measured.                                                                                                                      |
| `kpis.target`          | object           | optional                          | Target measurement expected for the KPI.                                                                                                                        |
| `kpis.target.value`    | number           | optional                          | Target value.                                                                                                                                                   |
| `kpis.target.date`     | date             | optional                          | Date when the target should be reached.                                                                                                                         |
| `timeframe`            | object           | optional                          | Time period during which the business objective is active or expected to be achieved.                                                                           |
| `timeframe.startDate`  | date             | optional                          | Start date for the business objective.                                                                                                                          |
| `timeframe.endDate`    | date             | optional                          | End date for the business objective.                                                                                                                            |
| `status`               | string           | optional                          | Lifecycle status of the business objective, such as `draft`, `active`, `paused`, `completed`, or `retired`.                                                     |
| `priority`             | string           | optional                          | Relative importance of the business objective, such as `low`, `medium`, `high`, or `critical`.                                                                  |
