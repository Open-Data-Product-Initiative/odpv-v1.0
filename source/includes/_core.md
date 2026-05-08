# Core


| Term                 | Type           | Description                                                                                                                                               | Used in          |
| -------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `DataProduct`        | object         | A managed data offering designed for reuse, with defined ownership, access, quality, usage terms, and value context.                                      | ODPS, ODPC, ODPG |
| `DataProductCatalog` | object         | A managed collection of data products and related portfolio objects, such as use cases, objectives, KPIs, signals, and references.                        | ODPC, ODPG       |
| `DataProductGraph`   | object         | A graph representation that connects data products, catalogs, use cases, objectives, KPIs, signals, and governance objects through defined relationships. | ODPG             |
| `Dataset`            | object         | A structured collection of data that may be part of, or exposed through, a data product. Aligns with DCAT where applicable.                               | ODPS, ODPC       |
| `Distribution`       | object         | A specific accessible form of a dataset, such as a file, API response, export, or downloadable representation. Aligns with DCAT where applicable.         | ODPS             |
| `DataService`        | object         | A service that provides access to data or data operations, such as an API, query endpoint, or data delivery service. Aligns with DCAT where applicable.   | ODPS             |
| `Provider`           | role           | A person, team, organization, or system that provides or publishes a data product, dataset, distribution, or data service.                                | ODPS, ODPC, ODPG |
| `Consumer`           | role           | A person, team, organization, system, or agent that uses or consumes a data product, dataset, distribution, or data service.                              | ODPS, ODPC, ODPG |
| `Owner`              | role           | A person, team, or organization accountable for a data product, catalog, dataset, service, or related object.                                             | ODPS, ODPC       |
| `Steward`            | role           | A person, team, or organization responsible for the operational management, quality, metadata, and lifecycle of a data product or related object.         | ODPS, ODPC       |
| `Domain`             | classification | A business, organizational, subject, or functional area used to group data products and related objects.                                                  | ODPS, ODPC, ODPG |
| `Identifier`         | reference      | A stable value used to uniquely identify a vocabulary term, specification object, product, catalog item, or graph node.                                   | ODPS, ODPC, ODPG |
| `Reference`          | reference      | A link or pointer to another object, specification file, external vocabulary term, system record, or graph node.                                          | ODPS, ODPC, ODPG |
                          |

