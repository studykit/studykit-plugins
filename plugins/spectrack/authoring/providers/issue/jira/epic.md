# Jira Issue Epic Authoring

Provider-specific binding for `epic` issues stored as Jira issues.

Read after:

- `../../../contracts/issue/epic.md`
- `./convention.md`
- `./anti-patterns.md`

## Scope

Use this binding for Jira `epic` issues. The final body structure is listed below.

## Final body structure

Use this final Jira body structure for `epic` issues. Emit each section in wiki markup (`h2. Name`); see `./convention.md` for the markup mapping.

Common required sections are defined by `../../../contracts/issue/epic.md`:

- `h2. Description`

Common optional sections are defined by `../../../contracts/issue/epic.md` and `../../../contracts/issue/body.md`:

- `h2. Coordination Notes`
- `h2. Acceptance Criteria`
- `h2. Related Work`
- `h2. Resume`
- `h2. Why Discarded`

Issue type is automatically set to `Epic`.
