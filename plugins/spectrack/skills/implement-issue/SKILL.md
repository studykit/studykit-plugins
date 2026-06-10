---
name: implement-issue
description: "Execute the plan recorded in a workflow `task`, `bug`, or `spike` issue: validate the recorded diagnosis with `resolution-auditor` first, then dispatch `issue-implementer` (which adopts the issue body's plan, or a plan-mode refresh you pass in), then `implementation-auditor` to verify the result. This skill dispatches and passes the reports through."
argument-hint: "<issue-ref> [additional requirements]"
disable-model-invocation: true
allowed-tools:
  - Agent
---

# Implement

Dispatcher for executing an issue's approved plan. The plan of record is
the issue body's `Approach` / `Affected Paths` / `Acceptance Criteria`,
authored in plan mode when the task was created. This skill does not
plan; it first sends the issue to `resolution-auditor` (which checks the
recorded root cause and approach against the current code, read-only),
then hands the issue — and, when you refreshed the plan in plan mode, the
refreshed plan — to `issue-implementer` (which adopts the plan, executes
it in an isolated worktree, and pushes a topic branch), then to
`implementation-auditor` (which cross-checks the result, read-only). The
skill owns dispatch only — the agents' bodies are the source of truth
for what they do and which states they return.

## Flow

1. **Parse the issue ref.** Take the first `$ARGUMENTS` token as the
   issue ref. If there is no recognizable ref, abort with `Usage:
   <issue-ref> [additional requirements]`. Everything past the ref is
   extra requirements, forwarded verbatim.

2. **Validate the recorded diagnosis** before any implementation. Call
   `Agent` with `subagent_type: spectrack:resolution-auditor`, naming the
   published issue ref (published mode). It checks the recorded root cause
   and approach against the current code read-only, appends a single
   verdict comment to the issue, and returns a `<report>` with a
   `verdict`. Then gate on the verdict:

   - `wrong-cause` or `ineffective-approach` — the recorded diagnosis is
     broken; building on it would waste an implementation cycle. Surface
     the auditor's `<report>` and comment to the user and ask whether to
     replan (in plan mode) or proceed anyway. Do not dispatch the
     implementer until the user decides.
   - `weak-diagnosis` — surface it as a caution but continue.
   - `ok` or `unverifiable` — continue.

   Skip this step for `spike` issues — a spike records a question to
   answer, not a cause/fix for the auditor to validate.

3. **Settle the plan.** The plan of record is the issue body's
   `Approach` / `Affected Paths` / `Acceptance Criteria`. Normally pass
   nothing extra — the implementer adopts the body's plan and checks it
   against the current code itself, reporting `paused` with what drifted
   and a suggested direction if it has. Converge a refreshed plan with
   the user in plan mode and carry it forward as an override only when
   you already know the body plan needs sharpening, or in response to a
   prior `paused`-for-drift report.

4. **Dispatch `issue-implementer`.** Call `Agent` with `subagent_type:
   spectrack:issue-implementer`, passing the issue ref, the extra
   requirements verbatim, and — only when you refreshed the plan in
   step 3 — the refreshed plan as an override. It executes in its own
   isolated worktree and returns a `<report>` whose `state` is
   `implemented`, `paused`, or `failed`.

5. **Dispatch `implementation-auditor`** only when the implementer's
   `state` is `implemented` — `paused` and `failed` leave no pushed
   branch to audit. Call `Agent` with `subagent_type:
   spectrack:implementation-auditor`, passing `issue-ref` (the same ref)
   and `report` (the implementer's `<report>` block, inline). It is
   read-only and returns a `<report>` with a `verdict`.

6. **Pass through.** Emit the implementer's `<report>`; when the audit
   ran, emit the auditor's `<report>` directly after. The skill adds
   nothing on top.

$ARGUMENTS
