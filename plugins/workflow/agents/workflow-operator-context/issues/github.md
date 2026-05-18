## configured issue commands

Use only the GitHub issue command family for this project. Invoke each
script via the workflow launcher: `$WORKFLOW <script>.py ...`. The launcher
resolves single-name scripts against its own directory, so no path prefix
is needed.

Do not use another issue provider command family in this project.

### Authoring path resolution

Resolve authoring paths with `$AUTHORING_RESOLVER --type <type> --role issue --json`.
The resolver returns absolute paths under `required_authoring_files`; pass
those paths back to the caller without reading them.

For comment-only requests, add `--scope comment` so the caller reads only
the Markdown and GitHub issue convention files.

### Fetch and lifecycle

- `$WORKFLOW github_issue_fetch.py` — fetch or refresh issues.
- `$WORKFLOW github_issue_lifecycle.py close` — close an issue.
- `$WORKFLOW github_issue_lifecycle.py reopen` — reopen an issue.

### Publish a new issue

Publish with `$WORKFLOW github_issue_drafts.py publish`. The caller supplies:

- Metadata flags: `--type`, `--title`, `--label`, `--state`, `--state-reason`.
- `--body-file <path>` — opaque body content, no frontmatter.

Publish only after explicit user approval. On success the script publishes,
refreshes the cache, deletes the body file, and returns the cached
`issue.md` path along with the issue ref and verified flag; return those to
the caller. On failure the body file is preserved so the caller can retry.

Apply relationships separately with `$WORKFLOW github_issue_relationships.py`
against the freshly-published issue when the caller's metadata included
relationship intent.

### Append a comment

Append with `$WORKFLOW github_issue_comments.py append`. The caller supplies:

- `--issue <ref>` — target issue.
- `--body-file <path>` — opaque body, no frontmatter.
- Optional `--state open|closed` and
  `--state-reason completed|not_planned|reopened` to change the issue state
  on the same call.

Append only after explicit user approval. The script runs a freshness check
on both the issue body and the comments target before posting. On success
it posts the comment, applies any requested state change, refreshes the
cache, deletes the body file, and returns the cached `issue.md` path along
with the issue ref, the posted comment, and whether state changed.

On freshness drift it returns `status=blocked` with `reread_required=true`,
preserves the body file, and applies no state change — tell the main agent
to reread the listed cache paths before retrying.

Apply relationship intent separately through
`$WORKFLOW github_issue_relationships.py`.

### Update an existing issue body

Update with `$WORKFLOW github_issue_writeback.py update`. The caller supplies:

- `--issue <ref>` — target issue.
- `--body-file <path>` — opaque body, no frontmatter.
- Optional `--title`, repeatable `--label`, `--state open|closed`,
  `--state-reason completed|not_planned|reopened` to update metadata or
  change state on the same call.

Update only after explicit user approval. The script runs a freshness check
on the issue body before mutation. On success it edits the issue, applies
any requested state change, refreshes the cache, deletes the body file, and
returns the cached `issue.md` path along with the issue ref, the verified
flag, and whether state changed.

On freshness drift it returns `status=blocked` with `reread_required=true`,
preserves the body file, and applies no metadata or state change — tell the
main agent to reread the listed cache paths before retrying.

The cached `issue.md` body is projection-owned and read-only; do not edit
it in place and do not source the new body from the cache. Apply
relationship intent separately through
`$WORKFLOW github_issue_relationships.py`.

### Other mutations

- `$WORKFLOW github_issue_relationships.py` — apply provider-native
  parent/dependency relationships.
- `$WORKFLOW github_issue_metadata.py` — metadata-only updates.

### Error handling

- Provider mutation scripts refresh affected cache projections internally.
- If a mutation response has `status=blocked` and `reread_required=true`,
  stop and tell the main agent to reread the listed cache paths before
  retrying.
- If a requested provider operation is unsupported, return that limitation
  and tell the main agent to decide whether to use a raw provider CLI
  outside the operator. Do not guess another provider command.
