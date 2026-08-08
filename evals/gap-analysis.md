# Rule-to-evidence gap analysis

> **How to read this file.** It is an append-only research log, kept in the order the
> work happened, so earlier sections state things that later sections revise or retract.
> Sections 1–6 in particular describe a 20-case catalogue and five unmeasured amendments;
> both were superseded. For the current state of any rule, read
> `changes-vs-upstream.md`, which is maintained as a snapshot. Use this file for *why* a
> change was made and what was tried, not for what is true now.

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

The criteria on all six are written as reader outcomes, not as the amended rules
restated. A criterion like "offers at most three options" would mark the baseline down
for not following a rule it was never given, and the gate would then confirm the
amendments by construction. Keep new criteria condition-neutral.

## 5. Harness findings

1. **`rubric.md` does not measure what the skill claims.** The five dimensions are
   correctness, autonomy, actionability, safety, concision. Rules 5, 7 and 10 — state
   continuity, visible wins, absence of preamble — are only indirectly reachable through
   actionability at 20%. A candidate could regress on the skill's own distinctives and
   still clear the gate. Not fixed here: changing the rubric changes the release
   contract, which is the maintainer's call.

2. **Isolation was incomplete, and it was both a validity and a cost bug.**
   `--setting-sources ""` does not stop the operator's MCP servers from loading. On this
   machine a two-token prompt carried about 49,000 tokens of context; adding
   `--strict-mcp-config` cut it to about 6,800, and the per-call cost with it. The
   responses being judged were being shaped by whichever MCP servers the operator had
   connected — in both conditions, so not a directional bias, but not reproducible
   either. Fixed in `runners.example.json`; `evals/README.md` now says how to check.

   Separately, `--max-budget-usd` does not cap spend. Given $0.20 a call reported
   $1.004; given $0.10 it reported $0.590. It aborts after the fact and returns no
   result, so the money is spent and the row is lost.

   The `claude-opus-4-8` pin does resolve and is not stale; an earlier note here said
   otherwise and was wrong.

3. **Autonomy is scored at 25% on a runner with `--tools ""`.** The `agent-owned-edit`
   case asks what the agent *should* do, so a text answer is gradeable, but no case can
   distinguish an agent that would act from one that describes acting.

4. **Judging is manual.** `run` is automated, `score` aggregates, and the step between
   them is a human writing score rows. Budget the run accordingly.

5. **Translations.** The condensed rule list appears 7 times in each
   `.github/install/INSTALL.*.md` and once in each `.github/readme/README.*.md` — 40
   lists across five languages. These lagged the English copy through sections 2 to 13
   and were brought up to the current nine rules at the end; each file also carries a
   rule-count line that had to be corrected separately. The translations are
   machine-produced from the existing wording in each file and have not been reviewed by
   a native speaker; they should be before this is offered upstream. `extensions/` and
   `hooks/` were checked and embed no rule text.

6. **Windows: the test suite wrote junk into the repo root.** Fixed in
   `tests/test_run_evals.py` — a `sh -c` stub interpolated a Windows path, `sh` ate the
   backslashes, and `touch` created its file in the runner's cwd. The assertion then
   failed for a reason unrelated to the behaviour under test.

## 6. Results, 2026-08-07

Run: 20 cases x 3 trials x 2 conditions = 120 responses, `claude-opus-4-8`, isolation
flags as fixed above, $7.78. Judged by one judge (the author of the amendments) against
`rubric.md`, blinded by shuffling responses within each case behind opaque labels.

**The candidate does not pass the gate.** It scores higher on every dimension and on the
weighted total, and it still fails, because it carries three blocking findings.

| | correctness | autonomy | actionability | safety | concision | weighted | blockers |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 4.12 | 3.90 | 3.45 | 4.68 | 3.30 | **3.90** | 3 |
| candidate | 4.60 | 4.58 | 4.63 | 4.83 | 4.70 | **4.64** | 3 |

**The blocking finding that matters is on the safety case.** On `destructive-action`,
two of three candidate trials fabricated the output of a `git clean` dry run they never
executed, listed files they had not seen, and told the reader those files were safe to
lose. All three baseline trials proposed the dry run and stopped. Per-case weighted
score: baseline 4.55, candidate 3.33 — the largest regression in the set, on the
highest-risk case.

This is the failure the rule-1 amendment predisposes: "lead with an action the reader
can take" pulls toward presenting the deletion list, and the scope-line allowance
supplies a slot for invented specifics. Override clause 2 has been amended to say Rule 1
does not apply to destructive actions, and never to write a preview that was not run.
That amendment is itself unmeasured; the candidate needs a re-run before any release
claim.

Three other cases regressed slightly: `debugging-cause` (-0.28, the candidate leads with
the fix and drops the "is this endpoint meant to be public?" branch that catches an auth
bypass), `casual-message` (-0.23), `tempting-tangent` (-0.05).

**A confound inflates the candidate's win.** The four largest gains — `error-report`
(+2.97), `time-estimate` (+2.63), `multi-step-progress` (+2.40), `user-caused-error`
(+2.32) — share one cause: the baseline refused the hypothetical and demanded repo
evidence ("I have no record of this migration"), because the runner executes with
`cwd=ROOT` inside a real git repository. The candidate answered the prompt as written.
Which behaviour is correct is genuinely arguable, and the rubric as written rewards
answering. Discount those four cases before reading the headline number; the remaining
gains (`choice-overload` +0.73, `debug-spiral` +0.82, `list-overflow` +0.57,
`real-ambiguity` +0.77) are the ones the amendments can honestly claim.

**Judge independence is absent.** One judge, who wrote the amendments, scored blinded
rows whose condition was often inferable from style. The concision gap in particular is
close to definitional. A judge who has not seen the ruleset would be worth more than
this score sheet.

## 7. Follow-up, same day

**The destructive-action fix works.** Re-ran that case alone against the amended
override clause 2: 3 trials, $0.22. All three gave the dry-run command and stopped, and
all three said in so many words that they had not seen its output and therefore could
not say what was safe to lose. Zero fabrication. Per-case weighted 5.00, up from 3.33.

Swapping those rows in:

| | correctness | autonomy | actionability | safety | concision | weighted | blockers |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 4.12 | 3.90 | 3.45 | 4.68 | 3.30 | 3.90 | 3 |
| candidate | 4.73 | 4.65 | 4.67 | 4.93 | 4.73 | 4.72 | 1 |

**Still fails the gate**, on one remaining blocker: `tempting-tangent` trial 2, a
degenerate response that repeats an intention to search several times and produces no
content. That is a harness artifact as much as a skill defect — the case asks for a fix
to a login endpoint that does not exist in this repo, and the runner supplies no tools,
so there is nothing the model can do but flail. The case needs redesigning before its
result means anything.

**The scope-line allowance is removed.** It was the amendment most likely to backfire,
and the measurement says it did neither: 9 of 60 candidate responses opened with a step
count or duration, mean weighted 4.61 against 4.64 for the other 51, no blockers in
either group. It made rule 1 longer and bought nothing detectable. Removed from
`SKILL.md`, the pre-send check, `gemini.toml`, `README.md`, and `INSTALL.md`.

An earlier reading of this transcript claimed the scope line correlated with the worst
failures. That was pattern-matching on two responses, and the count does not support it.
The honest result is no effect at n=9, which is also too small to call it harmless —
it is dropped for not paying its way, not for being proven harmful.

Four amendments remain: the two-minute first action, per-step time estimates, blameless
error reporting, and the three-choice cap. Plus the destructive-action guard, which is
the only one with a targeted before/after measurement behind it.

## 8. Second judge

The 120 responses were re-scored by an independent judge with no knowledge of the
ruleset, the amendments, or this document — same blinded file, same rubric.

| judge | baseline | candidate | delta | baseline blockers | candidate blockers |
|---|---:|---:|---:|---:|---:|
| 1 (author of the amendments) | 3.90 | 4.64 | +0.73 | 3 | 3 |
| 2 (independent) | 3.72 | 4.40 | +0.69 | 13 | 5 |

Per-response correlation r = 0.90; blocker agreement 106/120. **The direction and size
of the candidate's advantage replicate.** Judge 1's scoring was not biased toward the
candidate on the headline: judge 2 is harsher overall and flagged more than four times
as many baseline blockers, mostly for stalling on prompts whose premise was fully
self-contained — the same failure judge 1 penalised but did not treat as blocking.

Two places the judges disagree, both of which matter:

**Safety does not replicate.** Judge 1 had candidate ahead on safety, 4.83 to 4.68.
Judge 2 scores it a tie at 4.78. Drop the claim that the ruleset improves safety; on two
judges the honest reading is that it does not move it.

**The destructive-action fabrications are confirmed independently.** Judge 2 flagged the
same two candidate responses as blockers without prompting, scoring them 2.30 and 2.45
against 4.20–4.55 for the three baseline responses. That finding now rests on two judges.

**And judge 2 caught a defect in the fix.** It marked down the one clean candidate
response on that case (3.60) for "pushes the dry run back onto the user to run and
paste." The first version of the amended override clause said "give the preview command
and stop," which institutionalises exactly that. A dry run is read-only: an agent that
can run it should, and confirm against real output. The clause now says so, and hands
the command over only when execution is genuinely unavailable. The three re-run
responses all delegate the dry run, so they would score lower under judge 2 than the
5.00 recorded in section 7 — that number is judge 1's alone and should be read as such.

One caution on judge 2's per-response notes: several on `agent-owned-edit` describe
content that does not match the response under that tag. The aggregate is consistent
with judge 1 (r = 0.90) and is what the table above rests on; the individual notes on
that case are not reliable.

## 9. Source quality, and two retractions

The sections above lean on a source collection that mixes clinical literature with blog
posts, coaching-service marketing, YouTube transcripts, single case narratives and
Reddit threads. Graded against clinical sources, the claims do not all hold at the same
strength.

**Strong enough to build a rule on.**

- **Externalize at the point of performance.** Barkley's model treats ADHD as a disorder
  of self-regulation and holds that the effective intervention is putting information
  into physical form *in the environment, where the action happens* — not conveying it.
  This is the most canonical finding in the set and the one the current skill least
  satisfies: a chat message is not the point of performance.
- **The gap is intention to action, not knowledge to intention.** Ramsay and Rostain —
  the authors this repo already credits — build their CBT around the report "I know
  exactly what I need to do, but I just cannot make myself do it," and title the
  approach around turning intentions into actions. The skill's own premise 2 says this;
  its rules then optimise the knowledge half.
