#!/usr/bin/env python3
"""
Unit + integration gate for the PhyloCrates multi-platform package.

Unit checks: every JSON/YAML file in the repo parses, every YAML record
validates against the JSON schema, every SKILL.md/plugin manifest has the
fields its platform requires.

Integration checks: the four platform packages (Claude Code, ChatGPT,
Gemini Gem, Gemini CLI) agree on the parts of PhyloCrates that must never
drift between them -- the eight-stage protocol chain and the scope
boundary's MAY / MUST-NOT lists -- and every relative file path referenced
in docs actually exists.

Exit 0 = all gates green. Exit 1 = at least one failure, printed above the
summary line.
"""
import json
import re
import sys
from pathlib import Path

import yaml
import jsonschema

ROOT = Path(__file__).resolve().parent.parent
failures = []
checks_run = 0


def check(label, ok, detail=""):
    global checks_run
    checks_run += 1
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        failures.append(f"{label}: {detail}")
        if detail:
            print(f"       {detail}")


def load_json(path):
    return json.loads(path.read_text())


def load_yaml(path):
    return yaml.safe_load(path.read_text())


# ---------------------------------------------------------------------------
# UNIT: every JSON file parses
# ---------------------------------------------------------------------------
json_files = sorted(ROOT.rglob("*.json"))
for f in json_files:
    try:
        load_json(f)
        check(f"JSON parses: {f.relative_to(ROOT)}", True)
    except json.JSONDecodeError as e:
        check(f"JSON parses: {f.relative_to(ROOT)}", False, str(e))

# ---------------------------------------------------------------------------
# UNIT: every YAML file parses
# ---------------------------------------------------------------------------
yaml_files = sorted(ROOT.rglob("*.yaml")) + sorted(ROOT.rglob("*.yml"))
for f in yaml_files:
    try:
        load_yaml(f)
        check(f"YAML parses: {f.relative_to(ROOT)}", True)
    except yaml.YAMLError as e:
        check(f"YAML parses: {f.relative_to(ROOT)}", False, str(e))

# ---------------------------------------------------------------------------
# UNIT: every example-record.yaml validates against its schema
# ---------------------------------------------------------------------------
schema_files = list(ROOT.rglob("hypothesis-record.schema.json"))
record_files = list(ROOT.rglob("example-record.yaml"))
check("at least one schema file found", len(schema_files) > 0, str(schema_files))
check("at least one example record found", len(record_files) > 0, str(record_files))

for schema_path in schema_files:
    schema = load_json(schema_path)
    # find the record in the same output/ dir as this schema
    sibling_record = schema_path.parent / "example-record.yaml"
    if not sibling_record.exists():
        check(f"schema has sibling example record: {schema_path.relative_to(ROOT)}", False,
              f"no example-record.yaml next to {schema_path}")
        continue
    record = load_yaml(sibling_record)
    try:
        jsonschema.validate(instance=record, schema=schema)
        check(f"example record validates against schema: {sibling_record.relative_to(ROOT)}", True)
    except jsonschema.ValidationError as e:
        check(f"example record validates against schema: {sibling_record.relative_to(ROOT)}",
              False, e.message)

# ---------------------------------------------------------------------------
# UNIT: schema itself is a valid JSON Schema (Draft 2020-12)
# ---------------------------------------------------------------------------
for schema_path in schema_files:
    schema = load_json(schema_path)
    try:
        jsonschema.Draft202012Validator.check_schema(schema)
        check(f"schema is valid JSON Schema: {schema_path.relative_to(ROOT)}", True)
    except jsonschema.SchemaError as e:
        check(f"schema is valid JSON Schema: {schema_path.relative_to(ROOT)}", False, e.message)

# ---------------------------------------------------------------------------
# UNIT: SKILL.md files carry required frontmatter (name, description)
# ---------------------------------------------------------------------------
skill_files = sorted(ROOT.rglob("SKILL.md"))
check("at least one SKILL.md found", len(skill_files) > 0, "")
for f in skill_files:
    text = f.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        check(f"SKILL.md has frontmatter: {f.relative_to(ROOT)}", False, "no --- frontmatter block")
        continue
    fm = yaml.safe_load(m.group(1)) or {}
    has_desc = "description" in fm and bool(fm["description"])
    check(f"SKILL.md frontmatter has description: {f.relative_to(ROOT)}", has_desc, str(fm))

