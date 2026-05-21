---
name: implement-issue
description: "Implement a workflow `task`, `bug`, or `spike` issue: read the issue body, enter plan mode to converge on the implementation plan, and after the user approves, dispatch the implementation, verification, commit, push, and writeback to the `issue-implementer` agent."
argument-hint: "<issue-ref> [additional requirements]"
disable-model-invocation: true
allowed-tools:
  - 'Bash(workflow:*)'
  - 'Bash(mkdir -p:*)'
  - EnterPlanMode
  - ExitPlanMode
  - Read
  - Write
  - Grep
  - Glob
  - Agent
---

# Plan-Mode Implement

The issue body carries both the spec (the outcome to achieve) and the
planned approach (how the issue's author intends to get there) per the
workflow's authoring contract. Read it, enter plan mode to refine the
body's planned approach into a concrete execution plan, and after the
user approves that plan, dispatch the mechanical execution (implement,
verify, commit, push, decide terminal state, writeback) to the
`issue-implementer` agent. The skill owns the interactive plan-approval
gate; the agent owns the rest in its own context. The body's section
schema lives in the authoring docs — this skill does not restate it.
Provider command shapes (fetch, writeback, terminal transition,
freshness handling) come from the session's workflow policy context —
likewise not restated here.

## Scope

In scope: `task`, `bug`, `spike`. The type lives in the cached issue
body's frontmatter. For any other type (`epic`, `review`, `research`,
`usecase`, knowledge types), stop and redirect — these coordinate other
work or live on a different surface, and forcing plan-mode implementation
onto them distorts the type's role.

## Flow

1. **Read the issue body.** Fetch the ref from the first `$ARGUMENTS`
   token (ask when missing or ambiguous), then read the cached issue body
   file the fetch script returns. Follow the workflow links the body
   cites — parent, blocked-by, knowledge pages — to ground intent. **Do
   NOT open the source files named in `Affected Paths` yet.** The
   code-vs-body cross-check belongs inside plan mode in step 2, so the
   harness governs every step from code reading onward. Capture the
   cached body path — step 3 reuses it. Never edit the cached body or
   comment projections in place.

2. **Enter plan mode, cross-check the body against the current code,
   and converge on the plan.** Call `EnterPlanMode` before opening any
   source files so the harness governs the cross-check and plan
   drafting. Inside plan mode:

   - Open the files named in `Affected Paths` and the surrounding code
     the body's planned approach assumes — current signatures, module
     structure, dependency graph, surrounding helpers.
   - Compare the body (`Description`, `Approach`, `Affected Paths`,
     `Acceptance Criteria`, plus type-specific sections) against the
     code as it stands now. Note any drift: stale file paths, signatures
     that no longer match, helpers that moved or were removed,
     assumptions that no longer hold.
   - If you find material drift, **ask the user explicitly** whether to
     update the body via the provider's writeback flow before
     continuing. Surface the specific drifted elements and a concrete
     body-change proposal. Do not silently rewrite the plan around stale
     body text. Capture the user's decision (and the approved body
     draft, if any) so step 3 can execute the writeback.
   - Refine the body's planned approach into a concrete execution plan
     against its spec: files to touch by absolute path, the verification
     step for each Acceptance Criterion, and the intended commit split.

   Present the refined plan via `ExitPlanMode`; nothing proceeds before
   the user accepts it and exits plan mode.

3. **Apply any approved body update, save the plan, and dispatch to the
   `issue-implementer` agent.** After the user accepts the plan and
   plan mode exits:

   - If the user approved a body update in step 2, execute the
     provider's writeback flow now, then re-fetch the issue with
     `--cache-policy refresh` so the agent reads the updated body. Use
     the refreshed cache path as `issue-cache-path` below.
   - Write the approved plan text to
     `/tmp/workflow-plans/issue-<ref>-plan.md` (create the directory
     with `mkdir -p` if missing).
   - Dispatch the agent with:
     - `issue-cache-path` — the refreshed cached body path if step 2
       updated the body; otherwise the path captured in step 1. The
       agent will not re-fetch.
     - `plan-file` — the absolute path of the plan file you just wrote.
     - Any `$ARGUMENTS` tokens past the ref, verbatim as extra
       requirements.

   The agent runs in an isolated worktree the harness provisions via
   its `isolation: worktree` frontmatter, adopts the approved plan,
   implements, verifies every Acceptance Criterion, commits with the
   issue ref prefix, pushes the worktree's branch, opens a GitHub PR
   via `gh` that auto-closes the issue on merge, and writes back the
   issue's `Resume` to a handoff snapshot pointing at the PR. The
   harness cleans up the worktree automatically on agent exit — kept
   on disk when commits/uncommitted edits exist, removed otherwise.
   On AC verification failure, body-vs-reality divergence, or external
   decisions surfacing mid-execution, the agent publishes a `review`
   issue and links the implementation task as `blocked-by` instead of
   opening a PR on partial work.

   The skill does not run any edits, git commands, PR creation, or
   workflow writes itself after this dispatch — that is the agent's
   responsibility.

## Additional Requirements

Treat `$ARGUMENTS` past the issue ref as extra emphasis from the user.
Weave it into the plan you converge on in step 2, and pass it through
verbatim to the agent in step 3 so the agent can honour it during
execution.

$ARGUMENTS

## Output

Pass through what the agent returns. The skill itself adds nothing on top
beyond confirming dispatch. The agent's report shape:

1. Implementation issue ref and final state — one of:
   - `still open: handoff (PR: <url>)` — successful execution; also
     names `Waiting for` and `Next`
   - `resolved: <provider terminal reason>` (e.g. GitHub
     `state=closed --state-reason=not_planned`, Jira `Won't Do` /
     `Cancelled`)
   - `still open: blocked-by <review-ref>` — a `review` issue was
     published mid-execution; also names the concern type (`finding` /
     `gap` / `question`)
   - `still open: <other reason>` — paused, blocked by an internal
     unresolved question, etc.
   - `stopped: <reason>` — operational stop (out-of-scope type,
     freshness drift, write conflict, worktree or PR creation failure)
2. PR URL, or `none`.
3. Worktree path / branch, so the user can re-enter the work in progress.
4. Commit SHA(s), or `skipped`.
5. One line per Acceptance Criterion paired with its status: concrete
   evidence (PR opened), `deferred → <follow-up ref>`,
   `in progress: <state>` (open branches without PR), or
   `unverified: <blocker>` (blocked / stopped).
6. If a review was published: review ref, concern type, and one-sentence
   summary, plus any further review candidates the agent observed.
