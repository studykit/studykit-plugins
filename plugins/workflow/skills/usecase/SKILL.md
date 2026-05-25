---
name: usecase
description: "Shape a rough product idea into concrete workflow `usecase` issues through a Socratic, one-question-at-a-time interview. Publishes each confirmed use case as its own workflow `usecase` issue, surfaces knowledge side effects as `review` items, and at wrap-up dispatches `usecase-explorer` then `usecase-reviewer` for gap finding and quality review."
argument-hint: "<idea or vague concept to turn into use cases, or 'iterate' to resume>"
disable-model-invocation: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
  - Agent
  - WebSearch
  - WebFetch
---

# Use Case Discovery (Workflow)

A Socratic interviewer that helps the user discover what to build
through one-question-at-a-time dialogue. Confirmed use cases are
published as standalone workflow `usecase` issues; knowledge side
effects surface as separate `review` items rather than knowledge-page
edits in this session.

Discover use cases for: **$ARGUMENTS**

## Scope

In scope: producing **workflow `usecase` issues** (the discovery
surface defined in `${CLAUDE_PLUGIN_ROOT}/authoring/common/usecase-issue-authoring.md`).

Out of scope in this skill:

- Curated knowledge-side `usecase` pages — defer to a separate session
  when the flow is stable per the publishing rule in
  `${CLAUDE_PLUGIN_ROOT}/authoring/common/usecase-knowledge-authoring.md`.
- Editing knowledge pages (`domain`, `actors`, `nfr`, `context`,
  `architecture`, `spec`) — out of scope. The skill produces use
  case issues only; cross-surface alignment is left to the wrap-up
  `usecase-reviewer` (for actors) and to the user (for other
  knowledge surfaces).
- Implementation work — handed off to `task` / `bug` / `spike` issues
  authored separately once a use case is stable.

## Workflow policy and launcher

The SessionStart hook wraps every injected block in
`<policy>...</policy>`. Inside it this skill sees:

- `<launcher>` — the workflow launcher contract. Every workflow
  operation (issue fetch / new / comment / update / link) runs through it.
- `<authoring-resolver>` — the resolver invocation. Call it before
  drafting any `usecase` issue body, any `review` issue body, or any
  comment, to learn which authoring docs to read.
- `<runbook>` — reference docs (read on demand) at
  `${WORKFLOW_PLUGIN_ROOT}/authoring/runbook/<intent>/<provider>.md`.
  This skill uses `issue-fetch`, `issue-new`, `issue-comment`,
  `issue-update`, and `issue-link`. Read the matching intent file on
  demand for verb syntax and flag sets — never restate.

When the user has not been assigned by the caller, publish issues with
`--assignee me` so the user owns each created issue by default.

## Modes

Determine the mode from `$ARGUMENTS` and the configured issue
backend's current `usecase` issues:

- **New discovery** — `$ARGUMENTS` is an idea (free prose) and the
  backend has no in-progress `usecase` issues that match the idea.
  Run the interview from scratch.
- **Iteration** — `$ARGUMENTS` literally is `iterate`, or names an
  existing `usecase` issue ref, or the user explicitly asks to resume.
  Run `references/iteration-entry.md`.

Never overwrite a confirmed use case's body without an explicit
confirmation; iteration always preserves prior confirmed content.

## Session task list

Use the task list as a live workflow map.

**Naming convention:** phase-level tasks use the phase name. Sub-tasks
use `<phase prefix>: <detail>` and are created **dynamically** when
entering a phase.

**New discovery** — initial tasks:

- `"Step 1: Restate idea and confirm framing"` → `in_progress`
- `"Discovery: Use cases"` → `pending`
- `"Wrap Up: Explorer pass"` → `pending`
- `"Wrap Up: Reviewer pass"` → `pending`
- `"Wrap Up: Walk findings"` → `pending`
- `"Wrap Up: Session report"` → `pending`

**Iteration** — see `references/iteration-entry.md` for the task
backlog to seed.

**Conditional tasks** — add when the corresponding step fires:

- `"Discovery: UC-<ref> <title>"` — one per confirmed and published use case.
- `"Research: <topic>"` — when a similar-systems research dispatch fires.
- `"UI screen grouping"` — when the user agrees to group UI-related use cases.
- `"Mock: <screen slug>"` — when mock generation is requested.

## Workflow

### Step 1: Receive the idea (new discovery only)

Restate the idea back in one sentence to confirm understanding. Then:

1. Note the framing in the session task list — do **not** publish an
   anchor issue. The first publication is the first confirmed use case,
   not a wrapper. If a single epic-style anchor is wanted later, the
   user can publish an `epic` issue separately via `workflow issue
   new --type epic` per the runbook's `issue-new` intent and link the
   discovered use cases as `--child` from that epic.
2. Mark "Step 1" completed. Mark "Discovery: Use cases" in_progress.

### Steps 2–11: Interview phases

| Step | Phase | Procedure |
|------|-------|-----------|
| 2 | Discovery loop (four-gap interview + actor capture) | `references/discovery-loop.md` |
| 3 | Progressive use case extraction + publish | `references/progressive-extraction.md` |
| 4 | Use case splitting | `references/usecase-splitting.md` |
| 5 | Facilitation mode shifts (Contrarian / Simplifier / Reframer) | `references/facilitation-techniques.md` |
| 6 | Similar-systems research (on request, after 3+ use cases) | `references/research-procedure.md` |
| 7 | UI screen grouping + (optional) mock generation | `references/ui-screen-grouping.md` |

### Wrap Up

When the user indicates they're done, run `references/wrap-up.md`:
explorer → present candidates → reviewer → walk findings → session
report. Do **not** conclude on your own — the interview ends only when
the user says so.

## Agent dispatch

The skill spawns these subagents at wrap-up and at user request.
Context is passed via dispatch arguments (issue refs, output paths),
not agent memory.

- **Reviewer** — `Agent(subagent_type: "workflow:usecase-reviewer")`.
  Pass the list of `usecase` issue refs to review and the absolute
  output directory for the per-finding `review` issue draft bodies
  (the reviewer publishes the `review` issues itself).
- **Explorer** — `Agent(subagent_type: "workflow:usecase-explorer")`.
  Pass the list of `usecase` issue refs and the absolute output path
  for the advisory exploration report.
- **Mock generator** — `Agent(subagent_type: "workflow:mock-html-generator")`.
  Pass the participating use case refs, screen-group label, layout
  requirements, and an absolute output directory under
  `/tmp/workflow-mocks/<screen-slug>/`.

**Execution order in Wrap Up:** explorer first (find candidates the
existing set missed), then reviewer (validate the full set).

## Output

Pass-through is not the contract here — this skill drives an
interactive interview. The session's durable outputs are:

- Each confirmed use case → one workflow `usecase` issue (the
  `Description`, `Actors`, `Current Draft`, `Open Questions` sections
  defined by `usecase-issue-authoring.md`).
- Each knowledge side effect → one workflow `review` issue with
  `target:` set to the affected knowledge surface (or to the causing
  use case ref when the issue text itself is the problem).
- Each quality finding from the wrap-up reviewer → one workflow
  `review` issue, linked `--related` to the use case it targets.
- Optional: one `research` issue per similar-systems investigation,
  linked `--related` to the use cases it informs.
- Optional: mock HTML files at the absolute output path the mock
  dispatch named.

The skill itself emits a wrap-up summary that lists the refs created,
the open `review` items waiting for resolution, and which use cases
remain at `Open Questions`. The summary is dialogue, not a file.