# ---------------------------------------------------------------------------
# UNIT: plugin.json / gemini-extension.json carry required fields
# ---------------------------------------------------------------------------
manifest_specs = {
    ".claude-plugin/plugin.json": ["name", "description", "version"],
    "gemini-cli/gemini-extension.json": ["name", "version"],
}
for rel, required_fields in manifest_specs.items():
    p = ROOT / rel
    if not p.exists():
        check(f"manifest exists: {rel}", False, "missing file")
        continue
    data = load_json(p)
    missing = [k for k in required_fields if k not in data]
    check(f"manifest has required fields: {rel}", not missing, f"missing: {missing}")

# ---------------------------------------------------------------------------
# INTEGRATION: the four platform instruction sources agree on the protocol
# chain and the MAY / MUST-NOT scope lists
# ---------------------------------------------------------------------------
INSTRUCTION_SOURCES = {
    "claude-code": ROOT / "skills/phylocrates/instructions.md",
    "chatgpt": ROOT / "chatgpt/instructions.md",
    "gemini-gem": ROOT / "gemini/instructions.md",
    "gemini-cli": ROOT / "gemini-cli/skills/phylocrates/instructions.md",
}

PROTOCOL_CHAIN = (
    "Observation/Problem → Question → Assumptions → Alternatives → "
    "Predictions → Discriminating expectations → Scope of claim → "
    "Refined hypothesis set"
)

MUST_NOT_METHODS = ["PIC", "PGLS", "PGLMM", "BM", "OU", "Mk", "ASR", "BiSSE", "HiSSE", "BAMM"]

texts = {}
for platform, path in INSTRUCTION_SOURCES.items():
    if not path.exists():
        check(f"instructions.md exists: {platform}", False, str(path))
        continue
    texts[platform] = path.read_text()
    check(f"instructions.md exists: {platform}", True)

for platform, text in texts.items():
    check(f"protocol chain present verbatim: {platform}", PROTOCOL_CHAIN in text,
          "protocol chain string not found or drifted")

for platform, text in texts.items():
    missing_methods = [m for m in MUST_NOT_METHODS if m not in text]
    check(f"all named out-of-scope methods listed: {platform}", not missing_methods,
          f"missing from MUST-NOT list: {missing_methods}")

# cross-platform diff: normalize whitespace and compare the core instruction
# bodies aren't expected to be byte-identical (chatgpt/gemini wrappers are
# adapted), but the protocol chain and MUST-NOT method list ARE expected to
# be identical strings, which the checks above already enforce per-file.
# Additionally assert claude-code and gemini-cli are byte-identical, since
# gemini-cli's skill tree is documented as a straight copy of skills/.
if "claude-code" in texts and "gemini-cli" in texts:
    check("claude-code and gemini-cli instructions.md are identical (documented as a straight copy)",
          texts["claude-code"] == texts["gemini-cli"],
          "gemini-cli/skills/phylocrates/instructions.md has drifted from skills/phylocrates/instructions.md")

# ---------------------------------------------------------------------------
# INTEGRATION: gemini-cli/skills/phylocrates is a complete mirror of
# skills/phylocrates (every file present, byte-identical)
# ---------------------------------------------------------------------------
src_dir = ROOT / "skills/phylocrates"
mirror_dir = ROOT / "gemini-cli/skills/phylocrates"
if src_dir.exists() and mirror_dir.exists():
    src_files = {p.relative_to(src_dir) for p in src_dir.rglob("*") if p.is_file() and p.name != ".DS_Store"}
    mirror_files = {p.relative_to(mirror_dir) for p in mirror_dir.rglob("*") if p.is_file() and p.name != ".DS_Store"}
    missing_in_mirror = src_files - mirror_files
    extra_in_mirror = mirror_files - src_files
    check("gemini-cli skill mirror has every file skills/phylocrates has", not missing_in_mirror,
          f"missing: {missing_in_mirror}")
    check("gemini-cli skill mirror has no extra files", not extra_in_mirror,
          f"extra: {extra_in_mirror}")
    mismatched = []
    for rel in src_files & mirror_files:
        if (src_dir / rel).read_bytes() != (mirror_dir / rel).read_bytes():
            mismatched.append(str(rel))
    check("gemini-cli skill mirror files are byte-identical to skills/phylocrates", not mismatched,
          f"mismatched: {mismatched}")
else:
    check("both skills/phylocrates and gemini-cli/skills/phylocrates exist", False,
          f"src exists={src_dir.exists()} mirror exists={mirror_dir.exists()}")

