## github — fetch issues

```bash
spectrack issue fetch <issue> [<issue> ...] \
  [--cache-policy default|refresh]
```

The script returns the issue `title`/`state` inline plus paths to the
local `issue.md` body, a `state.md` projection, a `relation.md`
projection when the issue has links, and any `comment-*.md` files —
open those files to read the cached content.
`issue.md` is the pure body (no frontmatter); `state.md` carries native
state (`state` / `state_reason` / `assignees` / `labels`). Default cache
policy reuses the local copy when fresh; pass `--cache-policy refresh` to
force a remote re-read. Never edit the returned files in place.

References are GitHub issue numbers or configured-repo references
(e.g., `123`, `#123`, `<owner>/<repo>#123`,
`https://github.com/<owner>/<repo>/issues/123`).

When the output carries a `relationships` path, read that
`relation.md` to follow linked issues (parent, children,
blocked-by, blocking, related) and fetch them too.
