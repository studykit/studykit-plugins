# SpecTrack

Issue- and knowledge-backed workflow for Claude Code, Codex, and Hermes
sessions. The plugin treats the configured provider — GitHub Issues, Jira, or a
GitHub repository `wiki/` — as the source of truth and helps the assistant
draft, publish, refresh, and link work items without leaving the session.

## Supported Providers

- **Issues** — GitHub Issues, Jira (Data Center / Server), or a local
  filesystem provider.
- **Knowledge** — GitHub repository `wiki/`.

Issue tracking and knowledge documentation are configured independently, so
mixed setups (e.g., Jira issues + GitHub repository `wiki/`) are supported.

## Installation

Install from the studykit plugin marketplace inside Claude Code or Codex, or
install the plugin directory as a Hermes plugin. The Claude and Codex runtimes
receive the full hook, skill, slash-command, and agent surface. Hermes receives
first-turn workflow policy injection for repositories with `.spectrack/config.yml`
and bundled plugin skills such as `spectrack:handoff`.

For a local Hermes install from this repository:

```bash
ln -s /path/to/studykit-plugins/plugins/spectrack ~/.hermes/plugins/spectrack
hermes plugins enable spectrack
```

## Configuration

Per-project configuration lives at `.spectrack/config.yml` at the repository
root. The fastest way to create it is the bundled setup skill:

```
/setup
```

The skill walks through provider selection, fills in the required fields,
and writes `.spectrack/config.yml`. It also installs the Codex custom-agent
roles used by SpecTrack subagent workflows; restart Codex after setup so the
new `spectrack:*` roles are available.

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
`../../wiki/spectrack/spectrack-configuration.md`.

## Slash Commands

Once configured, the plugin exposes these slash commands:

- `/setup` — Generate and write `.spectrack/config.yml` for the current
  repository.
- `/usecase <idea>` — Walk a rough product idea through a Socratic,
  one-question-at-a-time discovery interview. Each confirmed use case is
  published as its own workflow `usecase` issue. Knowledge side effects
  (new domain concept, NFR, screen, etc.) surface as separate `review`
  issues. At wrap-up the skill dispatches the explorer and reviewer
  subagents to find gaps and quality issues. Run with `iterate` (or an
  existing `usecase` ref) to resume an earlier discovery session.
- `/implement-issue <issue-ref> [extra requirements]` — Execute the
  plan recorded in a `task`, `bug`, or `spike` issue. The issue body
  already carries the plan from when it was created in plan mode; refresh
  it in plan mode only if it has drifted from the current code. The
  command first checks the issue's recorded root cause and approach
  against the current code (see `/audit-resolution`) and pauses if the
  diagnosis looks wrong, then hands the issue (and any refreshed plan) to
  an implementer subagent that implements, verifies the acceptance
  criteria, commits, and pushes a topic branch for you to review and
  merge, after which an auditor subagent cross-checks the result and
  leaves an audit comment on the issue. Pass extra requirements after the
  ref to steer execution.
- `/audit-resolution <issue-ref>` — Validate a published `task` or `bug`
  issue's recorded root cause and proposed approach/fix against the
  actual code and git history. Dispatches an auditor subagent that flags
  when the named cause is not the real cause, or when the approach would
  not actually resolve it, and leaves a single verdict comment on the
  issue.
- `/handoff` — Wrap up a session by refreshing the `Resume` comment of
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
- Searches issues with the provider's native query (GitHub search syntax
  or Jira JQL) and returns a concise list of matching issues to drill into.
- Drafts and publishes new issues, comments, body updates, and
  relationship links through the configured provider.
- Keeps commit subjects prefixed with the related issue reference and the
  PR's `Closes` keyword pointing at the right issue.
- Refreshes in-flight issues at session handoff so the next session can
  pick up from provider issue context.

## Configuration Reference

- Provider configuration schema:
  `../../wiki/spectrack/spectrack-configuration.md`
- Provider model and reference formats:
  `../../wiki/spectrack/spectrack-provider-model.md`,
  `../../wiki/spectrack/spectrack-provider-reference-formats.md`
- Issue relationship policy:
  `../../wiki/spectrack/spectrack-issue-relationship-policy.md`
