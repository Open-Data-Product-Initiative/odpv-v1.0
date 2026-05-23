# ODPV Governance

ODPV Governance defines the terms used to describe how data products are controlled, protected, accessed, licensed, and operated.

These terms help connect data products to quality expectations, service commitments, access rules, usage rights, policies, compliance requirements, and responsibility models. They make governance visible as part of the product vocabulary instead of treating it as separate documentation.

The governance vocabulary supports trusted reuse. It helps teams describe who is accountable, what rules apply, how access works, what consumers are allowed to do, and what obligations must be followed.

Each term has one canonical ODPV name. Also known as terms help users map familiar governance, legal, operational, and technical language to the official vocabulary. Related terms show nearby concepts that are connected but should not be treated as identical.

> Snippet of YAML version:

```yml
id: DataQuality
uri: https://opendataproducts.org/odpv-v1.0/terms/DataQuality
type: object
status: stable
introducedIn: 1.0.0
preferredLabel:
  en: Data Quality
definition:
  en: The expected, measured, or reported quality of a data product, 
      dataset, distribution, or data service.
alsoKnownAs:
  en:
    - quality
    - data quality score
    - quality assessment
    - quality metrics
relatedTerms:
  - SLA
  - DataContract
  - Stewardship
  - ComplianceRule
usedIn:
  - ODPS
  - ODPC
  - ODPG
```

| Term                | Type           | Description                                                                                                                                                                     | Also known as                                                                            | Related terms                                                           | Used in          |
| ------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------- |
| `DataQuality`       | object         | The expected, measured, or reported quality of a data product, dataset, distribution, or data service.                                                                          | quality, data quality score, quality assessment, quality metrics                         | `SLA`, `DataContract`, `Stewardship`, `ComplianceRule`                  | ODPS, ODPC, ODPG |
| `SLA`               | object         | A service-level agreement or expectation that defines operational commitments for a data product, distribution, or data service.                                                | service level agreement, service commitment, operational commitment, service expectation | `DataQuality`, `Agreement`, `AccessMethod`, `DataContract`              | ODPS, ODPG       |
| `License`           | object         | The legal terms that define how a data product, dataset, distribution, or data service may be used, shared, or redistributed.                                                   | license, data license, usage license, legal license, redistribution terms                | `UsageRights`, `Agreement`, `DataAgreement`, `Policy`                   | ODPS, ODPC, ODPG |
| `DataAccess`        | object         | The access configuration or access description for a data product, dataset, distribution, or data service.                                                                      | dataAccess, data access, access configuration, access description                        | `AccessMethod`, `AccessCondition`, `DataService`, `Distribution`        | ODPS, ODPC, ODPG |
| `AccessMethod`      | object         | The method used to access a data product, dataset, distribution, or data service, such as API, file download, query endpoint, or platform access.                               | access channel, delivery method, access interface, data access method                    | `AccessCondition`, `DataService`, `Distribution`, `SLA`                 | ODPS, ODPC, ODPG |
| `PricingPlan`       | object         | A pricing, cost, subscription, or commercial plan that describes how a data product or data service may be paid for, charged, or monetized.                                     | pricingPlans, pricing plan, commercial plan, subscription plan                           | `Agreement`, `License`, `UsageRights`, `PaymentGateway`                 | ODPS             |
| `PaymentGateway`    | object         | A payment integration, payment service, or gateway used to process commercial access to a data product or data service.                                                        | paymentGateways, payment gateway, payment integration, payment service                   | `PricingPlan`, `Agreement`, `DataAccess`, `DataService`                 | ODPS             |
| `Support`           | object         | The support model or contact channel for help, issue handling, or operational assistance related to a data product or data service.                                            | support, product support, support contact, help channel                                  | `SLA`, `Stewardship`, `Owner`, `DataService`                            | ODPS             |
| `Agreement`         | object         | A formal or informal agreement that defines usage, commercial, legal, operational, or governance terms for a data product or data exchange.                                     | data agreement, usage agreement, service agreement, commercial agreement                 | `DataAgreement`, `License`, `UsageRights`, `SLA`                        | ODPS, ODPC, ODPG |
| `Policy`            | object         | A rule, guideline, or governance statement that applies to a data product, catalog, graph, use case, access method, or related object.                                          | governance policy, rule, guideline, control policy                                       | `ComplianceRule`, `GovernanceProfile`, `AccessCondition`, `Sensitivity` | ODPS, ODPC, ODPG |
| `ComplianceRule`    | object         | A specific rule or requirement used to assess, enforce, or document compliance.                                                                                                 | compliance requirement, control rule, regulatory rule, validation rule                   | `Policy`, `GovernanceProfile`, `DataQuality`, `Risk`                    | ODPS, ODPC, ODPG |
| `Sensitivity`       | classification | A classification that indicates how sensitive a data product, dataset, attribute, distribution, or service is from a privacy, security, commercial, or operational perspective. | sensitivity level, data sensitivity, security classification, privacy classification     | `Policy`, `AccessCondition`, `UsageRights`, `GovernanceProfile`         | ODPS, ODPC       |
| `UsageRights`       | object         | The rights granted to consumers for using, sharing, modifying, deriving, or redistributing a data product or dataset.                                                           | use rights, permitted use, usage permissions, allowed use                                | `License`, `Agreement`, `DataAgreement`, `AccessCondition`              | ODPS, ODPC       |
| `Retention`         | object         | The rules or expectations for how long data, metadata, logs, agreements, or related records should be retained.                                                                 | retention rule, retention period, record retention, data retention                       | `Policy`, `ComplianceRule`, `DataAgreement`, `Stewardship`              | ODPS, ODPC       |
| `AccessCondition`   | object         | A condition that must be met before a consumer can access a data product, dataset, distribution, or data service.                                                               | access rule, access requirement, eligibility condition, access constraint                | `AccessMethod`, `UsageRights`, `Policy`, `Sensitivity`                  | ODPS, ODPC, ODPG |
| `GovernanceProfile` | classification | A reusable governance classification that describes the expected level of control, assurance, review, or operational maturity for a data product or catalog item.               | governance level, assurance profile, control profile, maturity profile                   | `Policy`, `ComplianceRule`, `Sensitivity`, `Stewardship`                | ODPS, ODPC       |
| `DataAgreement`     | object         | A structured agreement that defines the allowed use, responsibilities, obligations, and constraints for a data product or data exchange.                                        | data sharing agreement, data usage agreement, data exchange agreement, product agreement | `Agreement`, `License`, `UsageRights`, `AccessCondition`                | ODPS, ODPC       |
| `DataContract`      | object         | A technical or operational contract that defines expectations for schema, quality, delivery, compatibility, and change management.                                              | schema contract, delivery contract, operational contract, technical contract             | `DataQuality`, `SLA`, `AccessMethod`, `Stewardship`                     | ODPS             |
| `Stewardship`       | object         | The assigned responsibility model for managing data product metadata, quality, lifecycle, and operational health.                                                               | data stewardship, product stewardship, metadata stewardship, lifecycle responsibility    | `Steward`, `Owner`, `DataQuality`, `GovernanceProfile`                  | ODPS, ODPC       |

[Suggest addition to the vocabulary](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/issues) 
