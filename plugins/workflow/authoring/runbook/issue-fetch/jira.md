## jira — fetch issues

```bash
workflow issue fetch <issue> [<issue> ...] \
  [--cache-policy default|refresh]
```

The script returns the issue `title`/`state` inline plus paths to the
local `issue.md` body, the `relationships.md` projection, and any
`comment-*.md` files — open those files to read the cached content.
`issue.md` is the pure body (no frontmatter). Default cache policy
reuses the local copy when fresh; pass `--cache-policy refresh` to
force a remote re-read. Never edit the returned files in place.

References are Jira issue keys (e.g., `PROJ-123`) or text containing
them. When the output carries a `relationships` path, read that
`relationships.md` to follow linked issues (parent, mapped link
buckets, unmapped issue links, external links) and fetch them too.
Cached `comments` paths point to sibling `comment-*.md` files — read
each for one cached comment.
