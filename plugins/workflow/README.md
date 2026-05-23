# Workflow Plugin

Issue- and knowledge-backed workflow for Claude Code and Codex sessions. The
plugin treats the configured provider — GitHub Issues, Jira, or a GitHub
repository `wiki/` — as the source of truth and helps the assistant draft,
publish, refresh, and link work items without leaving the session.

## Supported Providers

- **Issues** — GitHub Issues, Jira (Data Center / Server), or a local
  filesystem provider.
- **Knowledge** — GitHub repository `wiki/`.

Issue tracking and knowledge documentation are configured independently, so
mixed setups (e.g., Jira issues + GitHub repository `wiki/`) are supported.

## Installation

Install from the studykit plugin marketplace inside Claude Code or Codex.
The plugin works in both runtimes.

## Configuration

Per-project configuration lives at `.workflow/config.yml` at the repository
root. The fastest way to create it is the bundled setup skill:

```
/setup
```

The skill walks through provider selection, fills in the required fields,
and writes `.workflow/config.yml`.

A minimal hand-written configuration looks like:

```yaml
version: 1
mode: remote-native

providers:
  issues:
    kind: github
    repo: org/repo
  knowledge:
    kind: github

issue_id_format: github

commit_refs:
  enabled: true
  style: provider-native
```

For the full schema and per-provider fields, see
`../../wiki/workflow/workflow-configuration.md`.

## Slash Commands

Once configured, the plugin exposes three slash commands:

- `/setup` — Generate and write `.workflow/config.yml` for the current
  repository.
- `/implement-issue <issue-ref> [extra requirements]` — Read the issue
  body, converge on a plan with you, and then run implementation,
  verification, commit, push, and writeback for the approved plan.
- `/handoff` — Wrap up a session by refreshing the `Resume` section of
  every in-flight issue and, if needed, publishing `review`-type issues
  for residual findings, gaps, or questions.

## Output Styles

The plugin ships an opt-in output style:

- **Conversation First** — Shifts the assistant into a dialogue-first
  cadence: clarify ambiguity with focused questions, present 2–3 options
  with tradeoffs before implementing, and restate intent before any
  non-trivial tool use. Built-in coding behavior is preserved; only the
  conversational cadence changes.

Activate it from `/config` → **Output style** → **Conversation First**,
then run `/clear` (or start a new session) for it to take effect.

## What the Plugin Does for You

- Looks up issues by provider-native reference (`#123`, `KEY-456`, etc.)
  and surfaces a readable issue body inside the session.
- Drafts and publishes new issues, comments, body updates, and
  relationship links through the configured provider.
- Keeps commit subjects prefixed with the related issue reference and the
  PR's `Closes` keyword pointing at the right issue.
- Refreshes in-flight issues at session handoff so the next session can
  pick up from the issue body alone.

## Configuration Reference

- Provider configuration schema:
  `../../wiki/workflow/workflow-configuration.md`
- Provider model and reference formats:
  `../../wiki/workflow/workflow-provider-model.md`,
  `../../wiki/workflow/workflow-provider-reference-formats.md`
- Issue relationship policy:
  `../../wiki/workflow/workflow-issue-relationship-policy.md`
