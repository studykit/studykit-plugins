---
name: implement-issue
description: "Hand an approved plan for a workflow `task`, `bug`, or `spike` issue to `issue-implementer` for execution, then `implementation-auditor` to verify the result. Converge the plan in plan mode first; this skill dispatches and passes the reports through."
argument-hint: "<issue-ref> [additional requirements]"
disable-model-invocation: true
allowed-tools:
  - Agent
---

# Implement

Dispatcher for executing an **already-approved plan**. Converge the plan
with the user in plan mode *before* running this skill — the skill does
not plan. It hands the approved plan to `issue-implementer` (which
executes it in an isolated worktree and pushes a topic branch), then to
`implementation-auditor` (which cross-checks the result, read-only). The
skill owns dispatch only — the agents' bodies are the source of truth
for what they do and which states they return.

## Flow

1. **Parse the issue ref.** Take the first `$ARGUMENTS` token as the
   issue ref. If there is no recognizable ref, abort with `Usage:
   <issue-ref> [additional requirements]`. Everything past the ref is
   extra requirements, forwarded verbatim.

2. **Capture the approved plan.** Use the plan just converged with the
   user in this session's plan mode — the approach, the files to touch,
   the per-Acceptance-Criterion verification, and the commit split. If
   no plan has been agreed in the conversation, stop and tell the user
   to plan first (enter plan mode, converge a plan, approve), then
   re-run the skill.

3. **Dispatch `issue-implementer`.** Call `Agent` with `subagent_type:
   workflow:issue-implementer`, passing the issue ref, the approved plan
   (inline), and the extra requirements verbatim. It executes in its own
   isolated worktree and returns a `<report>` whose `state` is
   `implemented`, `paused`, or `failed`.

4. **Dispatch `implementation-auditor`** only when the implementer's
   `state` is `implemented` — `paused` and `failed` leave no pushed
   branch to audit. Call `Agent` with `subagent_type:
   workflow:implementation-auditor`, passing `issue-ref` (the same ref)
   and `report` (the implementer's `<report>` block, inline). It is
   read-only and returns a `<report>` with a `verdict`.

5. **Pass through.** Emit the implementer's `<report>`; when the audit
   ran, emit the auditor's `<report>` directly after. The skill adds
   nothing on top.

$ARGUMENTS
