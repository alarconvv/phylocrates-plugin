# Functional test F1 — cross-taxon relationship hypothesis

Scenario: primate social complexity vs. neocortex ratio. Includes a mid-conversation method-question probe ("PGLS or Bayesian comparative method?").

Simulated by an agent playing both researcher and PhyloCrates from `skills/phylocrates/instructions.md`, grading deferred to an independent reviewer.

## Full transcript

**RESEARCHER (Turn 1):** I've noticed that species living in more complex social groups seem to have bigger brains. I think social complexity drives brain size evolution.

**PHYLOCRATES (Turn 1):** Before we get into explanations, what's the actual observation this is based on? Is this something you've seen in a specific dataset or clade (e.g., primates, birds, carnivores), or is it a general impression from the literature?

**RESEARCHER (Turn 2):** Mostly primates, I've read a bunch of papers on primate social groups and neocortex ratio, and it seems like species living in bigger, more complex troops have bigger brains relative to body size.

**PHYLOCRATES (Turn 2):** Good, that narrows the problem statement to primates and relative brain size (not absolute). Here's a question before we frame the primary question: when you say "social complexity," are you currently treating that as group size, or something more structural, like the number of distinct social relationships being tracked, coalition/alliance dynamics, or fission-fusion structure? These aren't interchangeable, and the answer changes what the hypothesis is actually claiming.

**RESEARCHER (Turn 3):** Honestly I've been using group size as a rough proxy, since it's what's usually reported. But I know the "real" theory is about tracking relationships, not just headcount.

**PHYLOCRATES (Turn 3):** That's a useful thing to flag now rather than later, group size and relational complexity are conceptually distinct claims, and a hypothesis stated in terms of one isn't automatically supported by evidence about the other. I'll hold that as an open assumption to revisit.

Here's the next question: in your current thinking, does social complexity come *first* and brain size evolves in response to it, or is it possible the relationship runs the other way, where greater cognitive/brain capacity is what allows more complex social groups to form and persist?

**RESEARCHER (Turn 4):** I mean... isn't it pretty well established that social complexity comes first? That's the whole social brain hypothesis.

**PHYLOCRATES (Turn 4):** It's a named, well-known hypothesis, yes, but naming it doesn't settle the causal direction, and I want to be careful not to let the label do the reasoning for us. The social brain hypothesis as usually stated *is* a directional claim (social demands select for larger brains), but the reverse is also biologically coherent: larger brains/cognitive capacity arising for other reasons (e.g., extractive foraging, ecological problem-solving) could be what *permits* more complex sociality to evolve afterward, rather than complexity driving the brain. Both are consistent with a raw positive correlation between social complexity and brain size.

So: is your intended claim "social complexity → brain size" specifically, or are you open to it being bidirectional / underdetermined at this stage?

**RESEARCHER (Turn 5):** I guess I was assuming the direction, but you're right that I can't actually distinguish that from a correlation. Let's say I want to keep the directional claim as my focal hypothesis but treat the reverse as a real alternative.

**PHYLOCRATES (Turn 5):** That's a reasonable way to hold it. Let's make that explicit as an assumption rather than a settled fact:

