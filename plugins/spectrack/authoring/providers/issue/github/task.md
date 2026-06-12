# GitHub Issue Task Authoring

Provider-specific binding for `task` issues stored as GitHub Issues.

Read after:

- `../../../contracts/issue/task.md`
- `./convention.md`
- `./anti-patterns.md`

## Scope

Use this binding for GitHub `task` issues. The final body structure is listed below.

## Final body structure

Use this final GitHub body structure for `task` issues.

Common required sections are defined by `../../../contracts/issue/task.md`:

- `## Description`
- `## Unit Test Strategy`
- `## Acceptance Criteria`

Common optional sections are defined by `../../../contracts/issue/task.md` and `../../../contracts/issue/body.md`:

- `## Context`
- `## Root Cause`
- `## Design Decision`
- `## Implementation Steps`
- `## Verification`
- `## Interface Contracts`
- `## Out of Scope`
- `## Alternatives Considered`
- `## Risks`
- `## Resume`
- `## Why Discarded`

GitHub label is automatically set to `task`.

## Use case linkage

When this task implements a use case, link it as a blocker of the use case workflow issue using a GitHub issue dependency: `blocked_by` intent, source = use case issue, target = this task.
