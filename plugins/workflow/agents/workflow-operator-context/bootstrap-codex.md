## workflow operator bootstrap

The workflow launcher is not persisted into the operator's bash shell in
Codex. The launcher lives at `plugins/workflow/scripts/workflow` (relative
to the project root) and self-sources its own env file when invoked. When
operator-context fragments refer to `$WORKFLOW <script>.py ...`,
substitute the literal launcher path:
`plugins/workflow/scripts/workflow <script>.py ...`.

Do not derive the launcher path from project layout in any other way or
inspect runtime-specific session files directly.
