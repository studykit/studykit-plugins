## github — search issues

```bash
spectrack issue search "<query>" [--limit N]
```

`<query>` is a GitHub issue search query, passed verbatim to
`gh issue list --search` (e.g., `is:open label:bug assignee:@me`,
`sort:updated-desc author:octocat`). Open and closed issues are both in
scope; narrow state through the query (`is:open` / `is:closed`).
`--limit` caps the result count (default 30).

The script prints a lightweight JSON ref list — `{kind, query, count,
issues}` — where each entry carries `issue` (the bare issue number),
`title`, `state`, `assignees`, and `url`. Search does not write cache
files. Feed an `issue` value back to `issue fetch` to read the full body
and cache projections.
