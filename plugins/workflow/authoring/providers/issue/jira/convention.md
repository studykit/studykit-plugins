# Jira Issue Provider Convention

Provider-wide convention rules for issue-backed items stored as Jira issues.

## Scope

Use these rules for issue-backed items stored in Jira.

This file defines Jira-wide issue writing rules only. Provider relationship authoring boundaries belong in `./relationships.md`. Jira body anti-patterns belong in `./anti-patterns.md`. Type-specific body structure and allowed relationship body fallback sections belong in the matching Jira issue type authoring file.

## Body markup

Jira Data Center issue descriptions and comments render as **Jira wiki markup**, not GitHub Markdown. Emit wiki markup when writing any Jira issue body or comment.

Canonical section names from common authoring map to `h2. Name` headings. Use `h3. Name` / `h4. Name` for subsections.

Wiki markup has no native task-list. Where common authoring asks for a completion-oriented checklist (for example, `Acceptance Criteria` items), emit each item as a normal bulleted line (`* item`). Do not write `- [ ]` or `- [x]`; those render as literal text in Jira.

For Markdown-to-wiki mistake mappings (Markdown headings, bold, lists, inline code, code fences, links, tables, checklists), see the "Markdown leakage" section in `./anti-patterns.md`.

## Identity and references

Use Jira issue keys in visible text.

Examples:

- `PROJ-123`.
- `[PROJ-123]` in GitHub comments when GitHub for Atlassian should create a Jira link.
- Full Jira URL when outside Jira/Atlassian-aware contexts or when a portable link is needed.

## Relationships

Read `./relationships.md` for provider relationship storage and body-boundary rules.

Read `./anti-patterns.md` for forbidden relationship body sections.

Allowed body fallback sections for Jira relationships are type-specific and belong in the matching Jira issue type authoring file.

## `Related` body section

A `Related` section (rendered as `h2. Related`) is available to any Jira issue type.

Use it for human-readable references that are not stored as Jira-native issue links, hierarchy fields, or remote links. This includes implementation anchors, non-Jira review targets, follow-up work, external pages, or other soft references.

Do not use `Related` for parent, child, blocking, dependency, related-work, or remote-link relationships that are stored natively in Jira.

When used:

- Start with one bullet (`* …`) per related reference.
- Keep descriptions short.

## `Dependencies` body fallback

Use Jira issue links or remote links for dependency relationships whenever possible.

Use a `Dependencies` section (rendered as `h2. Dependencies`) only when dependency links cannot be stored natively and the issue body needs human-readable dependency context.

When used:

- Start with one bullet (`* …`) per dependency.
- Use Jira issue keys or full URLs whenever possible.
- Keep the section limited to blocking or ordering dependencies.

## Provider update intent

When running `workflow issue update` or
`workflow issue {state <KEY> <verb>|assign|unassign|set-type}`
to update provider-owned Jira issue fields, supply only the values needed
for the requested update.

Generic supported update intents:

- Issue key, plus desired summary/title when changing the Jira issue title.
- Issue key, plus the workflow type whose Jira issuetype to apply when
  swapping the issuetype (`issue set-type`). The script
  resolves the native Jira issuetype name via the `artifact_issue_types`
  mapping.
- Issue key, plus assignee username (or the literal `me`) when changing
  the assignee (`issue assign|unassign`).
- Issue key, plus the configured `state_transitions` mapping when closing
  or reopening (`issue state <KEY> close|reopen` or any configured verb).

Do not ask for generic status or priority changes from this contract.
Those writes require a separate project-specific workflow extension that
documents and supports the selected field or transition.

## Comments and logs

Use Jira comments, history, and worklog for discussion and work logs.

Do not create a body `Log` section (`h2. Log`). Keep the issue body structured and current.

## Implementation summary comments

When updating an issue after implementation, keep the comment concise.

Recommended shape (wiki markup):

```text
Implemented <short outcome>.

Why:
* <reason this change was needed>

Summary:
* <material change>
* <material change>

Validation: local workflow checks passed.
```

Rules:

- Include `Why:` when the motivation is not obvious, the change removes
  behavior or documentation, or the work changes an agent, provider, or
  authoring boundary.
- Do not paste unit test output, test file lists, or verbose validation logs into issue comments.
- Do not list commit references by default. When commit subjects prefix the
  Jira issue key (`ABC-123 …`) and the project has a DVCS or Smart Commit
  integration, Jira already links those commits to the issue.
- Include commit reference bullets only when the auto-link cannot fire (no
  DVCS integration, commits in a different repository, or commits whose
  subject does not carry the issue key) or when a few commits in a large set
  need explicit highlighting.
- Keep implementation details high-level; link or reference changed files only when the distinction matters.

## Branch, commit, and PR conventions

Default branch pattern:

```text
PROJ-123-some-name
```

Default commit pattern:

```text
PROJ-123 <summary>
```

Default PR title pattern:

```text
PROJ-123 <summary>
```

A slash branch pattern such as `PROJ-123/some-name` may work, but the default is hyphen for compatibility with Atlassian examples and common tooling.

## Smart Commits

Use Jira Smart Commit commands only when the workflow intentionally wants Jira command side effects.

Do not use Smart Commit commands merely to mention an issue.
