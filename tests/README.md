# PhyloCrates test gates

Four gates, run against the package in this repo. All must be green before shipping a change.

## 1. Unit + integration — `validate_packages.py`

```bash
pip install pyyaml jsonschema
python3 tests/validate_packages.py
```

Checks: every JSON/YAML file parses; `example-record.yaml` validates against `hypothesis-record.schema.json` in each of the four platform packages; every `SKILL.md` and plugin manifest carries its required fields; the four `instructions.md` copies (Claude Code, ChatGPT, Gemini Gem, Gemini CLI) agree verbatim on the eight-stage protocol chain and list every out-of-scope method; `gemini-cli/skills/phylocrates/` stays byte-identical to `skills/phylocrates/`; `PHYLOCRATES_SPEC.md`, `hypothesis-record.schema.json`, and `example-record.yaml` are byte-identical across all four platform copies; `MANIFEST.txt` matches the actual file tree exactly (no stale or missing entries); no `.DS_Store` cruft anywhere in the repo; every relative Markdown link resolves; the ChatGPT/Gemini instruction text stays under the 8,000-char Custom GPT limit.

76 checks, all green as of the last run.

## 2. Functional — behavioral conformance

Since PhyloCrates is a conversational skill, not executable code, "functional test" means: simulate a real multi-turn researcher/PhyloCrates conversation against a scenario, then grade the transcript and final Hypothesis Reasoning Record against `instructions.md`'s nine completion criteria and its Socratic-behavior rules (one focused question at a time, elicit → challenge → supplement → synthesize, no anchoring). Simulation and grading are run by separate agents to avoid self-grading bias.

Scenarios covered (see `reports/functional-*.md` for full transcripts and verdicts):
- Cross-taxon relationship hypothesis, with a mid-conversation method-question probe
- Continuous-trait process hypothesis, with a pushback-under-pressure probe
- Fast-forward path (user arrives with a near-complete hypothesis set)
- Method-first request with no stated hypothesis (must recover the biological claim first)
- Model/mechanism language firewall (a model-comparison result asserted as already proving causation)

## 3. Security — adversarial scope-boundary and prompt-injection resistance

PhyloCrates has no code execution, tool access, or data store — its only enforceable boundary is behavioral: never naming or recommending a phylogenetic comparative method, PCM family, sample size, measurement protocol, tree requirement, diagnostic, or analysis pipeline, regardless of framing, and resisting prompt injection (fake system/developer messages, injected "tool output," roleplay jailbreaks). See `reports/security-adversarial.md` for the full attack log and verdicts.

The one non-behavioral surface, `phylocrates-check`'s dev-only shell snippets, was reviewed separately: it only ever runs locally, under the invoking user's own shell permissions, against a path they supply themselves — not a privilege boundary, so not treated as an attack surface.

The website (`phylocrates-site/`) was scanned separately: fully static HTML/CSS, no `<script>`, no `eval`/`innerHTML`/`document.write`, no external hosts beyond Google Fonts, no secrets, no `target="_blank"` links. Minimal surface, clean.

## 4. Reports

- `reports/functional-summary.md` — pass/fail per scenario per completion criterion
- `reports/security-summary.md` — pass/fail per attack
- Full transcripts live alongside each summary for anyone who wants to re-derive the verdict themselves rather than trust the grade
