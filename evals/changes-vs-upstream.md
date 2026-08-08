# Changes against upstream

Base: `ayghri/i-have-adhd` at `2d19ad2`, which this fork matched exactly at the start
(verified by `git ls-remote`). Reasoning and full results live in `gap-analysis.md`;
this file is the change list.

**Scope of the skill**, recorded because it governs what counts as an in-scope change:
loosely based on *The Adult ADHD Tool Kit* (Ramsay & Rostain), adapted for **how an LLM
should respond to a person with ADHD — not how a person should organise their day.**

Evidence labels:

- **Ablated** — the rule was deleted, the same cases re-run, the difference counted.
- **Measured** — the behaviour moved in an A/B, but the rule was not isolated.
- **Reasoned** — grounded in a source, never isolated in a run.

Ablations are model-specific. A rule earns its place if **any** supported model needs it,
so redundancy must be shown on the most verbose model in scope, not the leanest — see
§"Cross-model" below for why that rule exists.

---

## 1. The ruleset: 10 rules to 9

| # | Rule | Changed? | Evidence |
| --- | --- | --- | --- |
| 1 | Lead with the next action | amended | **Ablated**: 3/3 → 0/3 |
| 2 | Number multi-step tasks | unchanged | Strongest external support; ablation in progress |
| 3 | End with one concrete next action | unchanged | **Ablated**: 8/9 → 1/9 (Opus 4.8); no effect on Haiku |
| 4 | Suppress tangents | unchanged | **Ablated**: no effect; kept, see below |
| 5 | Restate state every turn | amended then narrowed | **Measured**; strongest evidence discarded as out of scope |
| 6 | Give specific time estimates | amended | **Measured**: 2.28 → 4.92; ablation in progress |
| 7 | Matter-of-fact tone for errors | amended | **Measured**: 2.68 → 5.00; ablation in progress |
| 8 | Rank what you list; cap choices at 3 | rewritten | **Ablated**: cap vs rank |
| 9 | No preamble, recap or closers | unchanged | **Ablated**: 0/3 → 3/3 closers (Opus 4.8); no effect on Haiku |
| — | ~~Make completed work visible~~ | **merged into 5** | **Ablated** and **cross-model verified** |

### Rule 1 — the opening action gets a size limit

Added: the first action must be startable in under two minutes with no decision in it.

- **Why:** the 2-minute rule and task-initiation research put the activation barrier on
  the *first* step. The skill applied that to rule 3, the closing action, but not to
  rule 1.
- **Ablated:** removing rule 1 takes `error-report` from 3 of 3 opening with the fact or
  fix to 0 of 3 — replies open with "Before reporting, let me confirm…", a bare heading,
  and a code fence. The rule earns its place; the two-minute clause inside it was not
  isolated.

### Rule 5 — amended, then narrowed back

**Amended:** absorbed old rule 7 (say what now works, and how to see it), and gained a
clause directing durable state into the workspace — a file, a TODO at the line, the
commit message, the PR body.

**Then narrowed:** the workspace clause was removed. It described what an agent *leaves
behind*, not how it responds, which is outside the skill's stated purpose. It came from
Barkley's point-of-performance model — a finding about human environment design — mapped
onto agent side effects without checking it against scope.

What rule 5 keeps: restate state each turn; use the harness task tool for multi-step
work; say what now works and how to see it; re-anchor a reader returning after a gap in
the reply itself, without making the gap a subject.

- **The evidence went with the clause.** Its strongest result — 3 of 3 against 0 of 3 in
  a clean live-agent run with real write tools — measured TODO comments written to disk,
  precisely the behaviour now out of scope.
- **What justifies the retained re-entry sentence** is separate and weaker:
  `re-entry-after-gap` scored +0.70 weighted for the candidate on the independent judge,
  and re-entry is response shape.
- **An ablation against the pre-amendment rule** found the old wording already produced a
  durable record 2 times in 3, so the clause's marginal value was never established even
  on its own terms.

### Rule 6 — estimates go per step, never as clock times

- **Why:** estimates on bounded micro-tasks help — they bound how long the reader must
  tolerate the task before a stopping point (Stanford CTL). Estimates arranged as a
  schedule hurt: durations swing wildly, one overrun collapses the schedule, and the
  collapse ends the whole attempt. The old rule was silent on both, and its own example
  ("an afternoon if not") sat at the vague end it prohibits.
- **Measured:** `time-estimate` 2.28 → 4.92 weighted.

### Rule 7 — neutrality covers the reader, not just the error

