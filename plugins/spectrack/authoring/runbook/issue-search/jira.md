## jira — search issues

```bash
spectrack issue search "<jql>" [--limit N]
```

`<jql>` is a Jira Query Language string, passed verbatim to the Jira
search endpoint (e.g., `project = PROJ AND status = "In Progress"`,
`assignee = currentUser() ORDER BY updated DESC`). The query is pure
pass-through — scope it to a project with an explicit `project = ...`
clause when needed. `--limit` caps the result count (`maxResults`,
default 30).

The script prints a lightweight JSON ref list — `{kind, query, count,
issues}` — where each entry carries `issue` (the issue key), `title`,
`state` (the native status name), `assignees`, and `url` (the browse
link). Search does not write cache files. Feed an `issue` value back to
`issue fetch` to read the full body and cache projections.
