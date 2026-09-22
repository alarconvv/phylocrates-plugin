# Conceptual evolutionary question router

This router helps PhyloCrates choose **which hypothesis questions to ask**. It must never route to a statistical method or PCM family.

Multiple types may apply.

## Type A — Cross-taxon relationship
Typical claim: “Species with X tend to have Y.”

Probe:
- Is the intended claim associational or causal?
- Could a third process produce both X and Y?
- Could the pattern be inherited from one ancestor rather than repeatedly evolved?

## Type B — Continuous-trait process hypothesis
Typical claim: “Body size evolved toward an optimum / changed rapidly early / is constrained.”

Probe:
- Is the hypothesis descriptive or mechanistic?
- What biological mechanism is being proposed?
- What alternative process could produce a similar broad pattern?

## Type C — Phylogenetic resemblance / conservatism
Typical claim: “Closely related species resemble each other in X.”

Probe:
- Is resemblance itself the phenomenon, or is the user inferring a mechanism from it?
- Could the pattern reflect inheritance, niche conservatism, constraint, or repeated environmental sorting?

## Type D — Ancestral / historical-state hypothesis
Typical claim: “The ancestor was nocturnal” or “X evolved before Y.”

Probe:
- Is the claim about a specific ancestor, an ordering of events, or repeated historical sequences?
- What alternative ancestral histories would tell a different biological story?
- Is the user treating an inferred history as if it were observed?

## Type E — Discrete-transition hypothesis
Typical claim: “Loss of flight promotes island specialization.”

Probe:
- What direction of change is being claimed?
- Could both state changes be consequences of another transition?
- Does the hypothesis require repeated ordering across evolutionary events?

## Type F — Diversification hypothesis
Typical claim: “Trait X caused a radiation.”

Probe:
- Is the claim about coexistence with a diverse clade or repeated linkage between X and lineage proliferation?
- Could diversification heterogeneity be unrelated to X?
- Is one historical coincidence being generalized into a causal rule?
