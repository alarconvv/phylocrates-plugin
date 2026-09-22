# PhyloCrates for ChatGPT

Custom GPTs don't run plugin folders like Claude Code does — this is instructions + knowledge files, set up by hand.

1. ChatGPT → **Explore GPTs → Create** (or an existing Project's instructions + files).
2. Paste [`instructions.md`](instructions.md) into the **Instructions** field (7,200 chars, fits the 8,000-char limit).
3. Under **Knowledge**, upload every file in [`knowledge/`](knowledge) (flat — Custom GPT knowledge has no folders, filenames are how the instructions refer to them).
4. Leave Code Interpreter/Browsing off; PhyloCrates needs neither. File search/retrieval must be on (default when knowledge files are attached).

Same v0.6 behavior as the Claude Code skill: Socratic hypothesis refinement, hard stop before method/study-design choices.
