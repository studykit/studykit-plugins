---
name: turn
description: 'Turn guard on or off for the current session (evidence judge + approval gate), or with --project set the session-start default. Claude Code only.'
argument-hint: '[--project] [on|off]'
disable-model-invocation: true
---

This command is handled entirely by guard's `toggle` hook, which fires the moment you
type `/guard:turn` and flips the session's `enabled` flag (or, with `--project`, writes
the session-start default to `.claude/guard.local.json`) on its own. It has already run.
**Take no action.** Do not read files, run commands, edit state, or investigate how the
flag is stored — there is nothing for you to do. A `<system-reminder>` from the hook
reports the result; simply relay that to the user in one line (or say nothing further).
