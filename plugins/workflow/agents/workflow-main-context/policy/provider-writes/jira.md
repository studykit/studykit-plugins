## jira issue writes

The provider-write intents share one shape:

1. Resolve and read the authoring paths
   (`"$WORKFLOW" authoring_resolver.py ...`; see `../authoring.md`).
2. Write the body to a temp file you choose. Body content is what gets
   sent; if the file happens to start with a YAML frontmatter block, the
   script strips it before posting. The cached `snapshot.md` body is
   read-only — do not edit it in place when updating.
3. Present the metadata, issue ref (when applicable), and draft body to
   the user and wait for explicit approval.
4. Run the matching script (see below) and supply the required refs,
   `--body-file <path>` when the script accepts it, and any optional
   metadata or state change.
5. The script runs the required freshness check, applies the mutation,
   refreshes the cache, deletes the body file on success (when body-file
   flow is supported), and returns the cached `snapshot.md` path with the
   issue key and verification result. On freshness drift it returns
   `status=blocked` with the cache paths to reread; reread them and retry.
   Relationship intent triggers a follow-up `jira_issue_relationships.py`
   call.

## Publish a new issue

```bash
"$WORKFLOW" jira_issue_drafts.py publish \
  --type <task|bug|spike|epic|review|usecase|research> \
  --title <title> \
  --body-file <path> \
  [--label <label> ...] \
  [--issue-type <jira-issue-type>] \
  [--subtask-parent <PARENT-KEY>] \
  [--project-key <PROJECT>] \
  [--epic-name <X>] \
  [--parent <KEY>] [--epic <KEY>] [--blocked-by <KEY> ...] [--blocking <KEY> ...] \
  [--child <KEY> ...] [--related <KEY-or-URL> ...] \
  --json
```

Required: `--type`, `--title`, `--body-file`. Use `--issue-type` when the
Jira issue type must be set at create time. Use `--subtask-parent` when
publishing a Sub-task. Relationship flags (add-only on publish) apply the
relationships against the newly created issue after the create succeeds.

`--epic-name` overrides the Epic Name customfield at create time and is
valid only with `--type epic` (defaults to `--title`); supplying it for any
other type errors. `--epic <KEY>` adds an Epic Link from the newly created
issue to that Epic after publish; rejected when `--type epic`. Epic create
also requires `providers.issues.epic_fields.name` to be configured (see the
setup skill); missing config raises `ProviderOperationError`.

## Append a comment

```bash
"$WORKFLOW" jira_issue_comments.py append \
  --issue <KEY> \
  --body-file <path> \
  [--type <task|bug|...>] \
  [--state <verb>] \
  --json
```

Required: `--issue`, `--body-file`. `--state` is a free-form verb keyed in
`providers.issues.state_transitions.<verb>`; the script looks up the
configured transition name and POSTs that transition after the comment is
added. State-transition mappings are a setup-time prereq — discover the
workflow's transitions with `workflow_setup.py jira-state-transition-inspect`
and confirm them into the config through the setup skill's State Transition
Profiling step; an unknown verb (or a config with no `state_transitions`
section) raises `ProviderOperationError`.

## Update an existing issue body

```bash
"$WORKFLOW" jira_issue_writeback.py update \
  --issue <KEY> \
  --body-file <path> \
  [--type <task|bug|...>] \
  [--title <title>] \
  [--add-label <label> ...] [--remove-label <label> ...] \
  [--set-labels <label,label,...>] \
  [--state <verb>] \
  --json
```

Required: `--issue`, `--body-file`. At least one of body, title, labels,
or state must change. `--add-label` / `--remove-label` are repeatable;
`--set-labels` takes a single comma-separated list and replaces the entire
label set. Combining `--set-labels` with `--add-label` or `--remove-label`
exits with a clear error. Optional `--title` and `--state` ride along on
the same call. `--state` is a free-form verb keyed in
`providers.issues.state_transitions.<verb>` (see comment append) — discover
and confirm verbs through the setup skill's State Transition Profiling step
before relying on `--state` writes.

## Relationships: add, remove, or replace

