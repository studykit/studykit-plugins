---
name: implement-issue
description: "Implement a workflow `task`, `bug`, or `spike` issue: read the issue body, enter plan mode to converge on the implementation plan, apply the change, verify Acceptance Criteria, commit with the issue ref prefix, and close the issue with a refreshed Resume."
argument-hint: "<issue-ref> [additional requirements]"
disable-model-invocation: true
allowed-tools:
  - 'Bash("$WORKFLOW":*)'
  - 'Bash(git status:*)'
  - 'Bash(git diff:*)'
  - 'Bash(git add:*)'
  - 'Bash(git commit:*)'
  - EnterPlanMode
  - ExitPlanMode
  - Read
  - Edit
  - Write
  - Grep
  - Glob
---

# Plan-Mode Implement

The issue body is the spec. Read it, enter plan mode to converge on the
implementation plan, apply the change after approval, verify, commit, close.
Provider command shapes (fetch, writeback, close, freshness handling) come
from the session's workflow policy context — this skill does not restate
them.

## Scope

In scope: `task`, `bug`, `spike`. The type lives in the cached `issue.md`
frontmatter. For any other type (`epic`, `review`, `research`, `usecase`,
knowledge types), stop and redirect — these coordinate other work or live
on a different surface, and forcing plan-mode implementation onto them
distorts the type's role.

## Flow

1. **Read the issue.** Fetch the ref from the first `$ARGUMENTS` token (ask
   when missing or ambiguous), then read the cached `issue.md`. Follow the
   links the body cites: parent, blocked-by, knowledge pages, and paths
   named in `Affected Paths`. The body is the contract; its links complete
   it. Never edit the cached `issue.md` or `comment-*.md` projections in
   place.

2. **Enter plan mode and converge on the plan.** Call `EnterPlanMode`
   before drafting so the harness blocks edits during planning. Map the
   issue's `Description`, `Approach`, `Affected Paths`, `Unit Test
   Strategy`, and `Acceptance Criteria` (plus `Reproduction` for `bug`,
   `Hypothesis` / `Validation Method` for `spike`) onto a concrete plan:
   files to touch by absolute path, the verification step for each
   Acceptance Criterion, and the intended commit split. Present the
   converged plan via `ExitPlanMode`; no edits before the user accepts the
   plan and exits plan mode. If the plan keeps diverging from the body,
   the body itself is usually the problem — propose updating the body via
   the provider's writeback flow before iterating further on the plan.

3. **Implement.** Apply the approved plan exactly. Keep the change to the
   smallest shape that satisfies Acceptance Criteria; surface unrelated
   cleanups as follow-ups instead of folding them in. For `bug`, add the
   regression test first and confirm it fails on the unfixed code, then
   apply the fix and confirm it passes — both outputs become AC evidence.
   For `spike`, run the validation method and capture evidence; PoC code
   stays throwaway and production work belongs in a follow-up `task`.

4. **Verify Acceptance Criteria.** Pair every AC bullet with concrete
   evidence — test command and outcome, manual observation, artifact
   produced. Symmetry from a primary fix is not evidence for related ACs;
   each bullet needs its own check. If any AC fails, stop and ask the
   user before committing.

5. **Commit.** Stage only the changes the plan covered and split into
   meaningful commits (implementation, tests, scaffolding, tooling). Every
   subject carries the issue ref prefix per the session's commit-prefix
   policy. Do not list commit SHAs in the issue body or comments — the
   timeline already links commits by ref prefix.

6. **Push.** Push the commits to the remote before refreshing `Resume` or
   closing. The close should reference work that already exists on the
   remote so the timeline's ref-prefixed commit links resolve the moment
   the issue body lands.

7. **Decide terminal state.** Pick one of five outcomes — this is a
   judgment step, no writes yet.

   - `closed: completed` — every Acceptance Criterion met, no external
     gate remaining.
   - `closed: completed (with deferrals)` — core intent met *and* every
     unmet AC is **already captured in a separate follow-up issue**.
     This is a hard gate: if any unmet AC lacks a real follow-up ref,
     this branch is not eligible and the state falls back to
     `still open: handoff` or `still open: <reason>`.
   - `closed: <provider non-completion reason>` — the question is no
     longer load-bearing; close with the provider's non-completion state
     reason (GitHub `not_planned`, Jira `Won't Do` / `Cancelled` /
     similar transition). For `spike`, this branch is only taken when
     the user agrees the question is no longer load-bearing.
   - `still open: handoff` — local implementation is finished but
     external gates remain (push complete, review pending, merge,
     deploy, integration). Deferred items are articulated as follow-up
     **candidates** in `Open questions`, not yet split into separate
     issues. Distinguished from "paused" by `Waiting for` pointing at an
     external decision/action rather than an internal unresolved
     question.
   - `still open: <other reason>` — paused mid-flight, blocked by an
     internal unresolved question, or otherwise not ready to hand off.

   For `bug`, the regression test + fix evidence determines whether all
   AC are met. For `spike`, captured evidence (Artifact Links + short
   summary) accompanies the body update on whichever branch is chosen.

8. **Refresh `Resume` and execute the writeback.** The `Resume` shape
   varies by the terminal state chosen in step 7. Present the draft body
   to the user before invoking. On freshness drift, reread the cache
   paths the script reports and retry — never bypass the check.

   - **Closed branches** (`closed: completed` /
     `closed: completed (with deferrals)` /
     `closed: <provider non-completion reason>`): closed-state snapshot
     — `Approach` summarised, `Waiting for` empty, `Open questions`
     resolved or each one moved into a follow-up issue ref, `Next` empty
     or naming the follow-up. For the deferrals sub-branch, add an
     explicit `Deferred to: <follow-up refs>` line so the carve-out is
     visible from the closed body. Execute via the provider's writeback
     update that changes body + state in one call (or, when the body
     does not need to change, via the body-less close path).
   - **`still open: handoff`**: handoff snapshot —  `Approach`
     summarises what was delivered locally, `Waiting for` names the
     external gate (review, merge, deploy, etc.), `Open questions`
     enumerates deferred items each labelled as a follow-up
     **candidate** (not yet ticketed), `Next` names the immediate next
     action gating close. Execute via the provider's body-only writeback
     update — no close call.
   - **`still open: <other reason>`**: progress snapshot reflecting
     current state (what landed so far, what blocks the next move,
     unresolved questions, the next action). Execute via the provider's
     body-only writeback update — no close call.

## Additional Requirements

Treat `$ARGUMENTS` past the issue ref as extra emphasis from the user.
Incorporate it into the relevant step rather than tacking it on at the end.

$ARGUMENTS

## Output

Report only:

1. Issue ref and final state — one of:
   - `closed: completed`
   - `closed: completed (deferrals → <follow-up refs>)`
   - `closed: <provider non-completion reason>` (e.g. GitHub
     `not_planned`, Jira `Won't Do` / `Cancelled`)
   - `still open: handoff` — also name `Waiting for` and `Next`
   - `still open: <other reason>` — paused, blocked, etc.
2. Commit SHA(s), or `skipped`.
3. One line per Acceptance Criterion paired with its status: concrete
   evidence (closed branches), `deferred → <follow-up ref>`, or
   `in progress: <state>` (open branches).
