# Jira Issue Research Issue Authoring

Provider-specific binding for `research` issues stored as Jira issues.

Read after:

- `../common/research-issue-authoring.md`
- `./jira-issue-convention.md`
- `./jira-issue-relationships.md`
- `./jira-issue-anti-patterns.md`

## Scope

Use this binding for Jira `research` issues. The final body structure is listed below.

## Final body structure

Use this final Jira body structure for `research` issues. Emit each section in wiki markup (`h2. Name`); see `./jira-issue-convention.md` for the markup mapping.

Common required sections are defined by `../common/research-issue-authoring.md`:

- `h2. Description`
- `h2. Research Question`
- `h2. Mode`
- `h2. Options`

Common optional sections are defined by `../common/research-issue-authoring.md` and `../common/issue-body.md`:

- `h2. Scope`
- `h2. Sources To Check`
- `h2. Resume`

Issue type is automatically set to `Task`.

Summary prefix is automatically set to `[Research] `.
