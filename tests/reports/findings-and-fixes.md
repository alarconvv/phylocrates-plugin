# Findings and fixes — this QA pass

Real defects found and fixed during this engineering pass, in the order discovered. Nothing here was hypothetical; each was caught by an actual check or test run, then fixed and re-verified.

1. **No root README.** A newcomer landing in `phylocrates-plugin/` had no top-level explanation of what the repo is or which folder to use for which platform. **Fixed:** added `README.md`.

2. **Stale `MANIFEST.txt`.** `skills/phylocrates/MANIFEST.txt` still listed the pre-plugin package layout (`benchmarks/`, `platforms/chatgpt/instructions.md`, `platforms/claude/SKILL.md`, `README.md`) that never made it into the plugin restructuring, and didn't list `SKILL.md`, which does exist. Found by dogfooding the `phylocrates-check` dev skill's own manifest-diff step by hand. **Fixed:** regenerated from the actual file tree, propagated identically to the `gemini-cli` mirror, and added a permanent automated check (`validate_packages.py`) so this can't silently drift again.

3. **`.DS_Store` cruft.** Stray macOS Finder files under `skills/` and the repo root. **Fixed:** deleted, added `.gitignore`, added a permanent automated check.

4. **Scope-boundary gap: method *category* without a proper noun.** Functional testing (scenario F3b) had PhyloCrates correctly decline to name BiSSE/HiSSE for a diversification question — but its own self-review flagged uncertainty about whether describing the method's functional *category* ("a model where diversification rate depends on the trait") without naming it would also be out of scope, since `instructions.md`'s "select a PCM family" clause never said so explicitly. Re-verified with a researcher persona explicitly baiting exactly this ("just the category, not a specific tool") — PhyloCrates held the line and named its own reasoning correctly, but the *instructions* left this to model inference rather than stating it, which is a real robustness gap for weaker models or future edits. **Fixed:** the MUST-NOT clause in all four `instructions.md` copies now states explicitly that a method's functional category/class counts as "selecting a PCM family," with the reasoning included inline.

5. **No cross-platform drift check for the shared reference files.** `PHYLOCRATES_SPEC.md`, `hypothesis-record.schema.json`, and `example-record.yaml` are meant to be byte-identical across all four platform packages, but nothing enforced that beyond the `instructions.md`-specific checks already in place. Manually diffed all four copies of each file (all were clean at the time), then **added a permanent automated check** so future edits to one copy and not the others get caught immediately rather than silently drifting.

None of these were security breaches (the adversarial pass found zero — see `security-summary.md`) or functional failures (the behavioral scenarios found zero rubric violations — see `functional-summary.md`). All five are integrity/maintenance-quality issues, caught because the QA pass looked for them deliberately rather than because anything was actively broken for an end user at the time.

## Final gate status

```
$ python3 tests/validate_packages.py
76 checks run, 0 failed.
ALL GATES GREEN.
```

Plus: Claude Code plugin load smoke-tested (`claude --plugin-dir .`) — both skills discovered correctly. 4/4 functional scenarios PASS (including one re-verification). 8/8 adversarial security attacks HELD, re-verified against raw transcripts. Website security scan clean (no script surface).
