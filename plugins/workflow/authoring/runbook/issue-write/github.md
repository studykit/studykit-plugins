## github body-bearing writes

Every body-bearing write (publish / comment / update) shares this shape:

1. Draft the body to a temp file. A leading YAML frontmatter block is
   stripped before posting.
2. Present the draft + metadata + (for updates) the issue ref to the
   user and wait for approval.
3. Run the matching `workflow issue <verb>` invocation.

The script runs the freshness check, applies the mutation, refreshes
the cache, deletes the body file on success, and returns the cached
`issue.md` path with the issue ref. On `status=blocked` (freshness
drift) the body file is preserved — reread the listed cache paths,
then retry. Never bypass the freshness check.

Per-intent detail:

- `../issue-new/github.md` — publish a new issue
- `../issue-comment/github.md` — append a comment
- `../issue-update/github.md` — update body, title, labels, or state
- `../issue-link/github.md` — add / remove / replace relationships
- `../issue-state/github.md` — body-less changes (state, assign,
  unassign, set-type)

Run `workflow issue <verb> --help` for a flag not documented above.