Added: report the state, not the person. No "you forgot". And do not overcorrect into
softening, which reads as condescending.

- **Why:** the old rule banned "uh oh" and stopped there, leaving "you forgot the header"
  compliant. Emotional dysregulation and rejection sensitivity in ADHD are validated, and
  the documented result of attribution is disengagement rather than correction.
- **Caveat:** "rejection sensitive dysphoria" is **not** in DSM-5 and has no standardised
  criteria. This rule rests on emotional dysregulation, which is validated.
- **Measured:** `user-caused-error` 2.68 → 5.00 weighted.

### Rule 8 — ranks lists instead of capping them

Was "Cap lists at 5 items". Now: rank every list, never drop a correct item to hit a
length, cap only what the reader must *choose* between, at three.

- **Why the cap was wrong:** Miller's 7±2 governs *recall*; a list on screen is
  *recognition*. Cockburn, Gutwin & Greenberg's menu model and Hawkins et al. find Hick's
  Law log-linear to 20 visible alternatives. Misapplied cognitive science.
- **Why the choice cap survives:** choosing is not reading. Decision time grows with
  alternatives, and the ADHD sources add decision paralysis.
- **Ablated:** `list-overflow` went from 5, 5, 9 items to 9, 9, 7, all ranked worst-first.
  `choice-overload` went from 8, 3, 3 to 3, 3, 3 — the choice cap became *more* reliable
  once it stopped competing with a second number in the same rule.

### Rule 4 — null, kept anyway

The tangent lands in the last 15% of the reply and gets the same ~85 characters with or
without the rule. Kept because nothing else in the ruleset covers tangent suppression, so
removing it deletes guidance rather than deduplicating it, and the case tests only a
reader-flagged tangent — not rule 4's second paragraph about the agent resolving its own
mid-work questions.

### Old rule 7 — merged into rule 5

**Ablated:** identical counts with and without it, because rule 5's "Step 3 of 5 done:
schema updated" already *is* making completed work visible. Merged rather than deleted,
so no guidance was lost and one instruction slot was freed.

**Cross-model verified**, because this is the only rule *removed* on single-model
evidence and could have broken weaker models:

| model | pre-merge (10 rules) | current (9 rules) |
| --- | --- | --- |
| Haiku 4.5 | 3 of 6 | 3 of 6 |
| Sonnet 5 | 6 of 6 | 5 of 6 |
| Opus 5 | 5 of 6 | 5 of 6 |

Neutral on all three.

### Override clause 2 — destructive actions

Added: rule 1 does not apply; run the read-only preview yourself; never write a preview
you have not run.

- **Why:** two of three candidate trials on `destructive-action` fabricated the output of
  a `git clean` dry run they never executed and told the reader those files were safe to
  lose. All three baseline trials stopped at the dry run. An independent judge flagged the
  same two responses unprompted. Corroborated from a different direction: in the
  pharmaverse `{admiral}` repository an agent told to regenerate docs without R in its
  sandbox hand-wrote the generated file and presented it as output.
- **The run-it-yourself half** came from the independent judge, which marked down the one
  clean candidate response for delegating the dry run back to the user.
- **Measured:** after the guard, 3 of 3 gave the command and stopped, no fabrication.
  Candidate blockers 3 → 1.

### Override clause 5, and a sixth reading fact

Options capped at 2–3 rather than 2–4, aligning with rule 8. A sixth fact added: neutral
text is read as criticism, which motivates rule 7's blameless clause.

---

## 2. Reverted during the work

**The scope-line allowance** (rule 1 could carry step count and duration on the action
line) was added on gist-coherence grounds, then removed. 9 of 60 candidate responses used
it: mean weighted 4.61 against 4.64 for the other 51, no blockers either side. No
detectable effect in either direction, so it was not paying for its length.

---

## 3. Cross-model

Everything was measured on `claude-opus-4-8` — upstream's pin, not a choice made here.
That matters, because "would the agent make a mistake without this rule?" is a question
about a model.

Rules 3 and 9, re-ablated on Haiku 4.5:

| | Opus 4.8 | Haiku 4.5 |
| --- | --- | --- |
| Rule 3, ends with an action | 8/9 → 1/9 | 3/3 → 2/3 |
| Rule 9, closers appear | 0/3 → 3/3 | 3/3 → 3/3, identical |

**Not a failure.** The control arms settle which null it is: Haiku's *unassisted* output
is already terse, already opens on the answer, already ends on a next step. Opus 4.8
over-explains, so the rules have work to do there. **The rules' value scales with how
verbose the base model is** — which is why redundancy must be demonstrated on the most
verbose supported model, never the leanest.

