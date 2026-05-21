Refresh an existing issue's body (and optionally its state). The agent
uses this in two shapes.

Body-only `Resume` update (handoff / paused snapshots, no state change):

```bash
"$WORKFLOW" issue_writeback.py update \
  --issue <implementation-issue> \
  --body-file <updated-body-path>
```

Required: `--issue`, `--body-file`. Write the snapshot to a temp file
you choose; the cached body projection is read-only. On freshness drift
the script returns `status=blocked` with the cache paths to reread —
reread and retry.
