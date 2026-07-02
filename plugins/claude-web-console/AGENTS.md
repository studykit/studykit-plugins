# claude-web-console — contributor notes

Claude Code plugin that mirrors the live conversation (user prompts + assistant
text) into a **local web UI** and renders **renderable fenced code blocks** (PlantUML,
math) as rich output. **Claude Code only** — it depends on the `MessageDisplay` hook,
which has no Codex equivalent. There is intentionally no `.codex-plugin/` manifest and
no Codex marketplace registration.

Shape: short-lived stdlib-Python hooks (`hooks/`) POST conversation events to a
long-running stdlib server (`server/server.py`) started by the `/web-console` command;
the server broadcasts them over SSE to the browser viewer (`server/static/`), whose
markdown-it `fence` rule is the renderer registry. The source is the truth for control
flow.

## Deeper detail

**`dev/design.md`** (not auto-loaded) holds the architecture diagram, the grounded
external contracts (the `MessageDisplay` hook payload/cadence and the PlantUML PicoWeb
bridge, each cited to a saved ref), the env configuration, the vendored-frontend notes,
and the tracked open questions. **`dev/vendor.md`** holds the browser-library rebuild /
version-bump procedure. **`dev/transcript-schema.md`** holds the reverse-engineered
schema of Claude Code's stored session transcripts (`~/.claude/projects/*/*.jsonl`),
for the session-management workstream (browse / render stored sessions).
