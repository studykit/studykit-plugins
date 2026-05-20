# Workflow Plugin

Provider-backed workflow over GitHub Issues, Jira, GitHub repository `wiki/`
files, and Confluence.

The plugin keeps issue-backed work tracking separate from knowledge-backed
documentation. The provider is the source of truth.

## Runtime Surface

Key files:

- `.claude-plugin/plugin.json` — Claude plugin metadata.
- `.codex-plugin/plugin.json` — Codex plugin metadata.
- `hooks/hooks.json` — Claude hook declarations.
- `hooks/hooks.codex.json` — Codex hook declarations.
- `main-context/` — main-assistant policy fragments
  (always-loaded entry point + on-demand `policy/` detail files).
- `scripts/` — provider, cache, and hook entrypoints.
- `authoring/` — workflow artifact authoring contracts.

Use `hooks/README.md` for hook-specific behavior. Use
`../../wiki/workflow/workflow-configuration.md` for the configuration schema.

## Configuration

A configured project has `.workflow/config.yml` at the repository root.

Minimal shape:

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

Inspect resolved configuration:

```bash
"./plugins/workflow/scripts/workflow" workflow_config.py \
  --require \
  --json
```

The `scripts/workflow` launcher is the shell-tool entrypoint. It executes the
requested workflow script directly for Claude sessions and reads generated
exports from the Codex session-state file before execution for Codex sessions.
In a plain terminal, it falls back to local defaults for `WORKFLOW`,
`WORKFLOW_PLUGIN_ROOT`, and `WORKFLOW_PROJECT_DIR` without inventing a
`WORKFLOW_SESSION_ID`. Hooks publish `WORKFLOW`, `WORKFLOW_PLUGIN_ROOT`,
`WORKFLOW_PROJECT_DIR`, and `WORKFLOW_SESSION_ID` so repeated assistant shell
commands do not need to pass plugin root, project root, or session id flags.
When the launcher runs bundled Python scripts, it uses `uv run --script` so
scripts can declare inline dependencies such as `python-frontmatter` for
Markdown frontmatter and `PyYAML` for `.workflow/config.yml`.

## Authoring Policy

Workflow authoring contracts apply only to workflow artifact types:

- Issue-backed: `task`, `bug`, `spike`, `epic`, and `review`.
- Knowledge-backed: `spec`, `architecture`, `domain`, `context`, `nfr`, and
  `ci`.
- Dual-role: `usecase` and `research`.

Before editing a workflow artifact, resolve the required authoring paths via
`"$WORKFLOW" authoring_resolver.py --type <type> --role <role> --json`, then
read the returned files from `authoring/`. For non-workflow artifacts, such
as `AGENTS.md`, `CLAUDE.md`, plugin README files, ordinary docs outside
configured workflow knowledge, or host configuration files, the resolver
returns `NONE`.

## Workflow Scripts

The main assistant runs all workflow provider, cache, and authoring
operations through the workflow launcher, with runtime-specific guidance
under `main-context/policy/launcher/<runtime>.md`
(Claude uses the persisted `$WORKFLOW` contract; Codex invokes the
launcher by absolute path). Detailed procedures — launcher invocation,
authoring path resolution, and the publish/append/update body-file
contract — live as on-demand files under
`main-context/policy/`. The always-loaded entry point at
`main-context/session-policy.md` carries only the role
boundary and pointers to those detail files.

Scripts cover:

- Status and completion checks for provider-backed workflow issues.
- Cache-aware provider reads and refresh.
- GitHub and Jira issue writes through `*_drafts.py`, `*_writeback.py`,
  `*_comments.py`, `*_relationships.py`, and `*_metadata.py`.
- Authoring path discovery via `authoring_resolver.py`.
- Provider mutation verification and freshness-checked cache refresh.

Scripts return operational metadata, paths, relationship metadata, and
verification details. They do not summarize issue bodies, comments, or
knowledge page content; the main assistant reads and interprets content
directly.

## Hooks

Session hooks are intentionally concise:

- `SessionStart` injects configured workflow policy only for main sessions.
- `UserPromptSubmit` prepares cache projections for mentioned GitHub issue
  references and injects project-relative cache paths.
- Workflow manifests do not register `Stop`; there is no stop-time cache
  mutation.
- `PreToolUse` on writes protects provider cache issue body projections from
  unsafe frontmatter edits.

Non-workflow projects receive no workflow hook output.

## Cache Projections

GitHub issue reads may be cached under `.workflow-cache/`, which is ignored by
Git.

Treat cache layout and projection schemas as workflow-script internals.
Provider mutation scripts return the editable cache path and refresh the
projection after every successful write; do not edit `issue.md` or
`comment-*.md` files in place. Use the matching fetch / writeback /
comments / relationships script for explicit refresh, write-back,
comment, or relationship operations (see
`main-context/policy/provider-writes.md`).

## Validation

Run workflow plugin tests:

```bash
uv run --with pytest --with python-frontmatter --with PyYAML pytest plugins/workflow/tests
```
