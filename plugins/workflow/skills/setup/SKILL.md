---
name: setup
description: Initialize the workflow plugin in a repository by generating and writing .workflow/config.yml, including GitHub, Jira Data Center or Server, filesystem issues, GitHub repository wiki, Confluence Data Center or Server, filesystem knowledge, and Jira site profiling for relationship mappings, fields, Epic configuration, labels, and body format.
disable-model-invocation: true
---

# Workflow Setup

Use this skill to bootstrap the workflow plugin for a project. The only config
file this skill may create or recommend is repository-root `.workflow/config.yml`;
never create or recommend legacy `workflow.config.yml`.

## Entry Points

Resolve the workflow launcher relative to this `SKILL.md` as
`../../scripts/workflow`, then run `workflow_setup.py` through it. In installed
workflow sessions, `$WORKFLOW` may already point to the launcher.

Useful commands:

```bash
"$WORKFLOW" workflow_setup.py probe-git-remote --project <project-root> --json
"$WORKFLOW" workflow_setup.py profile-from-docs <profile-docs...> --json
"$WORKFLOW" workflow_setup.py capabilities --issue-provider <provider> --knowledge-provider <provider> --json
"$WORKFLOW" workflow_setup.py jira-relationship-inspect --jira-site <url> --issue <KEY> --json
"$WORKFLOW" workflow_setup.py jira-relationship-inspect --jira-site <url> --jira-project <PROJECT> --issue <ISSUE-123> --json
"$WORKFLOW" workflow_setup.py jira-relationship-inspect --jira-site <url> --field-query <field-name-or-id> --json
"$WORKFLOW" workflow_setup.py jira-relationship-mappings --issue-link blocked_by=Blocks:inward --field child=parent:target:key --json
"$WORKFLOW" workflow_setup.py build-config --project <project-root> --issue-provider <provider> --knowledge-provider <provider> <options...> --json
"$WORKFLOW" workflow_setup.py build-config --issue-provider jira --knowledge-provider <provider> --jira-snapshot-hidden-comment-marker '!git-event' <options...> --json
"$WORKFLOW" workflow_setup.py build-config --issue-provider jira --knowledge-provider <provider> --jira-epic-field-name <id> --jira-epic-field-link <id> --jira-epic-field-status <id> [--jira-epic-issue-type <NAME>] <options...> --json
"$WORKFLOW" workflow_setup.py write --project <project-root> --config <reviewed-yaml-file> --json
"$WORKFLOW" workflow_config.py --project <project-root> --require --json
```

## Setup Flow

1. Resolve the repository root. Prefer `git rev-parse --show-toplevel`; if the
   project is not a Git repository, use the user's explicit target directory.
2. If `.workflow/config.yml` already exists, summarize its issue provider,
   knowledge provider, local projection mode, and commit reference style. Do not
   overwrite it unless the user explicitly requests overwrite; pass `--force`
   only after that confirmation.
3. Collect the issue provider: `github`, `jira`, or `filesystem`. Ask the user
   when it was not already named explicitly by the user or a provider profile;
   do not infer it from a Git remote or assume GitHub.
4. Collect the knowledge provider: `github`, `confluence`, or `filesystem`.
   Ask the user when it was not already named explicitly by the user or a
   provider profile; do not infer it from the issue provider.
5. If the issue provider is `jira`, run the Jira site profiling flow before
   `capabilities` or `build-config`. Collect representative sample issue keys,
   inspect relationship surfaces, ask the user to confirm exact mappings, and
   generate mapping YAML with `jira-relationship-mappings`. If the sample
   issues or confirmed mappings are unavailable, stop setup as incomplete; do
   not offer to defer Jira relationship setup until later.
6. For Jira issue providers, ask whether generated `snapshot.md` files should
   hide automation comments by body marker. If the user gives markers such as
   `!git-event`, pass each one with
   `--jira-snapshot-hidden-comment-marker`.
7. Collect local projection mode (`none`, `ephemeral`, or `persistent`), local
   projection path when applicable, and commit reference style.
