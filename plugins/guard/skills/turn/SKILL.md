---
name: turn
description: 'Turn guard on or off for the current session (evidence judge + approval gate). Claude Code only.'
argument-hint: '[on|off]'
disable-model-invocation: true
---

This command is handled entirely by guard's `toggle` hook, which fires the moment you
type `/guard:turn` and flips the session's `enabled` flag on its own. It has already
run. **Take no action.** Do not read files, run commands, edit state, or investigate
how the flag is stored — there is nothing for you to do. A `<system-reminder>` from the
hook reports whether guard is now on or off; simply relay that to the user in one line
(or say nothing further).
