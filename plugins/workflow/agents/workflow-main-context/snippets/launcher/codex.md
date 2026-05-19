```bash
"{{WORKFLOW_PLUGIN_ROOT}}/scripts/workflow" <script>.py [...args]
```

Codex shell tool invocations do not inherit the workflow env contract between
calls, so the absolute launcher path above is required (`{{WORKFLOW_PLUGIN_ROOT}}`
is resolved to an absolute path before injection). The launcher self-sources
the session env file each invocation, so the launched script still receives
the full workflow contract.

When other policy detail files (such as `authoring.md`, `provider-writes/*.md`,
or `knowledge/*.md`) show commands using `"$WORKFLOW" <script>.py` or paths
under `"$WORKFLOW_PLUGIN_ROOT"`, those snippets are written for the Claude
runtime where the env vars are exported. In Codex, treat them as:

- `$WORKFLOW` → `{{WORKFLOW_PLUGIN_ROOT}}/scripts/workflow`
- `$WORKFLOW_PLUGIN_ROOT` → `{{WORKFLOW_PLUGIN_ROOT}}`

Substitute the absolute path inline when running the command — do not run
the literal `"$WORKFLOW"` form, since that variable is unset in your Bash
shell.

Discover scripts:

```bash
ls "{{WORKFLOW_PLUGIN_ROOT}}/scripts/"                                  # list available scripts
"{{WORKFLOW_PLUGIN_ROOT}}/scripts/workflow" <script>.py --help          # per-script usage
```

The launcher resolves single-name scripts against its own directory regardless
of the current working directory, so no path prefix on the script name is
needed. Do not probe the filesystem with `find` or `grep` to locate the
launcher or scripts — the launcher path is always
`{{WORKFLOW_PLUGIN_ROOT}}/scripts/workflow`.
