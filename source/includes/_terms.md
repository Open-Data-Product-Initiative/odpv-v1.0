# Terms used

Here's list of terms used and what we mean with them. The meaning of terms is mostly taken from existing knowledge eg articles and other trusted sources. The source is always linked to the term. In some rare cases term is defined for the specification purposes only. 

| Term | Description |
|---|---|
| `Open Data Product Specification (ODPS)` | Defines one data product, including metadata, ownership, access, quality, service levels, pricing, licensing, support, governance, and product strategy. |
| `Open Data Product Catalog Specification (ODPC)` | Defines reusable portfolio objects used for data product discovery, planning, prioritization, and portfolio management. |
| `Open Data Product Graph Specification (ODPG)` | Defines graphs and relationships between data products, product references, use cases, business objectives, signals, and other catalog objects. |
| `Catalog` | The top-level ODPC object that organizes reusable portfolio objects such as product references, use cases, business objectives, and signals. |
| `ProductReference` | A lightweight catalog object that identifies a data product and points to its authoritative product definition through `productModel`. |
| `UseCase` | A demand-side catalog object that describes why data is needed, who needs it, what decision or process it supports, and what outcome is expected. |
| `BusinessObjective` | A catalog object that defines a higher-level business, operational, policy, or strategic objective. It can include KPIs used to measure progress. |
| `Signal` | A catalog object that captures an observed market, operational, user, technology, policy, competitive, quality, usage, risk, or gap indicator. |
| `ProductModel` | The authoritative model or specification used to define a data product, such as `ODPS`, `DPDS`, or an internal product model. |
| `Graph` | A model that connects catalog objects through nodes and edges. In the OpenDataProducts.org family, `ODPG` is the native graph standard. |
| `Node` | An object represented in a graph, such as a product reference, use case, business objective, or signal. |
| `Edge` | A relationship between two graph nodes. It can include direction, type, confidence, weight, evidence, and source. |
| `KPI` | A key performance indicator used to measure progress, performance, or value. In ODPC, KPIs are defined inside `BusinessObjective`. |
| `Portfolio object` | A reusable object used to manage a data product portfolio. Examples include `ProductReference`, `UseCase`, `BusinessObjective`, and `Signal`. |
| `Relationship` | A connection between two or more objects, such as a use case using a product reference or a signal suggesting a use case. Relationship modeling belongs to graph standards such as `ODPG`. |
| `Graph standard` | The graph standard used to implement the catalog graph, such as `ODPG`, `RDF`, `JSON-LD`, `GraphML`, `openCypher`, `GQL`, `Gremlin`, `GraphSON`, or `GeoSPARQL`. |