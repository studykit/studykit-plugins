---
name: audit
description: 'On demand, audit the last completed turn for evidence grounding — guard dispatches the guardian subagent to check that turn''s technical claims against the repository. Use when you want a specific turn verified instead of guard auto-auditing every turn. Claude Code only.'
argument-hint: ''
disable-model-invocation: true
---

This command is handled by a guard hook, which fires the moment you type
`/guard:audit` and targets the last completed turn. It has already run. The hook emits
a `<system-reminder>` carrying the guardian dispatch inputs (session_id, prompt_id,
turn_file, verified_file, dispatcher).

**Follow that dispatch instruction:** dispatch the `guard:guardian` subagent with the
Agent tool exactly as the reminder specifies, then relay its verdict — if it reports
violations, address them; otherwise state that the turn passed.

If the reminder instead says there is nothing to verify (no completed turn yet), relay
that in one line and take no further action.

Do not read guard's state files or investigate how the pending turn is tracked — the
hook has already selected the turn; your only job is to dispatch the guardian when the
reminder asks for it.
