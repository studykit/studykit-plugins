## jira — fetch issues

```bash
workflow issue fetch <issue> [<issue> ...] \
  [--cache-policy default|refresh]
```

The script returns paths to local `issue.md` (and any
`comment-*.md`) projections — open those files to read the body and
frontmatter. Default cache policy reuses the local copy when fresh;
pass `--cache-policy refresh` to force a remote re-read. Never edit
the returned files in place.

References are Jira issue keys (e.g., `PROJ-123`) or text containing
them. Cached `comments` paths point to sibling `comment-*.md` files —
read each for one cached comment. `issue.md` frontmatter carries the
issue title, state, labels, `remote_links`, and `relationships`.
