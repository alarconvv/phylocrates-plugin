# PhyloCrates Hypothesis Reasoning Record schema v0.6

## Purpose

This schema defines PhyloCrates' own structured final output. It is an **independent hypothesis-reasoning record**, not a transfer package for another agent or platform.

The record captures the biological problem, scientific question, assumptions, competing hypotheses, predictions, discriminating expectations, claim scope, unresolved ambiguity, and reasoning rationale.

## Required fields

```yaml
schema_version: "0.6"
status: "complete | provisional"

motivating_problem:
  observation: "..."
  problem_statement: "..."

scientific_question:
  primary: "..."
  secondary: []

conceptual_question_types:
  - "cross_taxon_relationship | continuous_trait_process | phylogenetic_resemblance | ancestral_historical_state | discrete_transition | diversification"

assumptions:
  - id: A1
    statement: "..."
    status: "accepted | provisional | challenged"
    rationale: "..."

hypotheses:
  - id: H1
    role: "focal | alternative"
    statement: "..."
    explanation_type: "adaptive | mechanistic | associational | non-adaptive | historical | common-cause | reverse-direction | artifact | contingency | other"
    rationale: "..."

predictions:
  - hypothesis_id: H1
    prediction_id: P1
    statement: "..."
    rationale: "..."

discriminating_expectations:
  - compares: [H1, H2]
    statement: "..."
    status: "discriminating | partially-discriminating | non-discriminating"

claim_scope:
  biological_level: "..."
  temporal_scope: "..."
  taxonomic_scope: "..."
  geographic_scope: "..."
  claim_type: "descriptive | associational | directional | mechanistic | causal"
  explicit_nonclaims:
    - "..."

unresolved_ambiguities:
  - "..."

decision_rationale:
  - decision: "..."
    rationale: "..."
    source: "user | source-grounded principle | working assumption"
    status: "accepted | provisional | rejected | superseded"
```

## Scope exclusions

The Hypothesis Reasoning Record must not contain final decisions for:
- PCM family;
- named statistical method/model as the recommended solution;
- sample size;
- taxon-sampling design;
- operational measurement protocol;
- tree/branch-length requirement;
- priors;
- power analysis;
- analysis pipeline;
- diagnostic tests;
- sensitivity analyses;
- software/package choice.

These are deliberately outside the scientific scope of PhyloCrates. `conceptual_question_types` is not an exception: it describes the shape of the biological hypothesis, not an analytical recommendation.

## Completion rule

`status: complete` means the hypothesis reasoning is coherent and internally explicit enough to stand as a finished PhyloCrates output. It does **not** mean the hypothesis is true, empirically supported, or ready for any particular analysis.

Use `status: provisional` when important ambiguity remains but the user wants the current reasoning state summarized.
