---
name: audit-claims
description: 'On demand, audit the last completed turn for unsupported claims — guard dispatches the claims-auditor subagent to check that turn''s load-bearing claims against the repository. Use when you want a turn''s factual claims verified. Claude Code only.'
argument-hint: ''
disable-model-invocation: true
---

This command is handled by a guard hook, which targets the last completed turn and
emits the dispatch inputs for the `claims-auditor` subagent.

**Follow that dispatch instruction:** dispatch `guard:claims-auditor` with the Agent
tool exactly as the reminder specifies, then relay its verdict — if it reports
violations, address them; otherwise state that the turn passed.

This checks claims asserted without adequate evidence and nothing else. For the other
checks, run `/guard:audit-deferrals` and `/guard:correct-korean`.

The auditor records the turn's confirmed claims as verified facts on a pass, so later
turns can reuse them without re-deriving.

If the reminder instead says there is nothing to audit (no completed turn yet), relay
that in one line and take no further action.

Do not read guard's state files or investigate how the pending turn is tracked — the
hook has already selected the turn; your only job is to dispatch the auditor when the
reminder asks for it.
