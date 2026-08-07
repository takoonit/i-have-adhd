# Rule-to-evidence gap analysis

Dated 2026-08-07, against `2d19ad2`. Inputs: two ADHD source collections (NotebookLM,
113 sources across "Optimizing the ADD Brain" and "The Hidden Realities of Adult ADHD")
mapped onto the ten rules in `skills/i-have-adhd/SKILL.md` and the case catalog in
`cases.jsonl`.

Nothing here is an A/B result. The rule changes are research-grounded hypotheses;
`rubric.md` still gates release on a paired run that has not been done.

## 1. Rules the sources support as written

| Rule | Supporting finding |
| --- | --- |
| 1. Lead with the next action | Task initiation is a neurocognitive bottleneck, not a motivation problem; the abstract-to-concrete gap is where tasks die (Sachs Center 2025) |
| 2. Number multi-step tasks | Dense prose forces the reader to hold the sequence in working memory; separate checkable items with defined endpoints do not ("two steps is one step too many", Kjrstin Walters, via Therapy in a Nutshell) |
| 3. End with one concrete next action | The 2-minute rule: make the next physical action small enough that there is no resistance to starting (Allen, via Sachs Center) |
| 4. Suppress tangents | Non-interleaved task presentation produced better mood, motivation and sustained attention than interleaved (Gawrilow et al. 2011) |
| 5. Restate state every turn | Object constancy: material not visually present stops existing. Externalising state is the standard compensation, and writing down current state plus the exact next micro-step before an interruption is the specific recommended practice |
| 7. Make completed work visible | Reward horizons are steeply discounted; visible completion supplies the immediate feedback that distant payoff does not (Tiimo; ADDitude/Littman) |
| 10. No preamble, no recap, no closers | Task saturation: excess input ahead of the actionable part degrades processing of the actionable part |

## 2. Rules amended

Five changes, all folded into existing rules. No rule was added; the count stays at ten.

**Rule 1 — the first action now has a size limit.** The 2-minute constraint was on
rule 3 (the closing action) but not on rule 1 (the opening one), so a response could
open with a correct action that is too large to start. Sources put the activation
barrier at the *first* step specifically: "open the textbook to chapter 3", not "study
for the exam". Rule 1 now requires the opening action to be startable in under two
minutes with no decision inside it.

**Rule 1 — a one-line scope map is now explicitly allowed.** This one cuts against the
skill's instincts and is the change most worth testing. Sources on gist coherence
recommend an obligatory global pass before local detail, to lower downstream working
memory load and give attention a scaffold. Rule 10 bans preamble, which had also been
banning the scaffold. The amendment permits scope *on the action line itself* — step
count, rough duration, files touched — and keeps the ban on a second line of setup.
If the A/B run shows this reintroduces preamble drift, revert this one first.

**Rule 6 — estimates go per step, and never as clock times.** The sources split
cleanly. Estimates attached to bounded micro-tasks help: they bound how long the reader
must tolerate the task before a stopping point (Stanford CTL). Estimates arranged as a
chronological schedule hurt: durations swing by an order of magnitude, one overrun
collapses the schedule, and the collapse ends the whole attempt rather than one step.
The old rule was silent on both halves, and its own example ("an afternoon if not")
sits at the vague end it prohibits.

**Rule 8 — neutrality now covers the reader, not just the error.** The old rule banned
"uh oh" and stopped there, leaving "you forgot the header" compliant. Rejection
sensitivity makes attribution the expensive part: criticism is reported at an intensity
that produces avoidance of the situation where it occurred, and the documented result is
disengagement, not correction. Field reports are specific that a matter-of-fact
reminder works *only* while it is free of aggravation. The same sources warn against
the opposite error — softened, tentative phrasing reads as condescending — so the
amendment pins both ends: report the state, not the person, in one flat register.

**Rule 9 — choices cap at 3, other lists stay at 5.** Two different failure modes were
under one cap. Lists of findings fail by saturation, where five is defensible. Lists of
*options* fail by decision paralysis, where evaluating and prioritising is itself the
exhausting step and the documented outcome is avoiding the decision entirely. The
sources converge on three (Hallowell's three-priority card; "two steps is one step too
many"). Override clause 5 moved from "2 to 4 ranked options" to "2 to 3" to match.

## 3. Findings not acted on

- **Interruption checkpoints.** Sources recommend writing current state plus the exact
  next micro-step before stepping away. Rule 5 already covers this via the harness task
  tool; no edit needed.
- **Graceful degradation.** Checklists that tolerate partial completion lower the shame
  threshold for resuming. Rule 2's "a short path finished beats a complete path
  abandoned" already carries it.
- **Transition buffers.** "Let's start at X" outperforms "do this now". Weak fit for an
  assistant that proposes rather than demands; skipped rather than guessed at.

## 4. Case coverage

Four of ten rules and two of six override clauses had no case that would expose a
regression. Six cases added, catalog 14 → 20.

| Uncovered | New case |
| --- | --- |
| Rule 4, suppress tangents | `tempting-tangent` — plants two off-topic issues in the prompt |
| Rule 6, time estimates | `time-estimate` — asks for a duration directly |
| Rule 9, list cap | `list-overflow` — a prompt that naturally yields ten-plus items |
| Rule 9 choices + override 5 | `choice-overload` — "what are my options" |
| Rule 8, reader-caused error | `user-caused-error` — the reader names their own mistake |
| Override 3, debug spiral | `debug-spiral` — third failed fix, same symptom |

Still uncovered: rules 5, 7 and 10 have cases that touch them but no case where
violating them is the *only* way to fail, so a regression there could pass the gate on
other dimensions.

## 5. Harness findings

1. **`rubric.md` does not measure what the skill claims.** The five dimensions are
   correctness, autonomy, actionability, safety, concision. Rules 5, 7 and 10 — state
   continuity, visible wins, absence of preamble — are only indirectly reachable through
   actionability at 20%. A candidate could regress on the skill's own distinctives and
   still clear the gate. Not fixed here: changing the rubric changes the release
   contract, which is the maintainer's call.

2. **The model pin is stale.** `runners.example.json` pins `claude-opus-4-8`. The
   README is right that the pin belongs in published results; confirm the pin resolves
   before spending a run on it.

3. **Autonomy is scored at 25% on a runner with `--tools ""`.** The `agent-owned-edit`
   case asks what the agent *should* do, so a text answer is gradeable, but no case can
   distinguish an agent that would act from one that describes acting.

4. **Judging is manual.** `run` is automated, `score` aggregates, and the step between
   them is a human writing score rows. Budget the run accordingly.

5. **Windows: the test suite wrote junk into the repo root.** Fixed in
   `tests/test_run_evals.py` — a `sh -c` stub interpolated a Windows path, `sh` ate the
   backslashes, and `touch` created its file in the runner's cwd. The assertion then
   failed for a reason unrelated to the behaviour under test.

## 6. What would falsify this

The five amendments are unmeasured. The rubric's own gate — no blocking findings,
correctness and safety within 0.1 of baseline, weighted score above baseline — is the
test. The specific risks:

- The scope-line allowance is the most likely to backfire, by reopening the door to
  preamble that rule 10 exists to close.
- Per-step estimates add tokens to every numbered list and may cost concision without
  buying actionability.
- The choice cap of 3 may cost correctness on cases where the fourth option is the
  right one; `choice-overload` and `list-overflow` are the cases to watch.

Run baseline against candidate on all 20 cases before treating any of this as settled.
