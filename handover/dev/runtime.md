# Runtime integration

Handover supports Claude Code only. SessionStart exports the command directory
and the session's project root through CLAUDE_ENV_FILE. The shell wrapper uses
that project root and CLAUDE_CODE_SESSION_ID to record the handover, even after
the working directory changes.

SessionEnd with reason `clear` transfers the recorded handover once.
SessionStart with source `clear` consumes it; the transfer expires five minutes
after SessionEnd. Other end reasons do not create a transfer.

Run `python3 -m unittest discover -s handover/tests` from the marketplace root.
For runtime validation, start Claude Code in a clean Herdr pane and a throwaway
project with `--plugin-dir` pointing at the working tree. Invoke the actual
`/handover:handover` skill, then `/clear`, and verify the new session reads the
recorded document. Direct script calls only validate state logic.

Verified on 2026-09-11 with Claude Code 2.1.268 in a clean Herdr pane:
`/handover:handover` created and recorded a document, `/clear` replaced the
session, and the new session read that document and returned the exact pending
marker. The command and project environment were absent before Claude started.

Codex support was excluded after a v0.154.0 integration test: `/clear` started
a replacement session without immediately running SessionEnd. Delayed teardown
could transfer a stale handover, and SessionStart provided no predecessor ID.
