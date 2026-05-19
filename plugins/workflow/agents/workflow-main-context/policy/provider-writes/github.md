## github issue writes

The three provider-write intents — publish a new issue, append a comment,
and update an existing issue body — share one shape:

1. Resolve and read the authoring paths
   (`"$WORKFLOW" authoring_resolver.py ...`; see `../authoring.md`).
2. Write the body to a temp file you choose; body content only, no YAML
   frontmatter delimiter at the top. The cached `issue.md` body is
   read-only — do not edit it in place when updating.
3. Present the metadata, issue ref (when applicable), and draft body to
   the user and wait for explicit approval.
4. Run the matching script with `--body-file <path>`, the required refs,
   and any optional metadata, state change, or relationship intent.
5. The script runs the required freshness check, applies the mutation,
   refreshes the cache, deletes the temp file on success, and returns the
   cached `issue.md` path with the issue ref and verification result. On
   freshness drift it returns `status=blocked` with the cache paths to
   reread; reread them and retry. Relationship intent triggers a follow-up
   `github_issue_relationships.py` call.

## Publish a new issue

```bash
"$WORKFLOW" github_issue_drafts.py publish \
  --type <task|bug|spike|epic|review|usecase|research> \
  --title <title> \
  --body-file <path> \
  [--label <label> ...] \
  [--state open|closed] \
  [--state-reason completed|not_planned|reopened] \
  [--parent <ref>] [--blocked-by <ref> ...] [--blocking <ref> ...] \
  [--child <ref> ...] [--related <ref> ...] \
  --json
```

Required: `--type`, `--title`, `--body-file`. `--state` defaults to `open`.
Relationship flags (add-only on publish) apply the relationships against
the newly created issue after the create succeeds.

## Append a comment

```bash
"$WORKFLOW" github_issue_comments.py append \
  --issue <ref> \
  --body-file <path> \
  [--type <type>] \
  [--state open|closed] \
  [--state-reason completed|not_planned|reopened] \
  --json
```

Required: `--issue`, `--body-file`. `--type` defaults to `task`. `--state`
and `--state-reason` apply an inline state change on the same call.

## Update an existing issue body

```bash
"$WORKFLOW" github_issue_writeback.py update \
  --issue <ref> \
  --body-file <path> \
  [--type <type>] \
  [--title <title>] \
  [--label <label> ...] \
  [--state open|closed] \
  [--state-reason completed|not_planned|reopened] \
  [--parent <ref> | --replace-parent <ref> | --remove-parent] \
  [--blocked-by <ref> ...] [--remove-blocked-by <ref> ...] \
  [--blocking <ref> ...]  [--remove-blocking <ref> ...] \
  [--child <ref> ...]     [--remove-child <ref> ...] \
  [--related <ref> ...]   [--remove-related <ref> ...] \
  --json
```

Required: `--issue`, `--body-file`. Optional metadata flags apply on the
same call. Relationship flags (full add/remove/replace set) apply the
relationships against the same issue after the update succeeds. No
relationship flag means no relationship change.

## Relationships: add, remove, or replace

Single-call shape. The script builds inline intent from the flags, asks the
provider to apply it directly, and refreshes the cache. No flag means no
provider call (no-op).

```bash
"$WORKFLOW" github_issue_relationships.py <source-issue> \
  [--parent <ref> | --replace-parent <ref> | --remove-parent] \
  [--blocked-by <ref> ...] [--remove-blocked-by <ref> ...] \
  [--blocking <ref> ...]  [--remove-blocking <ref> ...] \
  [--child <ref> ...]     [--remove-child <ref> ...] \
  [--related <ref> ...]   [--remove-related <ref> ...] \
  [--type <type>] --json
```

Flag semantics:

- `--parent <ref>` — add parent; errors if a parent already exists.
- `--replace-parent <ref>` — set parent, replacing any existing parent.
- `--remove-parent` — detach the current parent; no-op when none exists.
- `--blocked-by`, `--blocking`, `--child`, `--related` (repeatable) — add
  the link.
- `--remove-blocked-by`, `--remove-blocking`, `--remove-child`,
  `--remove-related` (repeatable) — remove the specified link by ref.
- Add and remove flags may mix in one call. The same ref cannot appear in
  both add and remove for the same relationship (the script errors).
- Idempotent: adding an existing link is a no-op; removing a missing link
  is a no-op.
- `--parent`, `--replace-parent`, `--remove-parent` are mutually exclusive.
- GitHub has no native `related` link — `--related` lands as a body
  section fallback. See
  `../../../../authoring/providers/github-issue-relationships.md` for
  canonical intent usage (`parent`, `blocked_by`; invert source/target for
  `child`/`blocking`).

The same relationship flags can be supplied directly to `publish` and
`update` to apply relationships in one call after the issue create or
update.

## Other scripts

| Intent          | Script                                    |
|-----------------|-------------------------------------------|
| Metadata only   | `github_issue_metadata.py`                |
| Lifecycle       | `github_issue_lifecycle.py close|reopen`  |

Run `"$WORKFLOW" <script>.py --help` only when you need a flag not listed
above.

## Body-file lifecycle

- The script deletes the body file on success.
- The body file is preserved on `status=blocked` (freshness drift) and on
  any other failure, so the caller can retry without redrafting.
- Body files must not start with a YAML frontmatter delimiter (`---`).

## On freshness drift

If a mutation response has `status=blocked` and `reread_required=true`,
stop, reread the listed cache paths, and only then retry. Do not bypass
the freshness check.

## Do not call other provider families

Use only the GitHub issue script family for this project. Do not call
`jira_issue_*.py` scripts when GitHub is the configured issue provider.
