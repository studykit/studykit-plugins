# claude-web-console — contributor & runtime notes

Claude Code plugin that mirrors the live conversation (user prompts + assistant
text) into a **local web UI** and renders **renderable fenced code blocks** as
rich output. **Claude Code only** — it depends on the `MessageDisplay` hook,
which has no Codex equivalent. There is intentionally no `.codex-plugin/` manifest
and no Codex marketplace registration.

## How it fits together

```
Claude Code session
  │  hooks (short-lived, stdlib Python, silent no-op if server down)
  ├─ UserPromptSubmit  → POST /event  {type:"user", ...}
  ├─ MessageDisplay    → POST /event  {type:"assistant_delta", message_id, index, final, delta}
  └─ Stop              → POST /event  {type:"turn_end"}
        │  HTTP POST to 127.0.0.1:$CLAUDE_WEB_CONSOLE_PORT
        ▼
  server/server.py  (stdlib http.server, long-running, started by the /web-console command)
        ├─ POST /event      accept + broadcast to SSE clients, keep history for replay
        ├─ GET  /events      Server-Sent Events stream (text → browser)
        ├─ GET  /config.json  { plantumlServer }
        └─ GET  /  + static   the viewer
        ▼
  server/static/  (markdown-it in the browser; fence rule IS the renderer registry)
        ├─ ```plantuml``` → <img> at the local PlantUML PicoWeb server
        └─ ```math```/$$…$$ → KaTeX
```

## MessageDisplay contract (grounded)

Verbatim source and details: `.claude/guard/refs/messagedisplay-hook.md`
(from https://code.claude.com/docs/en/hooks#messagedisplay).

- Input carries: `turn_id`, `message_id` (stable across batches of one message),
  `index` (0-based batch index), `final` (true on the last batch), `delta` (the
  **newly completed lines** since the prior batch — incremental, not cumulative).
- Interactive: fires once per batch of newly completed lines. Non-interactive
  (`claude -p`, Agent SDK): once per message, `index=0`, `final=true`, `delta`=
  the whole message.
- The viewer accumulates `delta` per `message_id`, ordered by `index`, and treats
  `final` (not a non-empty delta) as end-of-message. Fenced blocks span multiple
  deltas, so a block only renders once its closing fence has arrived.

## PlantUML (grounded)

Source: `.claude/guard/refs/plantuml-picoweb.md` (https://plantuml.com/picoweb).

- Local render bridge: `java -jar <jar> -picoweb:<port>:127.0.0.1`.
- Request path: `http://127.0.0.1:<port>/plantuml/svg/{encoded}` (the `/plantuml`
  prefix is required). Rendering stays on the machine — no diagram text leaves it.
- java is optional. When java or a jar is missing, the launcher skips PicoWeb and
  the viewer shows an "engine unavailable" placeholder; markdown + math still work.
- The launcher reuses an existing jar via `CLAUDE_WEB_CONSOLE_PLANTUML_JAR`
  (defaults to probing `plugins/plantuml/skills/compose/scripts/plantuml*.jar`).

## Configuration (env)

- `CLAUDE_WEB_CONSOLE_PORT` — web server + hook POST port (default `8477`).
- `CLAUDE_WEB_CONSOLE_PLANTUML_PORT` — PicoWeb port (default `8478`).
- `CLAUDE_WEB_CONSOLE_PLANTUML_JAR` — path to plantuml.jar (default: probe repo).

## Frontend libraries (vendored)

- The viewer's browser libraries are vendored under `server/static/vendor/`, so
  the viewer never depends on a CDN staying reachable — a page load issues no
  external network requests. `markdown-it`, `markdown-it-texmath`, and
  `plantuml-encoder` are self-contained esbuild bundles (all transitive deps
  inlined); KaTeX ships as its official dist (`katex.mjs` + `katex.min.css` +
  `fonts/*.woff2`). `app.js` and `index.html` reference them by local `/vendor`
  path. Rebuild / version-bump procedure: `dev/vendor.md`.
- `.mjs` and `.woff2` must stay in `server.py`'s `CONTENT_TYPES`. Browsers refuse
  to execute an ES module served as `application/octet-stream`, so a missing
  `.mjs` mapping silently breaks the whole viewer (module never evaluates).

## Known v1 limitations (follow-ups)

- One-way viewer only. Bidirectional input (web UI → Claude Code) is deferred and
  unsolved — see the repo handover notes before building it.
- Renderer registry currently ships PlantUML + math; add types by extending the
  `fence` dispatch in `server/static/app.js`.
