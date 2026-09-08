---
name: implement-issue
description: "Implement a workflow `task`, `bug`, or `spike` issue from its spec. Use when the user gives an issue ref and wants the work implemented. Settle the implementation approach against the current code, get user approval, implement and verify it, then refresh the issue handoff."
---

# Implement

Dispatcher for implementing a workflow issue from its **spec**. The issue body
is `Context` / `Description` / `Acceptance Criteria` — a spec, not a stored
plan: it records *what* and *done*, never *how*. The implementation approach is
decided here, at implement time, against the current code — it is not read off
the body. This skill settles that approach with the user, then implements and
verifies it in the active session.

## Flow

1. **Parse the issue ref.** Take the first recognizable issue ref in the user's
   request. If there is no recognizable ref, abort with `Usage:
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
   - **Decide the approach.** Work the approach out using the host's planning
     facility (or a read-only planning subagent where available), grounded in the
     current code, and **get the user's explicit approval** of the approach
     before going further.
3. **Implement.** Re-check the approved approach against the current code. If
   it has materially drifted, stop and return to planning with the user.
   Otherwise apply the approach, verify every Acceptance Criterion, and commit
   the completed work on the current branch or an issue-named topic branch.

4. **Refresh `Resume`.** Upsert the provider-backed `Resume` comment with
   `spectrack issue comment resume`, recording what landed, any non-blocking
   questions, and the next handoff step. Do not mark work implemented when a
   required Acceptance Criterion remains incomplete.

5. **Report.** State the completed work, verification performed, commit, and
   any remaining non-blocking follow-up.
