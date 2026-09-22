# PhyloCrates

A Socratic hypothesis-refinement agent for phylogenetic comparative biology. It takes a researcher from a biological observation or uncertainty through an eight-stage protocol to a structured Hypothesis Reasoning Record, and stops deliberately before choosing a comparative method, study design, or analysis pipeline.

Full behavior, scope boundary, and rationale live in [`skills/phylocrates/instructions.md`](skills/phylocrates/instructions.md) and [`skills/phylocrates/PHYLOCRATES_SPEC.md`](skills/phylocrates/PHYLOCRATES_SPEC.md), every platform package below wraps that same core, unmodified.

## Pick your platform

| Platform | Package | Setup |
|---|---|---|
| Claude Code | [`skills/`](skills) | `claude --plugin-dir ./phylocrates-plugin` — see this repo's `.claude-plugin/plugin.json` |
| ChatGPT | [`chatgpt/`](chatgpt) | [`chatgpt/README.md`](chatgpt/README.md) |
| Gemini (app / Gems) | [`gemini/`](gemini) | [`gemini/README.md`](gemini/README.md) |
| Gemini CLI | [`gemini-cli/`](gemini-cli) | [`gemini-cli/README.md`](gemini-cli/README.md) |

## Maintainers

- `skills/phylocrates-check` is a dev-only, explicit-invocation skill that lints the package for manifest completeness and scope-boundary leaks (see its `SKILL.md`).
- `tests/validate_packages.py` is the unit + integration test gate: JSON/YAML validity, schema conformance, and cross-platform consistency (the four `instructions.md` copies must agree on the protocol chain and the scope boundary's MAY / MUST-NOT lists; `gemini-cli/skills/phylocrates/` must stay byte-identical to `skills/phylocrates/`). Run it with:

  ```bash
  pip install pyyaml jsonschema
  python3 tests/validate_packages.py
  ```

## Scope

PhyloCrates refines hypotheses. It never recommends a phylogenetic comparative method (PGLS, PIC, OU, BiSSE, etc.), sample size, measurement protocol, or analysis pipeline — under pushback, urgency, or reframing. See `instructions.md`'s scope boundary section for the full MAY / MUST NOT list.
