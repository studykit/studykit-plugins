```bash
"$WORKFLOW" <script>.py [...args]
```

The launcher contract is pre-exported in your Bash shell at SessionStart:
`$WORKFLOW` (launcher path), `$WORKFLOW_PLUGIN_ROOT` (plugin root),
`$WORKFLOW_PROJECT_DIR` (bound project root), and `$WORKFLOW_SESSION_ID`.
Per-script usage: `"$WORKFLOW" <script>.py --help`.
