# Term Governance Rules

ODPV is a shared vocabulary, not a catch-all list of every field used by every specification. New terms should be added when they improve shared understanding across the Open Data Products standards family or when they provide a stable bridge between specifications, tools, catalogs, graphs, and AI agents.

Use these rules when reviewing drift reports, GitHub issues, pull requests, or proposed vocabulary additions.

| Situation | Preferred action | Reason |
|---|---|---|
| A concept is shared by more than one standard, tool, catalog, graph, or agent workflow | Add an official ODPV term | Shared concepts need stable ids, labels, definitions, aliases, examples, and mappings. |
| A source term is only a different spelling, casing, plural form, or common synonym of an existing ODPV term | Add an alias in `alsoKnownAs` | The canonical term stays stable while search, drift checks, and agent matching improve. |
| A source term is narrower than an existing ODPV term but still useful to map | Add an alias only if the meaning is safely equivalent; otherwise add an external or close mapping | Avoid overloading broad terms with narrower meanings that could mislead tools. |
| A concept belongs only to one specification's internal structure | Keep it in that source specification | ODPV should not duplicate schema plumbing or implementation-only fields. |
| A concept belongs to a domain, organization, or implementation profile | Use an extension namespace or prefix | Domain-specific vocabulary should be extensible without changing the shared core. |
| A concept already has a strong external standard term | Add a mapping such as `exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`, or `relatedMatch` | External mappings make ODPV interoperable without forcing it to become a heavy ontology. |
| A source specification uses an unclear or inconsistent term | Open an issue against the source specification | Some drift is better fixed at the source rather than normalized into ODPV. |

## Adding A New Official Term

A new ODPV term should include:

- stable `id` and `uri`
- `type`
- `status`
- `introducedIn`
- `preferredLabel`
- clear definition
- useful `alsoKnownAs` aliases
- `relatedTerms`
- `usedIn`
- examples
- external `mappings` when an established vocabulary applies

Definitions should describe what the concept means, not where it appears in a schema. Examples should show practical use in ODPS, ODPC, ODPG, tools, catalogs, graphs, or AI workflows.

## Adding An Alias

Add an alias when the proposed term is safely equivalent to an existing ODPV term. Alias examples include:

- casing differences such as `license` for `License`
- plural schema names such as `pricingPlans` for `PricingPlan`
- source-spec naming differences such as `API` for `DataService`
- relationship wording differences such as `monitors` for `measures`

Do not add an alias when the source term would change the meaning of the canonical term. In that case, add a new term, add a mapping, use an extension, or open a source-spec issue.

## Adding External Mappings

Use external mappings to connect ODPV terms to established vocabularies such as DCAT, SKOS, PROV-O, ODRL, Dublin Core, schema.org, or SPDX.

Mapping strength matters:

| Mapping | Use when |
|---|---|
| `exactMatch` | The external concept has the same practical meaning. |
| `closeMatch` | The external concept is similar enough for interoperability, but not identical. |
| `broadMatch` | The external concept is broader than the ODPV term. |
| `narrowMatch` | The external concept is narrower than the ODPV term. |
| `relatedMatch` | The external concept is related but should not be treated as equivalent. |

When in doubt, prefer `closeMatch` over `exactMatch`.

## Drift Review Workflow

When a drift report shows `Possible drift`:

1. Check whether the source term already maps to an ODPV term through `alsoKnownAs`.
2. Decide whether the source term is a shared concept, alias, source-spec detail, extension candidate, or source-spec issue.
3. If adding or changing ODPV, update `source/vocab/odpv.yaml` first.
4. Regenerate artifacts with `scripts/generate_vocab_artifacts.py`.
5. Validate with `scripts/validate_vocab.py`.
6. Refresh the drift report with `scripts/check_cross_spec_drift.py`.

The goal is not to force every source term into ODPV. The goal is to keep shared vocabulary stable, useful, and interoperable.
