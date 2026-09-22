# PhyloCrates for Gemini CLI

A real extension (unlike the ChatGPT/Gemini-app packages, which are manual instructions+upload) — Gemini CLI supports the same `skills/*/SKILL.md` layout as the Claude Code plugin, so `skills/` here is a straight copy of [`../skills/`](../skills).

## Install

```bash
gemini extensions install /path/to/phylocrates-plugin/gemini-cli
```

or, from a Git remote once this repo is pushed:

```bash
gemini extensions install <repo-url> --path gemini-cli
```

## Use

- `GEMINI.md` loads automatically whenever the extension is active — it carries the identity and the hard scope boundary.
- The `phylocrates` skill carries the full eight-stage protocol; the model invokes it when a researcher brings a biological hypothesis to refine.
- The `phylocrates-check` skill is dev-only (package maintenance — manifest diff + scope-boundary lint), not for running the agent.

Verify: `gemini extensions list` should show `phylocrates`.
