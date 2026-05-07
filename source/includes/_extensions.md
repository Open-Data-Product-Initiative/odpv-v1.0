# Specification extensions

While the Open Data Product Catalog Specification defines the core catalog objects and attributes, organizations may need to add implementation-specific metadata for local tools, internal workflows, or platform-specific requirements.

Extension properties are implemented as patterned fields that are always prefixed with `x-`. These fields may appear in ODPC objects such as `Catalog`, `ProductReference`, `UseCase`, `BusinessObjective`, and `Signal`.

Extensions are not part of the official ODPC object model unless they are later adopted into the specification. Tooling may ignore extension fields unless explicit support has been added.

Extensions should not be used to redefine core ODPC semantics. They should be used only for additional metadata that does not fit the standard attributes.

Useful and widely adopted extensions may become candidates for future versions of the standard. To propose useful extensions, raise an issue in GitHub:

[Open Data Product Initiative GitHub issues](https://github.com/Open-Data-Product-Initiative/odpc-v1.0/issues)

> Example of extension usage:

```yml
catalog:
  id: CAT-001
  name:
    en: Urban Mobility Data Product Catalog
  description:
    en: Catalog of reusable portfolio objects related to urban mobility.
  x-internal-id: foobar123
  x-source-system: internal-catalog-platform
```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
|  **^x-** | any  |  | Allows extensions to the Open Data Catalogs Schema. The field name MUST begin with x-, for example, x-internal-id. The value can be null, a primitive, an array or an object. |
