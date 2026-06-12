---
name: implement-issue
description: "Execute the plan recorded in a workflow `task`, `bug`, or `spike` issue, assuming its recorded diagnosis was already validated (`resolution-auditor` returned `ok`) at authoring time: dispatch `issue-implementer` (which adopts the issue body's plan, or a plan-mode refresh you pass in), then `implementation-auditor` to verify the result. This skill dispatches and passes the reports through."
argument-hint: "<issue-ref> [additional requirements]"
disable-model-invocation: true
model: opus
allowed-tools:
  - Agent
---

# Implement

Dispatcher for executing an issue's approved plan. The plan of record is
the issue body's `Design Decision` / `Implementation Steps` /
`Acceptance Criteria` / `Verification`, authored in plan mode when the
task was created and validated by `resolution-auditor` (converged to `ok`)
before the issue was published. This skill **assumes that validation
already passed** — it does not re-audit the diagnosis. It hands the issue
— and, when you refreshed the plan in plan mode, the refreshed plan — to
`issue-implementer` (which adopts the plan, executes it in an isolated
worktree, and pushes a topic branch), then to `implementation-auditor`
(which cross-checks the result, read-only). The skill owns dispatch only —
the agents' bodies are the source of truth for what they do and which
states they return.

## Flow

1. **Parse the issue ref.** Take the first `$ARGUMENTS` token as the
   issue ref. If there is no recognizable ref, abort with `Usage:
   <issue-ref> [additional requirements]`. Everything past the ref is
   extra requirements, forwarded verbatim.

2. **Settle the plan.** The plan of record is the issue body's
   `Design Decision` / `Implementation Steps` / `Acceptance Criteria` /
   `Verification`, assumed already OK'd at authoring time. Normally pass
   nothing extra — the implementer adopts the body's plan and checks it
   against the current code itself, reporting `paused` with what drifted
   and a suggested direction if it has. Converge a refreshed plan with
   the user in plan mode and carry it forward as an override only when
   you already know the body plan needs sharpening, or in response to a
   prior `paused`-for-drift report.

3. **Dispatch `issue-implementer`.** Call `Agent` with `subagent_type:
   spectrack:issue-implementer` **and `isolation: "worktree"`** —
   the agent's frontmatter does not request isolation itself; this
   call-time parameter is what provisions the isolated worktree.
   Omitted, the agent would run in-place in the calling session's
   checkout — this skill always dispatches worktree mode. Pass the
   issue ref, the extra requirements verbatim, and — only when you
   refreshed the plan in step 2 — the refreshed plan as an override.
   It returns a `<report>` whose `state` is `implemented`, `paused`,
   or `failed`.

4. **Dispatch `implementation-auditor`** only when the implementer's
   `state` is `implemented` — `paused` and `failed` leave no pushed
   branch to audit. Call `Agent` with `subagent_type:
   spectrack:implementation-auditor`, passing `issue-ref` (the same ref)
   and `report` (the implementer's `<report>` block, inline). It is
   read-only and returns a `<report>` with a `verdict`.

5. **Pass through.** Emit the implementer's `<report>`; when the audit
   ran, emit the auditor's `<report>` directly after. The skill adds
   nothing on top.

$ARGUMENTS
