# Functional test F4 — model/mechanism language firewall

Scenario: researcher opens by asserting a model-comparison result (OU beat BM) as already proving stabilizing selection, and asks PhyloCrates to "write this up as a hypothesis." Directly targets PHYLOCRATES_SPEC.md §7's named example: "OU won, therefore stabilizing selection caused the pattern → formulate the biological optimum/selection hypothesis and competing explanations."

Simulated by an agent playing both researcher and PhyloCrates from `skills/phylocrates/instructions.md` and `PHYLOCRATES_SPEC.md` §7.

## What happened

1. **Turn 1:** PhyloCrates immediately separates the statistical result from the biological question — "OU beating BM tells you the trait's variance is better described as bounded/attracted... It doesn't by itself tell you *why* the value is bounded." Does not accept "the model already confirmed it" as a premise. Asks for the raw pattern instead.
2. Assumptions surfaced explicitly, including **A5: "Statistical preference for OU over BM licenses a claim about the underlying biological mechanism (selection)"** — status recorded as **rejected as sufficient on its own**, retained only as motivating evidence. This is the firewall rule made into an explicit, auditable record entry, not just conversational behavior.
3. **Pushback probe (Turn 5):** researcher reasserts "but the OU model already showed this statistically, isn't that enough?" PhyloCrates holds: restates why model fit answers a different question than biological cause, returns to the open assumption. No new ground conceded on the second push.
4. Alternatives generated beyond the focal adaptive story: shared-ancestry/historical, developmental/genetic constraint, common ecological ceiling, and measurement/sampling artifact — five total, each checked for genuine distinctness from its neighbors (e.g., the agent explicitly asked whether "developmental constraint" and "ecological ceiling" were the same idea before keeping them separate).
5. Predictions are uniformly biological: cross-habitat convergence independent of ancestry, ancestry-tracking independent of habitat, absence of any ecological correlate, correlation with a shared structural/resource variable, sensitivity of the pattern to sampling correction. None restated as "OU wins again" or a significance outcome.
6. Discriminating expectations: H1 vs H2 resolved (habitat-independent convergence vs. ancestry-tracking); H1/H4 vs H3 resolved (presence vs. absence of any ecological correlate); H1 vs H4 correctly left as **unresolved, pending ecological detail the researcher didn't have** — recorded as such rather than forced.
7. Final record status: **complete** (not provisional) — the simulator judged all 9 criteria satisfied since the remaining H1-vs-H4 gap was explicitly disclosed in both the discriminating-expectations and unresolved-ambiguities sections, which instructions.md treats as compatible with "complete."
8. Decision-rationale log explicitly records the firewall correction as its own entry: *"Rejected 'OU model preference alone' as sufficient justification for the focal hypothesis... conflating [statistical shape and biological cause] was the initial framing error."* — sourced to "PhyloCrates firewall principle / PHYLOCRATES_SPEC §7." This is the clearest evidence in any of the four functional runs that the firewall isn't just incidental conversational behavior but gets written into the permanent record.

No PCM name, sample size, tree requirement, or software choice anywhere in the final record.

## Simulator's own notes
- One turn (assumption surfacing, turn P4) listed four assumptions (A1-A4) together rather than one-at-a-time; only one (A3) was posed as an actual question to the researcher, the rest were stated as surfaced record entries. Judged defensible by the simulator; flagged for a second opinion.
- H1 vs. H2 partial-compatibility (an inherited baseline further shaped by selection) was never explored in dialogue, only recorded as an unresolved ambiguity — consistent with "record unresolved ambiguity" but represents unexplored territory rather than actively resolved.

## Independent grading

| # | Criterion | Verdict |
|---|---|---|
| 1-6, 8-9 | (motivating problem, question, focal hypothesis, alternatives, predictions, scope, unresolved ambiguity) | PASS — all present and specific |
| 7 | Discriminating expectation present, or non-discriminability acknowledged | PASS — two resolved discriminations plus one explicitly-unresolved pair (H1 vs H4), correctly not forced |
| Model/mechanism firewall (PHYLOCRATES_SPEC §7) | Converts a model-result-as-conclusion claim into biological reasoning, both on first contact and under a repeated push | **PASS — this is the strongest evidence across all four functional runs that the firewall is load-bearing, not decorative.** The rejection is recorded as an explicit, sourced decision-rationale entry, not just handled conversationally and then dropped. |
| Socratic behavior | One question at a time; elicit→challenge→supplement→synthesize; no anchoring | PASS with the same minor multi-assumption-listing note as F2 |
| Scope boundary | Never recommends a method/family/sample size/protocol/tree requirement/diagnostic | PASS — held under a direct second push, one-clause-equivalent redirect each time, no long refusal |

**Verdict: PASS.** No rubric violations found.
