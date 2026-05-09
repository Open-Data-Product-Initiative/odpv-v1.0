# ODPV Value

ODPV Value defines the terms used to describe why data products matter, where they create value, and how that value connects to business outcomes.

These terms help connect data products to use cases, objectives, KPIs, signals, gaps, opportunities, risks, and benefits. They make the vocabulary useful beyond technical metadata by linking data products to planning, prioritization, investment, and measurable impact.

The value vocabulary supports portfolio-level thinking. It helps teams describe which data products are needed, which use cases they support, what outcomes they contribute to, and where new opportunities or gaps exist.

Each term has one canonical ODPV name. Also known as terms help users map familiar business language to the official vocabulary. Related terms show nearby concepts that are connected but should not be treated as identical.

Example value term:

```yml
id: BusinessObjective
uri: https://opendataproducts.org/odpv-v1.0/terms/BusinessObjective
type: object
status: stable
introducedIn: 1.0.0
preferredLabel:
  en: Business Objective
definition:
  en: A business goal or intended outcome that data products, 
      use cases, or portfolio actions support.
alsoKnownAs:
  en:
    - objective
    - business goal
    - strategic goal
    - target outcome
relatedTerms:
  - Outcome
  - KPI
  - Impact
  - UseCase
usedIn:
  - ODPC
  - ODPG
```

| Term                | Type           | Description                                                                                                                                | Also known as                                                                   | Related terms                                             | Used in    |
| ------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------- |
| `UseCase`           | object         | A practical business, operational, analytical, or technical scenario where one or more data products are used to create value.             | use case, scenario, business scenario, application case                         | `DataProduct`, `BusinessObjective`, `DataNeed`, `Outcome` | ODPC, ODPG |
| `BusinessObjective` | object         | A business goal or intended outcome that data products, use cases, or portfolio actions support.                                           | objective, business goal, strategic goal, target outcome                        | `Outcome`, `KPI`, `Impact`, `UseCase`                     | ODPC, ODPG |
| `KPI`               | object         | A measurable indicator used to track progress toward a business objective, outcome, or portfolio goal.                                     | key performance indicator, metric, performance measure, success measure         | `BusinessObjective`, `Outcome`, `Impact`                  | ODPC, ODPG |
| `Impact`            | object         | The expected or observed effect created by a data product, use case, signal, or portfolio decision.                                        | effect, value impact, business impact, observed effect                          | `Outcome`, `Benefit`, `KPI`, `ValueProposition`           | ODPC, ODPG |
| `Signal`            | object         | An observed demand, trend, risk, gap, usage pattern, policy change, market change, or operational event that may require action.           | market signal, demand signal, trigger, observation                              | `Demand`, `Risk`, `Gap`, `Opportunity`                    | ODPC, ODPG |
| `Gap`               | object         | A missing data product, dataset, capability, quality level, access method, relationship, or portfolio coverage area.                       | missing capability, coverage gap, data gap, portfolio gap                       | `DataNeed`, `Opportunity`, `Signal`, `Priority`           | ODPC, ODPG |
| `Priority`          | classification | A ranking or importance level used to guide portfolio planning, product development, investment, or remediation.                           | importance level, ranking, urgency, priority level                              | `PortfolioPriority`, `Signal`, `Gap`, `Risk`              | ODPC, ODPG |
| `Outcome`           | object         | A desired or achieved result connected to a business objective, use case, KPI, or impact statement.                                        | result, target result, achieved result, intended outcome                        | `BusinessObjective`, `KPI`, `Impact`, `Benefit`           | ODPC, ODPG |
| `DataNeed`          | object         | A required data input, data product, dataset, attribute, capability, or access pattern needed to support a use case or objective.          | data requirement, data demand, required data, information need                  | `UseCase`, `Gap`, `Demand`, `DataProduct`                 | ODPC, ODPG |
| `Benefit`           | object         | A positive business, operational, financial, social, or technical value expected from a data product, use case, or portfolio action.       | value, expected benefit, positive impact, business benefit                      | `Impact`, `Outcome`, `ValueProposition`                   | ODPC       |
| `Demand`            | object         | Evidence of need or interest from consumers, stakeholders, systems, markets, policies, or operational processes.                           | need, interest, request, demand signal                                          | `Signal`, `DataNeed`, `Opportunity`, `UseCase`            | ODPC, ODPG |
| `Opportunity`       | object         | A possible area for value creation, reuse, innovation, service improvement, monetization, or better decision-making.                       | value opportunity, improvement area, innovation opportunity, reuse opportunity  | `Signal`, `Gap`, `Benefit`, `Impact`                      | ODPC, ODPG |
| `Risk`              | object         | A possible negative event, weakness, exposure, or uncertainty that may affect data product value, trust, access, compliance, or operation. | issue, exposure, threat, concern                                                | `Signal`, `Priority`, `Gap`, `Governance`                 | ODPC, ODPG |
| `ValueProposition`  | object         | A short explanation of why a data product, use case, or portfolio item matters and what value it is expected to create.                    | value statement, value case, product value, business value statement            | `Benefit`, `Impact`, `Outcome`, `UseCase`                 | ODPS, ODPC |
| `PortfolioPriority` | classification | A portfolio-level priority assigned to a data product, use case, signal, gap, or objective.                                                | portfolio ranking, portfolio importance, investment priority, planning priority | `Priority`, `Gap`, `Signal`, `BusinessObjective`          | ODPC, ODPG |

[Suggest addition to the vocabulary](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/issues) 
