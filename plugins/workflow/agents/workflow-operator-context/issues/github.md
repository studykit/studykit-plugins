## configured issue commands

Use only the GitHub issue command family for this project:

```bash
ISSUE_FETCH=github_issue_fetch.py
ISSUE_DRAFTS=github_issue_drafts.py
ISSUE_LIFECYCLE=github_issue_lifecycle.py
ISSUE_WRITEBACK=github_issue_writeback.py
ISSUE_COMMENTS=github_issue_comments.py
ISSUE_RELATIONSHIPS=github_issue_relationships.py
ISSUE_METADATA=github_issue_metadata.py
```

Do not use another issue provider command family in this project.

Resolve authoring paths with `authoring_resolver.py`.
For comment-only requests, resolve authoring paths with the resolver's comment
scope so the caller reads only the Markdown and GitHub issue convention files.
Fetch or refresh issues with `$ISSUE_FETCH`.
Use `$ISSUE_LIFECYCLE close` or `$ISSUE_LIFECYCLE reopen` for supported provider
lifecycle mutations.
Publish new provider issues with `$ISSUE_DRAFTS publish`. The caller supplies
the metadata (`--type`, `--title`, `--label`, `--state`, `--state-reason`) and
an opaque body file path (`--body-file`); the file must not contain
frontmatter. Publish only after explicit user approval. On success the script
publishes, refreshes the cache, deletes the body file, and returns the cached
`issue.md` path along with the issue ref and verified flag; return those to
the caller. On failure the body file is preserved so the caller can retry.
Apply relationships separately with `$ISSUE_RELATIONSHIPS` against the
freshly-published issue when the caller's metadata included relationship
intent.
Append a new comment with `$ISSUE_COMMENTS append`. The caller supplies the
issue ref (`--issue`) and an opaque body file path (`--body-file`); the file
must not contain frontmatter. Optional `--state open|closed` and
`--state-reason completed|not_planned|reopened` ride along on the same call
to change the issue state inline. Append only after explicit user approval.
The script runs a freshness check on both the issue body and the comments
target before posting. On success it posts the comment, applies any
requested state change, refreshes the cache, deletes the body file, and
returns the cached `issue.md` path along with the issue ref, the posted
comment, and whether state changed. On freshness drift it returns
`status=blocked` with `reread_required=true`, preserves the body file, and
applies no state change — tell the main agent to reread the listed cache
paths before retrying. Apply relationship intent separately through
`$ISSUE_RELATIONSHIPS`.
Update an existing issue body with `$ISSUE_WRITEBACK update`. The caller
supplies the issue ref (`--issue`) and an opaque body file path
(`--body-file`); the file must not contain frontmatter. Optional `--title`,
repeatable `--label`, `--state open|closed`, and `--state-reason
completed|not_planned|reopened` ride along on the same call to update
metadata or change state inline. Update only after explicit user approval.
The script runs a freshness check on the issue body before mutation. On
success it edits the issue, applies any requested state change, refreshes
the cache, deletes the body file, and returns the cached `issue.md` path
along with the issue ref, the verified flag, and whether state changed. On
freshness drift it returns `status=blocked` with `reread_required=true`,
preserves the body file, and applies no metadata or state change — tell the
main agent to reread the listed cache paths before retrying. The cached
`issue.md` body is projection-owned and read-only; do not edit it in place
and do not source the new body from the cache. Apply relationship intent
separately through `$ISSUE_RELATIONSHIPS`.
Use `$ISSUE_LIFECYCLE`, `$ISSUE_RELATIONSHIPS`, and `$ISSUE_METADATA` for
the remaining provider/cache mutations they support.
Provider mutation scripts refresh affected cache projections internally.
If a mutation response has `status=blocked` and `reread_required=true`, stop and
tell the main agent to reread the listed cache paths before retrying.
If a requested provider operation is unsupported, return that limitation and
tell the main agent to decide whether to use a raw provider CLI outside the
operator. Do not guess another provider command.
