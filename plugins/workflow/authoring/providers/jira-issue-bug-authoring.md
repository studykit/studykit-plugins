# Jira Issue Bug Authoring

Provider-specific binding for `bug` issues stored as Jira issues.

Read after:

- `../common/bug-authoring.md`
- `./jira-issue-convention.md`
- `./jira-issue-relationships.md`
- `./jira-issue-anti-patterns.md`

## Scope

Use this binding for Jira `bug` issues. The final body structure is listed below.

## Final body structure

Use this final Jira body structure for `bug` issues. Emit each section in wiki markup (`h2. Name`); see `./jira-issue-convention.md` for the markup mapping.

Common required sections are defined by `../common/bug-authoring.md`:

- `h2. Description`
- `h2. Reproduction`
- `h2. Unit Test Strategy`
- `h2. Acceptance Criteria`

Common optional sections are defined by `../common/bug-authoring.md` and `../common/issue-body.md`:

- `h2. Environment`
- `h2. Change Plan`
- `h2. Interface Contracts`
- `h2. Resume`
- `h2. Why Discarded`

Issue type is automatically set to `Bug`.
