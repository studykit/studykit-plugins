---
description: Start the claude-web-console local web UI and open it in the browser
allowed-tools: Bash
---

Start the **claude-web-console** viewer for this session.

Launch the long-running server in the background (do not block the session) by
running the launcher, then report the URL it prints:

```bash
uv run "${CLAUDE_PLUGIN_ROOT}/server/launcher.py"
```

If `${CLAUDE_PLUGIN_ROOT}` is not expanded in this context, resolve the launcher
path yourself: it is `server/launcher.py` inside this plugin
(`claude-web-console`) under the installed marketplace directory.

Guidance:

- The viewer serves at `http://127.0.0.1:8477/` by default (or the port in
  `$CLAUDE_WEB_CONSOLE_PORT`). Report the exact URL from the launcher output.
- If a server is already running on that port, do **not** start a second copy —
  just report the URL.
- PlantUML diagrams need a Java runtime and a `plantuml.jar`; without them,
  Markdown and math still render and diagrams show an "engine unavailable"
  placeholder.
- Once running, the plugin's hooks mirror this conversation into the page live.