8. Run `capabilities` for the selected providers and show limitations before
   confirmation.
9. Run `build-config --json`, show the generated YAML and warnings to the user,
   and ask for explicit confirmation before writing.
10. After confirmation, write with `write --config <reviewed-yaml-file>`. Then
   verify with `workflow_config.py --require --json`.

## Provider Rules

- GitHub issue setup should use an explicit `owner/repo` slug. If the user has
  not provided one, run `probe-git-remote` and ask before using the detected
  slug. When the issue repository is not on `github.com`, use
  `--github-issue-host`; use `--github-host` only as a shared fallback when the
  issue and knowledge repositories are on the same GitHub host.
- Always pass explicit `--issue-provider` and `--knowledge-provider` values to
  `build-config` or `write` when building config from options. Missing provider
  flags mean setup is incomplete; ask for the provider choice before continuing.
- GitHub knowledge setup represents a repository `wiki/<plugin>/` directory.
  Use `--github-wiki-path`, defaulting to `wiki/workflow` when the user accepts
  that path. If the knowledge/wiki repository host differs from the issue
  repository host, use `--github-wiki-host`.
- Jira setup targets Data Center or Server only. Reject or report Cloud,
  including `*.atlassian.net` sites.
- Confluence setup targets Data Center or Server only. Reject or report Cloud,
  including `*.atlassian.net` sites.
- Jira issue setup requires explicit `providers.issues.relationship_mappings`
  before final config generation. Collect sample issue keys, inspect the Jira
  site, and ask the user to confirm exact mappings. If site data or confirmed
  mappings are unavailable, pause setup as incomplete; do not build or write a
  Jira issue config and do not suggest configuring relationships later. Do not
  infer Jira link type, direction, remote-link surface, parent field,
  `write_to`, or value semantics from prose.
- For Jira relationship setup, use `jira-relationship-inspect` only to show
  observed link types, fields, and sample issue relationship data. Then ask the
  user to confirm the exact mappings and generate the mapping YAML with
  `jira-relationship-mappings`. Feed the confirmed YAML into `build-config`
  with `--jira-relationship-mappings-file` or
  `--jira-relationship-mappings-json`.
- When Jira setup needs site-specific field names, hierarchy semantics,
  issue-type rules, label policy, or body-renderer behavior, run the Jira site
  profiling flow in this skill before building the final config.
- Jira snapshot comment hiding is opt-in. Use
  `providers.issues.snapshot.hidden_comment_markers` only when the user or
  provider profile supplies exact body markers. The markers hide matching
  comments from generated `snapshot.md` files only; raw provider cache files
  still retain the original comments.
- Jira labels are opt-in. Do not copy local labels into Jira unless the user or
  provider profile explicitly asks for label writes.
- Jira Epic configuration (`providers.issues.epic_fields.{name,link,status}`
  and `artifact_issue_types.epic`) is opt-in and site-dependent. When the user
  plans Epic creation or Epic Link writes, source the values from
  `jira-relationship-inspect` (run with `--jira-project` so createmeta is
  available) and pass confirmed ids to `build-config` via
  `--jira-epic-field-name|link|status` and `--jira-epic-issue-type`. Do not
  assume values; if the site lacks Jira Software or returns non-default field
  schema, ask the user for explicit ids.
- Jira Data Center sites may not render Markdown. Report body-format uncertainty
  during setup when users plan Jira issue creation; prefer site-confirmed Jira
  wiki/plain text authoring over Markdown assumptions.
- Provider profile documents may seed defaults only when they explicitly discuss
  workflow providers. Ignore unrelated Git remote or commit-history documents.

## Jira Site Profiling

This flow is required whenever the issue provider is `jira`. Also use it when
Jira setup needs custom fields, issue type rules, label policy, body formatting,
or sub-task behavior. Keep a hard boundary between observed Jira data and
confirmed workflow config: inspect the site, show the evidence, ask for
confirmation, then use only the exact confirmed values in setup.

