<p align="center">
  <img src="./logo.png" alt="i-have-adhd" width="140" />
</p>
<p align="center">
  <strong align="center">ADHD-friendly outputs. No ADHD diagnosis needed!</strong>
</p>
<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/ayghri/i-have-adhd?style=flat" alt="License"></a>
</p>

## Install

🔗 [Installation Instructions](INSTALL.md)

## What it does

A skill for your coding assistant that stops it from burying the answer. Action first. Steps numbered. No "Hope this helps!"

## What changes

<table>
<tr>
<td width="50%">

## Before

> Great question! Let me think about this. Your auth flow has a few moving pieces: the middleware, the token verification, and the cookie handling. Looking at `src/auth.ts`, the `verifyToken` function (around lines 42-58) seems to be using an older `jsonwebtoken` API. One approach would be to update the package and rewrite that function. After making the change, you'd want to run the auth tests to confirm nothing breaks. By the way, you might also want to look at your dependency versions overall. Hope this helps! Let me know if you want to dig deeper.

</td>

<td width="50%">

## After

> Run `npm install jsonwebtoken@latest`, then edit `src/auth.ts:42`.
>
> 1. Open `src/auth.ts`
> 2. Replace `verifyToken` (lines 42–58) with the snippet below
> 3. Run `npm test -- auth.spec.ts`
>
> Next: paste the first failing line if any test fails.

</td>
</tr>
</table>

## The rules

9 rules. Full text in [SKILL.md](./skills/i-have-adhd/SKILL.md).

1. Lead with the next action, startable in under two minutes.
2. Number multi-step tasks.
3. End with one concrete next step.
4. Suppress tangents.
5. Restate state every turn, show what now works, and re-anchor a returning reader.
6. Specific time estimates, per step (minutes, not "a bit"; never clock times).
7. Matter-of-fact errors. State, not blame.
8. Rank lists rather than truncating them; cap choices at 3.
9. No preamble. No recap. No closers.

## What's measured, and what isn't

Every rule has been ablated: deleted one at a time, with the same prompts re-run and the difference counted. Removing seven of nine rules changed at least one counted feature of model output in the recorded runs. Most runs used three trials per case, so the moderate results for rules 2 and 6 remain provisional. Removing rule 3 produced the clearest switch, taking closing actions from 8 of 9 replies to 1 of 9.

What has **not** been measured: whether any of it helps a reader. Every number here is a property of generated text, not of a person. A literature sweep found nobody else has measured it either; the two closest trials in adults with ADHD both came back null.

An eight-trial-per-arm follow-up on `complex-plan` found no detectable change in estimate density after four explanatory lines were rewritten: 13.12 against 12.88 units per reply, exact permutation p = 0.959, 95% CI [−5.33, +4.83]. That result covers one case, one metric and one model. It does not establish that every explanation is behaviourally inert.

The skill now states output defaults instead of causal claims about ADHD readers. Clinical sources constrain what this project may claim; they do not show that these rules help a reader.

Receipts, including every retraction and eight metric errors: [evals/gap-analysis.md](./evals/gap-analysis.md).

## Tune it

Fork, edit `skills/i-have-adhd/SKILL.md`, then swap your copy in:

```bash
claude plugin uninstall i-have-adhd            # drop the upstream copy first:
claude plugin marketplace remove i-have-adhd   # fork and upstream share both names
claude plugin marketplace add <your-username>/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
```

Restart Claude Code, then re-invoke `/i-have-adhd`.

## Credits

Loosely based on *The Adult ADHD Tool Kit* by J. Russell Ramsay and Anthony L. Rostain. Adapted for how an LLM should respond, not how a human should organize their day.

Not medical advice, and not a clinical tool. It is a writing style.

## License

MIT.

Star ⭐ if it saved you one scroll past one "Great question!"
