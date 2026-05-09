# Extensions

ODPV defines a shared controlled vocabulary for the OpenDataProducts.org standards family. It provides stable terms, labels, definitions, concept groups, mappings, and relationship names used across ODPS, ODPC, and [ODPG](https://opendataproducts.org/odpg-v1.0/). Organizations may need additional terms for domain-specific, platform-specific, or organization-specific use cases. These terms can be added through vocabulary extensions.

Extensions should add new terms, labels, mappings, concept groups, related terms, or usage notes. They should not change the meaning of official ODPV terms. Extension terms should use a separate namespace or prefix to avoid conflict with official ODPV terms.

Examples:

* `x-mobility:CongestionIndex`
* `x-healthcare:PatientCohort`
* `x-finance:RiskExposure`
* `x-platform:InternalDataOwner`

Extension terms may define:

* `id`
* `preferredLabel`
* `alternativeLabels`
* `definition`
* `conceptGroup`
* `relatedTerms`
* `externalMappings`
* `notes`

> Snippet of YAML version:

```yml
id: x-mobility:CongestionIndex
preferredLabel:
  en: Congestion Index
definition:
  en: A domain-specific indicator describing the level 
      of traffic congestion for a mobility data product.
conceptGroup: x-mobility
relatedTerms:
  - KPI
  - Signal
externalMappings:
  - scheme: example-mobility-taxonomy
    value: congestion-index
notes:
  en: Extension terms use a separate namespace so they 
      do not conflict with official ODPV terms.
```

Extensions are not part of the official ODPV vocabulary unless they are later adopted into the specification. Tooling may ignore extension terms unless explicit support has been added. Extensions should not be used to redefine official ODPV terms such as `DataProduct`, `UseCase`, `BusinessObjective`, `KPI`, `Signal`, `DataQuality`, `License`, or `supports`.

Useful and widely adopted extensions may become candidates for future versions of ODPV. To propose useful extensions, raise an issue in GitHub:

[Open Data Products Vocabulary GitHub issues](https://github.com/Open-Data-Product-Initiative/odpv-v1.0/issues)
