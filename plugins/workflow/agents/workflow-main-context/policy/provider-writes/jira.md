## jira issue writes

The provider-write intents share one shape:

1. Resolve and read the authoring paths
   (`"$WORKFLOW" authoring_resolver.py ...`; see `../authoring.md`).
2. Write the body to a temp file you choose; body content only, no YAML
   frontmatter delimiter at the top. The cached `snapshot.md` body is
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
  [--parent <KEY>] [--blocked-by <KEY> ...] [--blocking <KEY> ...] \
  [--child <KEY> ...] [--related <KEY-or-URL> ...] \
  --json
```

Required: `--type`, `--title`, `--body-file`. Use `--issue-type` when the
Jira issue type must be set at create time. Use `--subtask-parent` when
publishing a Sub-task. Relationship flags (add-only on publish) apply the
relationships against the newly created issue after the create succeeds.

## Append a comment

Body-file flow for Jira comment append is being migrated; the current CLI
still uses the legacy bare-refs shape. Run
`"$WORKFLOW" jira_issue_comments.py --help` for current usage.

## Update an existing issue body

Body-file flow for Jira body update is being migrated; the current CLI
still uses the legacy bare-refs shape. Run
`"$WORKFLOW" jira_issue_writeback.py --help` for current usage.

## Relationships: add, remove, or replace

Single-call shape. The script builds inline intent from the flags, asks the
provider to apply it directly against configured Jira link types and remote
link surfaces, and refreshes the cache. No flag means no provider call
(no-op).

```bash
"$WORKFLOW" jira_issue_relationships.py <source-issue> \
  [--parent <KEY> | --replace-parent <KEY> | --remove-parent] \
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

See `../../../../authoring/providers/jira-issue-relationships.md` for
canonical intent usage (`parent`, `blocked_by`, `related`; invert
source/target for `child`/`blocking`).

The same relationship flags can be supplied directly to `publish` to apply
relationships in one call after the issue create.

## Other scripts

| Intent          | Script                                |
|-----------------|---------------------------------------|
| Metadata only   | `jira_issue_metadata.py`              |
| Lifecycle       | (state via writeback flags)           |

Run `"$WORKFLOW" <script>.py --help` only when you need a flag not listed
above.

## Body-file lifecycle (publish only, until migration)

- The script deletes the body file on success.
- The body file is preserved on `status=blocked` (freshness drift) and on
  any other failure, so the caller can retry without redrafting.
- Body files must not start with a YAML frontmatter delimiter (`---`).

## On freshness drift

If a mutation response has `status=blocked` and `reread_required=true`,
stop, reread the listed cache paths, and only then retry. Do not bypass
the freshness check.

## Do not call other provider families

Use only the Jira issue script family for this project. Do not call
`github_issue_*.py` scripts when Jira is the configured issue provider.
