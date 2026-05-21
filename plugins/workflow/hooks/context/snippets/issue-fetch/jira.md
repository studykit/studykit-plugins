```bash
"$WORKFLOW" jira_issue_fetch.py <KEY> [<KEY> ...] \
  [--cache-policy default|refresh]
```

Default cache policy reuses the cached `issue.md` projection when fresh;
pass `--cache-policy refresh` to force a remote re-read. The script emits a
JSON payload with a shared `basedir` and an `issues` array; each entry holds
the basedir-relative `issue` path, `title`, `state`, `cache_refreshed`, and
(when present) basedir-relative `comments` paths to sibling `comment-*.md`
files — read `issue.md` for the issue body and frontmatter (title, state,
labels, `remote_links`, `relationships`) and each `comment-*.md` file for
one cached comment. `cache_refreshed` is `false` when the call reused the
cached projection and `true` when this op pulled fresh data from the
provider. Never edit `issue.md` or `comment-*.md` in place.
