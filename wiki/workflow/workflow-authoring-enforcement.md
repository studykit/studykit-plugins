# Workflow Authoring Enforcement

## Purpose

Workflow authoring enforcement keeps workflow artifact edits grounded in the
correct plugin-bundled authoring contracts without exposing implementation
commands to the main assistant.

The operational rule is:

```text
required_authoring_files are read before a workflow artifact write
```

## Layer Boundaries

### Main assistant

The main assistant resolves required authoring paths through the workflow
launcher (`$WORKFLOW authoring_resolver.py --type <type> --role <role> --json`),
reads the returned files directly, drafts content, and runs the matching
provider/cache scripts (`$WORKFLOW github_issue_drafts.py publish`,
`*_writeback.py update`, `*_comments.py append`, `*_relationships.py`, etc.)
for writes and verification.

Detailed launcher usage, authoring path resolution, and the body-file write
contract live in on-demand main-assistant context policy files under
`plugins/workflow/hooks/context/main/policy/`.

### Workflow scripts

The bundled workflow scripts under `plugins/workflow/scripts/` resolve
authoring paths and perform provider/cache writes. The authoring resolver
returns:

- Required authoring file paths.
- Artifact type, role, and provider context when relevant.

Provider mutation scripts return operational metadata, the cached
`issue.md` / `snapshot.md` path, the issue ref, and verification details.
They do not summarize provider body content.

### Plugin contributors

Plugin contributors may inspect resolver, launcher, hook, cache, and test
implementation details while editing `plugins/workflow/`. Keep those details in
source code, tests, or contributor-facing documentation, not in main-agent
runtime guidance.

## Authoring Contract Source

Runtime authoring contracts live under `plugins/workflow/authoring/`.

Common contracts are provider-neutral. Provider contracts define provider
identity, relationship authoring boundaries, and provider-specific body rules.
Type-specific contracts define the body content expected for each artifact type.

For issue-backed `task` artifacts, a GitHub-backed resolution includes:

1. `common/issue-body.md`
2. `common/issue-authoring.md`
3. `common/task-authoring.md`
4. `providers/github-issue-convention.md`
5. `providers/github-issue-relationships.md`
6. `providers/github-issue-task-authoring.md`
7. Provider guardrails such as `providers/github-issue-anti-patterns.md`

Other artifact types and providers use the same layering: common contracts
first, then role, type, provider convention, provider relationship boundaries,
provider type binding, and provider guardrails when available. Relationship
files define provider-native relationship intent, body-boundary rules, and
operator handoff expectations.

## Intended Flow

1. SessionStart injects only the concise workflow policy entry point when
   `.workflow/config.yml` exists; detail files under
   `plugins/workflow/hooks/context/main/policy/` are loaded on demand.
2. Before a workflow artifact write, the main assistant runs
   `$WORKFLOW authoring_resolver.py --type <type> --role <role> --json` for
   required authoring paths.
3. If the resolver returns `NONE`, the target is not a workflow artifact for
   authoring-policy purposes.
4. The main assistant reads every returned authoring file and drafts the
   content.
5. The main assistant runs the matching workflow script (publish/append/
   update/relationships/metadata/fetch) for provider/cache writes, freshness
   checks, cache refresh, and verification, following the body-file flow.

## Scope

This policy applies to:

- Issue-backed artifacts.
- Knowledge-backed artifacts.
- Dual artifacts such as `usecase` and `research`.
- Local cache projections.
- Native provider writes.
- Provider/cache fallback paths handled by workflow scripts.

## Current Limitations

- Authoring-path discovery proves the required files were selected, not that the
  caller semantically applied every rule.
- Provider metadata capabilities vary by backend and project configuration.
- Non-workflow files intentionally return `NONE`; plugin contributor rules live
  outside this workflow artifact policy.

## Change Log

- 2026-05-13 — [#28](https://github.com/studykit/studykit-plugins/issues/28) — Published curated authoring enforcement page in repository `wiki/` directory.
- 2026-05-13 — [#30](https://github.com/studykit/studykit-plugins/issues/30) — Documented SessionStart authoring policy injection.
- 2026-05-13 — [#31](https://github.com/studykit/studykit-plugins/issues/31) — Documented hook read recording and local projection write guarding.
- 2026-05-16 — [#65](https://github.com/studykit/studykit-plugins/issues/65) — Reframed authoring enforcement around main, operator, and contributor boundaries.
