# Ablation arms

Alternate `SKILL.md` files, each differing from the shipped skill in one recorded way.
Feed one to `run_evals.py run --condition-skill <arm>` and compare against the shipped
skill run the same way.

They live here, tracked, rather than in `evals/results/` — which is gitignored, and is why
the arms behind `gap-analysis.md` §13–§20 no longer exist and those ablations cannot be
reproduced by anyone.

| Arm | Differs by | Result |
| --- | --- | --- |
| `SKILL-facts-original.md` | the six facts as shipped before the §22 rewrites | §27: no difference. 13.12 vs 12.88 time units per reply at n=8, p=0.96. The facts are inert on this metric. |
| `SKILL-facts-v2.md` | all five failing facts rewritten, including a rejected wording of fact 4 | §24, retracted by §26 and §27. Its apparent 32% effect was noise on n=3. |
| `SKILL-f4v3.md` | fact 4 only, the wording now shipped | §26: flat against the then-current skill. Kept for accuracy, not for behaviour. |

Two standing rules, both learned the expensive way:

1. **Change one thing per arm.** §26 credited a five-fact arm's shift to the one fact whose
   name matched the metric. Fact-specific metrics are not a substitute for isolation.
2. **n = 3 cannot resolve a shift in a noisy count.** §27.2 has the same condition sampled
   twice at n=3, landing 8 units apart, from one distribution. Use n = 8 or more for
   anything short of a behavioural on/off switch.