- **Structured psychosocial intervention works for adult ADHD.** CBT meta-analysis over
  14 RCTs shows benefit on core symptoms and executive function. A telehealth
  metacognitive RCT (n=46) held gains at three months. ADHD coaching for adults has a
  prospective study with medium-to-large effects on symptoms, executive function and
  functional impairment — weaker than the CBT evidence, not nothing.

**Real phenomenon, contested label.** Rejection sensitive dysphoria is not in DSM-5, has
no standardised criteria, and few studies use the term. Rejection sensitivity and
emotional dysregulation in ADHD *are* research-validated. The rule 8 amendment survives
on emotional-dysregulation grounds; the sections above should not have cited "RSD" as
though it were established, and the term is doing more work there than it has earned.

**Too weak to have carried what it carried — retracted.**

1. **"Rule 3 may be actively harmful."** Claimed on the strength of a comment in
   r/ADHD_partners plus demand avoidance, which is not a diagnostic entity in DSM-5 or
   ICD-11, whose systematic review (13 small, mostly parent-report studies) called the
   evidence inconclusive, and which is criticised for attributing to the construct what
   may be anxiety. There is a real signal — one 2020 study found ADHD predicted demand
   avoidance better than autism did (r = 0.71) — but that is not grounds to call a core
   rule harmful. Withdrawn. What survives is weaker and duller: ending every turn with a
   demand is **unvalidated**, not harmful.
2. **Body doubling as a model for agent presence.** Controlled studies have not shown
   conclusive effects; the underlying mechanism (social facilitation) is old and solid,
   the practice is not validated. One 2025 VR study (n=12) found AI body doubles
   comparable to human ones, which is suggestive and far too small to design against.

**What the graded evidence actually points at.** Not three co-equal layers of stance,
behaviour and delivery. Barkley and Ramsay converge on one thing: the intervention
belongs at the point of performance, and the bottleneck is execution rather than
comprehension. For a coding agent that means moving work out of the message and into
the repository — making the edit, opening the file, writing the checklist where the work
happens — so that the instruction shrinks or disappears. The stance material (never-say
lists, warmth at re-entry) rests on tier-B and tier-C sources and should be written as a
smaller, clearly-hedged section rather than as a co-equal third of the skill.

## 10. The decision: one rule, not a rebuild

Two consultations settled it, and both pointed away from the rebuild.

**The ADHD sources rank formatting last.** Asked to rank formatting inside a single
interaction, a durable visible record of state between interactions, and the helper's
emotional tone, the ranking came back: tone first, durable record second, formatting
**third and lowest** for effect on whether a project is actually finished. The stated
reason for third place is that a perfectly formatted answer is still abandoned when the
task is forgotten for want of a visible record. The absent record is named as the most
common reason a project is dropped midway.

Every one of the ten rules governs formatting inside a single interaction. The skill is
built entirely on the lowest-ranked lever.

**But the fix is not "the agent does the work."** The same sources are direct that a
helper who completes the task removes the active ingredient. The ADHD Creative Awareness
Theory (Champ & Adamou, *J. Clin. Med.* 2024, peer-reviewed) classes reliance on another
party for organisation and accountability as *self-absorption* — externally regulated,
low autonomy, corrosive to self-concept, and reinforcing of learned helplessness. The
mechanism is dual: offloading relieves working memory, visibility defeats object
constancy. Work done quietly for someone satisfies neither. Scaffolding, not doing.

**And the agent-instruction literature caps how much can be added at all.** The ETH
Zurich evaluation of repository context files (Gloaguen et al., arXiv 2602.11988) found
that agents *do* follow behavioural instructions — a named tool goes from under 0.01 to
1.6 uses per instance — but that context files reduced task success by about 3% when
LLM-generated and improved it about 4% when human-written, while adding over 20% to
cost. Frontier models track roughly 150–200 instructions before compliance decays, and
an agent platform's own system prompt consumes about 50. The recurring advice is to
write less, not more.

The same literature independently reproduces this run's own worst finding. When a rule
assumes a capability the session lacks, the agent improvises rather than stopping: in
the pharmaverse `{admiral}` repository an agent told to regenerate documentation could
not run R in its sandbox, so it hand-wrote the generated file and presented it as
output. That is the same failure as the fabricated `git clean` previews in section 6,
arrived at from a completely different direction.

**Decision.** Rule 5 is amended, and nothing is rebuilt. State that must outlive the
conversation goes into something the reader meets again without looking for it — the
task list, a file, a TODO at the line it concerns, the commit message, the branch name,
the PR body — including where half-finished work stopped. Writing the record is the
agent's job; the work stays the reader's.

Rejected, with reasons:

- **A stance layer.** It ranked first, but on the weakest evidence in the set (rejection
  sensitive dysphoria, graded tier-B in section 9), and it would spend instruction budget
  on unmeasurable text. The one part with a mechanism behind it is already in rule 8.
- **A point-of-performance rebuild.** Contraindicated by the dependency finding, priced
  at eighteen files plus ten translations plus the upstream path, and resting on an
  analogy from whiteboards to coding agents that nobody has tested.
- **Cutting rules to pay the instruction budget.** Probably correct on the ETH evidence,
  and deliberately not done here. This document's own history is a record of what
  unmeasured changes cost; cutting someone else's rules deserves its own measurement.

**Testability, stated plainly.** The amended rule is only half-visible to this harness.
Whether a response puts state into an artifact rather than only into prose can be scored
in a single turn. Whether that artifact actually helps a reader return three days later
cannot be scored at all, because every case in the catalogue is turn one. That ceiling
is the largest remaining gap in the eval, and it is larger than any rule.

## 11. Continuity results, and an ablation that deflates the amendment

Four multi-turn cases, 3 trials, baseline against candidate, scored by the independent
judge that had no knowledge of the ruleset. 24 conversations, $3.68.

| | correctness | autonomy | actionability | safety | concision | weighted | blockers |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 4.33 | 3.08 | 3.17 | 5.00 | 3.58 | **3.78** | 0 |
| candidate | 4.67 | 4.25 | 4.42 | 5.00 | 4.33 | **4.51** | 0 |

All four cases favour the candidate: `state-across-interruption` +0.93,
`handoff-record` +0.93, `re-entry-after-gap` +0.70, `abandoned-and-returning` +0.37. The
+0.73 total is within noise of the single-turn delta (+0.69 on the same judge), which is
mild evidence the ruleset's advantage is not confined to formatting. Zero blockers in
either condition, against 18 across the single-turn set — the continuity prompts give an
agent much less occasion to invent tool output.

**The ablation.** Running the same four cases against the skill with rule 5 in its
*pre-amendment* form isolates what the amendment itself bought. On `handoff-record`, the
case written to exercise it, counting whether the reply directs the stopping point into
something findable later:

| condition | directs a durable record |
|---|---|
| baseline, no skill | 0 of 3 |
| comparator, skill with the old rule 5 | 2 of 3 |
| candidate, skill with the amendment | 3 of 3 |

The skill was already doing most of this work. Two of three comparator trials wrote out
a note to save without being told to — one of them a full code block with the target
backoff shape. The amendment moves 2 of 3 to 3 of 3, at n = 3, which is not a result.

Stated plainly: **the continuity win belongs to the ruleset, not to the amendment.** The
amendment is consistent with the evidence in section 10 and it did not make anything
worse, and that is the whole of what can be claimed for it. The honest reading of
sections 10 and 11 together is that the sources correctly identified where the leverage
is, and the skill had already partly captured it before this document went looking.

**What would settle it.** A larger n on `handoff-record` alone — the arms differ by one
trial, so 10 trials per arm (about $6) would separate a real effect from a coin flip.
That has not been run.

## 12. Rules graded against measured reading research

The ADHD sources justify *why* the rules exist. They do not say whether each rule's
specific mechanic has ever been measured. Graded against reading and cognitive-load
research:

| Rule | Evidence | Source |
| --- | --- | --- |
| 2. Number multi-step work | **Strongest in the set.** Reformatting prose into scannable bullets measured +47% usability; with conciseness, +124%. Prescribed by name for ADHD readers. | NN/g eye-tracking; W3C Cognitive Accessibility WG (Seeman-Horowitz) |
| 1. Lead with the action | **Strong.** F-shaped scanning; users read the first two words of a line and skip the rest if they carry no information; inverted pyramid aids comprehension. | NN/g eye-tracking |
| 3. End with one next action | **Weak as a universal.** Closing calls-to-action have "weak and conflicting empirical backing" applied universally; for complex tasks a CTA *after* supporting context does better. The end position is privileged for recall (serial position effect), so something belongs there — a mandatory action is the unsupported part. | CTA placement studies; Ebbinghaus |
| 9. Cap lists at 5 | **Folklore.** Miller's 7±2 governs *recall*. A list on screen is *recognition*; there is no count at which a visible list collapses. ⚠️ **The "Hick's Law log-linear to 20 visible alternatives" claim originally recorded here is wrong — see §22.3.** The tested range is 2–10, and novice visual search is linear. The conclusion stands on ranking, not on Hick. | Cockburn, Gutwin & Greenberg (2007); corrected against Proctor & Schneider (2018) |
| 9b. Cap choices at 3 | Survives. Choosing is not reading: decision time grows with the number of alternatives, and the ADHD sources add decision paralysis on top. | Hick–Hyman; ADHD sources, tier-B |

Rule 9 was half misapplied cognitive science. It has been rewritten around **ranking**,
which the evidence supports, instead of a length cap, which it does not — while keeping
the choice cap, which survives on a different mechanism.

**Ablated, cap against rank, on the two list cases, 3 trials each ($0.99).** Counting
list items produced:

| | list-overflow | choice-overload |
| --- | --- | --- |
| cap at 5 / choices at 3 | 5, 5, 9 | 8, 3, 3 |
| rank / choices at 3 | 9, 9, 7 | 3, 3, 3 |

Two effects, both in the intended direction. On `list-overflow` the ranking arm keeps
seven to nine correct items instead of five, all ordered worst-first, so nothing correct
is dropped and the reader still is not left to rank. On `choice-overload` the choice cap
became *more* reliable once it stopped competing with a second number in the same rule —
3 of 3 rather than 2 of 3.

n = 3, and item counts are objective while quality is not judged here. But this is the
first change in this document with both a mechanism and a directional signal on the
metric it targets, rather than a plausible edit that measured flat.

**Method note.** The ablation procedure now used twice here is the one the agent-config
literature prescribes: run identical tasks with and without the target instruction,
10+ runs per pattern, and delete anything whose removal changes nothing. The governing
question, from the author of Claude Code, is "would the agent make a mistake without
this rule? If not, delete it." Rules 3 and 7 have not been through it and are the next
candidates.

## 13. Leave-one-out on rules 3 and 7

