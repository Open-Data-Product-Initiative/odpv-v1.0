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
        self.assertIn("terms=59", result.stdout)
        self.assertIn("relationships=16", result.stdout)

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


if __name__ == "__main__":
    unittest.main()
