```bash
"$WORKFLOW" <script>.py [...args]
```

The launcher contract is pre-exported in your Bash shell at SessionStart:
`$WORKFLOW` (launcher path), `$WORKFLOW_PLUGIN_ROOT` (plugin root),
`$WORKFLOW_PROJECT_DIR` (bound project root), and `$WORKFLOW_SESSION_ID`.

Discover scripts:

```bash
ls "$WORKFLOW_PLUGIN_ROOT/scripts/"     # list available scripts
"$WORKFLOW" <script>.py --help          # per-script usage
```

The launcher resolves single-name scripts against its own directory regardless
of the current working directory, so no path prefix on the script name is
needed. Do not probe the filesystem with `find` or `grep` to locate the
launcher or scripts — the launcher path is always
`$WORKFLOW_PLUGIN_ROOT/scripts/workflow`.