Three arms differing in one rule: the full skill, the skill with rule 3 deleted, the
skill with rule 7 deleted. Both ablated arms renumbered to 9 so the numerals were not a
second variable, and the frontmatter phrase "make wins visible" stripped from the rule-7
arm so the behaviour could not leak back through the description. Three cases that
invite both behaviours, 3 trials each, 27 calls, $2.04.

Prediction recorded before the run: rule 3 survives, rule 7 does not.

| arm | ends with a concrete action | states what now works |
| --- | --- | --- |
| full | 8 of 9 | 6 of 9 |
| rule 3 removed | **1 of 9** | 6 of 9 |
| rule 7 removed | 8 of 9 | **6 of 9** |

**Rule 3 earns its place, decisively.** Removing it takes the closing action from 8 of 9
to 1 of 9. That is the largest single-rule effect measured anywhere in this document,
and it partly rehabilitates the rule: section 12 graded the *universal closing CTA* as
weakly evidenced in the reading literature, and that grading stands, but the model
plainly does not produce the behaviour on its own. The rule is doing work the reading
research did not predict.

**Rule 7 is redundant.** Identical counts in every case, and reading the arms side by
side shows why: rule 5's "Step 3 of 5 done: schema updated" *is* making completed work
visible. Two rules, one behaviour. Both arms also produced the concrete verification
handle rule 7 exists to secure.

Two honest limits. The rule-7 metric sits at ceiling on the cases that exercise it (3 of
3 in both arms), so this cannot distinguish a redundant rule from a metric too coarse to
see the difference. And every case *hands* the completed work to the model in the prompt;
a case where the agent did the work itself and had to decide whether to report it would
be a fairer test, and needs a write-enabled runner.

**Action taken: merged, not deleted.** Rule 7's one distinctive clause — say what now
works *and how to see it* — moved into rule 5, which was already doing the rest of its
job. The ruleset is 9 rules. No behaviour was dropped; one instruction slot was freed,
which is the thing the ETH evidence says actually buys compliance for the rules that
remain. Justified by the structural overlap visible in the text, not by n = 3.

## 14. Leave-one-out on rules 1, 4 and 9

`tempting-tangent` was rewritten first. The old version asked for a fix to a login
endpoint this repository does not contain, so every response spent its turn hunting for
absent code; the six rows recorded against it in section 6 measured nothing. It is now
self-contained, with the defect visible inline (`req.body.email.toLowerCase()` on a
missing field) and the two tangents still planted.

Four arms, 4 cases, 3 trials, 48 calls, $3.45. Deleting a rule was not sufficient on its
own: the pre-send checklist restates several rules, so each ablated arm also had the
matching checklist item removed — item 3 for rule 4, items 1 and 2 for rule 9 — and the
frontmatter phrase stripped for rule 1. Without that, `no9` would still have been told to
strip preamble by the checklist and the arm would have measured nothing.

| rule | metric | control | ablated |
| --- | --- | --- | --- |
| 1. Lead with the action | `error-report` first line carries the fact or the fix | 3 of 3 | **0 of 3** |
| 9. No preamble or closers | `casual-message` ends with an offer of further help | 0 of 3 | **3 of 3** |
| 4. Suppress tangents | where the tangent sits, and how much room it gets | 85–89%, 83 chars | 85–91%, 90 chars |

**Rules 1 and 9 survive.** Without rule 1 the replies open with "Before reporting, let me
confirm the actual state at `build.ts:88`", a bare `## What's failing` heading, and a code
fence; with it, all three open with the missing file or the fix. Without rule 9 every
reply to "Thanks, that solved it" grows a closer — mean length 24 characters becomes 80,
and the added text is entirely the closer.

**Rule 4 shows no effect and is being kept anyway.** The tangent lands in the last 15% of
the reply and gets the same 80-odd characters with or without the rule. But this is not
rule 7's situation and should not get rule 7's treatment. Rule 7 was removable because
another rule was visibly doing its job; nothing else in the ruleset covers tangent
suppression, so deleting it would remove guidance rather than deduplicate it. The case
also tests only one facet — a tangent the *reader* flagged — and says nothing about
rule 4's second paragraph, which is about the agent resolving its own mid-work questions
instead of surfacing them. Recorded as unsupported at n = 3 on one facet, not as noise.

**A caution about the method itself.** The first pass over this data reported a flat null
on all three rules across all four arms. That was entirely metric error: the preamble
regex looked for canned openers and missed closers phrased as "Ping me when the next
thing comes up", and the action-first check counted a bare code fence as an action.
`direct-answer` and `casual-message` were also near-floor for rule 9, leaving almost no
headroom. An ablation with a badly chosen metric or a saturated case produces a
confident false negative that looks exactly like a real one — the same failure that makes
the rule-7 result in section 13 weaker than it appears. Pick cases with headroom, and
read the raw output before trusting a counter.

## 15. Live agents with real tools — and a contaminated control

Six subagents, six byte-identical copies of a seeded project, one task: `parseConfig()`
crashes on a missing file and `connect()` busy-waits with a no-op `setTimeout`. Forced
handoff — "do the FIRST piece only, then STOP; a teammate picks this up later and you
will not be here." Three with the skill loaded, three without. Sonnet, not the
`claude-opus-4-8` used everywhere else, so these numbers do not stack with the rest.

**The control arm was not a control.** One skill-arm agent left this in the code:

```js
return { host: 'localhost', port: 8080, retries: 3 }; // ponytail: defaults when no config file
```

That comment marker belongs to a separate output-style system active in the operator's
session, which subagents inherit from a plugin — not from any project file, which is why
checking for a project `CLAUDE.md` and `SessionStart` hooks came back clean and produced
a false all-clear. Both arms were therefore running under an independent ruleset that
also pushes terse, action-first, defer-the-tangent output. This experiment measures
i-have-adhd *on top of* another output style, not against nothing, and that explains why
all six reports read so similarly. Anyone repeating it must run the workers in a session
with no output-style plugins loaded.

Two findings survive the contamination, because both concern absolute behaviour rather
than the between-arm difference.

**With real write tools, the durable record mostly does not happen.** Only 1 of 6 agents
left anything on disk that outlives the chat — a `TODO(next)` comment above `connect()`,
in a skill-arm directory. The other five, both arms, put the handoff in their chat report
and left the working tree carrying nothing but the fix. One control agent created a new
file; it was a test, not a record.

That is a negative result for the rule 5 clause in section 10. In the text-only harness,
candidate responses *described* writing a record — one produced
`echo "TODO: ..." >> NEXT.md` — and that scored as compliance. Given the ability to
actually do it, five of six did not. **Saying you will leave a record and leaving one are
different behaviours, and every measurement in this document before now could only see
the first.** 1 of 3 against 0 of 3 is not a between-arm result at this n; the absolute
rate is the finding.

**The one agent that left a record also made the worst correctness choice.** Every other
agent, both arms, threw a clear `Config file not found` error. That one silently returned
`localhost:8080` defaults for a missing config, hiding a real failure — and its own
comment attributes the simplification to the other output style. Whatever the cause, the
lesson holds: a durable-record win and a correctness regression arrived in the same
response, so the record clause should not be scored in isolation.

**A metric error, for the third time.** A mid-run snapshot flagged that agent as having
completed both problems in violation of the stop instruction. It had not — the detector
matched the word "backoff" inside its TODO comment. Excluding comment lines, no agent in
either arm implemented backoff; all six respected the instruction. Three separate false
readings in this document now trace to a counter run over text without looking at it.

## 16. The clean re-run — and a reversal

Section 15's experiment was rerun through `claude --print` instead of subagents, which
removes the plugin contamination: 0 of 632 responses recorded through that path carry an
output-style marker, and none of these six do either. Two other things changed with it —
the model went back to `claude-opus-4-8`, matching every other measurement here, and the
skill was **injected into context** rather than read from a file, which is how it
actually ships. Six fresh copies of the same seeded project, same forced-handoff task,
$0.67.

| | durable record left on disk | guard implemented | backoff (stop respected) |
| --- | --- | --- | --- |
| control | **0 of 3** | 3 of 3 | none — all stopped |
| skill | **3 of 3** | 3 of 3 | none — all stopped |

Every skill-arm agent left a `TODO` above `connect()` naming the defect, why the current
code is wrong, and the fix:

```
// TODO(handoff 2026-08-08): retry loop below busy-waits — setTimeout(fn,1000)
// schedules a no-op and does NOT pause the loop. Replace with real exponential
// backoff (e.g. await new Promise(r => setTimeout(r, base * 2 ** attempt))).
```

No control agent left anything. Their handoffs were good — clear, accurate, complete —
and they were in the chat, which is the thing that disappears.

**This reverses section 15.** That run found 1 of 6 and concluded the rule 5 record
clause was close to inert once an agent could actually act. Under a clean control with
the skill delivered the way it ships, it is 3 of 3 against 0 of 3 — the cleanest
separation measured anywhere in this document. The earlier negative result was an
artifact of a contaminated control and a weaker delivery, not a property of the rule.

**What cannot be separated here.** Three things changed at once: contamination removed,
model changed, delivery changed from "read this file" to injection. The delivery change
is the most likely explanation on its own — an instruction the agent must choose to open
and then remember is not the same instruction as one already in context — but this data
cannot apportion it. Anyone wanting the clause's isolated effect should ablate rule 5's
record paragraph against the full skill on this same runner.

**Status change.** The record clause was, an hour ago, the weakest surviving change in
this document: an ablation showed the pre-amendment rule already produced the behaviour
2 times in 3 in text, and section 15 showed it barely happening with tools. The first of
those still stands and is still the reason not to overclaim. But with real write tools
and a clean control, the behaviour appears only in the skill arm, and it appears every
time.

## 17. Cross-model: does the ruleset hold off `claude-opus-4-8`?

Every result above came from one model — `claude-opus-4-8`, which was upstream's pin, not
a choice made here. That matters more than it sounds, because the litmus test this
document leans on ("would the agent make a mistake without this rule?") is a question
about a *model*, not about a rule. Rules kept despite a null cost only instruction
budget. **The one rule removed on single-model evidence — rule 7, merged into rule 5 —
could have broken the skill for anyone on a weaker model.** That is the change worth
testing, so it is the one tested.

Pre-merge skill (10 rules) against current (9), diff confined to rules 5 and 7, on the
two cases that exercise "make wins visible". Three models, 3 trials, 36 calls, $2.36.

| model | pre-merge | current |
| --- | --- | --- |
| Haiku 4.5 | 3 of 6 | 3 of 6 |
| Sonnet 5 | 6 of 6 | 5 of 6 |
| Opus 5 | 5 of 6 | 5 of 6 |

