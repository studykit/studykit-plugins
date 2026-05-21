# GitHub Issue Provider Convention

Provider-wide convention rules for issue-backed items stored as GitHub Issues.

## Scope

Use these rules for issue-backed items stored in GitHub Issues.

This file defines GitHub-wide issue writing conventions only.
Provider relationship boundaries belong in `./github-issue-relationships.md`.
GitHub body anti-patterns belong in `./github-issue-anti-patterns.md`.

## Body markup

GitHub Issue bodies render as GitHub-Flavored Markdown.

Canonical section names from common authoring map to `## Name` headings. Do not emit an H1; the issue title is stored separately.

Use GFM task-list items (`- [ ]` / `- [x]`) for completion-oriented sections such as `Acceptance Criteria`, review checklists, and migration checklists.

## Identity and references

Use GitHub-native references in visible text.

- Same repository: `#123`.
- Cross repository on the same host: `owner/repo#123`.
- Outside GitHub-native contexts or when ambiguous: full issue URL.

## Related body section

`## Related` is available to any GitHub issue type.

Use `## Related` for human-readable references that are not stored as
GitHub-native relationships. This includes implementation anchors, non-issue
review targets, follow-up work, external pages, or other soft references.

Do not use `## Related` for parent, child, blocking, or dependency
relationships that are stored as GitHub-native relationships.

When used:

- Start with one bullet per related reference.
- Keep descriptions short.

## Dependency body fallback

Use GitHub issue dependency relationships for blocking or ordering dependencies whenever possible.

Use `## Dependencies` only when dependency relationships cannot be stored natively and the issue body needs human-readable dependency context.

When used:

- Start with one bullet per dependency.
- Use GitHub issue references or full URLs whenever possible.
- Keep the section limited to blocking or ordering dependencies.

## Provider update intent

When running `$WORKFLOW issue.py update` or
`$WORKFLOW issue.py {state <ref> close|state <ref> reopen|assign|unassign|set-type}`
to update provider-owned GitHub issue fields, supply only the values
needed for the requested update.

Generic supported update intents:

- Issue reference, plus desired title when changing the GitHub issue title.
- Issue reference, plus desired workflow type when explicitly changing the workflow type
  (`issue.py set-type`).
- Issue reference, plus assignee login (or the literal `me`) when changing
  the assignee (`issue.py assign|unassign`).

Do not ask for generic status, priority, tag, label, or GitHub Project field
writes from this contract. Those writes require a separate project-specific
workflow extension that documents and supports the selected field.

## Comments and logs

Use GitHub comments for discussion, feedback, and work logs.

Do not create a body `## Log` section. Use GitHub comments for human-readable notes and GitHub timeline/events as provider audit history. Do not duplicate routine status changes in the issue body.

## Implementation summary comments

When updating an issue after implementation, keep the comment concise.

Recommended shape:

```markdown
Implemented <short outcome>.

Why:
- <reason this change was needed>

Summary:
- <material change>
- <material change>

Validation: local workflow checks passed.
```

Rules:

- Include `Why:` when the motivation is not obvious, the change removes
  behavior or documentation, or the work changes an agent, provider, or
  authoring boundary.
- Do not paste unit test output, test file lists, or verbose validation logs into issue comments.
- Do not list commit SHAs by default. When commit subjects prefix the issue
  ref (`#123 …`), the GitHub timeline already links those commits to the
  issue, so repeating them as bullets is noise.
- Include short SHA bullets only when the auto-link cannot fire (commits in a
  different repo, or commits whose subject does not carry the issue ref) or
  when a few commits in a large set need explicit highlighting.
- When SHAs are included, use plain short SHA text — no backticks, no full
  commit URLs. GitHub autolinks only unquoted SHA text in issue comments.
- Keep implementation details high-level; link or reference changed files only when the distinction matters.

## Closing keywords

Only generate GitHub closing keywords such as `Fixes #123` when the workflow intentionally wants GitHub to auto-close an issue.

Do not use closing keywords merely to express a relationship.
