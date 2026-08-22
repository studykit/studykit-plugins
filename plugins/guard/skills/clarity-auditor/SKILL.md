---
name: clarity-auditor
description: 'On demand, audit the last completed turn for whether its reader can follow it — guard dispatches the clarity-auditor subagent to check for terms used but never explained, mechanisms given with no concrete example, and explanation pitched wrong for what this reader already knows. Use when an answer was hard to follow. Claude Code only.'
argument-hint: ''
disable-model-invocation: true
---

This command is handled by a guard hook, which targets the last completed turn and
emits the dispatch inputs for the `clarity-auditor` subagent.

**Follow that dispatch instruction:** dispatch `guard:clarity-auditor` with the Agent
tool exactly as the reminder specifies, then relay its verdict — if it reports findings,
apply them to the answer file; otherwise state that the turn passed.

If its report says the reader profile is MISSING, say so in one line and mention
`/guard:reader-profile`. It audits at reduced coverage without one: it still checks for
missing examples and for terms the answer itself leaves undefined, but it cannot judge
whether an explanation was pitched right for you.

This checks comprehensibility and nothing else — not whether the answer is true, which is
`/guard:claims-auditor`, and not how the Korean reads, which is `/guard:korean-corrector`.

If the reminder instead says there is nothing to audit (no completed turn yet), relay
that in one line and take no further action.

Do not read guard's state files or investigate how the pending turn is tracked — the
hook has already selected the turn; your only job is to dispatch the auditor when the
reminder asks for it.