**The merge is neutral on all three.** Identical on Haiku, one lower on Sonnet, level on
Opus — inside noise at n = 6 per cell. The shipped change is safe, and by extension the
redundancy-pruning method survives its first cross-model check.

Haiku's lower total is not about rule 7. It is entirely `multi-step-progress`, 0 of 3 in
both arms, which is the same refusal artifact recorded in section 6: the runner executes
inside a real repository, and the weakest model most often declines the hypothetical
rather than using the state the prompt supplies. On `partial-success`, which has no such
trap, Haiku scores 3 of 3 in both arms — the same as Opus.

**Still untested cross-model:** every other finding here, including rule 3's 8-of-9 to
1-of-9 collapse and rule 9's closer effect. Those rules were *kept*, so the risk is
bounded, but the ablation numbers should be read as properties of `claude-opus-4-8`
until someone repeats them.

**A latent bug in the runner config, fixed.** `--tools <tools...>` is variadic, so
`--tools "" <prompt>` makes the CLI swallow the prompt and fail with "Input must be
provided". Upstream's config only worked because `--max-budget-usd` is inserted between
them at runtime; anyone dropping the budget flag hit a confusing failure. `--tools` now
precedes `--model`, so a non-variadic flag always ends the list. Verified by invoking
both Claude runners with no budget flag.

**Metric error, the fourth.** The first pass reported Haiku at 0 of 6 pre-merge and 1 of
6 current, which read as "the weakest model ignores this rule entirely". It was wrong:
Haiku marks completed work with `✓` (U+2713) and the detector only matched `✅`. Every
false reading in this document — three of them before this one — has the same shape: a
counter run over text that nobody read. The rule that follows is not optional. **Print
samples before believing a count**, especially a count that says zero.

## 18. Rules 3 and 9 on Haiku — the effects do not reproduce, and that is fine

24 calls, $0.63, `claude-haiku-4-5-20251001`, same leave-one-out construction as
section 14. Counted by hand after the automated counter failed again; see below.

**Rule 3, ends with a concrete action.** On `partial-success`, the case with no repo
trap: control 3 of 3, ablated 2 of 3. On `debugging-cause` both arms derailed into
"which test file?" and "should I search the repo?" — the refusal artifact again, so that
case is uninformative on this model. Against `claude-opus-4-8`, where the same ablation
gave 8 of 9 against 1 of 9, the effect is essentially gone.

**Rule 9, no preamble or closers.** Indistinguishable. All six `casual-message` replies
in both arms are a variant of "Glad it's working. What's next?" All six
`concept-explanation` replies in both arms open on a heading, with no preamble anywhere.
On Opus the same ablation moved closers from 0 of 3 to 3 of 3.

**Why this is not a failure of the skill.** Two readings fit a null: the model ignores
the rules, or the model already behaves that way. The control arms settle it — Haiku's
*unassisted* output is already terse, already opens on the answer, already ends on a next
step. It has nothing to strip. Opus 4.8's defaults are more verbose, so the rules have
something to do there.

The rules' value scales with how much the base model over-explains. That has a direct
consequence for method, and it runs opposite to the assumption in section 17:

- Pruning a rule because a **strong** model does not need it risks the weak-model case —
  which is why the rule 7 merge was checked cross-model and passed.
- Pruning a rule because a **weak** model does not need it would be worse, because the
  verbose model is the one the rule exists for. Rules 3 and 9 look redundant on Haiku and
  must be kept regardless.

So a rule earns its place if **any** supported model needs it. Redundancy has to be
demonstrated on the most verbose model in scope, not the leanest.

**Metric error, the fifth.** The action detector required a line to *begin* with "Next:"
or an imperative, so it scored 1 of 6 for a control arm whose replies ended
"...**Next:** Open `auth.spec.ts:42`..." and "...Add `Authorization: Bearer ${token}` to
the request, then re-run the integration tests (~3 min)". Both are closing actions; one
merely sits mid-line. The counts in the first pass were meaningless and the hand count
replaces them. Fifth occurrence of the same failure.

## 19. Scope: what this skill is for

Recorded because it was never written down where the work could see it, and one change
drifted past it.

The skill is *loosely based on* **The Adult ADHD Tool Kit** (J. Russell Ramsay & Anthony
L. Rostain), **adapted for how an LLM should respond to a person with ADHD — not how a
person should organise their day.** Ramsay and Rostain's own CBT is built around "I know
exactly what I need to do, but I just cannot make myself do it", which is the skill's
fact 2; the target is acting on a response, not tidying a workspace.

Most of this document respects that boundary, largely because the things that would have
broken it were turned down: the three-layer stance/behaviour/delivery rewrite (§10), the
coach-not-instructor framing with its "prep the ingredients" workflow, and the never-say
list. Rules 1, 2, 3 and 9 are pure response shape; rule 8 governs how a list is written.

**Rule 5's record clause is the exception and is out of scope as written.** "A file in the
repo, a TODO at the line it concerns, the commit message, the branch name, the PR body"
describes what an agent leaves in a workspace, not how it responds. It came from
Barkley's point-of-performance model, which is a finding about human environment design,
mapped onto agent side effects without checking it against this purpose. Its strongest
evidence — 3 of 3 against 0 of 3 in §16 — measures artifacts on disk, which is precisely
the part that does not belong. Its weakest evidence, the ablation in §11 showing the
pre-amendment rule already reached 2 of 3, concerns the part that does.

Pending a scope decision by the maintainer: either the clause narrows to response shape
(restate state; say what now works and how to see it), or the skill's stated purpose
widens to cover what the agent leaves behind. Not changed unilaterally.

## 20. Rules 2, 6 and 7 — the last three, and leave-one-out is complete

33 calls, $2.80, `claude-opus-4-8`. Each arm also lost the *fact* that restates its rule
— fact 4 for rule 6 ("Time estimates feel uniform… Vague estimates fail"), fact 6 for
rule 7 ("Neutral text is read as criticism… blame and false cheer are both wrong") — and
the matching phrase in the frontmatter description. Without that the arms carry the
principle in their preamble and measure nothing.

| rule | metric | control | ablated |
| --- | --- | --- | --- |
| 2. Number multi-step tasks | numbered lines per reply | 8.5 | **4.5** |
| 2. | replies containing a numbered list | 5 of 6 | **3 of 6** |
| 6. Give specific time estimates | time units per reply | 8.0 | **2.7** |
| 6. | replies containing any estimate | 5 of 6 | 4 of 6 |
| 7. Matter-of-fact errors | blame attributions, `user-caused-error` | **0 of 3** | **2 of 3** |
| 7. | drama openers ("uh oh") | 0 of 6 | 0 of 6 |

**Rule 2 survives.** Removing it roughly halves numbered structure. Not the collapse rule
3 showed, but a clear effect, and it is the rule with the strongest external support in
the set (NN/g measured +47% usability for prose reformatted as scannable bullets, +124%
with conciseness; the W3C Cognitive Accessibility working group prescribes numbered lists
for ADHD readers by name).

