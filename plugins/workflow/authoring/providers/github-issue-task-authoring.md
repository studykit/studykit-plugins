# GitHub Issue Task Authoring

Provider-specific binding for `task` issues stored as GitHub Issues.

Read after:

- `../common/task-authoring.md`
- `./github-issue-convention.md`
- `./github-issue-relationships.md`
- `./github-issue-anti-patterns.md`

## Scope

Use this binding for GitHub `task` issues. The final body structure is listed below.

## Final body structure

Use this final GitHub body structure for `task` issues.

Common required sections are defined by `../common/task-authoring.md`:

- `## Description`
- `## Unit Test Strategy`
- `## Acceptance Criteria`

Common optional sections are defined by `../common/task-authoring.md` and `../common/issue-body.md`:

- `## Change Plan`
- `## Interface Contracts`
- `## Out of Scope`
- `## Alternatives Considered`
- `## Risks`
- `## Resume`
- `## Why Discarded`

GitHub label is automatically set to `task`.

## Use case linkage

When this task implements a use case, link it as a blocker of the use case workflow issue using a GitHub issue dependency: `blocked_by` intent, source = use case issue, target = this task.
