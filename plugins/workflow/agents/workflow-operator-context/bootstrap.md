## workflow operator bootstrap

Two environment variables are persisted into the operator's shell at
SessionStart:

- `$WORKFLOW` — the bundled workflow script launcher.
- `$AUTHORING_RESOLVER` — the authoring-resolver script path.

Invoke any bundled workflow script as `$WORKFLOW <script>.py ...`; the
launcher resolves single-name scripts against its own directory regardless
of the current working directory.

Do not derive either path from project layout or inspect runtime-specific
session files directly.
