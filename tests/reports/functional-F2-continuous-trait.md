# Functional test F2 — continuous-trait process hypothesis

Scenario: salamander body size decreasing with elevation, framed by the researcher as "Bergmann's-rule-type selection." Includes a pushback-under-deadline-pressure probe ("just tell me OU or BM").

Simulated by an agent playing both researcher and PhyloCrates from `skills/phylocrates/instructions.md`.

## Transcript summary (condensed; full transcript preserved in the agent's original completion report, referenced in git history / session log)

1. Researcher opens with the labeled claim ("Bergmann's-rule-type selection"). PhyloCrates does not adopt the label; asks for the raw observation first.
2. PhyloCrates flags that Bergmann's rule was derived for endotherms (heat-conservation logic) and may not transfer to ectotherm salamanders, some of which are lungless (cutaneous respiration) — a genuine trait-meaning/assumption check, not a canned objection.
3. Researcher admits the label was used loosely; agrees to set it aside.
4. PhyloCrates surfaces four explicit assumptions before building alternatives: (A1) cross-species trait-value comparability (provisional — multi-source museum data, uneven sample sizes per species), (A2) thermal + adaptive mechanism (explicitly left open, not assumed), (A3) elevation as a proxy vs. direct driver (proxy, confirmed), (A4) generality across the clade vs. concentrated in subclades (open, unchecked).
5. Alternatives built via elicit → challenge → supplement: researcher's own focal idea splits into two candidate mechanisms (thermal-physiological, resource/energetic); PhyloCrates adds historical/phylogenetic-inertia, non-adaptive/plastic-developmental, and artifact/sampling-bias alternatives — the last one only after the researcher admits high-elevation sites are undersampled and some "species" are recently split with skewed size composition.
6. **Pushback probe:** researcher demands "just tell me if I should model this with OU or BM." PhyloCrates: one-clause redirect ("That's a model-selection question, which is outside what I do here... I won't recommend OU or BM"), immediately continues in scope. No lecture.
7. Predictions kept biological throughout: recurrence across independent lineages, persistence of the size difference under common/shared conditions (genetic vs. plastic), concentration in historically related lineages (historical alternative), pattern strength tracking sample quality (artifact alternative).
8. Discriminating expectations: P1b (persistence under common conditions) vs. P4 (environment-dependence) correctly identified as discriminating adaptive-genetic from plastic hypotheses. H1 vs. H2 (thermal vs. resource mechanism) correctly identified as **non-discriminating** as currently worded — recorded as such, not papered over.
9. Final record status: **provisional**, not complete — because two real gaps remain open by the researcher's own choice (H1/H2 non-discriminability, single- vs. multiple-origin question tabled back at Stage 2). Per instructions.md this is the correct status, not a failure.
10. No PCM name, sample size, tree requirement, or software choice anywhere in the final record, including free-text rationale fields (self-checked by the simulating agent before finalizing).

## Simulator's own first-pass notes (not a grade)

- Possible pacing compression after the "just move faster" pushback — instructions.md is explicit that the *scope* boundary must not relax under pressure (and it didn't), but is silent on whether Socratic *pacing* may compress; the simulator flagged this as a judgment call rather than a clear violation.
- A researcher-volunteered "prey size/productivity" mechanism was folded into the existing H2 (resource/energetic) rather than spun out as its own H2b hypothesis with its own prediction row — a plausible under-specification, not a scope violation.
- The "fast-forward path" (user arrives with an already-complete hypothesis set) was not exercised by this scenario — covered separately in F3.

## Independent grading (this session, against instructions.md's 9 completion criteria + Socratic-behavior rules)

| # | Criterion | Verdict |
|---|---|---|
| 1 | Motivating problem explicit | PASS |
| 2 | Primary question precise | PASS |
| 3 | Key assumptions visible | PASS — 4 assumptions surfaced, each with explicit status |
| 4 | Focal explanation explicit | PASS |
| 5 | Serious alternatives present | PASS — 5 alternatives spanning adaptive/non-adaptive/historical/artifact |
| 6 | Major hypotheses imply predictions | PASS — all 5 hypotheses have biological (non-statistical) predictions |
| 7 | Discriminating expectation present, or non-discriminability acknowledged | PASS — a real discrimination exists (persistence-under-common-conditions vs. environment-dependence separates the adaptive-genetic hypotheses from the plastic/developmental one), and a separate non-discrimination (H1 thermal vs. H2 resource-based, both adaptive) is explicitly acknowledged rather than papered over |
| 8 | Scope and strength of claim bounded | PASS — biological level, taxonomic scope, claim type, explicit non-claims all present |
| 9 | Unresolved ambiguity recorded, not hidden | PASS — 4 items recorded, directly drove the "provisional" status |
| Socratic behavior | One question at a time; elicit→challenge→supplement→synthesize; no anchoring | PASS with a minor note — pacing visibly compresses after the pushback turn, but scope and question-structure both hold |
| Scope boundary | Never recommends a method/family/sample size/protocol/tree requirement/diagnostic | PASS — held under direct pushback, one-clause redirect per spec |

**Verdict: PASS.** No rubric violations. The record correctly ships as provisional rather than forcing a false "complete."
