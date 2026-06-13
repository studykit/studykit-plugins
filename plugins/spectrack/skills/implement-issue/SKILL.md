---
name: implement-issue
description: "Implement a workflow `task`, `bug`, or `spike` issue from its spec. The issue body is a spec (`Context` / `Description` / `Acceptance Criteria`), not a stored plan: the implementation approach is settled here, at implement time, against the current code — investigate, decide in plan mode, get the user's approval, and audit it (size + resolution). Then dispatch `issue-implementer` with the approved approach, then `implementation-auditor` to verify the result. This skill settles the approach and passes the agents' reports through."
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
result, read-only). The skill owns the plan-settling pass and dispatch; the
agents' bodies are the source of truth for what they do and which states they
return.

## Flow

1. **Parse the issue ref.** Take the first `$ARGUMENTS` token as the
   issue ref. If there is no recognizable ref, abort with `Usage:
   <issue-ref> [additional requirements]`. Everything past the ref is
   extra requirements, forwarded verbatim.

2. **Settle the plan.** The body is a spec, not a plan, so settle the
   implementation approach now, against the current code:
   - **Fetch and read.** `spectrack issue fetch <ref>` — it reports the
     local cache location of the fetched issue (a `Base:` directory with the
     body and comment file paths under it). Read the body and comments
     there. The cached copy is read-only — never edit it in place.
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
   - **Audit.** Both auditors are file-based: each writes a sidecar review
     (`<file>.audit.md`) and returns only the verdict's first paragraph plus
     that path, so **read the sidecar to get the actionable reasoning**.
     - Size: copy the fetched body to a temp file — the cached copy is
       read-only, and the auditor writes its sidecar beside the file you
       pass — and dispatch `task-size-auditor` with that temp path. It
       surfaces decomposition when the work is not a single task.
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
   the agent's frontmatter does not request isolation itself; this
   call-time parameter is what provisions the isolated worktree.
   Omitted, the agent would run in-place in the calling session's
   checkout — this skill always dispatches worktree mode. Pass the
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

5. **Pass through.** Emit the implementer's `<report>`; when the audit
   ran, emit the auditor's `<report>` directly after. The skill adds
   nothing on top.

$ARGUMENTS
