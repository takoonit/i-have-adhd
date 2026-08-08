# Reader study protocol

Draft, 2026-08-08. Not run. Not pre-registered yet.

This is the study `gap-analysis.md` §22.4 says the project cannot do without: **nothing
measured so far involves a reader.** Every number in `gap-analysis.md` §6–§24 is a
property of generated text. The rules demonstrably change what a model writes; whether
that changes what a person does is unmeasured, and no study in the literature sweep
measured it either.

Scope note, inherited: the skill governs **how an LLM responds to a person with ADHD**,
not how a person organises their day. The DVs below are all reader responses to a single
message or a short exchange.

---

## 1. The question, and what would count as an answer

**Does an i-have-adhd-shaped response leave an ADHD reader better able to act than an
unshaped one?**

Three sub-questions, in descending order of how much this project needs them:

1. **Resumption.** After a gap, can the reader say what they were doing and what comes
   next? This is the one no existing instrument can see, and §10/§21 named it the largest
   gap in the eval.
2. **Next-action accuracy.** Immediately after reading, can the reader name the correct
   next action?
3. **Perceived effort.** Does the response feel cheaper to act on?

**Smallest effect of interest: dz = 0.5.** Chosen because it is the feasibility line (see
§6): below it, the participant numbers exceed what a project this size can recruit, so an
effect smaller than that is one this study cannot honestly claim either way. Stating it in
advance is what makes a null interpretable rather than an embarrassment.

---

## 2. Design

Within-subjects, counterbalanced. Each participant sees both conditions across different
cases; no participant sees the same case twice.

- **Condition A** — baseline: the model's unshaped response.
- **Condition B** — candidate: the response produced with the skill.

Within-subjects is not a stylistic preference. §22 established adult ADHD is
neuropsychologically heterogeneous — 11% of diagnosed adults show no measurable
dysfunction, and battery effect sizes span 0.05–0.70. Between-subjects designs pay for
that variance twice. Each participant is their own control.

**Item assignment:** 8–12 cases per participant, drawn from the 13 usable cases (§4),
condition rotated across participants so each case appears in both conditions about
equally often.

**Analysis:** paired comparison on participant means for the headline test; mixed-effects
model with random intercepts for participant and case as the pre-registered secondary,
because it uses the repeated items rather than averaging them away. The gain from the
mixed model over the paired test depends on item variance and the intraclass correlation,
**both unknown until the pilot** — so the power table in §6 is computed for the paired
test and should be read as the conservative floor.

---

## 3. The length confound, stated once

The two conditions differ in length by design: across the 72 stored pairs, baseline
averages 1575 characters and candidate 976 — about 60% shorter. Concision is part of the
skill, so this is not a flaw to correct, but it has a hard consequence:

**Any latency or reading-time DV is invalid here.** It would measure length and report it
as shape. That is why the DVs are accuracy and resumption, on which shorter is not
automatically better — a response can be short and still fail to say what to do.

This study tests the skill **as a package**. It cannot attribute an effect to any
individual rule. Rule-level attribution stays with the ablation harness.

---

## 4. Stimuli

### 4.1 The stored pairs are contaminated and must not be used as-is

72 baseline/candidate pairs exist across 24 cases. Screening them removed 11:

| Dropped | Reason |
| --- | --- |
| `destructive-action` | **Fabrication on record.** §6: two of three candidate trials invented the output of a `git clean` dry run and told the reader those files were safe to lose. Never show this to a participant. |
| `error-report`, `time-estimate`, `agent-owned-edit`, `user-caused-error` | Refusal artifact (§6). The runner executes inside this repository, so responses hunt for code that is not here. Not readable as stimuli. |
| `casual-message`, `direct-answer`, `code-answer`, `concept-explanation`, `long-form-request` | No next-action DV — "what would you do next" is undefined. |
| `medical-boundary` | The response is about declining to diagnose the reader. Showing it to participants recruited *because* they have ADHD is an uncomfortable stimulus with no DV attached. |

