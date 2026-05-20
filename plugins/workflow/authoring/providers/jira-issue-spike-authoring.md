# Jira Issue Spike Authoring

Provider-specific binding for `spike` issues stored as Jira issues.

Read after:

- `../common/spike-authoring.md`
- `./jira-issue-convention.md`
- `./jira-issue-relationships.md`
- `./jira-issue-anti-patterns.md`

## Scope

Use this binding for Jira `spike` issues. The final body structure is listed below.

## Final body structure

Use this final Jira body structure for `spike` issues. Emit each section in wiki markup (`h2. Name`); see `./jira-issue-convention.md` for the markup mapping.

Common required sections are defined by `../common/spike-authoring.md`:

- `h2. Description`
- `h2. Hypothesis`
- `h2. Validation Method`
- `h2. Acceptance Criteria`

Common optional sections are defined by `../common/spike-authoring.md` and `../common/issue-body.md`:

- `h2. Artifact Links`
- `h2. Approach`
- `h2. Affected Paths`
- `h2. Resume`
- `h2. Why Discarded`

Issue type is automatically set to `Task`.

Summary prefix is automatically set to `[Spike] `.
