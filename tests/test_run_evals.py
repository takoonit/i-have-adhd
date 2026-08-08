import argparse
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import run_evals  # noqa: E402


class EvaluationHarnessTest(unittest.TestCase):
    def test_case_catalog_is_valid_and_balanced(self):
        cases = run_evals.load_cases(ROOT / "evals" / "cases.jsonl")
        errors = run_evals.validate_cases(cases)

        self.assertEqual([], errors)
        self.assertGreaterEqual(len(cases), 12)
        self.assertGreaterEqual(len({case["category"] for case in cases}), 8)

    def test_multi_turn_cases_are_validated_and_expanded(self):
        base = {"id": "c", "category": "continuity", "risk": "low", "criteria": ["x"]}

        self.assertEqual([], run_evals.validate_cases([{**base, "turns": ["a", "b"]}]))
        self.assertEqual(["a", "b"], run_evals.case_turns({**base, "turns": ["a", "b"]}))
        self.assertEqual(["a"], run_evals.case_turns({**base, "prompt": "a"}))

        for bad, expected in (
            ({}, "exactly one of prompt or turns"),
            ({"prompt": "a", "turns": ["a", "b"]}, "exactly one of prompt or turns"),
            ({"turns": ["a"]}, "list of 2 or more"),
            ({"turns": ["a", "  "]}, "non-empty string"),
        ):
            with self.subTest(bad=bad):
                errors = run_evals.validate_cases([{**base, **bad}])
                self.assertTrue(
                    any(expected in error for error in errors), errors
                )

    def test_replay_prompt_leaves_the_first_turn_byte_identical(self):
        """Rows recorded before multi-turn support must stay comparable."""
        skill = ROOT / "skills" / "i-have-adhd" / "SKILL.md"
        for condition, path in (("baseline", None), ("candidate", skill)):
            with self.subTest(condition=condition):
                self.assertEqual(
                    run_evals._condition_prompt("ask", condition, path),
                    run_evals._replay_prompt([], "ask", condition, path),
                )

        later = run_evals._replay_prompt([("q1", "a1")], "q2", "baseline", None)
        self.assertIn("<user>\nq1\n</user>", later)
        self.assertIn("<you>\na1\n</you>", later)
        self.assertIn("<user>\nq2\n</user>", later)
        self.assertLess(later.index("q1"), later.index("q2"))

    def test_score_summary_applies_weights_and_release_gates(self):
        scores = []
        for condition, value in (("baseline", 3), ("candidate", 4)):
            scores.append(
                {
                    "case_id": "direct-answer",
                    "trial": 1,
                    "condition": condition,
                    "correctness": value,
                    "autonomy": value,
                    "actionability": value,
                    "safety": value,
                    "concision": value,
                    "blocker": False,
                    "notes": "fixture",
                }
            )

        summary = run_evals.summarize_scores(scores)

        self.assertAlmostEqual(3.0, summary["conditions"]["baseline"]["weighted_score"])
        self.assertAlmostEqual(4.0, summary["conditions"]["candidate"]["weighted_score"])
        self.assertTrue(summary["release_gate"]["passed"])

    def test_candidate_blocker_fails_release_gate(self):
        rows = []
        for condition in ("baseline", "candidate"):
            rows.append(
                {
                    "case_id": "dangerous-action",
                    "trial": 1,
                    "condition": condition,
                    "correctness": 5,
                    "autonomy": 5,
                    "actionability": 5,
                    "safety": 5,
                    "concision": 5,
                    "blocker": condition == "candidate",
                    "notes": "fixture",
                }
            )

        summary = run_evals.summarize_scores(rows)

        self.assertFalse(summary["release_gate"]["passed"])
        self.assertIn("blocking", " ".join(summary["release_gate"]["reasons"]))

    def test_conditions_judged_on_different_cases_are_rejected(self):
        rows = [
            self._score_row("destructive-action", "baseline", 2),
            self._score_row("medical-boundary", "baseline", 2),
            self._score_row("direct-answer", "candidate", 5),
        ]

        with self.assertRaisesRegex(ValueError, "not judged on the same rows"):
            run_evals.summarize_scores(rows)

    def test_duplicate_score_rows_are_rejected(self):
        rows = [
            self._score_row("direct-answer", "baseline", 3),
            self._score_row("direct-answer", "candidate", 4),
            self._score_row("direct-answer", "candidate", 5),
        ]

        with self.assertRaisesRegex(ValueError, "duplicate score rows"):
            run_evals.summarize_scores(rows)

    @staticmethod
    def _score_row(case_id, condition, value, trial=1):
        return {
            "case_id": case_id,
            "trial": trial,
            "condition": condition,
            "correctness": value,
            "autonomy": value,
            "actionability": value,
            "safety": value,
            "concision": value,
            "blocker": False,
            "notes": "fixture",
        }

    def test_duplicate_case_ids_are_rejected(self):
        case = {
            "id": "duplicate",
            "category": "direct-answer",
            "prompt": "What is 2 + 2?",
            "risk": "low",
            "criteria": ["Answers 4."],
        }
        errors = run_evals.validate_cases([case, dict(case)])
        self.assertTrue(any("Duplicate" in error for error in errors))

    def test_jsonl_loader_reports_invalid_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.jsonl"
            path.write_text(json.dumps({"id": "ok"}) + "\nnot-json\n")
            with self.assertRaisesRegex(ValueError, "line 2"):
                run_evals.read_jsonl(path)

    def test_unmetered_runner_is_rejected_before_any_call(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            marker = tmp_path / "ran"
            runner_config = tmp_path / "runners.json"
            runner_config.write_text(
                json.dumps(
                    {
                        "stub": {
                            # as_posix(): sh eats the backslashes in a Windows path,
                            # so `touch` would create a junk file in the runner's cwd
                            # (the repo root) instead of the temp dir.
                            "command": ["sh", "-c", f"touch '{marker.as_posix()}' && echo hi"],
                            "response_format": "text",
                        }
                    }
                )
            )
            args = argparse.Namespace(
                cases=ROOT / "evals" / "cases.jsonl",
                runner_config=runner_config,
                runner="stub",
                condition="baseline",
                condition_skill=None,
                case=["direct-answer"],
                trials=1,
                retries=0,
                budget_usd=1.0,
                allow_unmetered=False,
                model=None,
                output=tmp_path / "out.jsonl",
            )

            with self.assertRaisesRegex(RuntimeError, "never reports dollar cost"):
                run_evals.run_evaluations(args)

            self.assertFalse(marker.exists(), "runner was invoked before the rejection")
            self.assertFalse((tmp_path / "out.jsonl").exists())

            args.allow_unmetered = True
            self.assertEqual(0, run_evals.run_evaluations(args))
            self.assertTrue(marker.exists())

    def test_completed_keys_support_resuming_partial_runs(self):
        row = {"case_id": "direct-answer", "trial": 1, "condition": "baseline",
               "runner": "claude", "model": "m1"}

        self.assertEqual(
            {("direct-answer", 1, "baseline", "claude", "m1")},
            run_evals.completed_keys([row]),
        )

    def test_resume_does_not_reuse_rows_from_another_model(self):
        """A case answered by a different model is a different run, not a completed one."""
        row = {"case_id": "direct-answer", "trial": 1, "condition": "baseline",
               "runner": "claude", "model": "m1"}
        done = run_evals.completed_keys([row])

        self.assertNotIn(("direct-answer", 1, "baseline", "claude", "m2"), done)

    def test_rows_without_a_model_are_not_credited_to_any_model(self):
        """Inferring a model would mis-assign the row the moment the pin moves."""
        legacy = {"case_id": "direct-answer", "trial": 1, "condition": "baseline",
                  "runner": "claude"}

        self.assertEqual(set(), run_evals.completed_keys([legacy]))

    def test_resolve_model_reads_the_pin_from_the_command(self):
        self.assertEqual("x", run_evals.resolve_model(["claude", "--model", "x", "p"]))
        self.assertEqual("unpinned:claude", run_evals.resolve_model(["claude", "--print"]))
        self.assertEqual("unpinned:claude", run_evals.resolve_model(["claude", "--model"]))

    def test_unpinned_runners_do_not_share_one_identity(self):
        """Two providers that both omit --model are not the same model."""
        self.assertNotEqual(
            run_evals.resolve_model(["codex", "exec"]),
            run_evals.resolve_model(["claude", "--print"]),
        )

    def test_incomplete_rows_never_satisfy_a_resume_key(self):
        """A conversation cut off by the budget must be re-run, not counted as done."""
        row = {"case_id": "c", "trial": 1, "condition": "baseline", "runner": "r",
               "model": "m", "incomplete": True}

        self.assertEqual(set(), run_evals.completed_keys([row]))

    def test_null_or_blank_prompt_is_rejected(self):
        """A null prompt used to reach subprocess.run as None."""
        base = {"id": "c", "category": "x", "risk": "low", "criteria": ["y"]}
        for bad in (None, "", "   "):
            with self.subTest(prompt=bad):
                errors = run_evals.validate_cases([{**base, "prompt": bad}])
                self.assertTrue(any("non-empty string" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
