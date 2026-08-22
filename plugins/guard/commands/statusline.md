---
name: statusline
description: 'Add guard''s audit indicator to the status line, or show how. Wires `guard_hook.py status` into the user''s existing status line so whether audits are on for this session is visible without asking. Use when the user wants the guard segment shown, or when it stopped appearing. Claude Code only.'
argument-hint: ''
disable-model-invocation: true
---

guard cannot install a status line itself — a plugin's `settings.json` honors only `agent`
and `subagentStatusLine`, and the main `statusLine` is a user or project setting. So this
adds a **segment** to whatever status line the user already runs.

**This writes the user's own settings file.** Show the exact change and get explicit
agreement before touching it. A direct "add it" counts.

## 1. Find the pieces

- guard's script: resolve the absolute path to `scripts/guard_hook.py` in this plugin. Do not
  use `${CLAUDE_PLUGIN_ROOT}` — that is set for hooks, not for a status-line command.
- the current setting: read `statusLine` from `~/.claude/settings.json`, then from
  `.claude/settings.json` and `.claude/settings.local.json` if the user setting is absent.
  Say which file you found it in; that is the one to change.

Check the segment works before proposing anything:

```sh
printf '{"session_id":"probe","workspace":{"project_dir":"<project root>"}}' | "<guard>/scripts/guard_hook.py" status
```

Expect one short field (`guard 3`, `guard off`, or `guard ·`) or nothing. If it prints
nothing for a project with agents switched on, stop and say so rather than wiring up a
segment that will stay blank.

## 2. Propose the change

**If there is no status line yet**, the whole setting is guard's segment:

```json
{
  "statusLine": {
    "type": "command",
    "command": "\"<guard>/scripts/guard_hook.py\" status"
  }
}
```

**If one already exists, wrap it — never replace it.** The catch is that stdin can be read
only once, so the wrapper captures the JSON and feeds the same text to both commands. Write
this to `~/.claude/statusline-with-guard.sh`, `chmod +x` it, and point `command` at it:

```sh
#!/bin/sh
# Renders the existing status line with guard's audit indicator in front of it.
JSON=$(cat)
GUARD=$(printf '%s' "$JSON" | "<guard>/scripts/guard_hook.py" status 2>/dev/null)
MINE=$(printf '%s' "$JSON" | <the existing command> 2>/dev/null)
[ -n "$GUARD" ] && printf '%s | ' "$GUARD"
printf '%s' "$MINE"
```

Keep every other field of the existing `statusLine` object (`padding`, `refreshInterval`)
as it was.

**If guard's segment is already wired**, say so and change nothing.

## 3. Afterwards

Tell the user two things and stop:

- The segment reads three states: `guard N` (N agents armed), `guard off` (muted for this
  session with `/guard:toggle`), `guard ·` (installed, nothing switched on for this project).
- If it ever goes blank, the plugin path moved — a plugin update can relocate the install
  directory — and re-running this command fixes it. Blank is deliberate: the segment prints
  nothing rather than an error, because a status line is the wrong place to report a failure.
