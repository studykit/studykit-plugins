# Jira Issue Use Case Issue Authoring

Provider-specific binding for `usecase` issues stored as Jira issues.

Read after:

- `../../../contracts/issue/usecase.md`
- `./convention.md`
- `./relationships.md`
- `./anti-patterns.md`

## Scope

Use this binding for Jira `usecase` issues. The final body structure is listed below.

## Final body structure

Use this final Jira body structure for `usecase` issues. Emit each section in wiki markup (`h2. Name`); see `./convention.md` for the markup mapping.

Common required sections are defined by `../../../contracts/issue/usecase.md`:

- `h2. Description`
- `h2. Actors`
- `h2. Current Draft`
- `h2. Open Questions`

Common optional sections are defined by `../../../contracts/issue/usecase.md` and `../../../contracts/issue/body.md`:

- `h2. Resume`

Issue type is automatically set to `Story`.
