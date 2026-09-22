# PhyloCrates for Gemini (Gems)

Gemini has no plugin-folder mechanism either — a Gem is instructions + uploaded knowledge files, set up by hand in the app.

1. Gemini app → **Explore Gems → New Gem**.
2. Paste [`instructions.md`](instructions.md) into the **Instructions** field. It's 7,200 characters — well past Google's 500–2,000 char *recommendation*, but there's no hard published limit; the full spec is kept intact to match the Claude Code and ChatGPT versions behaviorally. If Gemini feels sluggish or forgets earlier turns in long chats, that's the shared context-window cost of a long instruction + knowledge files — trim `instructions.md` first if it becomes a problem.
3. Under **Knowledge**, add every file in [`knowledge/`](knowledge) (flat — same 16 files as the ChatGPT package; check the Gem editor for its current file-count cap, since Google doesn't publish a fixed number).
4. Save. No other tools needed.

Same v0.6 behavior as the Claude Code skill and the ChatGPT Custom GPT: Socratic hypothesis refinement, hard stop before method/study-design choices.
