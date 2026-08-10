import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_count_facts(control: Path, candidate: Path, env=None):
    return subprocess.run(
        [sys.executable, ROOT / "scripts" / "count_facts.py", control, candidate],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        check=False,
    )


class CountFactsTest(unittest.TestCase):
    def test_unicode_samples_print_when_stdout_starts_as_cp1252(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "evals" / "results") as tmp:
            tmp_path = Path(tmp)
            control = tmp_path / "control.jsonl"
            candidate = tmp_path / "candidate.jsonl"
            row = json.dumps({"case_id": "unicode", "response": "1. Move A \u2192 B"})
            control.write_text(row + "\n", encoding="utf-8")
            candidate.write_text(row + "\n", encoding="utf-8")

            env = os.environ.copy()
            env["PYTHONIOENCODING"] = "cp1252"
            completed = run_count_facts(control, candidate, env)

            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("Move A \u2192 B", completed.stdout)

    def test_rejects_input_outside_evaluation_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            outside = Path(tmp) / "outside.jsonl"
            outside.write_text(
                json.dumps({"case_id": "outside", "response": "secret"}) + "\n",
                encoding="utf-8",
            )

            completed = run_count_facts(outside, outside)

            self.assertNotEqual(0, completed.returncode)
            self.assertIn("evals/results", completed.stderr)


if __name__ == "__main__":
    unittest.main()
