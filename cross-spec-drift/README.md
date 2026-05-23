# ODPV Cross-Spec Drift Reports

This folder contains dated drift reports that compare published Open Data Product family schemas against the canonical ODPV vocabulary.

ODPV is the shared vocabulary layer for the standards family. These reports help detect when terms used by ODPS, ODPC, or ODPG are not yet represented in ODPV as official terms or aliases.

## Report Files

Reports use this filename pattern:

```text
YYYY-MM-DD-odpv-cross-spec-drift.md
```

There is one report per day. If the drift check runs more than once on the same day, the latest run overwrites that day's report. This keeps a daily history without creating multiple near-duplicate files.

## Current Inputs

The drift check compares ODPV against the published online schemas:

| Spec | Source |
|---|---|
| ODPG | `https://opendataproducts.org/odpg-v1.0/schema/odpg.yaml` |
| ODPC | `https://opendataproducts.org/odpc-v1.0/schema/odpc.yaml` |
| ODPS | `https://opendataproducts.org/v4.1/schema/odps.yaml` |
| ODPV | `source/vocab/odpv.yaml` |

## How To Read A Report

Start with the top-level totals:

- `Checked terms` shows how many schema terms were compared against ODPV.
- `Possible drifts` shows how many terms had no exact ODPV id or alias match.
- `Possible Drift Summary` lists unresolved drift candidates when any exist.

The detailed tables show each compared term:

| Status | Meaning |
|---|---|
| `Exact match` | The source term is an official ODPV term id. |
| `Alias match` | The source term maps to an official ODPV term through `alsoKnownAs`. |
| `Possible drift` | No exact id or alias match was found. Human review is needed. |

Rows marked `Possible drift` should be reviewed and resolved by either adding an ODPV term, adding an alias to an existing ODPV term, or updating the source specification if the term belongs there instead.

## Automation

The weekly GitHub Action is defined in:

```text
.github/workflows/cross-spec-drift.yml
```

It runs every Monday at 06:00 UTC and can also be started manually with `workflow_dispatch`. The action:

1. installs Python dependencies,
2. runs `scripts/check_cross_spec_drift.py`,
3. validates the generated report and vocabulary artifacts,
4. commits changed files under `cross-spec-drift/`.

## Local Commands

Generate or refresh today's report:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_cross_spec_drift.py
```

Check that today's committed report is in sync:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_cross_spec_drift.py --check
```

After changing vocabulary terms, also run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_vocab.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_vocab_artifacts.py --check
```

## AI Analysis Use

These dated reports are intended to become a history of terminology alignment across ODPS, ODPC, ODPG, and ODPV. They can be used later as input for AI-assisted analysis of how drift appears, how quickly it is resolved, and which specifications introduce new shared vocabulary needs.
