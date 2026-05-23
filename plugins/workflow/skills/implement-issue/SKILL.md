---
name: implement-issue
description: "Implement a workflow `task`, `bug`, or `spike` issue: dispatch `issue-planner` to refine the body autonomously, dispatch `issue-implementer` when the planner reports `planned`, then dispatch `implementation-auditor` on the implementer's result unless the implementer declined or failed. Pass each agent's report through."
argument-hint: "<issue-ref> [additional requirements]"
disable-model-invocation: true
context: fork
model: sonnet
allowed-tools:
  - Agent
---

# Autonomous Implement

Three-stage autonomous pipeline for workflow `task`, `bug`, and `spike`
issues.

Stage 1 dispatches `issue-planner`, which reads the body, cached
comments, and 1-hop related issues; cross-checks against the current
code; refines `Approach` / `Affected Paths` / `Acceptance Criteria` in
the body; and appends a plan comment carrying the refined plan,
body-change rationale, and any autonomous decisions.

Stage 2 dispatches `issue-implementer` against the refined body, which
adopts the plan, implements, verifies every Acceptance Criterion,
commits, pushes the worktree's branch, and refreshes the issue's
`Resume` to a handoff snapshot.

Stage 3 dispatches `implementation-auditor` to cross-check the
implementer's `<report>` against the implementation issue and
observable artifacts (pushed branch, commits, referenced refs, refreshed
`Resume`). The audit is read-only; it adds a prose verdict in its own
sidecar file and surfaces a `<conclusion>` block to the user.

The skill itself owns dispatch and state branching only — no plan mode,
no interactive approval gates, no code reading by the skill, no
`/tmp/workflow-plans/` scratch files. The agents do the substantive
work in their own contexts.

## Scope

In scope: `task`, `bug`, `spike`. The type lives in the cached issue
body's frontmatter and is enforced by both `issue-planner` and
`issue-implementer`. Out-of-scope types (`epic`, `review`, `research`,
`usecase`, knowledge) surface as `declined` from `issue-planner`,
which this skill passes through unchanged.

## Flow

1. **Parse the issue ref.** Take the first `$ARGUMENTS` token as the
   issue ref. If there is no recognizable ref, abort with the message
   `Usage: <issue-ref> [additional requirements]` — do **not** prompt
   for clarification. The fork context cannot reliably round-trip a
   question; the user can re-invoke with the ref filled in. Capture
   any additional `$ARGUMENTS` past the ref verbatim as extra
   requirements; both `issue-planner` and `issue-implementer` accept
   these as emphasis to weave into their relevant flow steps.

2. **Dispatch `issue-planner`.** Call `Agent` with `subagent_type:
   workflow:issue-planner`, passing the issue ref and the extra
   requirements verbatim. The agent fetches the issue, reads its
   comments and 1-hop related issues, cross-checks against the
   current code, refreshes the body's `Approach` / `Affected Paths` /
   `Acceptance Criteria`, and appends a single plan comment. It exits
   with a structured `<report>` and one of these terminal states:

   - `planned` — body refined, plan comment appended. Proceed to
     step 3.
   - `published-review` — body too ambiguous, or code drift forced a
     body redesign, or an AC was unverifiable; the agent published a
     `review` and linked the planning task as `blocked-by`. Pass the
     report through and stop.
   - `awaits-prereq` — a pre-existing `blocked_by` prerequisite is
     unresolved. Pass through and stop.
   - `declined` — issue type out of scope. Pass through and stop.
   - `failed` — operational failure (write conflict, freshness drift,
     fetch failure). Pass through and stop.

   For any state other than `planned`, the skill emits the planner's
   `<report>` verbatim and exits. No implementer dispatch, no audit.

3. **Dispatch `issue-implementer`.** Only when the planner returned
   `planned`. Call `Agent` with `subagent_type:
   workflow:issue-implementer`, passing the same issue ref and the
   same extra requirements verbatim. The implementer runs in an
   isolated worktree the harness provisions via its `isolation:
   worktree` frontmatter; it fetches the issue fresh — the planner's
   body update and plan comment are already on the issue because the
   planner's writeback refreshed the cache — adopts the plan from the
   refreshed body plus the plan comment, implements, verifies every
   Acceptance Criterion, commits with the issue ref prefix, pushes
   the worktree's branch, and refreshes the `Resume` to a handoff
   snapshot. The harness cleans up the worktree automatically on
   agent exit — kept on disk when commits or uncommitted edits exist,
   removed otherwise.

   The implementer exits with a `<report>` whose `state` line carries
   one of: `implemented`, `resolved`, `awaits-prereq`,
   `published-review`, `paused`, `declined`, `failed`. The report's
   main-session response opens with the sentence `Implementation
   report saved to <absolute report path>.` — capture that path; the
   auditor needs it in step 4.

   On AC verification failure or body-vs-reality divergence the
   implementer publishes its own `review` issue (separate from any
   planner-published review) and links the implementation task as
   `blocked-by` rather than opening a partial handoff — that surfaces
   as state `published-review`.

4. **Dispatch `implementation-auditor`.** When the implementer's
   `state` is **not** `declined` and **not** `failed`, call `Agent`
   with `subagent_type: workflow:implementation-auditor`, passing:

   - `issue-ref` — the same ref.
   - `report` — the absolute path the implementer named in its
     `Implementation report saved to <path>.` sentence.

   The auditor is read-only on every surface (issue, branch, commits,
   referenced refs). It cross-checks the implementer's claims against
   observable artifacts on four axes (report fidelity, AC evidence
   quality, open-questions legitimacy, intent alignment), writes a
   prose review to its sidecar file (default
   `/tmp/workflow-audits/issue-<ref>-audit.md`), and returns a short
   main-session response containing the `Audit report saved to
   <path>.` sentence plus a `<conclusion>` block carrying the verdict
   in natural prose. Verdicts: `ok`, `unverifiable`,
   `report-claim-inaccurate`, `intent-divergence`, `weak-ac-evidence`,
   `open-questions-evasive`.

   Skip the audit when the implementer's `state` is `declined` (issue
   type out of scope — no artifacts to audit) or `failed`
   (operational stop — no artifacts to audit). The skill's output in
   those two cases stops at the implementer's report.

5. **Pass through.** Emit the implementer's `<report>` first; when the
   audit ran, emit the auditor's main-session response (saved-path
   sentence plus `<conclusion>` block) directly after. The skill adds
   nothing on top.

## Additional requirements

Anything in `$ARGUMENTS` past the issue ref is forwarded verbatim to
`issue-planner` and `issue-implementer` in step 2 and step 3. The
auditor in step 4 does not take extra requirements — it grounds its
judgment in the issue, the report, and observable artifacts only. Do
not paraphrase, summarize, or filter when forwarding to the first two
agents.

$ARGUMENTS

## Output

Pass through what each dispatched agent returns. The skill itself adds
nothing on top.

- Planner returned a non-`planned` state → skill output is the
  planner's `<report>`.
- Planner returned `planned`, implementer ended in `declined` or
  `failed` → skill output is the implementer's `<report>`.
- Planner returned `planned`, implementer ended in any other state →
  skill output is the implementer's `<report>` followed by the
  auditor's main-session response.

The planner's body update and plan comment are visible on the issue
itself; the implementer's full report lives at the path named in its
saved-report sentence; the auditor's prose review lives at the path
named in its saved-report sentence. The report shapes themselves are
documented in each agent's body.
