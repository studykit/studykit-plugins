---
name: audit-korean
description: 'On demand, audit the last completed turn''s Korean for naturalness — guard dispatches the korean-auditor subagent to flag 번역체 phrasing and suggest what a Korean developer would write. A non-Korean response is never flagged. Claude Code only.'
argument-hint: ''
disable-model-invocation: true
---

This command is handled by a guard hook, which targets the last completed turn and
emits the dispatch inputs for the `korean-auditor` subagent.

**Follow that dispatch instruction:** dispatch `guard:korean-auditor` with the Agent
tool exactly as the reminder specifies, then relay its verdict — if it reports
violations, address them; otherwise state that the turn passed.

This checks Korean prose that reads as translated English (번역체), and nothing else.
For the other checks, run `/guard:audit-claims` and `/guard:audit-deferrals`.

Identifiers, paths, commands and established loanwords are left as they are — the
auditor never asks for a technical term to be translated.

If the reminder instead says there is nothing to audit (no completed turn yet), relay
that in one line and take no further action.

Do not read guard's state files or investigate how the pending turn is tracked — the
hook has already selected the turn; your only job is to dispatch the auditor when the
reminder asks for it.