---

## 4. Evaluation harness

| Change | Reason |
| --- | --- |
| `--strict-mcp-config` on the Claude runner | `--setting-sources ""` does not stop the operator's MCP servers loading. A two-token prompt carried ~49,000 tokens of context; the flag cuts it to ~6,800. A validity bug before a cost bug — judged responses were shaped by whichever servers that operator happened to have connected. |
| UTF-8 decoding in `run_evals.py` | `subprocess.run(text=True)` with no codec decodes as the locale encoding. On Windows that is cp1252; the decode raises in subprocess's reader thread, stdout returns `None`, and `_parse_response` dies on `json.loads(None)`. Killed a run after 10 of 40 rows. |
| `marker.as_posix()` in `test_run_evals.py` | A `sh -c` stub interpolated a Windows path; `sh` ate the backslashes and `touch` wrote a junk file into the repo root. |
| `--tools` reordered before `--model` | `--tools <tools...>` is variadic, so `--tools "" <prompt>` makes the CLI swallow the prompt and fail with "Input must be provided". Upstream's config only worked because `--max-budget-usd` is inserted between them at runtime. Verified by invoking both runners with no budget flag. |
| Multi-turn cases | Every case was turn one, so re-entry, state across an interruption, and mid-task handoff were structurally unmeasurable. Cases now carry `prompt` or a `turns` array; turns replay, since the runner uses `--no-session-persistence`. Turn 1 is byte-identical to a single-turn prompt, pinned by a test, so rows recorded earlier stay comparable. |
| `claude-readonly-tools` runner | Behaviour requiring the agent to act cannot be exercised with `--tools ""`. |
| `evals/README.md` | Documents the isolation check, that `--max-budget-usd` aborts *after* the cap rather than preventing spend, and the multi-turn contract. |
| Catalogue 14 → 24 cases | Four of ten rules and two of six override clauses had no case that would expose a regression. `tempting-tangent` was later rewritten self-contained, after its first version asked for a fix to code this repo does not contain. |

---

## 5. Documentation removed

The five translated READMEs and five translated INSTALL guides were deleted, along with
the language selector row. The ruleset changed nine times on this branch and the
translations went stale after every one; they were hand-corrected once and rule 5's
narrowing put them wrong again the same day. A copy of the rules that is usually wrong is
worse than none, because it reads as authoritative. It also removed ~40 duplicated rule
lines that had to move in lockstep with every result. Cost: an upstream PR for those
files is no longer possible.

---

## 6. Retractions and method failures

Three retractions:

1. **"Rule 3 may be actively harmful"** — rested on a Reddit comment plus demand
   avoidance, which is not in DSM-5 or ICD-11 and whose systematic review called the
   evidence inconclusive. The ablation then showed rule 3 is among the most load-bearing
   rules in the set.
2. **"The candidate improves safety"** — one judge had it ahead 4.83 to 4.68; the
   independent judge scored a tie at 4.78.
3. **"The `claude-opus-4-8` pin is stale"** — it resolves and runs. Flagged on appearance
   without checking.

Also reversed twice in both directions: rule 5's record clause was called near-inert on a
contaminated live-agent run, then vindicated 3/3 on a clean one, then removed anyway on
scope grounds.

**Five metric errors**, every one the same shape — a counter run over text nobody read:

| # | The counter said | The text said |
| --- | --- | --- |
| 1 | candidate destructive-action complied | it had fabricated the dry-run output |
| 2 | rules 1, 4 and 9 all null | the regex missed closers phrased "Ping me when the next thing comes up", and counted a bare code fence as an action |
| 3 | an agent violated the stop instruction | the detector matched "backoff" inside its TODO comment |
| 4 | Haiku scored 0 of 6 | Haiku marks completed work with `✓` (U+2713); the regex only matched `✅` |
| 5 | rule 3 control scored 1 of 6 | replies ended "…**Next:** Open `auth.spec.ts:42`" — the detector required a line to *begin* with the action |

Standing rule: print samples before believing a count, especially a count that says zero.

---

## 7. Still unmeasured

- Rules 2, 6 and 7 — leave-one-out in progress at the time of writing.
- Rule 4's null stands at n = 3 on one facet.
- Every ablation except the rule 7 merge is single-model.
- `rubric.md` still has no dimension for the skill's own distinctives; state continuity,
  visible wins and absence of preamble reach the score only through actionability at 20%.
