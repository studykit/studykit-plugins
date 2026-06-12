# Jira Issue Task Authoring

Provider-specific binding for `task` issues stored as Jira issues.

Read after:

- `../../../contracts/issue/task.md`
- `./convention.md`
- `./anti-patterns.md`

## Scope

Use this binding for Jira `task` issues. The final body structure is listed below.

## Final body structure

Use this final Jira body structure for `task` issues. Emit each section in wiki markup (`h2. Name`); see `./convention.md` for the markup mapping.

Common required sections are defined by `../../../contracts/issue/task.md`:

- `h2. Description`
- `h2. Unit Test Strategy`
- `h2. Acceptance Criteria`

Common optional sections are defined by `../../../contracts/issue/task.md` and `../../../contracts/issue/body.md`:

- `h2. Context`
- `h2. Root Cause`
- `h2. Design Decision`
- `h2. Implementation Steps`
- `h2. Verification`
- `h2. Interface Contracts`
- `h2. Out of Scope`
- `h2. Alternatives Considered`
- `h2. Risks`
- `h2. Resume`
- `h2. Why Discarded`

Issue type is automatically set to `Task`.
