# Jira Issue Epic Authoring

Provider-specific binding for `epic` issues stored as Jira issues.

Read after:

- `../common/epic-authoring.md`
- `./jira-issue-convention.md`
- `./jira-issue-relationships.md`
- `./jira-issue-anti-patterns.md`

## Scope

Use this binding for Jira `epic` issues. The final body structure is listed below.

## Final body structure

Use this final Jira body structure for `epic` issues. Emit each section in wiki markup (`h2. Name`); see `./jira-issue-convention.md` for the markup mapping.

Common required sections are defined by `../common/epic-authoring.md`:

- `h2. Description`

Common optional sections are defined by `../common/epic-authoring.md` and `../common/issue-body.md`:

- `h2. Coordination Notes`
- `h2. Acceptance Criteria`
- `h2. Related Work`
- `h2. Resume`
- `h2. Why Discarded`

Issue type is automatically set to `Epic`.
