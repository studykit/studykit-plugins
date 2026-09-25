# Lens

This is a Herdr terminal UI plugin. Keep project operations independent of Herdr
runtime context, and never send editor commands into the user's source pane. The
one exception is comments: when the user submits a message they have seen and
edited, Lens sends it to the target agent pane through `agent.prompt`, and nothing
else.

Every place that takes typed text edits with the Emacs keys of `command_line.edit`
(and C-g cancels it); a new prompt or text field must use it too, not its own
key handling.

Run `uv run --no-config --no-project --with rich==15.0.0 python -m unittest discover -s lens/tests` from the repository root.
See `dev/testing.md` for host integration checks and API references.
