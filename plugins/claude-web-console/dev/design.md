# claude-web-console — design & open questions

See `../AGENTS.md` for the architecture overview and the grounded
MessageDisplay / PlantUML contracts.

## Grounded references (evidence)

- MessageDisplay hook payload + cadence:
  `.claude/guard/refs/messagedisplay-hook.md`
  (https://code.claude.com/docs/en/hooks#messagedisplay).
- PlantUML PicoWeb start command + URL path:
  `.claude/guard/refs/plantuml-picoweb.md` (https://plantuml.com/picoweb).

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

## v1 limitations

- Browser libs load from CDN (esm.sh / jsdelivr); offline vendoring is a
  follow-up. Conversation text never leaves the machine.
- Read-only viewer; bidirectional input (web → Claude Code) is deferred.