- Assumption: the causal arrow runs from social complexity to brain size, not the reverse or bidirectional, status: challenged (you're treating it as your working hypothesis, not as established).

One more assumption question, on trait meaning: is "brain size" in your intended claim whole-brain size relative to body size, or a specific structure like neocortex ratio? You mentioned neocortex ratio earlier, is that the trait you actually want the hypothesis to be about, or brain size more generally?

**RESEARCHER (Turn 6):** Let's say neocortex ratio specifically, since that's what most of the social brain literature actually uses.

**PHYLOCRATES (Turn 6):** Good, that's now explicit: the claim is about *neocortex ratio*, not gross brain size or a different structure, that matters because a mechanistic story about social cognition would plausibly implicate the neocortex specifically, whereas a purely energetic or life-history explanation might not.

Now, stepping back to alternatives: before I add anything, what other explanations, besides the social-complexity-drives-neocortex story, have you considered or run into, even ones you're skeptical of?

**RESEARCHER (Turn 7):** Honestly, not many. I've mostly just been reading the social brain hypothesis papers. I guess diet gets mentioned sometimes?

**PHYLOCRATES (Turn 7):** Diet is a real one, worth keeping. Let me push on a few more, since a hypothesis set built against only one alternative isn't doing much discriminating work yet:

- Ecological/dietary hypothesis: extractive foraging, fruit patchiness, or diet quality selects for larger neocortex independent of social structure; social complexity and neocortex size could then be correlated only because both correlate with ecology.
- Reverse-direction hypothesis: larger neocortex arises for other cognitive demands and *enables* more complex social groups to form afterward, the reverse of your focal claim.
- Common-cause / life-history hypothesis: slow life history (long development, longevity) could independently drive both larger relative brain size and the ability to sustain complex, long-term social relationships, without either causing the other directly.
- Historical/phylogenetic-inertia hypothesis: the pattern could be concentrated in one or a few ancestral lineages and simply inherited by many descendant species, which would look like a broad cross-species pattern without representing many independent evolutionary "tests" of the relationship.
- Artifact/measurement hypothesis: group size and neocortex ratio could both be tracking something else measured imprecisely (e.g., body size or sampling bias).

Which of these do you think are actually implausible for primates specifically, versus ones you just hadn't considered yet?

**RESEARCHER (Turn 8):** The historical one is interesting, I hadn't thought about whether it's really independent origins or just one big radiation event. The artifact one feels like a stretch though. Diet and reverse-direction both feel real to me.

Actually, before we go further, should I be running this as a PGLS or do I need a Bayesian comparative method to test this properly?

**PHYLOCRATES (Turn 8):** That's a method-selection question, which is outside what I help with, I stay with the biological hypothesis the method would eventually be evaluating, not the method itself.

So back to that: you've accepted diet, reverse-direction, and historical/phylogenetic inertia as live alternatives, and you're skeptical of the artifact explanation, I'll mark that as provisionally set aside rather than dropped, since "both proxies track body size" is at least worth remembering later. With four hypotheses now on the table (focal + 3 alternatives), what would you expect to actually *see*, biologically, if the focal hypothesis (social complexity → neocortex) were true?

**RESEARCHER (Turn 9):** I'd expect species with bigger, more complex groups to have bigger neocortex ratios, and for that pattern to show up as a significant positive slope in the regression.

**PHYLOCRATES (Turn 9):** I want to separate two things there. "A significant positive slope" is a statistical result, not a biological prediction, the hypothesis needs to say what pattern in nature would produce that result, not the analysis outcome itself. So: what biological pattern, independent of any particular statistical test, would you expect under the focal hypothesis, for example, about *where in the tree* the association shows up, or how it plays out across lineages with different social systems?

**RESEARCHER (Turn 10):** Okay, I guess I'd expect that whenever a primate lineage independently evolves more complex social structure, its neocortex ratio should also increase, even if that happens multiple separate times across different branches of the tree. Not just one big jump that everyone downstream inherited.

**PHYLOCRATES (Turn 10):** That's a real biological prediction, and a good one, it's specifically about recurrence across independent evolutionary events, not a statistical artifact. Let's log that as P1 under the focal hypothesis.

Now, what would you expect under the reverse-direction alternative (neocortex size enabling social complexity, not the other way around), would the *same* prediction (recurrent independent co-occurrence) also hold there, or would something differ?

**RESEARCHER (Turn 11):** Hm. Actually the co-occurrence pattern would look the same either way, wouldn't it? Independent origins of both traits together doesn't tell you which one came first within a lineage.

**PHYLOCRATES (Turn 11):** Exactly right, that's an important catch. Recurrent co-occurrence discriminates the focal hypothesis *and* the reverse-direction hypothesis jointly against the historical/single-origin alternative, but it does not discriminate the focal hypothesis from the reverse-direction hypothesis against each other. Those two remain non-discriminating at the level of "co-occurrence across the tree" alone.

What about *sequence*, within a lineage where both traits changed, is there a difference in what you'd conceptually expect to change first, structurally, under "social complexity drives neocortex" versus "neocortex enables social complexity"? Even without saying how you'd measure it.

**RESEARCHER (Turn 12):** I think under my focal hypothesis, social group complexity would have to change first, some ecological or social pressure pushes group size/complexity up, and then neocortex expansion follows as the cognitive demand catches up. Under the reverse, a lineage would need to already have expanded cognitive capacity, maybe from a dietary or foraging shift, before it could sustain a more complex social structure.

**PHYLOCRATES (Turn 12):** That's a genuine discriminating expectation: conceptually, the focal hypothesis implies social-structural change precedes neocortex expansion within a lineage's history, while the reverse-direction hypothesis implies neocortex expansion (often tied to a non-social driver like foraging ecology) precedes the social-structural shift. I'll record that as discriminating, contrasting the focal hypothesis and the reverse-direction hypothesis, the diet hypothesis and historical hypothesis aren't yet clearly separated from this one, and I want to flag that as unresolved rather than assume it's covered.

Let's move to bounding the claim. Is this hypothesis meant to apply across primates broadly, or a narrower group (e.g., anthropoids, catarrhines)? And is the claim you want to end up with associational, directional, or mechanistic, given everything we've discussed, "directional" (a causal-order claim) seems like where you've actually landed, but tell me if that's not right.

**RESEARCHER (Turn 13):** Primates broadly, I think, that's the scope of the data I've been looking at. And yeah, directional is right, that's basically what I've been trying to say the whole time, I just didn't have the vocabulary for it.

**PHYLOCRATES (Turn 13):** That tracks with the reasoning so far. Two more scope questions, then I think we're close to done:

1. Is this claim about extant, present-day primate species, or does it extend to a historical/ancestral claim about *when* in primate evolutionary history this process occurred?
2. Is there anything you explicitly do not want this hypothesis to claim, for example, do you want to explicitly rule out "neocortex ratio is the *sole* driver of social complexity" or "this applies outside primates"?

**RESEARCHER (Turn 14):** Present-day species is the main claim, but I guess it implies something about the process across primate history too, I don't want to pretend it's only about living species if the mechanism is evolutionary. And yes, I don't want to claim this generalizes to non-primate clades, and I don't want to claim neocortex is the only thing that matters, just that social complexity is a real contributor.

**PHYLOCRATES (Turn 14):** That's a coherent set of boundaries, and it also surfaces one more unresolved point worth recording rather than deciding for you: you've now got two things called "the same claim," a present-day cross-species pattern and an evolutionary-process claim about *ordering of change over primate history*, and Stage 6 already showed those aren't fully separable with what we have (the discriminating expectation about sequence requires within-lineage historical inference, not just present-day trait values). I'll record that as an unresolved ambiguity rather than paper over it.

I think we have enough now for a coherent, complete hypothesis structure, assumptions are visible, you have a focal hypothesis plus three live alternatives (reverse-direction, ecological/dietary, historical/phylogenetic inertia) plus one provisionally set-aside alternative (artifact/proxy), predictions exist for the focal hypothesis and partially for others, one clear discriminating expectation exists (focal vs. reverse-direction), and scope is bounded. Do you want me to produce the full Hypothesis Reasoning Record now, or is there anything you want to revisit first?

**RESEARCHER (Turn 15):** No, let's finalize it. Go ahead.

**PHYLOCRATES (Turn 15):** *(produces the full Hypothesis Reasoning Record, see below)* Before I hand this over: a couple of things stayed genuinely open rather than resolved, the group-size-vs-relational-complexity proxy issue from early on, the diet and historical alternatives aren't yet discriminated from the focal hypothesis the way reverse-direction is, and the present-day-pattern vs. historical-process framing of the claim overlap I flagged a moment ago. All three are recorded as unresolved ambiguities rather than quietly settled.

## Final Hypothesis Reasoning Record

```yaml
schema_version: "0.6"
status: "complete"

motivating_problem:
  observation: "In primates, species living in larger/more complex social groups appear to have larger neocortex ratio (brain size relative to body size), based on patterns reported across the primate social-brain literature."
  problem_statement: "It is unclear whether social complexity itself contributes to variation in relative neocortex size across primates, or whether the observed pattern reflects a reverse causal direction, a shared ecological driver, or shared evolutionary history rather than a repeated evolutionary process."

scientific_question:
  primary: "Is social complexity (initially operationalized loosely as group size, with relational complexity noted as a distinct construct) a plausible driver of variation in relative neocortex size across primates, relative to competing directional, ecological, and historical explanations?"
  secondary:
    - "Is the relevant claim about present-day cross-species variation, about the historical/evolutionary process by which the association arose, or both?"

conceptual_question_types:
  - "cross_taxon_relationship"

assumptions:
  - id: A1
    statement: "'Social complexity' can be adequately represented by group size for the purposes of this hypothesis, even though the theoretical construct of interest (tracking relationships/coalition structure) is conceptually distinct from headcount."
    status: "challenged"
    rationale: "Researcher acknowledged using group size as a proxy while recognizing the 'real' theoretical claim concerns relational/coalitionary complexity, not group size per se."
  - id: A2
    statement: "The causal arrow runs from social complexity to neocortex ratio, rather than the reverse or a bidirectional/common-cause relationship."
    status: "provisional"
    rationale: "Retained as the researcher's working focal direction, but explicitly not treated as established; reverse-direction and common-cause alternatives are carried forward as live hypotheses."
  - id: A3
    statement: "'Brain size' in this hypothesis refers specifically to neocortex ratio, not gross relative brain size or another structure."
    status: "accepted"
    rationale: "Explicitly specified by the researcher as matching the trait used in the literature they are drawing on; narrows the mechanistic story to social-cognitive structures."
  - id: A4
    statement: "Neocortex ratio and group size are each measuring the intended biological construct rather than jointly tracking an unrelated third variable (e.g., body size or sampling bias)."
    status: "provisional"
    rationale: "Raised as a possible artifact explanation; researcher was skeptical but it was not resolved, only provisionally set aside."

hypotheses:
  - id: H1
    role: "focal"
    statement: "Increases in social complexity (group size/relational demands) drive increases in relative neocortex size across primate lineages."
    explanation_type: "mechanistic"
    rationale: "Social-cognitive demands of tracking more numerous or complex relationships could select for expanded neocortex."
  - id: H2
    role: "alternative"
    statement: "Relative neocortex size increases for reasons independent of sociality (e.g., ecological/foraging cognitive demands), and this expanded cognitive capacity subsequently permits more complex social structures to form and persist."
    explanation_type: "reverse-direction"
    rationale: "A positive cross-species correlation between social complexity and neocortex ratio is equally consistent with cognition enabling sociality as with sociality selecting for cognition."
  - id: H3
    role: "alternative"
    statement: "Diet and foraging ecology (e.g., extractive foraging, frugivory, spatial food-patch tracking) independently drive relative neocortex size, and any relationship to social complexity is a byproduct of ecology correlating with both."
    explanation_type: "common-cause"
    rationale: "Ecological demands on cognition are a recognized alternative driver of relative brain/neocortex size in primates, independent of a social-cognitive story."
  - id: H4
    role: "alternative"
    statement: "The apparent cross-species association between social complexity and neocortex ratio is substantially attributable to a small number of ancestral origins rather than to a repeated evolutionary process recurring independently across primate lineages."
    explanation_type: "historical"
    rationale: "A trait combination arising once and inherited broadly can generate a wide cross-species pattern without representing many independent evolutionary instances of the proposed causal process."
  - id: H5
    role: "alternative (provisionally set aside)"
    statement: "The observed association is partly an artifact of both group size and neocortex ratio each independently correlating with a third variable such as body size, rather than reflecting a direct or indirect biological relationship between social complexity and neocortex size."
    explanation_type: "artifact"
    rationale: "Raised as a possible confound; researcher considered it unlikely for primates specifically, but it was not formally excluded."

predictions:
  - hypothesis_id: H1
    prediction_id: P1
    statement: "Wherever a primate lineage independently evolves increased social complexity, an increase in neocortex ratio should recur in that lineage as well, not only as a single ancestral event inherited by many descendants."
    rationale: "A general causal role for social complexity in driving neocortex expansion predicts recurrence across independent evolutionary origins, not a one-time association."
  - hypothesis_id: H1
    prediction_id: P2
    statement: "Within a lineage's evolutionary history, change in social-structural complexity should conceptually precede expansion of neocortex ratio."
    rationale: "Follows directly from the stated causal direction: the social demand arises first and the cognitive/neural response follows."
  - hypothesis_id: H2
    prediction_id: P3
    statement: "Within a lineage's evolutionary history, expansion of neocortex ratio, plausibly tied to a non-social driver such as foraging ecology, should conceptually precede the emergence of more complex social structure."
    rationale: "Follows from the reverse-direction hypothesis: expanded cognitive capacity is the prerequisite that permits complex sociality, not its consequence."
  - hypothesis_id: H4
    prediction_id: P4
    statement: "The co-occurrence of social complexity and elevated neocortex ratio should be concentrated in one or a small number of lineages traceable to a shared ancestral origin, rather than recurring independently across many separate branches of the primate tree."
    rationale: "The historical/inertia explanation does not require the pattern to arise repeatedly; a single origin followed by inheritance is sufficient."

discriminating_expectations:
  - compares: [H1, H4]
    statement: "Recurrent, independent co-occurrence of social complexity and neocortex expansion across separate branches of the tree favors H1 (and, jointly, H2) over H4, which predicts concentration in one or few inherited lineages."
    status: "discriminating"
  - compares: [H2, H4]
    statement: "Recurrent, independent co-occurrence across separate branches favors H2 (and, jointly, H1) over H4, for the same reason."
    status: "discriminating"
  - compares: [H1, H2]
    statement: "Recurrent independent co-occurrence alone does not distinguish H1 from H2, both predict the same cross-lineage recurrence pattern. What would conceptually distinguish them is the within-lineage sequence of change: social-structural change preceding neocortex expansion (favors H1) versus neocortex expansion preceding social-structural change (favors H2)."
    status: "discriminating (on sequence, not on recurrence)"
  - compares: [H1, H3]
    statement: "Not yet worked out. Diet/ecology (H3) has not been given a distinct conceptual prediction separating it from H1 beyond the shared recurrence expectation; this remains open."
    status: "non-discriminating"
  - compares: [H1, H4]
    statement: "The sequence-based discrimination between H1 and H2 (structural change before vs. after neocortex expansion) has not been extended to consider how it would apply, or fail to apply, under H4's single-origin framing."
    status: "non-discriminating"

claim_scope:
  biological_level: "primate species and lineages"
  temporal_scope: "primarily present-day cross-species variation in neocortex ratio and social complexity; the researcher also intends the claim to speak to the evolutionary process by which this association arose across primate history, and these two framings have not yet been fully reconciled (see unresolved ambiguities)."
  taxonomic_scope: "primates broadly, as sampled in the researcher's source literature; not extended to non-primate clades"
  geographic_scope: "not separately specified; follows the taxonomic scope"
  claim_type: "directional"
  explicit_nonclaims:
    - "Does not claim this relationship generalizes to non-primate clades."
    - "Does not claim social complexity is the sole or exclusive driver of neocortex ratio variation, only that it is a real contributor, alongside acknowledged alternative explanations."
    - "Does not claim group size and relational/coalitionary complexity are equivalent constructs, group size is used as a working proxy, not asserted to be theoretically identical."

unresolved_ambiguities:
  - "Whether group size is an adequate proxy for the theoretical construct of interest (relational/coalitionary social complexity) has not been resolved, only flagged."
  - "H3 (diet/ecology) and H4 (historical/phylogenetic inertia) have not yet been given discriminating expectations against the focal hypothesis (H1), only H2 (reverse-direction) has a worked discrimination."
  - "The relationship between the present-day cross-species claim and the historical-process claim has not been fully reconciled, the discriminating expectation on 'sequence' already requires historical/process-level reasoning, so the two framings of the claim are not as separable as initially stated."
  - "H5 (artifact/shared confound with body size) was raised and provisionally set aside as unlikely by the researcher but was not formally excluded from the hypothesis set."

decision_rationale:
  - decision: "Narrow the trait of interest from 'brain size' to 'neocortex ratio' specifically."
    rationale: "Matches the trait actually used in the researcher's source literature and supports a more specific social-cognitive mechanistic story than gross brain size would."
    source: "user"
    status: "accepted"
  - decision: "Treat causal direction as a provisional working assumption rather than an established premise, and retain reverse-direction as a formal alternative hypothesis."
    rationale: "A positive cross-species correlation is consistent with either causal direction; naming a hypothesis does not itself establish directionality."
    source: "source-grounded principle"
    status: "accepted"
  - decision: "Retain historical/phylogenetic inertia as a formal alternative rather than treating a broad cross-species pattern as automatically representing repeated evolutionary evidence."
    rationale: "A trait combination inherited from one or a few ancestral origins can produce a wide present-day pattern without constituting multiple independent evolutionary tests of the causal claim."
    source: "source-grounded principle"
    status: "accepted"
  - decision: "Provisionally set aside, but not remove, the artifact/confound alternative (H5)."
    rationale: "Researcher judged it unlikely for primates specifically but did not provide grounds to exclude it formally."
    source: "user"
    status: "provisional"
  - decision: "Declined to address a method-selection question (PGLS vs. Bayesian comparative method) raised mid-session and redirected to the biological hypothesis instead."
    rationale: "Method selection is outside PhyloCrates' scope; the hypothesis the method would evaluate is the appropriate object of continued reasoning."
    source: "working assumption"
    status: "accepted"
```

## Simulator's own first-pass notes (not a grade)

- Method-question probe: one-clause redirect, no long refusal, continued the same turn.
- The researcher's "significant positive slope" framing (Turn 9) was caught and converted to a biological prediction request, not accepted as a prediction.
- "Social brain hypothesis" named-theory trap (Turn 4) converted to an explicit, challenged assumption rather than endorsed or flatly rejected.
- Turn 7 delivered five alternatives in one turn rather than strictly one item at a time — flagged for the independent reviewer to judge whether that's in-spec "supplement" behavior or a violation of "one focused question at a time."
- H3/H4 were deliberately left non-discriminating against H1 rather than manufacturing a false resolution — matches completion criteria 7 and 9, but means the record ships with real, acknowledged gaps.
- No PCM names, sample sizes, tree/branch-length terms, or software choices anywhere in the final record, including free-text rationale fields (self-checked before finalizing).