1. Resolve the Jira site, deployment, API version, and project key from the
   user, provider profile, or `.workflow/config.yml`.
2. Collect sample issue keys for each relationship surface the user cares about:
   an issue with dependencies or related links, a parent issue with sub-tasks, a
   sub-task, and any site-specific hierarchy example.
3. Run `jira-relationship-inspect` for link types, native `parent/subtasks`,
   and requested field queries. When `--jira-project` is supplied, the same
   call returns an `epic` block: Epic Name / Link / Status customfield ids
   discovered by Greenhopper schema or name heuristic, candidate Epic issue
   types from createmeta, per-issue-type Epic Link availability, and warnings.
4. When the user plans Epic creation or Epic Link writes on the site, extract
   `epic.fields.{name,link,status}.id`, `epic.issue_types`, and any
   `epic.warnings` from the inspect output and confirm with the user. When
   `epic.issue_types` returns zero or two-or-more candidates, ask the user for
   the exact Epic issue-type name. If `epic.fields` are missing or
   `epic.warnings` indicate a non-default schema, ask for explicit field ids
   before continuing. Skip this step when the site lacks Jira Software or the
   user has no Epic intent.
5. If issue creation behavior matters, inspect issue type metadata and ask
   before running any create/update test. Sub-task creation is a mutation.
6. Ask the user for the issue body format when it is not already documented.
   Default to `jira_wiki`; use `plain` or `markdown` only when the user or a
   provider profile says that is the right renderer.
7. Determine label policy from the user or provider profile. Labels are opt-in;
   never copy local labels into Jira by default.
8. Determine whether automation comments should be hidden from generated Jira
   snapshots, and record only exact user-confirmed markers.
9. Summarize observed link types, hierarchy surfaces, custom fields, confirmed
   Epic field ids and Epic issue-type, body format guidance, label policy,
   snapshot-hidden comment markers, confirmed relationship mapping YAML, and
   open questions before generating the final config.

Rules:

- Do not hardcode organization values in skills or setup defaults.
- Do not infer `link_type`, `direction`, `surface`, field id, `write_to`, or
  value kind from prose.
- Do not map a custom field to a workflow relationship until the user confirms
  the relationship name and direction.
- Keep portfolio, team, parent-link, or other hierarchy fields site-specific.
  Report what Jira returned; do not assign global semantics.
- Treat `parent` and `child` as Jira native parent/subtask or explicitly
  confirmed hierarchy mappings only.
- Do not assume Epic field ids or Epic issue-type names. Use only values
  confirmed against the `epic` block in `jira-relationship-inspect` output and
  explicit user confirmation. Pass confirmed ids to `build-config` via
  `--jira-epic-field-name|link|status` (and `--jira-epic-issue-type` when the
  Epic issue-type name differs from the default `Epic`).
  `relationship_mappings.epic` is auto-injected by `build-config` when
  `epic_fields.link` is supplied; do not write it manually in
  `--jira-relationship-mappings-file` or `--jira-relationship-mappings-json`.
- Do not create, update, delete, or link Jira issues without explicit user
  approval for that mutation.

## Jira Relationship Mapping Shape

Use `--jira-relationship-mappings-json` or
`--jira-relationship-mappings-file`. Each mapping must include explicit
`surface`.

The compact mapping helper accepts exact relationship specs:

```bash
"$WORKFLOW" workflow_setup.py jira-relationship-mappings \
  --issue-link blocked_by=Blocks:inward \
  --issue-link blocking=Blocks:outward \
  --remote-link "related=relates to" \
  --remote-application-type studykit.workflow \
  --remote-application-name Workflow \
  --field child=parent:target:key \
  --json
```

```yaml
blocked_by:
  surface: issue_link
  link_type: Blocks
  direction: inward
blocking:
  surface: issue_link
  link_type: Blocks
  direction: outward
related:
  surface: remote_link
  relationship_label: relates to
  application_type: studykit.workflow
  application_name: Workflow
```
