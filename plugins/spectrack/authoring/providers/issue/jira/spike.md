# Jira Issue Spike Authoring

Provider-specific binding for `spike` issues stored as Jira issues.

Read after:

- `../../../contracts/issue/spike.md`
- `./convention.md`
- `./anti-patterns.md`

## Scope

Use this binding for Jira `spike` issues. The final body structure is listed below.

## Final body structure

Use this final Jira body structure for `spike` issues. Emit each section in wiki markup (`h2. Name`); see `./convention.md` for the markup mapping.

Common required sections are defined by `../../../contracts/issue/spike.md`:

- `h2. Description`
- `h2. Hypothesis`
- `h2. Validation Method`
- `h2. Acceptance Criteria`

Common optional sections are defined by `../../../contracts/issue/spike.md` and `../../../contracts/issue/body.md`:

- `h2. Artifact Links`
- `h2. Implementation Steps`
- `h2. Resume`
- `h2. Why Discarded`

Issue type is automatically set to `Task`.

Summary prefix is automatically set to `[Spike] `.
