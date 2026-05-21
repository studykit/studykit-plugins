Refresh an existing issue's body (and optionally its state). The agent
uses this in two shapes.

Body-only `Resume` update (handoff / paused snapshots, no state change):

```bash
"$WORKFLOW" jira_issue_writeback.py update \
  --issue <implementation-key> \
  --body-file <updated-body-path>
```

Body + state update (closing with a non-completion reason — `<verb>` is
the Jira transition the project uses, e.g. `Won't Do` or `Cancelled`):

```bash
"$WORKFLOW" jira_issue_writeback.py update \
  --issue <implementation-key> \
  --body-file <updated-body-path> \
  --state <verb>
```

Required: `--issue`, `--body-file`. Write the snapshot to a temp file
you choose; the cached body projection is read-only. On freshness drift
the script returns `status=blocked` with the cache paths to reread —
reread and retry.
