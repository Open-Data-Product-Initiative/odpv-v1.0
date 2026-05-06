---
title: Open Data Product Catalogs (ODPC) version DEV | Linux Foundation 

language_tabs: # must be one of https://git.io/vQNgJ
- yaml

toc_footers:
  - License <a href='https://www.apache.org/licenses/LICENSE-2.0'>Apache 2.0</a>
  - <br/><a href='https://opendataproducts.org'>Specification home</a>
  - <br/>Linux Foundation</a>

includes:
- productreference
- usecase
- businessobjective
- signal
- catalog
- contributors
- terms

search: true

code_clipboard: true

meta:
  - name: description
    content: The Open Data Product Catalogs, ODPC, is a vendor-neutral, open-source, machine-readable model for cataloging data product portfolios. ODPC defines reusable portfolio objects around data products, including product references, use cases, business objectives, KPIs, signals, and catalog items. 
---

# OPEN DATA PRODUCT CATALOGS - The Linux Foundation

## Version DEV 
The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “NOT RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in BCP 14 ([RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119) and [RFC 8174](https://datatracker.ietf.org/doc/html/rfc8174)) when, and only when, they appear in all capitals, as shown here.

The specification is shared under <a href='https://www.apache.org/licenses/LICENSE-2.0'>Apache 2.0</a> license. 
Development of the specification is under the umbrella of the Linux Foundation. 

| Topic | Link | Description |
|---|---|---|
| Version source | <a href="https://github.com/Open-Data-Product-Initiative/odpc-v1.0">Open Data Product Catalogs on GitHub</a> | Official source repository for the ODPC specification |
| Contribute | [Raise an issue in GitHub](https://github.com/Open-Data-Product-Initiative/odpc-v1.0/issues) | Submit issues or suggestions to the specification maintainers |

## Introduction
The Open Data Product Catalogs, ODPC, is a vendor-neutral, open-source, machine-readable catalog model for data product portfolios. It defines reusable catalog objects such as data product references, use cases, business objectives, KPIs, signals, and catalog items.

ODPC is part of the OpenDataProducts.org standards family. It complements the Open Data Product Specification, ODPS, by adding the catalog and portfolio layer around individual data products.

ODPS defines one data product. ODPC defines the reusable portfolio objects around data products. [Open Data Product Graphs, ODPG](https://opendataproducts.org/odpg-v1.0/), defines the relationships between those objects.

The goal of ODPC is to help organizations move from isolated data product descriptions to managed data product portfolios that connect products to demand, use cases, business objectives, and measurable outcomes.

## ODPC is ODPS-native, but not ODPS-only
ODPC is designed to work naturally with ODPS. ODPS remains the preferred product definition model in the OpenDataProducts.org standards family.

At the same time, ODPC is not limited to ODPS. Many organizations already use other product descriptions, internal schemas, vendor catalogs, marketplace definitions, or data mesh descriptors. ODPC supports those models through the ProductReference object and mapping profiles.

This makes it possible to catalog data products described with:

* ODPS YAML files
* DPDS descriptors
* internal enterprise product templates
* vendor catalog assets
* marketplace product definitions
* API-based product metadata sources

The ProductReference object provides the bridge between the catalog layer and the source product definition.

## Why ODPC is needed
Data product management does not stop at one product. Organizations need to understand which data products exist, which use cases they support, which business objectives they contribute to, and which signals indicate demand, risk, opportunity, or change.

A catalog should not only list products. It should help organizations manage data products as a portfolio.

ODPC defines the structure for that portfolio layer.

It enables organizations to catalog:

* data products
* use cases
* business objectives
* KPIs
* signals
* ownership
* priorities
* lifecycle status
* references to source definitions

This creates a reusable foundation for discovery, governance, prioritization, AI-assisted planning, and graph-based portfolio analysis.

## Specification aims and aspects
ODPC aims to:

* enable interoperability between catalogs, data platforms, marketplaces, and tools
* provide reusable catalog objects for data product portfolio management
* connect data products to use cases, business objectives, KPIs, and signals
* support ODPS-native and non-ODPS product definitions
* reduce metadata conversion friction between systems
* support AI-assisted discovery, cataloging, and portfolio planning
* provide the reusable object layer for Open Data Product Graphs, ODPG
* support machine-readable cataloging with YAML and schema validation

**Note!** In the "Open Data Product" focus is on the latter words and the prefix "open" refers to the openness of the standard. Any kind of connotations to open data are not intentional, intended, or desirable.

## Core design principle
The OpenDataProducts.org standards family follows a simple separation of concerns.

* **ODPS defines the product.**
* **ODPC defines the reusable portfolio objects.**
* **ODPG defines the relationships.**

This keeps each specification focused. ODPC should not redefine the full structure of a data product. That belongs to ODPS or to another source product model. ODPC should also not define graph traversal, graph analytics, or relationship semantics. Those belong to ODPG.

## Main ODPC objects
> Example of ProductReference:

```yml
productReference:
  id: DP-001
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
```

The first version of ODPC focuses on these objects:

* ProductReference
* UseCase
* BusinessObjective
* Signal
* Catalog

These objects are designed to be reusable across catalogs, tools, AI workflows, and graph models.



