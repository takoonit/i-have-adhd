"""Counters for the facts-v2 arm comparison (gap-analysis.md 23).

Every counter prints its matches. The repo has seven recorded metric errors and
all seven were a count nobody read; printing is not optional here.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

TIME = re.compile(
    r"\b\d+\s*(?:-|–)?\s*\d*\s*"
    r"(?:min|mins|minute|minutes|hr|hrs|hour|hours|sec|secs|second|seconds|day|days|week|weeks)\b",
    re.I,
)
BIG_UNIT = re.compile(r"\b(?:hour|hours|day|days|week|weeks|afternoon|morning)\b", re.I)
STEP = re.compile(r"^\s*(?:\d+[.)]|[-*])\s+(.*)$")
REF = re.compile(r"`[^`]+`|\b\w+\.(?:ts|js|py|sql|json|md|ya?ml|tsx)\b")
VERIFY = re.compile(r"\b(?:try|run|open|verify|check|confirm)\b[^.\n]{0,60}`", re.I)
# Pre-filter only. Section 20 and section 23.5 both caught "the step you skipped" as a false
# positive: a neutral reference to a step, not an attribution to the person.
BLAME = re.compile(r"\byou (?:forgot|skipped|missed|should have|failed to|didn't|did not)\b", re.I)


def load(path: Path) -> dict[str, list[str]]:
    by_case: dict[str, list[str]] = defaultdict(list)
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("response"):
            by_case[row["case_id"]].append(row["response"])
    return by_case


def spec_depth(text: str) -> tuple[int, int, list[str]]:
    total = specified = 0
    bare: list[str] = []
    for line in text.splitlines():
        m = STEP.match(line)
        if not m:
            continue
        body = m.group(1).strip()
        if len(body) < 8:
            continue
        total += 1
        if REF.search(body):
            specified += 1
        else:
            bare.append(body[:90])
    return total, specified, bare


def report(label: str, by_case: dict[str, list[str]]) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    print(f"\n{'=' * 78}\n{label}\n{'=' * 78}")
    for case in sorted(by_case):
        rs = by_case[case]
        n = len(rs)
        units = sum(len(TIME.findall(t)) for t in rs) / n
        big = sum(1 for t in rs if BIG_UNIT.search(t))
        ver = sum(1 for t in rs if VERIFY.search(t))
        tot = spec = 0
        for t in rs:
            a, b, _ = spec_depth(t)
            tot += a
            spec += b
        rate = spec / tot if tot else 0.0
        blame_hits = [m.group(0) for t in rs for m in BLAME.finditer(t)]
        out[case] = {
            "n": n, "time_units": units, "big_unit": big,
            "verify": ver, "spec_rate": rate, "steps": tot,
            "blame_prefilter": len(blame_hits),
        }
        print(f"{case:22} n={n} time/reply={units:5.1f} big={big}/{n} "
              f"verify={ver}/{n} spec={spec}/{tot}={rate:.2f} blame*={len(blame_hits)}")
    return out


def main() -> None:
    ctl, cand = Path(sys.argv[1]), Path(sys.argv[2])
    a, b = report("CONTROL (shipped facts)", load(ctl)), report("FACTS-V2", load(cand))

    print(f"\n{'=' * 78}\nDELTA  (facts-v2 minus control)\n{'=' * 78}")
    print(f"{'case':22} {'time/reply':>18} {'spec rate':>16} {'verify':>12} {'big-unit':>12}")
    for case in sorted(set(a) & set(b)):
        x, y = a[case], b[case]
        print(f"{case:22} {x['time_units']:7.1f} -> {y['time_units']:5.1f} "
              f"{x['spec_rate']:7.2f} -> {y['spec_rate']:5.2f} "
              f"{int(x['verify']):5d} -> {int(y['verify']):3d} "
              f"{int(x['big_unit']):5d} -> {int(y['big_unit']):3d}")

    # Standing rule: print samples before believing a count.
    print(f"\n{'=' * 78}\nBLAME PRE-FILTER HITS - hand-classify every one\n{'=' * 78}")
    for label, path in (("control", ctl), ("facts-v2", cand)):
        for case, rs in load(path).items():
            for t in rs:
                for m in BLAME.finditer(t):
                    s = max(0, m.start() - 110)
                    print(f"[{label}/{case}] ...{t[s:m.end() + 110]}...\n{'-' * 78}")

    print(f"\n{'=' * 78}\nBARE STEPS in facts-v2 - confirm they are really unspecified\n{'=' * 78}")
    for case, rs in load(cand).items():
        for t in rs:
            _, _, bare = spec_depth(t)
            for step in bare[:2]:
                print(f"[{case}] {step}")


if __name__ == "__main__":
    main()
