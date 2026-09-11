# Handover

Handover writes a self-contained, uncommitted session handover in `.handover/` so later work can resume without the original conversation.

This plugin supports Claude Code only. A recorded handover is announced after `/clear` so the replacement session can read it and resume your work.

Install with `/plugin install handover@studykit-plugins`. The plugin requires `uv` and Bash.

Run `/handover:handover` when you want to hand off, wrap up, or prepare to clear a conversation. Add `--commit` only when you want to commit the session's non-handover changes before writing the document.
