# Jira Issue Bug Authoring

Provider-specific binding for `bug` issues stored as Jira issues.

Read after:

- `../../../contracts/issue/bug.md`
- `./convention.md`
- `./relationships.md`
- `./anti-patterns.md`

## Scope

Use this binding for Jira `bug` issues. The final body structure is listed below.

## Final body structure

Use this final Jira body structure for `bug` issues. Emit each section in wiki markup (`h2. Name`); see `./convention.md` for the markup mapping.

Common required sections are defined by `../../../contracts/issue/bug.md`:

- `h2. Description`
- `h2. Reproduction`
- `h2. Unit Test Strategy`
- `h2. Acceptance Criteria`

Common optional sections are defined by `../../../contracts/issue/bug.md` and `../../../contracts/issue/body.md`:

- `h2. Context`
- `h2. Environment`
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

Issue type is automatically set to `Bug`.
