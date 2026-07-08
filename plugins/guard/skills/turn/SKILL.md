---
name: turn
description: 'Turn guard''s approval gate on or off for the current session (the gate that blocks file edits until you approve), or with --project set the session-start default. The evidence judge is controlled separately with /guard:audit-mode. Claude Code only.'
argument-hint: '[--project] [on|off]'
disable-model-invocation: true
---

This command is handled entirely by guard's `toggle` hook, which fires the moment you
type `/guard:turn` and flips the session's `edit_gate` flag (or, with `--project`,
writes the session-start default to `.claude/guard.local.json`) on its own. It has
already run. **Take no action.** Do not read files, run commands, edit state, or
investigate how the flag is stored — there is nothing for you to do. A
`<system-reminder>` from the hook reports the result; simply relay that to the user in
one line (or say nothing further).
