# Jira Issue Task Authoring

Provider-specific binding for `task` issues stored as Jira issues.

Read after:

- `../common/task-authoring.md`
- `./jira-issue-convention.md`
- `./jira-issue-relationships.md`
- `./jira-issue-anti-patterns.md`

## Scope

Use this binding for Jira `task` issues. The final body structure is listed below.

## Final body structure

Use this final Jira body structure for `task` issues. Emit each section in wiki markup (`h2. Name`); see `./jira-issue-convention.md` for the markup mapping.

Common required sections are defined by `../common/task-authoring.md`:

- `h2. Description`
- `h2. Unit Test Strategy`
- `h2. Acceptance Criteria`

Common optional sections are defined by `../common/task-authoring.md` and `../common/issue-body.md`:

- `h2. Change Plan`
- `h2. Interface Contracts`
- `h2. Out of Scope`
- `h2. Alternatives Considered`
- `h2. Risks`
- `h2. Resume`
- `h2. Why Discarded`

Issue type is automatically set to `Task`.
