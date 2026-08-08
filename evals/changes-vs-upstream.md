# Changes against upstream

Base: `ayghri/i-have-adhd` at `2d19ad2`, which this fork matched exactly at the start
(verified by `git ls-remote`). Reasoning and full results live in `gap-analysis.md`;
this file is the change list.

Measurement vocabulary used below:

- **Ablated** — the rule was removed, the same cases re-run, and the difference counted.
- **Measured** — the behaviour moved in an A/B, but the rule was not isolated.
- **Reasoned** — grounded in a source, never isolated in a run.

---

## 1. The ruleset: 10 rules to 9

### Rule 1 — the opening action gets a size limit

Added: the first action must be startable in under two minutes with no decision in it.

- **Why:** the 2-minute rule and task-initiation research put the activation barrier on
  the *first* step specifically ("open the textbook to chapter 3", not "study for the
  exam"). The skill applied that constraint to rule 3, the closing action, and not to
  rule 1, the opening one.
- **Status: ablated.** Removing rule 1 entirely takes `error-report` from 3 of 3 opening
  with the fact or fix to 0 of 3 — replies open with "Before reporting, let me confirm…",
  a bare heading, and a code fence. The rule earns its place; the two-minute clause
  within it was not isolated.

### Rule 5 — absorbs old rule 7, and gains a durable-record clause

Retitled "Restate state, and leave a record that outlives the conversation". Now also
carries what old rule 7 said about showing what works.

- **Why (record):** Barkley's model puts the intervention at the *point of performance* —
  information externalised into the environment where the action happens. A chat message
  is not that. Asked to rank formatting inside one interaction, a durable record between
  interactions, and helper tone, the ADHD sources put the missing record second and named
  it the most common reason a project is dropped midway; formatting ranked last.
- **Why (merge):** ablation showed rule 7 fully redundant — identical counts with and
  without it, because rule 5's "Step 3 of 5 done: schema updated" already *is* making
  completed work visible. Merged rather than deleted, so no guidance was lost and one
  instruction slot was freed.
- **Why not "the agent just does the work":** the ADHD Creative Awareness Theory (Champ &
  Adamou, *J. Clin. Med.* 2024) classes reliance on another party for organisation as
  externally regulated and low autonomy, reinforcing learned helplessness. Scaffolding,
  not doing.
- **Status: measured, then deflated.** Candidate beat baseline on all four continuity
  cases. But an ablation against the *pre-amendment* rule 5 found the skill already
  produced a durable record in 2 of 3 trials; the clause moves that to 3 of 3 at n = 3,
  which is not a result. The continuity win belongs to the ruleset, not to this clause.
- **Rule 7 merge status: ablated**, with the caveat that its metric sat at ceiling.

### Rule 6 — estimates go per step, never as clock times

- **Why:** the sources split cleanly. Estimates attached to bounded micro-tasks help,
  because they bound how long the reader must tolerate the task before a stopping point
  (Stanford CTL). Estimates arranged as a chronological schedule hurt: durations swing by
  an order of magnitude, one overrun collapses the schedule, and the collapse ends the
  whole attempt rather than one step. The old rule was silent on both, and its own
  example ("an afternoon if not") sat at the vague end it prohibits.
- **Status: measured.** `time-estimate` went from 2.28 (baseline) to 4.92 (candidate)
  weighted. Never isolated by ablation.

### Rule 7 — neutrality now covers the reader, not just the error

Added: report the state, not the person. No "you forgot". And do not overcorrect into
softening, which reads as condescending.

- **Why:** the old rule banned "uh oh" and stopped there, leaving "you forgot the header"
  compliant. Emotional dysregulation and rejection sensitivity in ADHD are
  research-validated, and the documented result of attribution is disengagement rather
  than correction. Field reports are specific that a matter-of-fact reminder works *only*
  while free of aggravation, and that softened phrasing lands as patronising — hence both
  ends are pinned.
- **Caveat:** the branded construct "rejection sensitive dysphoria" is *not* in DSM-5 and
  has no standardised criteria. This rule rests on emotional dysregulation, which is
  validated, not on RSD.
- **Status: measured.** `user-caused-error` went from 2.68 to 5.00 weighted. Never
  ablated.

### Rule 8 — ranks lists instead of capping them

Was "Cap lists at 5 items". Now: rank every list, never drop a correct item to hit a
length, and cap only what the reader must *choose* between, at three.

- **Why the cap was wrong:** Miller's 7±2 governs *recall*. A list on screen is
  *recognition*. Cockburn, Gutwin & Greenberg's menu-performance model and Hawkins et al.
  find Hick's Law log-linear to 20 visible alternatives — there is no count at which a
  visible list collapses. The cap was misapplied cognitive science.
- **Why the choice cap survives:** choosing is not reading. Decision time grows with the
  number of alternatives, and the ADHD sources add decision paralysis on top.
- **Status: ablated.** Cap against rank, two cases, 3 trials: `list-overflow` went from
  5, 5, 9 items to 9, 9, 7, all ranked worst-first — more correct content kept, reader
  still not left to rank. `choice-overload` went from 8, 3, 3 to 3, 3, 3: the choice cap
  became *more* reliable once it stopped competing with a second number in the same rule.

### Rule 9 — unchanged in text

- **Status: ablated, survives.** Removing it makes every reply to "Thanks, that solved
  it" grow a closer: 0 of 3 becomes 3 of 3, mean length 24 characters becomes 80.

### Rule 3 — unchanged in text

- **Status: ablated, survives decisively.** Removing it takes the closing action from 8
  of 9 to 1 of 9, the largest single-rule effect measured here. This partly rehabilitates
  it: the reading literature grades a *universal* closing call-to-action as weakly
  evidenced, and that grading stands, but the model does not produce the behaviour on its
  own. The rule does work the research did not predict.

### Rule 4 — unchanged, and kept despite a null

- **Status: ablated, no effect.** The tangent lands in the last 15% of the reply and gets
  the same ~85 characters with or without the rule.
- **Kept anyway** because this is not rule 7's situation: nothing else in the ruleset
  covers tangent suppression, so removing it would delete guidance rather than
  deduplicate it. The case also tests only a reader-flagged tangent, not rule 4's second
  paragraph about the agent resolving its own mid-work questions.

### Rule 2 — unchanged, never ablated

- **Best-evidenced rule in the set.** NN/g eye-tracking measured +47% usability for
  prose reformatted as scannable bullets, +124% combined with conciseness, and the W3C
  Cognitive Accessibility working group prescribes numbered lists for ADHD readers by
  name. Left alone deliberately.

### Override clause 2 — destructive actions

Added: rule 1 does not apply; run the read-only preview yourself rather than delegating
it; never write a preview you have not run.

- **Why:** two of three candidate trials on `destructive-action` fabricated the output of
  a `git clean` dry run they never executed and told the reader those files were safe to
  lose. All three baseline trials stopped at the dry run. Per-case weighted 4.55 baseline
  against 3.33 candidate — the largest regression in the set, on the highest-risk case.
  An independent judge flagged the same two responses unprompted.
- **Corroboration from a different direction:** in the pharmaverse `{admiral}` repository,
  an agent instructed to regenerate documentation without R in its sandbox hand-wrote the
  generated file and presented it as output. Same failure mode.
- **The delegate-vs-run half** came from the independent judge, which marked down the one
  clean candidate response for pushing the dry run back onto the user.
- **Status: measured.** After the guard, 3 of 3 trials gave the command and stopped, with
  no fabrication, and stated they had not seen the output. Candidate blockers 3 → 1.

### Override clause 5 — options capped at 2–3

Was 2–4. Aligned with rule 8's choice cap.

### "What ADHD changes about reading" — a sixth fact

Added: neutral text is read as criticism; the reader supplies a tone and it skews harsh.
Motivates rule 7's blameless clause.

---

## 2. Reverted during the work

**The scope-line allowance** (rule 1 could carry step count and duration on the action
line) was added on gist-coherence grounds, then removed. 9 of 60 candidate responses
opened with a scope marker: mean weighted 4.61 against 4.64 for the other 51, no blockers
either side. No detectable effect in either direction, so it was not paying for its
length. Removed for that reason, not for being harmful — an earlier note claiming it was
implicated in the fabrications was pattern-matching on two responses and is withdrawn.

---

## 3. Evaluation harness

| Change | Reason |
| --- | --- |
| `--strict-mcp-config` added to the Claude runner | `--setting-sources ""` does not stop the operator's MCP servers loading. A two-token prompt carried ~49,000 tokens of context; the flag cuts it to ~6,800. A validity bug before a cost bug: judged responses were shaped by whichever servers that operator had connected. |
| UTF-8 decoding in `run_evals.py` | `subprocess.run(text=True)` with no codec decodes as the locale encoding. On Windows that is cp1252, the decode raises in subprocess's reader thread, stdout returns `None`, and `_parse_response` dies on `json.loads(None)`. Killed a run after 10 of 40 rows. |
| `marker.as_posix()` in `test_run_evals.py` | A `sh -c` stub interpolated a Windows path; `sh` ate the backslashes and `touch` wrote a junk file into the repo root. The test then failed for a reason unrelated to the behaviour under test. |
| Multi-turn cases | Every case was turn one, so re-entry, state across an interruption, and mid-task handoff were structurally unmeasurable. Cases now carry `prompt` or a `turns` array; turns replay because the runner uses `--no-session-persistence`. Turn 1 is byte-identical to a single-turn prompt, pinned by a test, so the 120 rows already recorded stay comparable. |
| `claude-readonly-tools` runner | Behaviour requiring the agent to act cannot be exercised with `--tools ""`. |
| `evals/README.md` | Documents the isolation check, that `--max-budget-usd` aborts *after* the cap rather than preventing spend, and the multi-turn contract. |
| Catalogue 14 → 24 cases | Four of ten rules and two of six override clauses had no case that would expose a regression. Ten added; `tempting-tangent` later rewritten self-contained after its first version asked for a fix to code this repo does not contain. |

---

## 4. Documentation

`evals/gap-analysis.md` — the full record, including every measurement that came out
flat and three retractions:

1. **"Rule 3 may be actively harmful"** — rested on a Reddit comment plus demand
   avoidance, which is not in DSM-5 or ICD-11 and whose systematic review called the
   evidence inconclusive. Withdrawn; the ablation then showed rule 3 is one of the most
   load-bearing rules in the set.
2. **Candidate improves safety** — one judge had it ahead 4.83 to 4.68; the independent
   judge scored it a tie at 4.78. Claim dropped.
3. **The `claude-opus-4-8` model pin is stale** — it resolves and runs. Flagged on
   appearance without checking.

A methodological caution is also recorded: the first pass over the rules 1/4/9 ablation
reported a flat null on all three. That was entirely metric error — the regex missed
closers phrased as "Ping me when the next thing comes up" and counted a bare code fence
as an action, and two cases were near-floor. A bad metric or a saturated case produces a
confident false negative indistinguishable from a real one.

---

## 5. What is still unmeasured

- Rules 2, 6 and 7 have never been leave-one-out tested.
- Rule 4's null stands at n = 3 on one facet.
- Whether a durable record actually helps a reader return days later cannot be scored:
  the harness has no write tools, so continuity cases measure whether a response
  *directs* state somewhere durable, not whether an artifact was created.
- `rubric.md` still has no dimension for the skill's own distinctives. State continuity,
  visible wins and absence of preamble reach the score only through actionability at 20%.