Single-call shape. The script builds inline intent from the flags, asks the
provider to apply it directly against configured Jira link types and remote
link surfaces, and refreshes the cache. No flag means no provider call
(no-op).

```bash
"$WORKFLOW" jira_issue_relationships.py <source-issue> \
  [--parent <KEY> | --replace-parent <KEY> | --remove-parent] \
  [--epic <KEY> | --replace-epic <KEY> | --remove-epic] \
  [--blocked-by <KEY> ...] [--remove-blocked-by <KEY> ...] \
  [--blocking <KEY> ...]  [--remove-blocking <KEY> ...] \
  [--child <KEY> ...]     [--remove-child <KEY> ...] \
  [--related <KEY-or-URL> ...] [--remove-related <KEY-or-URL> ...] \
  [--type <type>] --json
```

Flag semantics:

- `--parent <KEY>` — add parent; errors if a parent already exists.
- `--replace-parent <KEY>` — set parent, replacing any existing parent.
- `--remove-parent` — detach the current parent; no-op when none exists.
- `--epic <KEY>` — set Epic Link; errors if an Epic Link already exists.
- `--replace-epic <KEY>` — set Epic Link, replacing the current value.
- `--remove-epic` — clear the Epic Link; no-op when none exists.
- `--blocked-by`, `--blocking`, `--child`, `--related` (repeatable) — add
  the link. `--related` uses the configured remote-link mapping and
  accepts a Jira key or absolute URL.
- `--remove-blocked-by`, `--remove-blocking`, `--remove-child`,
  `--remove-related` (repeatable) — remove the specified link.
- Add and remove flags may mix in one call. Overlapping refs in add and
  remove for the same relationship error.
- Idempotent: adding an existing link is a no-op; removing a missing link
  is a no-op.
- `--parent`, `--replace-parent`, `--remove-parent` are mutually exclusive.
- `--epic`, `--replace-epic`, `--remove-epic` are mutually exclusive among
  themselves but independent of the parent group; `parent` and `epic` may
  both appear in a single call against the same issue (Epic Link is a
  separate customfield from `parent`).

See `../../../../authoring/providers/jira-issue-relationships.md` for
canonical intent usage (`parent`, `blocked_by`, `related`; invert
source/target for `child`/`blocking`).

The same relationship flags can be supplied directly to `publish` to apply
relationships in one call after the issue create.

## Other scripts

| Intent           | Script                                                          |
|------------------|-----------------------------------------------------------------|
| Body-less change | `jira_issue_fields.py {<verb> ...|assign|unassign|set-type}`   |

`jira_issue_fields.py` covers state transitions, assignee changes, and
issuetype swaps. Lifecycle subcommands are dynamic: one subcommand per
`<verb>` key in `providers.issues.state_transitions`. Each takes
`<issue> [--comment <text>]` and POSTs the configured transition.
`assign` / `unassign` / `set-type` are reserved static subcommands and
cannot be overridden by a verb of the same name (setup rejects those
verbs at config time). Invoking an unknown verb prints the configured
verb list, the reserved verbs, and the config path on stderr and exits
non-zero. `assign me` resolves the current Jira user via
`/rest/api/<v>/myself`. `set-type` PUTs `fields.issuetype` using the
`artifact_issue_types` mapping (built-in defaults plus
`.workflow/config.yml` overrides). Use `jira_issue_writeback.py update`
when the change must also rewrite the body or title.

Run `"$WORKFLOW" <script>.py --help` only when you need a flag not listed
above.

## Body-file lifecycle

- The script deletes the body file on success.
- The body file is preserved on `status=blocked` (freshness drift) and on
  any other failure, so the caller can retry without redrafting.
- A leading YAML frontmatter block is stripped before the body is sent.

## On freshness drift

If a mutation response has `status=blocked` and `reread_required=true`,
stop, reread the listed cache paths, and only then retry. Do not bypass
the freshness check.

## Do not call other provider families

Use only the Jira issue script family for this project. Do not call
`github_issue_*.py` scripts when Jira is the configured issue provider.
