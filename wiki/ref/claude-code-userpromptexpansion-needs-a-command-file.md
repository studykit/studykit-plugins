# A `UserPromptExpansion` matcher does nothing without a command/skill file of that name

Source: probe of `claude` 2.1.241 (the docs state this nowhere)
Retrieved: 2026-08-23
Local path: `wiki/ref/claude-code-userpromptexpansion-needs-a-command-file.md`

A `UserPromptExpansion` hook is registered by *matcher*, so it reads as though the matcher
itself creates the command. It does not. The host resolves `/name` against the
skill/command files first; a name with no file is rejected before any hook runs.

## Result

| Typed | `skills/<name>/SKILL.md` present | Outcome |
| --- | --- | --- |
| `/tp4:real` | yes | skill body ran; hook **fired** (`REAL_HOOK_FIRED` logged) |
| `/tp4:ghost` | no | `Unknown command: /tp4:ghost`; hook **did not fire** (log unchanged) |

So deleting a command file silently disarms its matcher. Nothing reports the orphan: the
hook stays in `hooks.json`, `/plugin` still lists the plugin, and the only symptom is
`Unknown command` when someone types the name.

## The probe

Throwaway plugin `tp4` under `--plugin-dir` with **two** matchers and **one** skill:

`hooks/hooks.json`

```json
{
  "hooks": {
    "UserPromptExpansion": [
      { "matcher": "^(tp4:)?ghost$",
        "hooks": [{ "type": "command",
                    "command": "echo GHOST_HOOK_FIRED >> \"$PROBE_LOG\"; echo 'ghost hook context here'",
                    "timeout": 5 }] },
      { "matcher": "^(tp4:)?real$",
        "hooks": [{ "type": "command",
                    "command": "echo REAL_HOOK_FIRED >> \"$PROBE_LOG\"; echo 'real hook context here'",
                    "timeout": 5 }] }
    ]
  }
}
```

`skills/real/SKILL.md` exists (`disable-model-invocation: true`, body `Say REAL_BODY_RAN.`).
There is no `ghost` skill and no `commands/ghost.md`.

Run, once per name, with the log emptied first:

```bash
claude -p --plugin-dir "$SP/tp4" --permission-mode bypassPermissions "/tp4:real"
claude -p --plugin-dir "$SP/tp4" --permission-mode bypassPermissions "/tp4:ghost"
```

`/tp4:real` printed `REAL_BODY_RAN` and appended `REAL_HOOK_FIRED`. `/tp4:ghost` printed
`Unknown command: /tp4:ghost` and appended nothing — the log held only the `real` line
afterwards.

## Relation to the other invocation probe

`wiki/ref/claude-code-skill-invocation-paths.md` establishes that
`UserPromptExpansion` fires when the **user types** `/name` and not when the model calls the
`Skill` tool. This adds the other precondition: the typed name must resolve to a file. Both
together mean a matcher is reachable only through a user-typed command that exists.

## Not covered here

Whether a matcher can attach to a **built-in** command name, and whether a matcher for a name
supplied by a *different* plugin fires. Both would need their own runs.