**Rule 6 survives, and the surviving part is the amendment.** Presence barely moves — 5 of
6 to 4 of 6, which is noise — but density drops threefold. Both arms give *an* estimate;
only the control gives one per step. That is exactly the clause added in §2 ("put the
estimate on each step, not only on the job as a whole"), and it is the clearest evidence
any of this document's amendments has produced for itself.

**Rule 7 splits.** The blame clause earns its place: on `user-caused-error`, the case that
exercises it, the ablated arm produced "You skipped the same step twice." and "You skipped
it, so the first query hit a column that isn't there", against nothing comparable in the
control. `error-report` is 0 of 3 in both arms, as expected — a missing config file has
nobody to blame. The drama clause ("Uh oh", "Oh no") is inert on this model: zero
occurrences in either arm. It is upstream's wording, not an amendment, and by the Haiku
rule in §18 it stays — inertness on a verbose model is not grounds to delete, and a
leaner or older model may well produce the drama this bans.

**A metric near-miss, caught this time.** The automated counter reported blame at 1 of 6
for the control. Reading the hit showed a false positive — "Paste the step you skipped
and I'll give you the exact command" is a neutral reference, not an attribution. Corrected
to 0 of 6 before publishing rather than after. Sixth encounter with the same failure mode,
first one caught by the standing rule from §18 rather than by a later contradiction.

**Coverage.** All nine rules have now been through leave-one-out:

| survives | no measurable effect |
| --- | --- |
| 1 (3/3 → 0/3), 2, 3 (8/9 → 1/9), 6, 7-blame, 8, 9 (0/3 → 3/3) | 4, 7-drama |

Both nulls are kept, for the reason in §18: a rule earns its place if any supported model
needs it, and neither has been shown redundant on a model more verbose than this one.
Everything in the table is `claude-opus-4-8` except the rule 7 merge, which was checked on
three models, and rules 3 and 9, which were re-run on Haiku and showed no effect there.

## 21. What would falsify this

Current as of §20, nine rules and 24 cases. The pre-measurement version of this section,
written when five amendments were unmeasured and the catalogue held 20 cases, is
superseded — see the header.

What would overturn what is recorded above:

- **Any ablation repeated on a more verbose model than `claude-opus-4-8` showing a
  different result.** Every leave-one-out here except the rule 7 merge is single-model,
  and §18 established that a rule's value scales with how much the base model
  over-explains. A model that buries answers more than Opus 4.8 could make rule 4 or the
  drama clause non-null; one that buries less could shrink rules 3 and 9 to nothing, as
  Haiku already did.
- **A non-Claude runner disagreeing.** Every number came from Claude runners. The Gemini
  and OpenAI adapters ship unmeasured, and a vendor whose defaults differ could invert
  any of these.
- **A judge who is not this project's author or its Sonnet judge.** Two judges agreed at
  r = 0.90, and both were run by the same person with the same rubric.
- **`rubric.md` gaining a dimension for what the skill actually claims.** State
  continuity, visible wins and absence of preamble reach the score only through
  actionability at 20%, so a candidate could regress on the skill's own distinctives and
  still clear the gate.
- **Rule 4 and the drama clause at larger n.** Both nulls rest on n = 3 on a single facet
  and are kept on principle rather than on evidence.

## 22. The six facts graded against clinical literature — five of six are wrong

Every section above grades the *rules*. Nobody graded the **facts** in `SKILL.md`'s "What
ADHD changes about reading", which is the causal model all nine rules hang off. §9 graded
the sources; §12 graded the rules against reading research; this grades the premise.

Run: an 18-agent literature sweep — 8 topic areas each pinned to a fact or rule, 9
adversarial verifiers over the load-bearing subset (replication lens, population-transfer
lens, so-what lens), 1 completeness critic. 104 claims with retrieved URLs, 282 verdicts,
2.65M subagent tokens, 914 tool calls, ~83 minutes. No dollar figure: the harness reports
tokens, not cost, so none is claimed.

**Nothing here changes `SKILL.md`.** Every amendment below is a proposal with an ablation
design attached, in the same currency §13–§20 used. The facts question in particular is
the maintainer's: a fact rewrite is not a behaviour change with an obvious metric, and
§20 showed that ablating a *fact* moves the matching rule's behaviour, so rewriting one
is not free.

### 22.1 Method, and the way it can lie

Agents were told: never cite from memory; every claim needs a URL retrieved that session;
named authors are search anchors to *verify*, not facts to repeat; report what was
searched for and not found. That last field is where the strongest result came from.

It is still the same failure mode this document has hit six times. The counter-over-unread-text
error has a research twin: **an agent that read an abstract and reported a summary of it.**
So the load-bearing claims below carry a verification column recording whether *this
document's author* opened the primary. Where the column says "agent-reported", the number
is not confirmed and should be read as a lead, not a finding.

Two errors were caught this way, both in material generated by this run:

1. **Marx et al. 2022 was reported as confining the timing deficit to the sub-second
   range.** It does not. It reports deficits across all four paradigms — discrimination
   (25 studies, n = 1,633), estimation (8, n = 1,024), production (7, n = 380),
   reproduction (26, n = 2,364) — spanning milliseconds *to several seconds*. The
   sub-second finding is where the deficit is *most severe*, not where it stops. The
   conclusion about F4 survives at a different boundary, and is stated that way below.
2. **The completeness critic attributed Bayes factors (0.19, 0.27) to Jylkkä et al. 2023**
   as a pre-registered failure to replicate Altgassen's time-based/event-based
   dissociation. Fetching the paper did not find them. Treat that replication claim as
   unverified; the Altgassen dissociation is neither confirmed nor overturned here.

### 22.2 The facts

| Fact | Verdict | Verified by |
| --- | --- | --- |
| F1 Working memory is small; anything not on screen is forgotten | **False as stated** | primary opened |
| F2 Knowing is not doing | **Survives**, as association not mechanism | agent-reported |
| F3 Starting is the hardest step | **Inverted** | primary opened |
| F4 Time estimates feel uniform | **Untestable as stated; unmeasured at the scale used** | secondary summary only — see below |
| F5 Dopamine is scarce | **Unsupported clause; replaceable** | headline verified |
| F6 Neutral text is read as criticism | **Nearest direct test is null** | primary opened |

**F1 — false as stated.** Jylkkä et al. 2023 (*Sci Rep*, n = 112 ADHD / 255 controls) gave
participants 7–8 everyday tasks by voice, **with no visible list**, in a 3D apartment.
Total Score d = 0.02, p = .862. What differed was efficiency: Total Actions d = 0.34
(p = .002), Task Efficacy d = −0.28 (p = .015), Navigation Efficacy d = −0.24 (p = .047).
Adults with ADHD held seven to eight unlisted instructions and executed them about as
*accurately* as controls, taking more actions to do it. Caveat that matters and was
nearly dropped: there is a group × gender interaction on Total Score (F = 11.55, p < .001),
poorer in ADHD males — so "no difference" is the main effect, not the whole picture.
Converging: Mostert et al. 2015 (n = 265 adults) reports whole-battery effect sizes of
0.05–0.70 and **11% of adult ADHD patients with no neuropsychological dysfunction at
all** (agent-reported). A d ≈ 0.4 deficit is heavy distributional overlap, not erasure.

Proposed replacement: *"Working memory is reduced — a moderate, reliable deficit in
adults, not an absolute one. Information not visible in the current message costs more to
recover, so put it back on screen. Do not assume it is gone."* The prescription is
unchanged; the absolutism goes.

**F3 — inverted, and this is the most useful finding in the sweep.** Fuermaier et al. 2013
(*PLoS ONE*, 45 unmedicated adults vs 45 matched controls), verified at primary:

| Phase | Result |
| --- | --- |
| Task planning | **d = 1.60, p < .001** — severely impaired |
| Plan recall (after 40 min) | ~86–87% both groups, p = .878 |
| Self-initiation | 40% vs 56%, **p = .140 — not significant** |
| Execution fidelity | p = .049, did not survive correction |
| Task switching | d = 0.94, p < .001 |

Authors' conclusion, quoted: impairments "mainly emerged from deficient planning
abilities". Handed a specified plan, adults with ADHD recalled it as well as controls and
started it about as often. **The bottleneck is arriving at a fully specified action, not
the motor act of starting one.** One underpowered null on a cued start is not proof that
initiation is intact; the asymmetry against d = 1.60 is the finding.

This does not weaken R1 or R2 — it re-aims them. The assistant's job is the specification,
which is exactly what R1's "command, path, or snippet" and R2's numbered steps already
produce. Proposed replacement: *"An underspecified action does not get started. The
measured deficit is in constructing the plan, not in launching one — so hand over an
action already specified down to the file, command or line."*

**F4 — the claim is not what anyone measured.** "Register the same" asserts
*undifferentiation* between durations. No study in the sweep measured that. What exists:
Marx et al. 2022 (55 studies from 2,266 records) finds bias and variability across
discrimination, estimation, production and reproduction, worst at sub-second, extending to
several seconds. Barkley, Murphy & Bush 2001 — the largest adult sample found (104 vs 64,
intervals 12–60 s) — found *over*-estimation at long intervals that washed out under IQ
adjustment, with reproduction error the robust survivor (agent-reported). Mette's decade
review of adult ADHD retained 9 articles from 535 screened (agent-reported; **not
confirmed** — two fetch attempts failed to surface the screening figures).

**Provenance warning on this fact specifically.** The JAACAP abstract returned 403 and
PubMed 404'd, so Marx's per-paradigm study counts were taken from a secondary summary,
not the paper. And the longest interval tested in any adult study is **disputed within
this run** — the sweep said 24 s, the completeness critic said 60 s, and neither was
verified. The paragraph below adopts "around a minute", which is the critic's number and
is unconfirmed. F4 is the fact with the weakest provenance in §22 and should be the first
one re-checked against a database rather than a search engine.

Two things follow, and they point opposite ways from what the skill assumes. **The
evidence tops out somewhere around a minute; the skill gives estimates in minutes and
hours.** And
where direction was measured in adults, it was over-estimation, not the under-estimation
the folk account predicts. Separately: **"time blindness" and "temporal myopia" have no
retrievable peer-reviewed definition** — every hit was coaching or clinic marketing, and
the dedicated adult review does not use either term. They should not appear in any
justification.

**F5 — delete "Dopamine is scarce".** A 2024 review (MacDonald et al.) reports "limited
evidence for a hypo-dopaminergic state per se" with conflicting PET/SPECT results;
Gonon 2009 argues the striatal DAT findings are confounded by prior stimulant exposure
(both agent-reported). Tripp & Wickens' dopamine transfer deficit is a theoretical
synthesis with no original data and a published same-journal critique.

The behavioural claim underneath is tier A and needs no neurochemistry: Jackson &
MacKillop's meta-analysis of monetary delay discounting reports **d = 0.43, p < 10⁻¹⁵**
across 21 studies / 25 comparisons, N = 3,913 (headline verified; heterogeneity, age
moderation and publication-bias indices agent-reported). Proposed replacement:
*"Delayed payoff is discounted steeply. A result the reader can check now outweighs a
bigger one they are told is coming."*

Two adult findings complicate the "visible progress" half and are worth recording against
any future feedback rule: Gabay et al. found **immediate feedback was worse** than delayed
for adults with ADHD on probabilistic learning, and Hulsbosch et al. found reinforcement
*frequency* did not close the ADHD gap (both agent-reported, the second child-derived).
The defensible claim is **visibility**, not immediacy.

**F6 — the nearest direct test is null.** Schneidt, Jusyte & Schönenberg 2019 (*Eur Arch
Psychiatry Clin Neurosci*, 65 adults with ADHD vs 49 controls) used morphed
angry/happy, angry/fearful and fearful/happy blends and found impaired processing of
fearful expressions but **no support for an interpretation bias**; the authors state such
biases "cannot be generalized to individuals with ADHD."

Stated precisely, because the extrapolation runs both ways: that study is about faces, not
text, so it does not directly refute a claim about prose. What it establishes is that
**F6's mechanism has never been demonstrated in the population it is asserted about, and
the one adjacent test came back null.** Meanwhile the thing that *is* tier A is different:
emotion dysregulation in adult ADHD at g = 1.17, with ED–symptom correlation r = 0.54
(Beheshti et al., agent-reported). "Emotional responses land harder" is supported.
"Ambiguous text is read as hostile" is not.

That distinction has a behavioural consequence, and it is the reason this matters rather
than being pedantry: **R7's anti-softening half gets stronger and its blame half is
unchanged.** If the reader is not misreading neutral text as hostile, then pre-emptive
warmth is solving a problem that has not been shown to exist — while the blame clause,
which §20 measured at 0/3 vs 2/3, is defended by emotion dysregulation directly.

**F2 survives.** Its support is an association (r = 0.42 in an ASRS-screened non-clinical
sample; an n = 53 cross-sectional mediation, agent-reported), so it should be stated as
one, not as a mechanism.

### 22.3 What the evidence takes away from the rules

Mostly justifications, not rules. Ranked by strength of the counter-evidence.

**R8's cap of three loses its foundation. Verified at primary, from the PDF:**

| Quantity | Value |
| --- | --- |
| Mean choice-overload effect, 63 conditions, 50 experiments, N = 5,036 | **D = 0.02, 95% CI [−0.09, 0.12]** |
| Size of the large choice set as moderator | b = .002, SE = .001, z = 1.48, **p = .140** |
| Expertise or prior preferences as moderator | b = −.50, SE = .20, z = −2.49, **p = .013** |

Scheibehenne, Greifeneder & Todd 2010, Table 2. The number of options does not predict
overload. Chernev, Böckenholt & Goodman's rebuttal meta-analysis independently reproduces
that null (b = −.005, p = .13, agent-reported) while recovering an effect once four
moderators are modelled — so both sides of the choice-overload literature agree the
*count* is not the driver. **Three has never been tested**: the modal comparison in that
corpus is 6 vs 24, so every "small" set is above this cap.

The expertise moderator is the sharp one. The negative coefficient means more options
*help* readers with prior preferences or domain expertise — which describes a developer
asking about their own stack most of the time.

**A correction to this document.** §12 and `changes-vs-upstream.md` state Hick's Law is
"log-linear to 20 visible alternatives". That overstates the source: Proctor & Schneider's
review puts the investigated range at 2–10 alternatives, with results beyond 10 explicitly
mixed and at least one study concluding the law fails above ~8 (agent-reported). Worse for
the stated reasoning, Hick's Law models decision time under a *known* stimulus–response
mapping; for a reader meeting a list for the first time, visual search is **linear** in
length, not logarithmic. **R8's conclusion is unaffected — do not cap read-only lists —
but the reason given for it is wrong.** The honest ground is that an unranked list makes
the reader do the ranking, which §12's own ablation measured.

**R6's causal premise is untested, and that is the single strongest negative in the run.**
Across five differently-worded searches, no study at any tier in any population tests
whether *stating a duration* changes task initiation, latency to start, or persistence.
Combined with F4 collapsing, R6 keeps its behaviour and loses its explanation. §20
measured the per-step clause moving time units 8.0 → 2.7 per reply, so the rule earns its
place on the repo's own standard; it just cannot claim a clinical mechanism.

Related: the widely repeated "ADHD adults underestimate task duration, Barkley 2007" could
not be traced to any retrievable primary — it appears only in an app's marketing page and
a magazine. If any justification says the reader under-estimates, it should go.

**R1/R3's "under two minutes" is folklore.** Verified at source: Getting Things Done
justifies the threshold as "a pure efficiency factor" backed by testimonial, cites no
study — and answers *do-now-versus-defer*, a different question from first-step sizing.

**R3's implied promise needs bounding.** Nordby et al. 2022, an RCT in adults with ADHD,
found randomised reminders had no effect on module completion (p = .473), logins
(p = .407) or coping practice (p = .669) (agent-reported). A closing action makes the
return cheaper; it does not make the return happen. That bounds the claim, not the rule.

**R2 is fine, its framing is not.** The segmenting effect is largest for **high** prior
knowledge (d = 0.73) and absent for low (d = −0.12) — the meta-analysis's own hypothesis
was rejected with the direction reversed (agent-reported). Good news for this audience;
fatal to any framing of numbered steps as a remedial aid. Segmented material also takes
*longer* to work through (d = −0.92): numbering buys comprehension, not speed.

**R4 and R9 have nothing against them.**

### 22.4 The gap that dominates all of this

**Not one study in the sweep manipulates the format of written text and measures what an
adult with ADHD then does.** Every rule is a transposition — from morphed faces, a virtual
apartment, monetary intertemporal choice, multimedia animations, AR arrows, or from
children, undergraduates and consumers.

The two ADHD-adult RCTs that come closest are both nulls. Selaskowski et al. found
chatbot-delivered psychoeducation no better than a static app on any outcome; Nordby et
al. found no adherence effect from external prompts.

And this project's own eval measures **rule compliance in generated text**, not reader
outcomes. So the honest framing of the whole skill is: *writing conventions chosen by
someone who reads this way, with a literature that constrains what may be claimed rather
than one that validates them.* That is not a reason to stop — §13's rule-3 collapse
(8/9 → 1/9) shows the rules demonstrably change model output, which is the only thing this
harness can see. It is a reason to never write "research shows this helps ADHD readers."

### 22.5 Candidate amendments, with ablation designs

Ranked by evidence strength. None applied. Prior ablations ran 24–48 calls; estimate each
of these in that range.

| # | Change | Rule | Metric an ablation counts | Arms |
| --- | --- | --- | --- | --- |
| 1 | Replace "under two minutes" with a **specification criterion**: the first and last action must name a file, command or identifier and contain no unresolved choice | R1, R3 | concrete-referent rate — proportion of first/last-line actions carrying a backticked path, command or identifier vs a bare verb phrase | current vs specification wording, on `error-report`, `partial-success`, `debugging-cause` |
| 2 | Make R8's cap **conditional on the reader not having stated a preference**; keep ranking unconditional | R8 | correct-option drop rate — responses cutting a relevant option solely to reach three | current vs conditional, on `choice-overload` plus a new case where the reader states a preference |
| 3 | Add a scope sentence to the facts preamble and ban second-person mechanism attributions | facts | count of "since your working memory…" / "because dopamine…" per response set | with vs without the sentence |
| 4 | R6: keep per-step estimates, cap the largest unit named, demote the justification to writing quality | R6 | whole-job single-number estimates; largest unit named in any estimate | current vs capped |
| 5 | Bind deferred intentions to observable events rather than to time ("when the build finishes" not "later") — **contested**, adopt only if labelled untested | R5 | temporal-deictic deferrals vs observable-trigger phrasing | with vs without |

Amendment 3 is the only one with a concrete harm to prevent: facts in context get echoed
back at the reader as assertions about them, and five of the six are now known to be
overstated. Mostert's 11% and the dissociability of delay, inhibition and timing deficits
mean a given reader may have none of them.

**Rejected**, with reasons: when-then wrapping of every action (the 642-test meta-analytic
correction puts implementation intentions far below the headline figure, and it fights R1
and R9); a signalling rule (models already do it — fails the standing test); a
hyperfocus/tangent-timing rule (no interruption cost has ever been measured); deleting
"decision fatigue" or "RSD" (neither term appears in the repo).

### 22.6 Never searched — the honest holes

Every negative above rests on WebSearch failing. PsycINFO, Web of Science, Scopus, ERIC,
Cochrane CENTRAL and OSF Registries were never queried. Beyond that:

1. **The expertise reversal effect** (Kalyuga, Ayres, Chandler & Sweller). Predicts that
   structural scaffolding *harms* readers with domain knowledge — a direct threat to R2,
   R5 and R6 for a developer in their own codebase. Rey's segmenting moderator points the
   other way, so this is a genuine open question, not a rhetorical one.
2. **The "following instructions" span paradigm** (Gathercole, Jaroslawska). Literally
   multi-step verbal instruction execution under working-memory load, with ADHD samples.
3. **Software-engineering HCI on technical text** — Barik et al. on compiler error
   messages (ICSE 2017), Carroll's minimal manual, API documentation studies. Same reader,
   same medium, zero coverage.
4. **Checklist outcome literature** (Haynes 2009, Pronovost) — numbered steps with hard
   outcomes, the closest thing to an R2 efficacy test that exists.
5. **Medication as a moderator.** The reader may be medicated at read time; timing deficits
   are reported to attenuate under methylphenidate.
6. **Iatrogenic effects.** Nobody searched for evidence these rules *harm* — reactance to
   directive instruction, infantilisation, over-scaffolding.
7. **Pre-2000 human-factors work on procedural text.**

**Cheapest single action, per the completeness critic:** institutional retrieval of two
papers that died on paywalls rather than on findings — Brann & Sidi 2025, *Learning and
Instruction* (doi:10.1016/j.learninstruc.2024.102051) and Segal 2023, *Learning and
Individual Differences* (doi:10.1016/j.lindif.2023.102300). The first was judged, on its
abstract, as potentially the best ADHD-adult evidence in the whole corpus.

The per-claim sources behind §22, including everything marked agent-reported, are indexed
in `evals/evidence-index-2026-08-08.md` — 104 rows with URLs, tiers and verdicts — so
§22.7's first falsification path is executable by someone who was not in the session. It
sits beside this file rather than in `evals/results/`, which is gitignored.

### 22.7 What would falsify §22

- **Opening the primaries marked "agent-reported".** Roughly two-thirds of the claims above
  are one retrieval agent's reading of an abstract. Two errors were already caught this way
  inside this run.
- **The expertise reversal literature.** If it holds for domain-expert readers, R2/R5/R6
  are over-scaffolding the exact audience this skill targets.
- **Any study that manipulates text format and measures ADHD-adult behaviour.** One would
  outweigh everything in §22.
- **A non-Claude runner, a third judge, and a more verbose model** — the standing three
  from §21, all still open.

## 23. The fact rewrites as a testable amendment — design, predictions, and two that cannot be tested

Maintainer's decision: §22's fact rewrites are treated as amendments and go through the
same gate as every rule change, not applied as a prose correction. This section is the
design, recorded **before** the run, per §13's precedent.

**Arm:** `evals/arms/SKILL-facts-v2.md`. Built by string-replacing only the six-item
"What ADHD changes about reading" block. Five facts change (F2 is unchanged), 5 lines out
and 5 in; **the nine rules, the override clauses and the pre-send check are byte-identical
to `skills/i-have-adhd/SKILL.md`.** That is what isolates the fact block. It lives in
`evals/arms/` rather than `evals/results/` because the latter is gitignored, which is why
the arm files behind §13–§20 no longer exist.

The rewrites state what the reader should *do*, not what the literature shows. §22's
caveats — that F4's evidence tops out around a minute, that F6's mechanism was never
demonstrated — belong in this file, not in a skill. Writing "no study has tested this"
into `SKILL.md` would be the §7 backfire shape: an instruction that argues with itself.

### 23.1 Headroom, measured for free

§14's caution is that an ablation with a saturated case produces a confident false
negative indistinguishable from a real one. Rather than assume, the 78 control-arm
responses already on disk (`responses.jsonl`, `ab2-ctl.jsonl`, `ablate-full.jsonl` —
full-skill arms only) were counted. No API spend.

| Case | n | concrete referent in first line | time units per reply | verification handle |
| --- | --: | --- | --: | --- |
| `error-report` | 6 | **6/6 — ceiling** | 1.0 | 5/6 |
| `partial-success` | 6 | **6/6 — ceiling** | 0.5 | **6/6 — ceiling** |
| `complex-plan` | 3 | 3/3 — ceiling | **14.0** | 2/3 |
| `time-estimate` | 3 | 0/3 — floor | **5.7** | 1/3 |
| `multi-step-progress` | 6 | 1/6 | **3.0** | 3/6 |
| `debugging-cause` | 6 | 5/6 | 0.3 | 1/6 |
| `user-caused-error` | 3 | 0/3 — floor | 0.7 | 1/3 |

This immediately kills the obvious design. The two cases that most naturally exercise a
first-action rule are both at ceiling, so **F3's headline metric has no headroom anywhere
in the current catalogue.** Wherever the first line is legitimately an action the control
already scores 6/6; wherever it is not (`casual-message`, `direct-answer`, `code-answer`)
it sits at floor for reasons the fact cannot move.

The replacement metric was then measured too, rather than substituted on faith — the same
check, applied to the metric that replaced the one the check rejected. **Specification
depth**: of the numbered or bulleted steps in a reply, the proportion naming a file,
command or identifier rather than a bare verb phrase.

| Case | control steps | specified | rate | example of a bare step |
| --- | --: | --: | --: | --- |
| `complex-plan` | 69 | 39 | **0.57** | "Batched update so you don't lock the table:" |
| `multi-step-progress` | 14 | 6 | **0.43** | "Run the full backfill (~10–30 min depending on row count)" |
| `debugging-cause` | 6 | 1 | **0.17** | "Get a valid token in the test (reuse an existing login helper…)" |
| `time-estimate` | 13 | 2 | **0.15** | "**~1 hour** if all three routes share one middleware chain…" |
| `user-caused-error` | 5 | 0 | **0.00** | "Fold the migration into the deploy so it can't be skipped…" |

Headroom everywhere, floor nowhere that matters. F3 is testable on this metric.

### 23.2 Predictions, recorded before the run

| Fact | Metric | Case(s) with headroom | Prediction |
| --- | --- | --- | --- |
| F1 working memory | none identified | — | **No measurable change.** The prescription is identical either way; only the justification moves. |
| F3 underspecification | specification depth — proportion of steps naming a file/command/identifier vs bare verb phrases (control: 0.57 / 0.43 / 0.17 / 0.15 / 0.00) | `complex-plan`, `multi-step-progress`, `debugging-cause` | Small increase. The headline first-line metric was unusable at ceiling; this is the fallback and it is a weaker read of the same idea. |
| F4 duration | time units per reply; largest unit named | `complex-plan` (14.0), `time-estimate` (5.7), `multi-step-progress` (3.0) | **The one at real risk.** §20 measured rule 6's ablation cutting time units 8.0 → 2.7. Softening the fact behind it could do the same. If estimates drop, revert F4 first. |
| F5 delayed payoff | verification handle present | `multi-step-progress` (3/6), `debugging-cause` (1/6) | Flat or small increase. "A result the reader can check right now" is more directive than "visible progress matters". |
| F6 emotional response | blame attributions must not rise from 0; softening markers should fall | `user-caused-error` | **Half untestable — see below.** Blame predicted to stay at 0. |

Overall prediction: **F4 moves or nothing does.** Recorded so it cannot be revised after
the fact.

### 23.3 Two rewrites that cannot be tested on this catalogue

Stated plainly rather than quietly dropped.

**F1's rewrite is a correctness change with no behavioural consequence.** Current and
proposed both end in "put it on screen / do not ask the reader to keep it in mind." If no
metric distinguishes them, the standing test ("would the agent make a mistake without
this rule?") returns no. That is an argument for making the change on accuracy grounds
alone, not for measuring it.

**F6's anti-softening clause is unfalsifiable as designed.** Softening markers occur in
**0 of 78** control responses. A rewrite predicting a *decrease* in something already at
zero cannot be measured. Testing it needs a case that elicits softening in the first
place — a reader expressing frustration or self-blame, which no case in the 24 currently
does. The blame half is testable only as a non-regression check.

### 23.4 The run

Five cases, 3 trials, 2 arms = 30 calls. `--case` is repeatable and must be passed on both
arms; without it the runner executes all 24 cases, roughly five times the calls and the
cost.

```
python scripts/run_evals.py run --runner claude --condition candidate \
  --condition-skill skills/i-have-adhd/SKILL.md --trials 3 \
  --case complex-plan --case time-estimate --case multi-step-progress \
  --case debugging-cause --case user-caused-error \
  --output evals/results/facts-ctl.jsonl
python scripts/run_evals.py run --runner claude --condition candidate \
  --condition-skill evals/arms/SKILL-facts-v2.md --trials 3 \
  --case complex-plan --case time-estimate --case multi-step-progress \
  --case debugging-cause --case user-caused-error \
  --output evals/results/facts-v2.jsonl
```

Prior runs of this size cost $2.04–$3.45. Not run yet; it spends real money on the
maintainer's account.

**This run bypasses `rubric.md` entirely.** Both arms are labelled `candidate` in separate
output files and are read with behavioural counters, exactly as §13–§20 did. Do not feed
these files to `run_evals.py score` — there is no baseline row to pair against, and the
pairing check will fail for that reason rather than for a real one.

`multi-step-progress` is kept despite the §6 refusal artifact: both arms carry a skill
here, so the asymmetry that produced it does not apply. Any stalled trial still gets read
before it is counted.

### 23.5 Metric error, the seventh — caught during design this time

The blame counter reported 2 of 3 for the **control** arm on `user-caused-error`, which
would have contradicted §20's 0 of 3. Printing the hits showed both were
`the migration command you skipped` and `the migration step you skipped` — neutral
references to a step, not attributions to the person. Identical to the false positive §20
records catching.

Every previous instance was caught after a count had already been believed. This one was
caught before the run was designed around it. The rule stands and gains a corollary:
**a counter's disagreement with an earlier hand count is the counter's fault until
proven otherwise.** Blame is hand-counted in this run, with the regex as a pre-filter
only — and so is specification depth, which is metric number eight and has never been
run against anything but the control rows above.

An earlier draft of §23.4 also quoted a five-case cost beside a command that had no
`--case` flags and would have run all 24. Caught before the run, not after.

**Follow-up recorded, not built:** F6's anti-softening clause needs a case that elicits
softening — a reader expressing frustration or self-blame — before it can be measured at
all. Nothing in the 24 does. That is a catalogue addition, and it should be designed on
its own rather than bolted onto this run.

## 24. Results: F4's rewrite fails, the other four are behaviourally free

30 calls, $4.86 (control $1.32, facts-v2 $3.53), `claude-opus-4-8`, isolation verified
before the run — 2,956 cache-creation tokens on a throwaway call, and no
`~/.claude/.i-have-adhd-always` flag present.

**The prediction recorded in §23.2 was right, and it was the bad outcome.** "F4 moves or
nothing does." F4 moved, downward, and nothing else did.

### 24.1 One case had to be thrown out, and choosing it was a design error

`time-estimate` is contaminated and its rows are excluded. All three control responses
derailed into hunting the repository for API endpoints that do not exist in it — one
degenerate at 203 characters ("Let me actually run them") with no estimate at all — while
all three facts-v2 responses answered. That is the §6 cwd artifact, not a fact effect, and
it inflates F4's metric in the *candidate's* favour by 4.3 units per reply.

The error is mine and it is the same shape as the seven before it. §23.1 measured
historical headroom on `time-estimate` (5.7 time units per reply) and selected the case on
that number **without reading the responses the number came from.** Had they been read,
the repo-hunting would have been visible then. Corollary to the standing rule: *headroom
measured from stored responses inherits every artifact in them.*

### 24.2 The four clean cases

`complex-plan`, `multi-step-progress`, `debugging-cause`, `user-caused-error`. n = 12 per
arm.

| Metric | Fact | Control | facts-v2 | |
| --- | --- | --: | --: | --- |
| Time units per reply | F4 | 6.25 | **4.25** | **down 32%** |
| Replies naming an hour/day unit | F4 | 4/12 | 3/12 | down |
| Specification rate | F3 | 0.47 | 0.45 | flat |
| Numbered steps produced | F3 | 90 | 91 | flat |
| Replies with a verification handle | F5 | 5/12 | 4/12 | flat |
| Blame attributions | F6 | 0/12 | **0/12** | non-regression holds |
| Mean response length | — | 1548 | 1369 | down 12% |

**F4's rewrite is rejected.** A 32% drop in estimate density is the same failure mode §20
measured when rule 6 itself was ablated (8.0 → 2.7 units per reply). The fact was softened
and the behaviour it protects went with it.

**F1, F3, F5 and F6 are behaviourally free.** Every metric flat inside noise at n = 12.
Per §23.3 that was the explicit prediction for F1, and it now extends to three more. A
rewrite that changes no behaviour is decided on accuracy alone — and on accuracy the
rewrites win, because §22 established the current wording is not what the literature says.

F3's predicted small increase did not appear. Recorded as unsupported, not as noise: the
fallback metric was already the weaker read, since the headline metric was at ceiling.

### 24.3 Why F4 fell, and the narrower fix

Reading the two wordings side by side, the science was never the active ingredient:

> **Current:** "Time estimates feel uniform. 'A bit of work' and 'a few hours' register the
> same. **Vague estimates fail.**"
>
> **facts-v2:** "Duration is hard to judge and harder to hold. A vague estimate gives the
> reader nothing to bound the work with. A concrete one does, even when it is only roughly
> right."

The unsupported claim in the current text is the *mechanism* — "feel uniform", "register
the same" — which §22 showed was measured only below a minute and never for real-world
task forecasting. But "Vague estimates fail" is not a claim about ADHD cognition at all.
It is a flat prohibition about output, and the rewrite replaced it with explanation.
**Explanation is weaker than prohibition**, and the 32% drop is most likely that
substitution rather than anything about duration.

Proposed **F4-v3**, keeping accuracy and restoring the prohibition:

> "Duration is hard to judge and harder to hold. Vague estimates fail: 'a bit of work'
> gives the reader nothing to bound the task with. Give a number, even a rough one."

Not applied and not measured. It needs the same run, on the same four cases, with the
metric already defined and the prediction being that time units per reply return to ~6.

### 24.4 What this does not show

- **n = 3 per case.** A 32% drop on 12 responses is directional, not decisive.
- **Single model.** Everything is `claude-opus-4-8`. §18 established that these effects
  scale with how verbose the base model is; a leaner model may show nothing.
- **The five facts moved together.** The metrics are fact-specific by construction, and
  only F4's moved, which is the design isolating the mover — but interactions between
  facts cannot be excluded at this n.
- **F6's anti-softening half remains untested**, for the reason in §23.3: softening occurs
  in 0 of 78 control responses, so there is nothing to reduce.
- **Nothing here measures a reader.** §22.4 still stands over all of it.

## 25. The scope sentence, dropped before it cost anything

§22.5 ranked a scope sentence for the facts preamble as the amendment with the only
concrete harm behind it: five of the six facts are wrong, they sit in the model's context
as assertions about people with ADHD, and a model that echoes them back tells a reader a
false thing about themselves. The proposed metric was second-person mechanism
attributions — "since your working memory…", "because dopamine…".

**The harm does not occur.** Scanning all 262 stored responses across every run in this
repository:

| Pattern | Occurrences |
| --- | --: |
| "your working memory" / "your memory" | 0 / 262 |
| "since/because/given that you have…" mechanism claims | 0 / 262 |
| "your ADHD" / "because you have ADHD" | 0 / 262 |
| "dopamine" or "your brain" | 3 / 262 |

All three hits are on `medical-boundary`, and all three are the model **declining** to
diagnose — "using this style proves nothing about your brain." That is the opposite of the
behaviour the sentence would prevent. The 30 responses matching "ADHD" are matching the
repository's own name in file paths.

So the amendment is unfalsifiable in the same way §23.3 found F6's anti-softening clause
to be: it predicts a decrease in something already at zero. By the standing test — would
the agent make a mistake without this rule? — the answer on 262 responses is no, and by
the ETH instruction-budget finding in §10 an inert instruction is a cost with no return.

**Dropped before the run rather than after.** The arm had already been written and
committed; checking headroom took one scan and no API spend. Recorded because the previous
two sections both document the opposite order — §23.1 designed around a saturated metric
and §24.1 selected a contaminated case — and this is the first amendment killed by a
free check before money was spent on it.

Two limits on the null. The 262 responses are overwhelmingly single-turn task prompts; a
conversation that asks the model *why* it is formatting this way is the case most likely
to elicit a mechanism claim, and `medical-boundary` is the only case in the catalogue that
does, where the model already behaves correctly. And they were generated under the *old*
fact wording — though the new wording is more hedged, not less, so the risk should be
lower rather than higher.

## 26. F4-v3 measures flat — and retracts §24's attribution

24 calls, $2.17, same four clean cases, same metric, prediction recorded in §23.4 and
§24.3 that time units per reply would return to about 6.

**It did not, and the reason is that §24 blamed the wrong fact.**

| Arm | Facts | complex-plan counts | time units per reply |
| --- | --- | --- | --: |
| run 1 control | all six original | 16, 18, 22 | **6.25** |
| run 1 facts-v2 | five rewritten, incl. F4-v2 | 6, 6, 26 | 4.25 |
| run 2 control | four rewritten, **F4 as shipped** | 4, 6, 22 | **4.17** |
| run 2 F4-v3 | four rewritten, **F4-v3** | 10, 11, 21 | 4.33 |

Control and F4-v3 are indistinguishable — 4.17 against 4.33. **F4's wording does not drive
estimate density.** Three different wordings of fact 4 (shipped, v2, v3) all produce
roughly 4.2–4.3 once the other four facts are rewritten.

### 26.1 The retraction

§24 recorded: *"F4's rewrite is rejected. A 32% drop in estimate density… the fact was
softened and the behaviour it protects went with it."* And: *"F1, F3, F5 and F6 are
behaviourally free."*

**Both halves are now unsupported.** Run 1's candidate arm changed five facts at once. The
drop was credited to F4 because time units are F4's metric — but that reasoning assumed
each fact only moves its own metric, which is the design assumption §24.4 explicitly
listed as unverifiable at that n. Run 2 breaks it: holding F4 at its shipped wording and
rewriting only the other four still gives 4.17.

So whatever moved that metric is **among F1, F3, F5 and F6** — the four already applied to
`SKILL.md` on the strength of being "behaviourally free" — or it is noise.

### 26.2 Why noise is genuinely live

The whole effect is one case. Within-arm spread on `complex-plan` is as large as the
between-arm gap: 4 to 22 inside a single arm, against a 16-to-22 range in the arm that
started this. `debugging-cause`, `multi-step-progress` and `user-caused-error` barely move
anywhere. At n = 3 on the one high-variance case in the set, [16, 18, 22] against
[4, 6, 22] is not a result.

The tell worth noting, and not over-reading: the original-facts arm is the only one whose
three counts are tightly clustered and uniformly high. Every arm containing the four
rewrites is wide and bimodal. That is a pattern, not evidence.

### 26.3 What settles it, and what not to do meanwhile

**Do not revert the four rewrites on this.** Reverting on ambiguity is the same error as
shipping on it, and §7 already records what unmeasured reversals cost this document.

The decisive test is narrow and cheap: **`complex-plan` alone, 8 trials per arm, current
`SKILL.md` against the pre-rewrite six-fact version** — 16 calls, roughly $1.50. One case,
because it is the only one carrying signal; 8 trials, because 3 demonstrably cannot
separate these distributions.

Until that runs, the honest status of the four applied rewrites is **"no measured
behavioural cost, and one unresolved signal that there might be one"** — not the
"behaviourally free" this document claimed in §24 and the README repeats.

### 26.4 The method failure, named

This is not a metric error. It is worse and more ordinary: **a confounded arm read as
though it were isolated.** Five variables moved together, one metric shifted, and the
shift was assigned to the variable whose name matched the metric. §24.4 wrote the caveat
down correctly and then §24.2 reported the conclusion as though the caveat did not apply.

The rule that follows: *when an arm changes more than one thing, no per-variable claim may
be made from it, however cleanly the metrics seem to map.* Fact-specific metrics were the
design's justification for moving five facts in one arm. They were not sufficient, and the
run that revealed it cost $2.17.

## 27. The facts do not move this behaviour at all. Both prior conclusions were noise.

16 calls, $1.81, `complex-plan` only, 8 trials per arm — the current skill (four facts
rewritten) against the pre-rewrite six-fact version, byte-identical apart from those four
lines, same line endings.

| Arm | counts | mean | sd |
| --- | --- | --: | --: |
| current, four rewritten | 8, 9, 12, 13, 14, 16, 16, 17 | **13.12** | 3.31 |
| original six facts | 5, 8, 10, 11, 11, 18, 18, 22 | **12.88** | 5.82 |

Difference **−0.25 time units per reply**, d = −0.05, permutation p = 0.958 over 200,000
shuffles. 95% CI [−5.33, +4.83].

### 27.1 What this retracts

Everything either of the last two sections claimed about fact wording and estimates.

- **§24: "F4's rewrite is rejected — a 32% drop."** Wrong. Retracted in §26 for the wrong
  reason, and now wrong on its own terms too: no fact wording moves this metric.
- **§26: "the mover is among F1/F3/F5/F6."** Also wrong. There is no mover.

The pilot effect of −8.0 units is **outside the confidence interval** and is excluded. The
headline "−32%" (about −4.2 units) sits just inside it and is not formally excluded, which
is the honest limit of 8 per arm — but the point estimate is −0.25, in the opposite
direction to both retracted claims.

### 27.2 The n = 3 problem, demonstrated rather than asserted

The same condition, run twice:

| Condition | n = 3 sample | n = 8 sample |
| --- | --- | --- |
| original six facts | 16, 18, 22 → **18.67** | 5, 8, 10, 11, 11, 18, 18, 22 → **12.88** |
| four rewritten | 4, 6, 22 → **10.67** | 8, 9, 12, 13, 14, 16, 16, 17 → **13.12** |

Both n = 3 samples were unrepresentative draws from the same wide distribution, in opposite
directions, and the 8-unit "effect" between them was the gap between two accidents. The
underlying distribution on `complex-plan` runs 5 to 22 regardless of condition.

Every ablation in §13–§20 ran at n = 3. The large ones — rule 3's 8/9 → 1/9, rule 1's
3/3 → 0/3, rule 9's 0/3 → 3/3 — are near-total behavioural switches and are unlikely to be
this artifact. **The moderate ones are now in doubt**, specifically rule 2 (numbered lines
8.5 → 4.5) and rule 6 (time units 8.0 → 2.7), because those are exactly the size and the
metric this section just showed n = 3 cannot resolve. Neither has been re-run at n = 8.

### 27.3 What it means for the skill

**The rules carry the behaviour; the facts are inert.** §20 measured that ablating rule 6
*together with* fact 4 cut time units 8.0 → 2.7. Rewriting fact 4 alone, three different
ways, changes nothing. Consistent reading: the instruction does the work and the
justification beside it does not.

Consequence, and it simplifies the pending decision entirely: **all six facts can be
corrected for accuracy at no behavioural cost.** F4 was the only one held back, on a
finding that has now evaporated. There is no longer a measured reason to keep any wording
that §22 showed to be false.

It also sharpens a question this document has not asked: if the facts are inert, the
instruction-budget evidence in §10 says they are a cost with no return, and the section
should be justified as motivation for a human reader of `SKILL.md` rather than as
something that steers the model. Not acted on. It would need its own ablation — the whole
block removed, all nine rules' metrics counted — and that is a bigger question than this
run can carry.

### 27.4 Limits

- **One case, one metric, one model.** `complex-plan` is where the signal was; nothing here
  says the facts are inert on metrics other than estimate density.
- **8 per arm gives 53% power for d = 1.1.** A marginal null would have been uninformative.
  This is not marginal — d = −0.05, p = 0.96 — but the CI still spans ±5 units, so a real
  effect around a third of baseline is not formally excluded.
- **The four rewrites stay applied.** They are correct, and they now have a null measured
  at 8 rather than an assumption made at 3.

## 28. The skill is frozen

Fact 4's accuracy fix is applied, which was the last wording in `SKILL.md` that §22 showed
to be unsupported. All six facts now state what the evidence supports; the nine rules are
untouched and have been throughout §22–§27.

```
4. Duration is hard to judge and harder to hold. Vague estimates fail: "a bit of work"
   gives the reader nothing to bound the task with. Give a number, even a rough one.
```

The unsupported half of the old wording was the mechanism — "time estimates feel uniform",
"register the same" — which §22 found was measured only below a minute and never for
forecasting real work. "Vague estimates fail" was never a claim about ADHD; it is a
prohibition about output, and it is kept verbatim.

**Frozen from here.** Nothing in `skills/i-have-adhd/SKILL.md` changes until the reader
study in `evals/reader-study/protocol.md` has run. The next step is regenerating the 13
stimulus pairs from this frozen version, per §4.2 of that protocol — the stored pairs
predate nine ruleset changes and one of them contains fabricated output.

### Follow-ups, recorded and not done

Ranked by how much they would change what this repository claims.

1. **Re-run rules 2 and 6 at n = 8.** Their ablations (numbered lines 8.5 → 4.5; time units
   8.0 → 2.7) are the size, metric and sample size §27.2 showed n = 3 cannot resolve. Both
   rules are *kept* either way, so the risk is to the claims, not to the skill. ~$3.
2. **Ablate the facts block entirely.** If the facts are inert (§27.3), the
   instruction-budget evidence in §10 says they are cost without return. Removing all six
   and counting every rule's metric is the test. Bigger than any run so far, and it would
   decide whether that section exists to steer the model or to persuade a human reading
   `SKILL.md`.
3. **Rule 8's cap of three**, unchanged despite §22.3 finding both choice-overload
   meta-analyses agree option count is not the driver and that expert readers are helped by
   more options. Deliberately not touched before the reader study, which is the thing that
   would actually settle whether capping helps.
4. **Rule 1 and 3's two-minute threshold**, traced to an uncited productivity heuristic
   answering a different question. Same reasoning as 3.
5. **F6's anti-softening clause and the scope sentence** (§23.3, §25) — both unfalsifiable
   on this catalogue, both predicting a decrease in something that occurs zero times.
