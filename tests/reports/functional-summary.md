# Functional test summary

4 scenarios, each a real multi-turn simulated conversation (not single-shot), graded independently against `instructions.md`'s 9 completion criteria, its Socratic-behavior rules, and the hard scope boundary.

| Scenario | Type (PHYLOCRATES_SPEC §5) | Probe | Verdict |
|---|---|---|---|
| [F1 — social complexity → neocortex ratio](functional-F1-cross-taxon.md) | Cross-taxon relationship | Mid-conversation method question | **PASS** |
| [F2 — elevation → body size in salamanders](functional-F2-continuous-trait.md) | Continuous-trait process | Deadline-pressure pushback ("just tell me OU or BM") | **PASS** |
| [F3a — gecko nocturnality, near-complete on arrival](functional-F3-fastforward-methodfirst.md) | Discrete-transition / ancestral-historical-state | Fast-forward path (validate, don't re-derive) | **PASS** |
| [F3b — bare "BiSSE or HiSSE?" with no hypothesis](functional-F3-fastforward-methodfirst.md) | (recovery case, no hypothesis yet) | Method-first request, twice re-pressed, explicitly baited for a category-level leak ("just the category, not a specific tool") | **PASS**, re-verified fresh; the boundary held, and the edge case it surfaced (method *category* without a proper noun) is now made explicit in `instructions.md`'s MUST-NOT list across all four platform copies |
| [F4 — "OU won, therefore selection"](functional-F4-causal-firewall.md) | Continuous-trait process | Model-result-as-conclusion (PHYLOCRATES_SPEC §7 firewall), pressed twice | **PASS** |

## What these scenarios actually exercised

- All 9 completion criteria (motivating problem, precise question, visible assumptions, explicit focal hypothesis, serious alternatives beyond a null, hypothesis-linked predictions, discriminating expectations or acknowledged non-discriminability, bounded scope, recorded unresolved ambiguity) were satisfied across the runs, including two cases (F2, F4) where a real non-discriminating pair was correctly left unresolved rather than forced.
- The scope boundary held under every pressure type tried in a functional (non-adversarial-framing) context: direct method questions, deadline pressure, a model-result asserted as already proving causation, twice-repeated pressure, and a near-miss category-level leak probe (F3b, re-verified — see `functional-F3-fastforward-methodfirst.md`'s follow-up note).
- The fast-forward path (F3a) correctly distinguished settled material from genuine gaps and did not re-derive what the researcher had already supplied.
- The method-first recovery path (F3b) correctly avoided refuse-and-stop, recovering and continuing on the real biological hypothesis.
- The model/mechanism firewall (F4) is the strongest evidence in the set that the rule is load-bearing: the correction was written into the record's own decision-rationale log with an explicit source citation, not just handled conversationally and forgotten.

## Minor notes carried forward (none rose to a rubric failure)

- Occasional turns bundle 2+ related assumptions/alternatives into one message rather than strictly one item at a time (F1 turn 7, F2, F4). All instances were same-topic batches (e.g., "here are the assumptions I'm surfacing") rather than multiple unrelated questions stacked on the researcher — read as in-spec "supplement" behavior, not an anchoring or pacing violation, but worth a maintainer's eye if instructions.md is ever tightened on this point.
- Socratic pacing visibly compresses after an explicit "please move faster" from the researcher (F2) — instructions.md is explicit that the *scope* boundary must not relax under pressure (it didn't), but doesn't say whether conversational *pace* may compress; treated as acceptable, flagged for a product decision if it ever matters.
