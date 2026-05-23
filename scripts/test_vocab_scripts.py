import json
import re
import subprocess
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class VocabScriptTests(unittest.TestCase):
    def run_script(self, *args):
        return subprocess.run(
            [sys.executable, *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_generate_check_reports_current_artifacts_are_in_sync(self):
        result = self.run_script("scripts/generate_vocab_artifacts.py", "--check")

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("Vocabulary artifacts are in sync", result.stdout)

    def test_validate_vocab_reports_expected_counts(self):
        result = self.run_script("scripts/validate_vocab.py")

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("Validation OK", result.stdout)
        self.assertIn("terms=71", result.stdout)
        self.assertIn("relationships=24", result.stdout)

    def test_search_vocab_returns_json_matches_for_aliases_and_examples(self):
        result = self.run_script(
            "scripts/search_vocab.py",
            "customer churn reusable data offering",
            "--json",
            "--limit",
            "3",
        )

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        matches = json.loads(result.stdout)
        self.assertGreaterEqual(len(matches), 1)
        self.assertEqual(matches[0]["id"], "DataProduct")
        self.assertIn("uri", matches[0])
        self.assertIn("score", matches[0])
        self.assertIn("matchedFields", matches[0])

    def test_odpg_terms_are_aligned_without_promoting_aliases(self):
        import yaml

        data = yaml.safe_load((ROOT / "source/vocab/odpv.yaml").read_text(encoding="utf-8"))
        terms_by_id = {
            term["id"]: {"section": section["id"], **term}
            for section in data["sections"]
            for term in section["terms"]
        }

        expected_sections = {
            "Agent": "core",
            "Workflow": "core",
            "Capability": "core",
            "StrategicOpportunity": "value",
            "uses": "relationships",
            "produces": "relationships",
            "consumes": "relationships",
            "ownedBy": "relationships",
            "alignsWith": "relationships",
            "impacts": "relationships",
            "exposes": "relationships",
            "identifies": "relationships",
        }
        for term_id, section_id in expected_sections.items():
            with self.subTest(term_id=term_id):
                self.assertIn(term_id, terms_by_id)
                self.assertEqual(terms_by_id[term_id]["section"], section_id)

        self.assertNotIn("API", terms_by_id)
        self.assertNotIn("monitors", terms_by_id)
        self.assertIn("API", terms_by_id["DataService"]["alsoKnownAs"]["en"])
        self.assertIn("monitors", terms_by_id["measures"]["alsoKnownAs"]["en"])
        self.assertIn("GraphReference", terms_by_id["Reference"]["alsoKnownAs"]["en"])
        self.assertIn("ProductReference", terms_by_id["Reference"]["alsoKnownAs"]["en"])
        self.assertIn("ProductModel", terms_by_id["Reference"]["alsoKnownAs"]["en"])
        self.assertIn("Catalog", terms_by_id["DataProductCatalog"]["alsoKnownAs"]["en"])

    def test_cross_spec_drift_check_reports_online_schema_alignment(self):
        report_date = datetime.now(timezone.utc).date().isoformat()
        report_path = ROOT / f"cross-spec-drift/{report_date}-odpv-cross-spec-drift.md"
        legacy_report_path = ROOT / "cross-spec-drift/odpv-cross-spec-drift.md"
        result = self.run_script("scripts/check_cross_spec_drift.py")

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertTrue(report_path.exists())
        self.assertFalse(legacy_report_path.exists())

        report = report_path.read_text(encoding="utf-8")
        self.assertIn("# ODPV Cross-Spec Drift Report", report)
        self.assertRegex(report, r"- Last drift detection run: `\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z`")
        self.assertIn("- ODPG schema: `https://opendataproducts.org/odpg-v1.0/schema/odpg.yaml`", report)
        self.assertIn("- ODPC schema: `https://opendataproducts.org/odpc-v1.0/schema/odpc.yaml`", report)
        self.assertIn("- ODPS schema: `https://opendataproducts.org/v4.1/schema/odps.yaml`", report)
        self.assertIn("## Possible Drift Summary", report)
        self.assertIn("| Spec | Source | Term | Suggested action |", report)
        self.assertIn("| ODPS | Product component | `pricingPlans` | Review whether to add an ODPV term, add an alias, or update the source specification. |", report)
        self.assertIn("## ODPG to ODPV", report)
        self.assertIn("| ODPG source | ODPG term | ODPV match | Status | Notes |", report)
        self.assertIn("| Node type | `API` | `DataService` | Alias match | ODPG term maps through ODPV alias.", report)
        self.assertIn("| Edge type | `monitors` | `measures` | Alias match | ODPG term maps through ODPV alias.", report)
        self.assertIn("## ODPC to ODPV", report)
        self.assertIn("| ODPC source | ODPC term | ODPV match | Status | Notes |", report)
        self.assertIn("| Schema definition | `UseCase` | `UseCase` | Exact match | ODPC term is an official ODPV id.", report)
        self.assertIn("| Schema definition | `GraphReference` | `Reference` | Alias match | ODPC term maps through ODPV alias.", report)
        self.assertIn("| Schema definition | `ProductReference` | `Reference` | Alias match | ODPC term maps through ODPV alias.", report)
        self.assertIn("| Schema definition | `ProductModel` | `Reference` | Alias match | ODPC term maps through ODPV alias.", report)
        self.assertIn("| Schema definition | `Catalog` | `DataProductCatalog` | Alias match | ODPC term maps through ODPV alias.", report)
        self.assertNotIn("`CatalogMeta`", report)
        self.assertIn("## ODPS to ODPV", report)
        self.assertIn("| ODPS source | ODPS term | ODPV match | Status | Notes |", report)
        self.assertIn("| Product component | `SLA` | `SLA` | Exact match | ODPS term is an official ODPV id.", report)
        self.assertIn("| Product component | `dataQuality` | `DataQuality` | Alias match | ODPS term maps through ODPV alias.", report)
        self.assertIn("| Product component | `contract` | `DataContract` | Alias match | ODPS term maps through ODPV alias.", report)
        self.assertIn("| **Product component** | **`pricingPlans`** |  | **Possible drift** | **No exact ODPV id or alias match found.** |", report)

    def test_cross_spec_drift_check_can_validate_existing_report(self):
        self.run_script("scripts/check_cross_spec_drift.py")
        result = self.run_script("scripts/check_cross_spec_drift.py", "--check")

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("Cross-spec drift report is in sync", result.stdout)


if __name__ == "__main__":
    unittest.main()