# ---------------------------------------------------------------------------
# INTEGRATION: canonical reference files that ship identically to every
# platform (spec, schema, worked example) haven't drifted between copies
# ---------------------------------------------------------------------------
SHARED_FILES = {
    "PHYLOCRATES_SPEC.md": {
        "claude-code": ROOT / "skills/phylocrates/PHYLOCRATES_SPEC.md",
        "chatgpt": ROOT / "chatgpt/knowledge/PHYLOCRATES_SPEC.md",
        "gemini-gem": ROOT / "gemini/knowledge/PHYLOCRATES_SPEC.md",
        "gemini-cli": ROOT / "gemini-cli/skills/phylocrates/PHYLOCRATES_SPEC.md",
    },
    "hypothesis-record.schema.json": {
        "claude-code": ROOT / "skills/phylocrates/output/hypothesis-record.schema.json",
        "chatgpt": ROOT / "chatgpt/knowledge/hypothesis-record.schema.json",
        "gemini-gem": ROOT / "gemini/knowledge/hypothesis-record.schema.json",
        "gemini-cli": ROOT / "gemini-cli/skills/phylocrates/output/hypothesis-record.schema.json",
    },
    "example-record.yaml": {
        "claude-code": ROOT / "skills/phylocrates/output/example-record.yaml",
        "chatgpt": ROOT / "chatgpt/knowledge/example-record.yaml",
        "gemini-gem": ROOT / "gemini/knowledge/example-record.yaml",
        "gemini-cli": ROOT / "gemini-cli/skills/phylocrates/output/example-record.yaml",
    },
}
for name, platforms in SHARED_FILES.items():
    existing = {p: path for p, path in platforms.items() if path.exists()}
    missing = set(platforms) - set(existing)
    check(f"{name} present in all four platform packages", not missing, f"missing from: {missing}")
    if len(existing) > 1:
        reference_platform, reference_path = next(iter(existing.items()))
        reference_bytes = reference_path.read_bytes()
        drifted = [p for p, path in existing.items()
                   if path.read_bytes() != reference_bytes and p != reference_platform]
        check(f"{name} is byte-identical across all platform copies", not drifted,
              f"drifted from {reference_platform}: {drifted}")

# ---------------------------------------------------------------------------
# INTEGRATION: every relative markdown link in every .md file resolves to
# a real file on disk (catches broken cross-references after edits)
# ---------------------------------------------------------------------------
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
md_files = sorted(ROOT.rglob("*.md"))
for f in md_files:
    text = f.read_text()
    for link in LINK_RE.findall(text):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = (f.parent / link).resolve()
        check(f"link resolves: {f.relative_to(ROOT)} -> {link}", target.exists(), f"{target} does not exist")

# ---------------------------------------------------------------------------
# UNIT: MANIFEST.txt matches the actual file tree (no stale/missing entries)
# ---------------------------------------------------------------------------
manifest_path = ROOT / "skills/phylocrates/MANIFEST.txt"
if manifest_path.exists():
    manifest_dir = manifest_path.parent
    listed = set(manifest_path.read_text().splitlines())
    actual = {
        str(p.relative_to(manifest_dir))
        for p in manifest_dir.rglob("*")
        if p.is_file() and p.name not in ("MANIFEST.txt", ".DS_Store")
    }
    check("MANIFEST.txt has no stale entries (files it lists that don't exist)",
          not (listed - actual), f"stale: {listed - actual}")
    check("MANIFEST.txt has no missing entries (files that exist but aren't listed)",
          not (actual - listed), f"missing: {actual - listed}")
else:
    check("skills/phylocrates/MANIFEST.txt exists", False, str(manifest_path))

# ---------------------------------------------------------------------------
# UNIT: no .DS_Store or other OS-cruft files shipped in the package
# ---------------------------------------------------------------------------
cruft = [p for p in ROOT.rglob(".DS_Store")]
check("no .DS_Store files in the repo", not cruft, f"found: {cruft}")

# ---------------------------------------------------------------------------
# UNIT: ChatGPT instructions.md stays under the Custom GPT 8,000 char limit
# ---------------------------------------------------------------------------
for platform in ("chatgpt", "gemini-gem"):
    if platform in texts:
        n = len(texts[platform])
        check(f"{platform} instructions.md under char budget (8000)", n <= 8000, f"{n} chars")

print()
print(f"{checks_run} checks run, {len(failures)} failed.")
if failures:
    print("\nFAILURES:")
    for f in failures:
        print(f" - {f}")
    sys.exit(1)
else:
    print("ALL GATES GREEN.")
    sys.exit(0)
