import json
import subprocess
import sys
import unittest
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


if __name__ == "__main__":
    unittest.main()
