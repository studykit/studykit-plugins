---
name: mode
description: 'Set how guard judges evidence this session — headless (in-hook judge that blocks) or subagent (dispatch the guardian subagent) — or with --project set the session-start default. Claude Code only.'
argument-hint: '[--project] [headless|subagent]'
disable-model-invocation: true
---

This command is handled entirely by guard's `set-mode` hook, which fires the moment
you type `/guard:mode` and switches the session's evidence-judge mode (or, with
`--project`, writes the session-start default to `.claude/guard.local.json`) on its own.
It has already run. **Take no action.** Do not read files, run commands, edit state, or
investigate how the mode is stored — there is nothing for you to do. A
`<system-reminder>` from the hook reports the result; simply relay that to the user in
one line (or say nothing further).
