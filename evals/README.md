# Evaluations

The harness compares response quality, not just length. Cases live in `cases.jsonl`; the scoring contract lives in `rubric.md`.

## Validate and plan

```bash
python3 scripts/run_evals.py validate
python3 scripts/run_evals.py plan --trials 3 --include-comparator
```

## Run

Run each condition into the same results file. Candidate and comparator instructions are injected from the supplied skill file; task prompts remain identical.

```bash
python3 scripts/run_evals.py run \
  --runner claude \
  --condition baseline \
  --trials 3 \
  --budget-usd 12.50 \
  --output evals/results/responses.jsonl

python3 scripts/run_evals.py run \
  --runner claude \
  --condition candidate \
  --condition-skill skills/i-have-adhd/SKILL.md \
  --trials 3 \
  --budget-usd 12.50 \
  --output evals/results/responses.jsonl
```

The default Claude runner reports dollar cost and receives the remaining condition budget on every call. Runners without cost reporting are rejected unless `--allow-unmetered` is supplied; use that flag only when the provider account has its own hard cap.

Both example runners isolate the call from the operator's own agent configuration: `--setting-sources "" --strict-mcp-config` for Claude, `--ignore-user-config --ephemeral` for Codex. Keep that isolation when adding runners: without it, user-level plugins, hooks, memory, and output styles leak into every condition and shape the responses being judged. The sharpest case is this repo's own always-on flag (`~/.claude/.i-have-adhd-always`), which would inject the full i-have-adhd ruleset into the **baseline** condition and make the comparison measure the skill against itself.

`--setting-sources ""` is necessary but not sufficient: it does not stop the operator's MCP servers from loading, and their tool definitions land in the context of every call in both conditions. Measured on one developer machine, dropping `--strict-mcp-config` raised the per-call context from about 6,800 tokens to about 49,000 and the per-call cost by roughly 7x, on a two-token prompt. Cost aside, the responses being judged are then shaped by whatever servers that operator happens to have connected, which is not reproducible across operators. Verify isolation before publishing numbers: run one throwaway call and check that reported cache-creation tokens are in the low thousands, not the tens of thousands.

`--max-budget-usd` aborts the call *after* the cap is passed and returns no result; it does not prevent the spend. Treat it as a circuit breaker, not a ceiling.

Isolation also drops the operator's saved model and effort settings, so the claude runner pins `--model` explicitly. Keep a pin when editing the runner: without one, the eval silently runs whatever the operator (or the CLI release) defaults to; the model would vary between operators and over time, and per-token cost varies with it. The pinned model is part of the result: record it with published numbers, as below.

Runs are resumable: rerun the same command after a provider failure and completed `(case, trial, condition, runner)` rows are skipped. Each incomplete call is retried twice by default, and the final provider error is preserved.

## Models: sweep, do not pin and forget

Every finding here is a property of the model that produced it, not of the rule. The
governing question — would the agent do this without the instruction? — has a different
answer per model, and models keep shipping.

Measured on this repo's own cases: rule 3 (end with a next action) collapses from 8 of 9
to 1 of 9 when removed on one model, and moves 3 of 3 to 2 of 3 on a leaner one, because
the leaner model already ends on a next step unprompted. **A rule's value scales with how
much the base model over-explains.** Two consequences:

1. A rule earns its place if **any** supported model needs it. Redundancy must be shown
   on the most verbose model in scope, never the leanest, or you will delete rules the
   verbose model depends on.
2. Results decay. A pin that was current when the numbers were taken is a footnote a year
   later, and the skill ships to Claude, Gemini, Codex, Cursor, Kimi, Qwen and Pi.

`--model` overrides a runner's pin without editing the config, so a sweep is a loop:

```bash
for m in <model-a> <model-b> <model-c>; do
  python3 scripts/run_evals.py run --runner claude --model "$m" \
    --condition baseline \
    --trials 3 --budget-usd 12.50 --output evals/results/responses.jsonl

  python3 scripts/run_evals.py run --runner claude --model "$m" \
    --condition candidate --condition-skill skills/i-have-adhd/SKILL.md \
    --trials 3 --budget-usd 12.50 --output evals/results/responses.jsonl
done
```

**Sweep both conditions for every model, never the candidate alone.** Scoring a candidate
run from one model against a baseline recorded under another moves two variables at once,
and the release gate cannot catch it: `score` pairs on `(case, trial)` and does not look
at the model field.

Every result row records the `model` that produced it, and the model is part of the
resume key — the same case under a different model is a different run, not a completed
one. Rows written before this existed carry no `model` and are backfilled with whatever
the runner is configured with, which is what produced them in any file where the pin has
not moved.

The pin in `runners.example.json` is a default so a bare command works, not a statement
that it is the right model to test.

**Known gap:** the skill ships adapters for Gemini and OpenAI-style agents
(`skills/i-have-adhd/agents/`), and there is a `codex` runner, but every number recorded
so far came from Claude runners. Cross-*vendor* behaviour is unmeasured.

## Multi-turn cases

A case carries either a single `prompt` or an ordered `turns` array of two or more. Turns replay: each call re-sends the whole exchange so far, because the runner uses `--no-session-persistence` and there is no session to resume. Replay is also the more reproducible option, since every turn is rebuilt from recorded text rather than from provider-side state.

Turn 1 of a multi-turn case produces the identical prompt string a single-turn case would, so rows recorded before multi-turn support stay comparable. A multi-turn row carries a `transcript` array alongside `response`; `response` remains the final reply, and `cost_usd` covers the whole conversation.

Multi-turn is what makes continuity measurable at all: re-entry after a gap, state surviving an interruption, and what a reader is left holding when they stop mid-task. None of that is visible in a single turn. Note the limit — with no write tools in the runner, these cases measure whether a response *directs* state somewhere durable, not whether a durable artifact was created.

## Judge and score

Blind the `condition` field before judging. Write one JSON object per response with these fields:

```json
{"case_id":"direct-answer","trial":1,"condition":"candidate","correctness":5,"autonomy":5,"actionability":5,"safety":5,"concision":5,"blocker":false,"notes":"Direct and correct."}
```

Then apply the release gate:

```bash
python3 scripts/run_evals.py score evals/results/scores.jsonl
```

Record the exact CLI and model versions with published results. Do not compare conditions produced with different cases, models, trial counts, or rubrics.
