## jira issue writes

The provider-write intents share one shape:

1. Resolve and read the authoring paths
   (`workflow authoring_resolver.py ...`; see `../authoring.md`).
2. Write the body to a temp file you choose. Body content is what gets
   sent; if the file happens to start with a YAML frontmatter block, the
   script strips it before posting. The cached `issue.md` (frontmatter
   metadata + issue body) and sibling `comment-*.md` files are read-only —
   do not edit them in place when updating.
3. Present the metadata, issue ref (when applicable), and draft body to
   the user and wait for explicit approval.
4. Run the matching `issue.py <verb>` invocation (see below) and supply
   the required refs, `--body-file <path>` when the verb accepts it, and
   any optional metadata or state change.
5. The script runs the required freshness check, applies the mutation,
   refreshes the cache, deletes the body file on success (when body-file
   flow is supported), and returns the cached `issue.md` path with the
   issue key and verification result. On freshness drift it returns
   `status=blocked` with the cache paths to reread; reread them and retry.
   Relationship intent triggers a follow-up `issue.py link` call.

## Publish a new issue

```bash
workflow issue new \
  --type <task|bug|spike|epic|review|usecase|research> \
  --title <title> \
  --body-file <path> \
  [--label <label> ...] \
  [--issue-type <jira-issue-type>] \
  [--subtask-parent <PARENT-KEY>] \
  [--project-key <PROJECT>] \
  [--epic-name <X>] \
  [--assignee <user>] \
  [--parent <KEY>] [--epic <KEY>] [--blocked-by <KEY> ...] [--blocking <KEY> ...] \
  [--child <KEY> ...] [--related <KEY-or-URL> ...] \
```

Required: `--type`, `--title`, `--body-file`. Use `--issue-type` when the
Jira issue type must be set at create time. Use `--subtask-parent` when
publishing a Sub-task. Relationship flags (add-only on publish) apply the
relationships against the newly created issue after the create succeeds.

### Native Sub-task vs parent issue-link

`--subtask-parent` and `--parent` look interchangeable but produce
structurally different issues. Pick by what the new issue should *be*, not
by which flag name reads better:

| Flag                       | When the create happens | Effect on the new issue                                                          | Config requirement                                       |
|----------------------------|-------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------|
| `--subtask-parent <KEY>`   | At create time          | Forces `issuetype=Sub-task` and sets Jira's native Sub-task parent to `<KEY>`.   | None beyond standard issue-create config.                |
| `--parent <KEY>`           | Post-create             | Adds an issue link to `<KEY>`. Issuetype is unchanged (Task, Bug, etc.).         | `providers.issues.relationship_mappings.parent` must be configured; publish fails after create otherwise. |

Selection guidance:

- Goal is "new Sub-task under `<P>`" — use `--subtask-parent <P>`. The
  resulting issue is a native Jira Sub-task and shows up under `<P>` in
  the Sub-tasks panel.
- Goal is "new Task/Bug/etc. linked to `<P>` as a parent" — use
  `--parent <P>`. The resulting issue keeps its own issuetype and gets
  an issue link of the type configured in `relationship_mappings.parent`.
- When unsure, inspect a sibling under the same parent first: if existing
  siblings are Sub-tasks, use `--subtask-parent`; otherwise use
  `--parent`. (Auto-inspection is intentionally out of scope.)

The two flags are mutually exclusive in practice — using `--parent` does
not create a Sub-task, and using `--subtask-parent` does not add an
extra issue-link relationship.

`--assignee <user>` sets the assignee at create time. The literal `me`
resolves the current Jira user via `/rest/api/<v>/myself` and uses the
returned `name` on the create payload. To clear an assignee on an
existing issue, use `issue.py unassign <KEY>`.

`--epic-name` overrides the Epic Name customfield at create time and is
valid only with `--type epic` (defaults to `--title`); supplying it for any
other type errors. `--epic <KEY>` adds an Epic Link from the newly created
issue to that Epic after publish; rejected when `--type epic`. Epic create
also requires `providers.issues.epic_fields.name` to be configured (see the
setup skill); missing config raises `ProviderOperationError`.

## Append a comment

```bash
workflow issue comment \
  --issue <KEY> \
  --body-file <path> \
  [--type <task|bug|...>] \
  [--state <verb>] \
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
workflow issue update \
  --issue <KEY> \
  --body-file <path> \
  [--type <task|bug|...>] \
  [--title <title>] \
  [--add-label <label> ...] [--remove-label <label> ...] \
  [--set-labels <label,label,...>] \
  [--state <verb>] \
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
workflow issue link <source-issue> \
  [--parent <KEY> | --replace-parent <KEY> | --remove-parent] \
  [--epic <KEY> | --replace-epic <KEY> | --remove-epic] \
  [--blocked-by <KEY> ...] [--remove-blocked-by <KEY> ...] \
  [--blocking <KEY> ...]  [--remove-blocking <KEY> ...] \
  [--child <KEY> ...]     [--remove-child <KEY> ...] \
  [--related <KEY-or-URL> ...] [--remove-related <KEY-or-URL> ...] \
  [--type <type>]
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

The same relationship flags can be supplied directly to `issue.py new`
to apply relationships in one call after the issue create.

## Other verbs

| Intent           | Verb                                                                |
|------------------|---------------------------------------------------------------------|
| Body-less change | `issue.py state <KEY> <verb>` / `issue.py {assign\|unassign\|set-type} ...` |

The `state` / `assign` / `unassign` / `set-type` verbs cover state
transitions, assignee changes, and issuetype swaps. Lifecycle dispatch is
dynamic: `issue.py state <KEY> <verb> [--comment <text>]` accepts any
`<verb>` keyed in `providers.issues.state_transitions` and POSTs the
configured transition. `assign` / `unassign` / `set-type` are reserved
static verbs and cannot be overridden by a configured verb of the same
name (setup rejects those verbs at config time). Invoking an unknown
state verb prints the configured verb list, the reserved verbs, and the
config path on stderr and exits non-zero. `assign <KEY> me` resolves the
current Jira user via `/rest/api/<v>/myself`. `set-type` PUTs
`fields.issuetype` using the `artifact_issue_types` mapping (built-in
defaults plus `.workflow/config.yml` overrides). Use `issue.py update`
when the change must also rewrite the body or title.

Run `workflow issue <verb> --help` only when you need a flag not
listed above.

## Body-file lifecycle

- The script deletes the body file on success.
- The body file is preserved on `status=blocked` (freshness drift) and on
  any other failure, so the caller can retry without redrafting.
- A leading YAML frontmatter block is stripped before the body is sent.

## On freshness drift

If a mutation response has `status=blocked` and `reread_required=true`,
stop, reread the listed cache paths, and only then retry. Do not bypass
the freshness check.

## Dispatcher routing

`issue.py` loads `.workflow/config.yml` and routes to the Jira backend
automatically when `providers.issues.kind` is `jira`. `<verb> --help`
shows only the active backend's options; supplying a GitHub-only flag
exits with a clean parser error.