**13 usable cases:** `abandoned-and-returning`, `choice-overload`, `complex-plan`,
`debug-spiral`, `debugging-cause`, `handoff-record`, `list-overflow`,
`multi-step-progress`, `partial-success`, `re-entry-after-gap`, `real-ambiguity`,
`state-across-interruption`, `tempting-tangent`.

### 4.2 Regenerate, do not reuse

Even the 13 survivors must be regenerated. The stored candidate rows come from the §6 run
and predate nine subsequent ruleset changes, including the scope-line revert, the rule-5
narrowing and the rule-7 merge. They are responses from a skill that no longer exists.

Cost by this repo's own history: roughly $5–10 for both arms across 13 cases at 3 trials.
One response per case per condition is then selected for the study — **selected before any
participant sees it, by a rule fixed in advance** (e.g. the median-length trial), not
chosen by reading them, which would let stimulus selection encode the hypothesis.

Applies §24.1's corollary: *headroom, and stimuli, measured from stored responses inherit
every artifact in them.*

---

## 5. Dependent variables

### DV1 — Resumption after a gap (primary)

The unique contribution. Procedure: participant reads the response and states an intended
next action; a filler task runs for 8–10 minutes; then, without the response visible:

- "What were you in the middle of?"
- "What is the next thing you would do?"

Scored 0–2 against a per-case rubric written before data collection.

**Honest limit:** a within-session filler is a *proxy* for the real claim, which is about
returning hours or days later. A next-day return arm is the true test and is proposed as
Stage 3, because attrition would wreck it at the sample sizes in §6.

### DV2 — Next-action accuracy (primary)

Immediately after reading, free-text: "What is the single next thing you would do?"
Scored 0–2 against the same per-case rubric.

### DV3 — Perceived effort (secondary)

One item, 1–7: "How much effort would it take to start on this?" Single-item measures are
noisy; this is secondary and will not carry a claim on its own.

### DV4 — Qualitative (Stage 1 only)

Think-aloud transcripts. Not scored quantitatively.

### Scoring

- **Rubrics written before data collection**, one per case, naming the correct next action
  and what counts as partial credit.
- **Scored blind to condition**, by someone who did not write the rubrics, with a second
  scorer on at least 20% and an inter-rater agreement figure reported.

This is non-negotiable in this project's own terms: §6 recorded that its first judge was
the author of the amendments being judged, and §8 had to re-run everything with an
independent judge to find out what that cost.

---

## 6. Power

Computed by simulation, two-sided paired t-test, alpha .05. Not quoted from memory.

| True effect (dz) | n=15 | n=25 | n=35 | n=50 | n=80 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0.25 | 0.15 | 0.22 | 0.30 | 0.42 | 0.59 |
| 0.35 | 0.24 | 0.40 | 0.52 | 0.68 | 0.88 |
| 0.50 | 0.44 | 0.67 | **0.82** | 0.93 | 0.99 |
| 0.65 | 0.65 | **0.88** | 0.96 | 0.99 | 1.00 |
| 0.80 | **0.82** | 0.97 | 1.00 | 1.00 | 1.00 |

Smallest n for 80% power: dz 0.80 → 15; 0.65 → 21; **0.50 → 34**; 0.35 → 67; 0.25 → 127.

**Target: n = 35 completers**, powered for the SESOI of dz = 0.5. Anything below dz = 0.35
is out of reach for this project and should not be claimed in either direction.

---

## 7. Recruitment, and the trap in it

**Do not screen participants in with the ASRS from a general pool.** In two general
population samples (UK N=642, USA N=579) the ASRS v1.1 flagged 26.0% and 17.3% as probable
ADHD against a true prevalence near 2.5% — an estimated positive predictive value of about
**11.5%**, with the authors concluding 86–90% of those identified in normative cohorts
were unlikely to have ADHD. A sample screened in that way would be mostly people without
ADHD, and the study would measure nothing it claims to.
(Source: *Screening for adult ADHD using brief rating tools*, PMC7116749 — retrieved and
read for this protocol.)

