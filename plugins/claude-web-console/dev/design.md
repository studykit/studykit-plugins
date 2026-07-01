# claude-web-console — design detail

Deep reference for `claude-web-console` contributors. Not auto-loaded; open it when
working here. `../AGENTS.md` is the always-loaded map and points here. The source
(`hooks/`, `server/`) is the truth for control flow — this file records the
architecture, the grounded external contracts, config, and the open questions.

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

Source (official docs): https://code.claude.com/docs/en/hooks#messagedisplay — fetch
the `.md` raw endpoint (`https://code.claude.com/docs/en/hooks.md`) for the full
`### MessageDisplay` section; WebFetch summaries truncate it.

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

Source (official docs): https://plantuml.com/picoweb.

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

The viewer's browser libraries are vendored under `server/static/vendor/`, so a page
load issues no external network requests — the viewer never depends on a CDN staying
reachable. `markdown-it`, `markdown-it-texmath`, and `plantuml-encoder` are
self-contained esbuild bundles (all transitive deps inlined); KaTeX ships as its
official dist (`katex.mjs` + `katex.min.css` + `fonts/*.woff2`). `app.js` and
`index.html` reference them by local `/vendor` path.

The rebuild / version-bump procedure is in `vendor.md`. Serving gotcha: `.mjs` and
`.woff2` must stay in `server.py`'s `CONTENT_TYPES` — a browser refuses to execute an
ES module served as `application/octet-stream`, so a missing mapping silently breaks
the viewer (the comment on `CONTENT_TYPES` in `server/server.py` records the why).

## To verify against current official docs (do not assume)

- **`${CLAUDE_PLUGIN_ROOT}` expansion inside a command body.** It is confirmed to
  expand in hook `command` strings (see `hooks/hooks.json`, matching the `guard`
  plugin). Whether it expands the same way inside a slash-command markdown body
  is NOT verified here — `commands/web-console.md` is written defensively with a
  fallback. Confirm against the current Claude Code command docs before relying
  on it, and simplify the command once confirmed.

## Open question (tracked)

- **Drop the Stop hook, use MessageDisplay `final`?** The Stop hook currently
  emits a `turn_end` event that the viewer does not actually need (each message's
  last delta already rendered its fenced blocks, and `final: true` marks that
  message's end). `final` is a per-message end signal and is reliable even when
  the final delta is empty (message ends on a newline). Stop, by contrast, marks
  the whole-turn boundary (after any tool calls). If the viewer needs nothing at
  whole-turn granularity, the Stop hook can be removed and `final` used instead.
  Verify by testing once the basic path runs. If confirmed, drop `hooks/stop.py`
  and the `Stop` entry in `hooks/hooks.json`, and have the viewer key any
  finalize logic off `final`.

## v1 limitations / follow-ups

- One-way viewer only. Bidirectional input (web UI → Claude Code) is deferred and
  unsolved — see the repo handover notes before building it.
- Renderer registry currently ships PlantUML + math; add types by extending the
  `fence` dispatch in `server/static/app.js`.
