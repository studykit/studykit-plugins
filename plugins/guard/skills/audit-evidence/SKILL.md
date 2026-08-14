---
name: audit-evidence
description: 'On demand, audit the last completed turn for evidence grounding — guard dispatches the evidence-auditor subagent to check that turn''s claims against the repository. In Codex, run guard:setup first to install the named auditor. Use when you want a specific turn verified instead of guard auto-auditing every turn.'
argument-hint: ''
disable-model-invocation: true
---

This command is handled by a guard hook, which targets the last completed turn.
The hook emits the evidence-auditor dispatch inputs (session_id, prompt_id,
turn_file, verified_file, dispatcher).

In Codex, run `$guard:setup` once per project first. It installs the project-local
`guard_evidence_auditor` named agent. Dispatch that named agent read-only with the
turn file supplied by the hook.

**Follow that dispatch instruction:** dispatch the requested evidence-auditor subagent with the
Agent tool exactly as the reminder specifies, then relay its verdict — if it reports
violations, address them; otherwise state that the turn passed.

If the reminder instead says there is nothing to verify (no completed turn yet), relay
that in one line and take no further action.

Do not read guard's state files or investigate how the pending turn is tracked — the
hook has already selected the turn; your only job is to dispatch the evidence auditor when the
reminder asks for it.
