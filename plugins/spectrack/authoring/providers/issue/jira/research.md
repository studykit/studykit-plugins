# Jira Issue Research Issue Authoring

Provider-specific binding for `research` issues stored as Jira issues.

Read after:

- `../../../contracts/issue/research.md`
- `./convention.md`
- `./anti-patterns.md`

## Scope

Use this binding for Jira `research` issues. The final body structure is listed below.

## Final body structure

Use this final Jira body structure for `research` issues. Emit each section in wiki markup (`h2. Name`); see `./convention.md` for the markup mapping.

Common required sections are defined by `../../../contracts/issue/research.md`:

- `h2. Description`
- `h2. Research Question`
- `h2. Mode`
- `h2. Options`

Common optional sections are defined by `../../../contracts/issue/research.md` and `../../../contracts/issue/body.md`:

- `h2. Scope`
- `h2. Sources To Check`
- `h2. Resume`

Issue type is automatically set to `Task`.

Summary prefix is automatically set to `[Research] `.
