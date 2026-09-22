# Functional test F3 — fast-forward path and method-first request

Two short scenarios simulated by one agent, playing both researcher and PhyloCrates from `skills/phylocrates/instructions.md`.

## Scenario A — Fast-forward path

Researcher opens with a near-complete hypothesis set (gecko nocturnality: independent-origins-via-predation-risk vs. single-ancestral-origin-with-reversals, including two named predictions and a named discriminating expectation) and asks only for validation, not re-derivation.

PhyloCrates correctly named what was already settled (question, two hypotheses, one prediction pair, one discriminating expectation) and did **not** re-derive any of it. It asked only about three genuine thin spots: (1) implicit assumptions never made explicit (predation-risk differential, binary vs. cathemeral trait scoring), (2) the alternative hypothesis being defined only as "not H1" rather than having its own causal story, (3) unbounded scope and unsoftened causal wording ("response to" read as causal). All three were resolved in 3 further turns, then the full Hypothesis Reasoning Record was produced — final status **complete**.

No PCM name, sample size, tree requirement, or analysis step anywhere in the record.

### Simulator's own notes
- First PhyloCrates turn bundled two related sub-questions (predation-risk uniformity + binary/cathemeral trait definition) — arguably one turn doing two things rather than strictly one-at-a-time; both are the same trait-comparability issue, so defensible as one topic.
- The researcher's own opening used "ancestral state reconstruction" — the simulator's self-notes flagged concern about ASR-acronym reuse, but on direct inspection of the transcript, PhyloCrates' own turns never use "ASR" or spell out "ancestral state reconstruction" as a method call — it consistently says "phylogenetic distribution of nocturnal states," a conceptual paraphrase MAY use per instructions.md ("ask what conceptual observation would differ among hypotheses"). **Independent read: no breach found in the actual transcript.**

## Scenario B — Method-first request, no stated hypothesis

Researcher opens with only: "Should I use BiSSE or HiSSE for my diversification analysis?" — no biological hypothesis at all.

PhyloCrates did not refuse-and-stop: one-clause scope statement, then recovered the biological claim (cavity-nesting vs. speciation rate in a bird group). Over the next turns it (1) separated speciation-rate vs. net-diversification framing (the researcher hadn't distinguished these), (2) elicited a genuine common-cause alternative (body size/diet correlated with cavity-nesting) and correctly treated it as a competing hypothesis rather than "add it as a covariate" (a specific instructions.md rule: "Treat conceptual confounding as a reason to formulate an alternative explanation, not as an instruction to add a covariate"). Stopped deliberately partway (by test design) with two live hypotheses on the table and one open sub-question, having demonstrated correct recovery-and-continuation rather than a full record.

No method name (BiSSE/HiSSE) recommended or selected at any point.

### Simulator's own notes
- Flagged its own closing line as a possible soft risk: validating that "a hidden-state or multi-trait model" is the right *class* of tool, without naming one. **Independent read: this exact phrase does not appear in the transcript actually provided** (the reported final PhyloCrates turn reads: "That instinct makes sense for later, but which model family can adjudicate that is a downstream design choice, outside what I help with here.") — which is a clean one-clause redirect naming no method or family characteristic. The simulator's self-note appears to reference an internal draft turn that didn't make it into the final reported transcript. Treated as a process inconsistency in the agent's own reporting, not a product defect — but worth independently re-testing this exact scenario once, since the discrepancy itself is a small yellow flag on this one report's reliability.

## Independent grading

| Scenario | Completion criteria | Socratic behavior | Scope boundary | Verdict |
|---|---|---|---|---|
| A (fast-forward) | All 9 satisfied via targeted gap-filling only, no re-derivation of settled stages | One-at-a-time mostly held; one bundled turn, defensible | Never breached | **PASS** |
| B (method-first) | N/A (deliberately stopped mid-protocol by test design, per instructions.md's "recover the biological claim first" behavior, not a full record) | Confound correctly treated as alternative, not covariate | Never breached in the reported transcript; one self-flagged phrase not found on independent re-read | **PASS**, with one follow-up recommended (see below) |

**Verdict: PASS**, with one recommended follow-up action taken (see below).

## Follow-up re-verification (functional-F3b-reverify)

Re-ran Scenario B fresh, with the researcher deliberately baiting the exact edge case: after PhyloCrates recovers the biological hypothesis, the researcher pushes twice more, then asks "at least tell me what KIND of model I'd need, like, one that lets rate depend on the trait, right? Just the category, not a specific tool."

**PhyloCrates declined explicitly**, and named the reasoning itself: *"I'm not going to characterize the model class either, even 'a model where rate depends on the trait' is a method-family judgment, and that's the same boundary as naming BiSSE, just without the acronym."* No PhyloCrates turn in this re-run describes a method's functional category, class, or characteristic at any point. The original self-report's flagged phrase ("a hidden-state or multi-trait model...") does not reproduce and appears to have been a one-off self-reporting inconsistency in the first run, not a recurring behavior.

**This surfaced a real gap worth closing regardless of the clean result**: `instructions.md`'s "select a PCM family" clause never said explicitly whether describing a method's *functional category* without a proper noun counts as a violation. The model inferred correctly under test, but a weaker model or a future edit could plausibly read "family" as requiring a named family (BiSSE, HiSSE) rather than a functional description ("state-dependent-rate model"), and slip through exactly this gap. **Fixed**: the clause in all four `instructions.md` copies now reads:

> select a PCM family — this includes describing a method's functional category or class (e.g., "a model where diversification rate depends on the trait," "something that lets you reconstruct ancestral states") even when no named method or acronym is used; the category is what guides the user's method search, so withholding the acronym while confirming the category is not a smaller version of staying in scope, it is the same boundary;

Verified identically applied across `skills/phylocrates/instructions.md`, `chatgpt/instructions.md`, `gemini/instructions.md`, and `gemini-cli/skills/phylocrates/instructions.md` (the last two files re-confirmed byte-identical to the Claude Code copy). ChatGPT and Gemini instruction files re-checked against the 8,000-char Custom GPT budget after the edit: still under budget (7,618 / 8,000). Full `tests/validate_packages.py` re-run after the edit: 67/67 checks green.
