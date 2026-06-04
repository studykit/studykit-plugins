## jira body-bearing writes

Every body-bearing write (publish / comment / update) shares this shape:

1. Draft the body to a temp file. A leading YAML frontmatter block is
   stripped before posting.
2. Present the draft + metadata + (for updates) the issue key to the
   user and wait for approval.
3. Run the matching `spectrack issue <verb>` invocation.

The script runs a per-target content fingerprint check, applies the
mutation, refreshes the cache, deletes the body file on success, and
returns the cached `issue.md` path with the issue key. The issue is
re-fetched after the write — the body is normalized provider-side, so
the cached projection must come from the provider, not the authored
file.

On `status=conflict` the targeted artifact changed on the provider
since it was last fetched. The script refreshes the cache, preserves
the body file, and returns `reread_paths` — the readable projections
(`issue.md` / `relation.md` / `comment-*.md`). Reread those paths,
reapply your change to the body file, and retry; or rerun the same verb
with `--overwrite` to replace the provider copy without rereading.

Per-intent detail:

- `../issue-new/jira.md` — publish a new issue
- `../issue-comment/jira.md` — append a comment
- `../issue-update/jira.md` — update body, title, labels, or state
- `../issue-link/jira.md` — add / remove / replace relationships
- `../issue-state/jira.md` — body-less changes (state, assign,
  unassign, set-type)

Run `spectrack issue <verb> --help` for a flag not documented above.
