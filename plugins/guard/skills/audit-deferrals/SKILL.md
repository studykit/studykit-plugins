---
name: audit-deferrals
description: 'On demand, audit the last completed turn for unjustified deferrals — guard dispatches the deferrals-auditor subagent to find questions punted as "TBD" / "확인 필요" that the repository can answer. Use when an answer left too much open. Claude Code only.'
argument-hint: ''
disable-model-invocation: true
---

This command is handled by a guard hook, which targets the last completed turn and
emits the dispatch inputs for the `deferrals-auditor` subagent.

**Follow that dispatch instruction:** dispatch `guard:deferrals-auditor` with the Agent
tool exactly as the reminder specifies, then relay its verdict — if it reports
violations, address them; otherwise state that the turn passed.

This checks work punted that the repository could have answered, and nothing else. For
the other checks, run `/guard:audit-claims` and `/guard:audit-korean`.

If the reminder instead says there is nothing to audit (no completed turn yet), relay
that in one line and take no further action.

Do not read guard's state files or investigate how the pending turn is tracked — the
hook has already selected the turn; your only job is to dispatch the auditor when the
reminder asks for it.
