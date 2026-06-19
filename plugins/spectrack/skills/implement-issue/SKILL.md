---
name: implement-issue
description: "Implement a workflow `task`, `bug`, or `spike` issue from its spec. Use when the user gives an issue ref and wants the work implemented. Settle the implementation approach against the current code, get user approval, run size and resolution audits, dispatch `issue-implementer` in an isolated worktree, then run `implementation-auditor` when implementation succeeds."
argument-hint: "<issue-ref> [additional requirements]"
disable-model-invocation: true
model: opus
allowed-tools:
  - Agent
---

# Implement

Dispatcher for implementing a workflow issue from its **spec**. The issue body
is `Context` / `Description` / `Acceptance Criteria` — a spec, not a stored
plan: it records *what* and *done*, never *how*. The implementation approach is
decided here, at implement time, against the current code — it is not read off
the body. This skill settles and validates that approach with the user, then
hands it to `issue-implementer` (which adopts the approach, derives the concrete
steps against the current code, executes it in an isolated worktree, and pushes
a topic branch), then to `implementation-auditor` (which cross-checks the
result, read-only).

## Flow

1. **Parse the issue ref.** Take the first `$ARGUMENTS` token as the
   issue ref. If there is no recognizable ref, abort with `Usage:
   <issue-ref> [additional requirements]`. Everything past the ref is
   extra requirements, forwarded verbatim.

2. **Settle the plan.** The body is a spec, not a plan, so settle the
   implementation approach now, against the current code:
   - **Fetch and read.** `spectrack issue fetch <ref>`, then read the
     fetched issue body and comments from the paths it reports. Treat
     fetched issue files as read-only.
   - **Pre-flight the premise.** Before planning, check the spec's premises
     against the current code — the files, symbols, commands, and behaviors
     it names actually exist and behave as the body claims. A backlog spec
     may have been captured long before pickup and gone stale, or the work
     may already be done. If a premise is wrong, stop and resolve it with
     the user (re-scope or re-capture the issue) rather than planning
     against a false premise.
   - **Investigate.** For a `bug`, diagnose the root cause against the
     current code when the body does not already pin one — the spec leaves
     the cause to implement time. Locate the code the Acceptance Criteria
     implicate.
   - **Decide the approach.** Work the approach out in plan mode (or via a
     `Plan` subagent where the runtime provides one), grounded in the
     current code, and **get the user's explicit approval** of the approach
     before going further.
   - **Audit.** Run the size and resolution audits and read the full audit
     output paths they return before dispatching implementation.
     - Size: dispatch `task-size-auditor` with a writable copy of the
       fetched body. It surfaces decomposition when the work is not a
       single task.
     - Resolution: write the settled approach to a temp plan file and
       dispatch `resolution-auditor` (plan-audit mode) with that path; it
       validates the cause and the approach against the current code.
     Resolve their findings — sharpening the approach, or on a size verdict
     decomposing the work — before dispatching.

   Carry the temp plan file you wrote (the settled, user-approved approach)
   forward as the `plan` for step 3. The implementer's plan of record is that
   approach; the body carries none and is never edited into a stored plan
   here.

3. **Dispatch `issue-implementer`.** Call `Agent` with `subagent_type:
   spectrack:issue-implementer` **and `isolation: "worktree"`** —
   this skill always dispatches implementation in worktree mode. Pass the
   issue ref, the extra requirements verbatim, and the settled approach
   from step 2 as the `plan` (the implementer's plan of record — the body
   carries none). It returns a `<report>` whose `state` is `implemented`,
   `paused`, or `failed`.

4. **Dispatch `implementation-auditor`** only when the implementer's
   `state` is `implemented` — `paused` and `failed` leave no pushed
   branch to audit. Call `Agent` with `subagent_type:
   spectrack:implementation-auditor`, passing `issue-ref` (the same ref)
   and `report` (the implementer's `<report>` block, inline). It is
   read-only and returns a `<report>` with a `verdict`.

5. **Report.** Emit the implementer's `<report>`; when the audit ran, emit
   the auditor's `<report>` directly after without adding new conclusions.

$ARGUMENTS
