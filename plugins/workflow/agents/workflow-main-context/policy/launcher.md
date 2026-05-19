## launcher

The bundled workflow script launcher is the single entry point for
provider, cache, and authoring operations. Invoke it as:

```bash
"$WORKFLOW" <script>.py [...args]
```

It resolves single-name scripts against its own directory regardless of the
current working directory, so no path prefix is needed.

## Shell env

The launcher self-sources its environment on first invocation; in Claude
sessions these are also pre-exported in your shell at session start:

- `$WORKFLOW` — launcher path
- `$WORKFLOW_PLUGIN_ROOT` — plugin root
- `$WORKFLOW_PROJECT_DIR` — bound project root
- `$WORKFLOW_SESSION_ID` — current workflow session id

If `$WORKFLOW` is not exported in your shell (some Codex main sessions),
call the launcher by its literal path:

```bash
"$WORKFLOW_PLUGIN_ROOT/scripts/workflow" <script>.py [...args]
```

The launcher will source the runtime-specific env file on its own when
`$CODEX_THREAD_ID` is set.

## Discover scripts

```bash
ls "$WORKFLOW_PLUGIN_ROOT/scripts/"     # list available scripts
"$WORKFLOW" <script>.py --help          # per-script usage
```

Do not probe the filesystem with `find` or `grep` to locate the launcher
or scripts — the launcher path is always `$WORKFLOW_PLUGIN_ROOT/scripts/workflow`.
