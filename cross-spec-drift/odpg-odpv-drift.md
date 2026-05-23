# ODPG to ODPV Drift Report

This report compares ODPG schema node and edge examples against the canonical ODPV vocabulary.

- ODPG schema: `https://opendataproducts.org/odpg-v1.0/schema/odpg.yaml`
- ODPV source: `source/vocab/odpv.yaml`
- Checked terms: 29
- Possible drifts: 0

No unresolved drift detected.

| ODPG source | ODPG term | ODPV match | Status | Notes |
|---|---|---|---|---|
| Node type | `DataProduct` | `DataProduct` | Exact match | ODPG term is an official ODPV id. |
| Node type | `UseCase` | `UseCase` | Exact match | ODPG term is an official ODPV id. |
| Node type | `BusinessObjective` | `BusinessObjective` | Exact match | ODPG term is an official ODPV id. |
| Node type | `KPI` | `KPI` | Exact match | ODPG term is an official ODPV id. |
| Node type | `Domain` | `Domain` | Exact match | ODPG term is an official ODPV id. |
| Node type | `Dataset` | `Dataset` | Exact match | ODPG term is an official ODPV id. |
| Node type | `API` | `DataService` | Alias match | ODPG term maps through ODPV alias. |
| Node type | `Policy` | `Policy` | Exact match | ODPG term is an official ODPV id. |
| Node type | `Workflow` | `Workflow` | Exact match | ODPG term is an official ODPV id. |
| Node type | `Agent` | `Agent` | Exact match | ODPG term is an official ODPV id. |
| Node type | `Capability` | `Capability` | Exact match | ODPG term is an official ODPV id. |
| Node type | `StrategicOpportunity` | `StrategicOpportunity` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `uses` | `uses` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `supports` | `supports` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `contributesTo` | `contributesTo` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `measures` | `measures` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `tracks` | `measures` | Alias match | ODPG term maps through ODPV alias. |
| Edge type | `dependsOn` | `dependsOn` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `produces` | `produces` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `consumes` | `consumes` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `governedBy` | `governedBy` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `ownedBy` | `ownedBy` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `alignsWith` | `alignsWith` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `relatedTo` | `relatedTo` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `impacts` | `impacts` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `derivedFrom` | `derivedFrom` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `exposes` | `exposes` | Exact match | ODPG term is an official ODPV id. |
| Edge type | `monitors` | `measures` | Alias match | ODPG term maps through ODPV alias. |
| Edge type | `identifies` | `identifies` | Exact match | ODPG term is an official ODPV id. |