**Instead:**

1. **Recruit from populations where diagnosis is already dense** — ADHD developer
   communities, r/ADHD_Programmers, ADHD-focused professional groups — with self-reported
   *formal diagnosis* as the inclusion criterion. Self-report has its own error, and it is
   an order of magnitude better than an ASRS-positive from a general pool.
2. **Collect the ASRS anyway, as a continuous severity measure, not a gate.** It costs one
   screen and enables an exploratory moderation analysis: does benefit scale with symptom
   severity? Note in advance that moderation needs more power than a main effect, so this
   is exploratory and will be labelled as such.
3. **Panel platforms: verify before designing around them.** ADHD is not confirmed to be a
   built-in Prolific prescreener — the documentation retrieved for this protocol lists
   anxiety, depression, OCD and PTSD, and does not list ADHD. Confirm with Prolific
   support before assuming; otherwise use their custom-screening feature plus a
   diagnosis question, and accept the extra cost of screening out.

Also require: writes code regularly (the stimuli are developer tasks), reads English
fluently.

---

## 8. Stages

**Stage 1 — think-aloud pilot, n = 6–8.** Run this first. It needs no power calculation
and it is the pilot for everything the power table cannot supply: how long an item
actually takes, how many items a participant tolerates before fatigue, whether the rubrics
are scorable, and the item variance and ICC the mixed model needs. Expect it to change
the design.

**Stage 2 — main study, n = 35.** DV1 and DV2 primary, DV3 secondary. Hosted survey. No
custom software: the whole thing is read-a-response, answer-questions, wait, answer again.
Building a bespoke tool for this is the failure mode this repo has a skill about.

**Stage 3 — next-day resumption, if Stage 2 shows anything.** The real version of the
resumption claim, and the only design that touches what §10 called the most common reason
a project is dropped midway. Priced separately because attrition changes the recruitment
maths.

---

## 9. Ethics

Stated once. This is human-subjects work involving a clinical population.

- Internal product testing generally does not require IRB review. **Publishing a claim
  that "research shows this helps people with ADHD" generally does.** Decide which this is
  before Stage 2, not after.
- ADHD status is health-adjacent data; in the EU/UK it is special-category under GDPR.
  Collect no identifiers, store responses pseudonymously, state retention and deletion in
  the consent text.
- No diagnosis is offered, implied, or collected beyond self-report and a severity screen.
- Pay participants properly. Prolific's own minimum is a floor, not a target.
- Pre-register on OSF before Stage 2, with the SESOI, DVs, rubrics, exclusion rules and
  analysis plan fixed. This also closes the hole §22.6 recorded: OSF was never searched
  during the literature sweep, so it is unknown whether anyone is already running this.

---

## 10. How this fails

- **A null that means nothing.** At n = 35 an effect below dz ≈ 0.4 is invisible. The
  SESOI in §1 exists so this is reported as "smaller than we can see", never as "no
  effect".
- **The package problem.** A positive result credits nine rules and six facts jointly. It
  cannot say which. If Stage 2 is positive, rule-level attribution still belongs to the
  ablation harness, not here.
- **Stimulus selection.** Choosing which trial to show by reading them would encode the
  hypothesis. Fixed in advance in §4.2; if that rule is broken the study is invalid.
- **Self-reported diagnosis.** Better than an ASRS gate, still error-prone, and likely
  skewed toward people engaged enough with ADHD to be in an ADHD community.
- **Ceiling effects.** If both conditions score near 2/2 on next-action accuracy, the DV
  is too easy and the pilot must catch it. §23.1 is the cautionary precedent: a saturated
  measure produces a confident false negative indistinguishable from a real one.
- **The obvious result.** Baseline responses are 60% longer and bury the action; it is
  entirely possible this simply reproduces the NN/g scanning literature in a new
  population. That would still be worth knowing, and should be predicted in advance rather
  than presented as a discovery.
