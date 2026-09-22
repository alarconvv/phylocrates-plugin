---
name: phylocrates-check
description: Dev-only scope-compliance and manifest linter for the PhyloCrates package. Explicit invocation only.
disable-model-invocation: true
---

# PhyloCrates dev check

Run this when maintaining the PhyloCrates package itself (not when running the agent for a researcher).

1. **Manifest completeness** — from the plugin's `skills/phylocrates/` directory, diff the actual file tree against `MANIFEST.txt`:
   ```
   find . -type f ! -name MANIFEST.txt | sed 's|^\./||' | sort > /tmp/actual.txt
   sort MANIFEST.txt > /tmp/listed.txt
   diff /tmp/listed.txt /tmp/actual.txt
   ```
   Report any file present but unlisted, or listed but missing.

2. **Scope-boundary lint** — given a hypothesis record (path passed by the user, default `skills/phylocrates/output/example-record.yaml`), grep it for banned method/design terms drawn from `skills/phylocrates/instructions.md` (PIC, PGLS, PGLMM, BM, OU model, Mk, ASR, BiSSE, HiSSE, BAMM, sample size, power, taxon sampling, tree requirement, branch length requirement, prior, diagnostic, sensitivity analysis). Flag every hit with its line, including free-text rationale fields — these are the fields the spec warns leak method prescriptions.

3. Summarize: manifest diff (if any) + banned-term hits (if any) + a one-line verdict (clean / needs fixing).
