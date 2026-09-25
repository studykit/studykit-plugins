# Development and verification

The action reads Herdr's focused pane and foreground directory, then opens a
popup entrypoint. The entrypoint attaches to a dedicated tmux server. Its session
key includes the Herdr socket, pane ID, and terminal ID so a reused pane ID does
not inherit an old shell. The Herdr action key also detaches the popup client;
`exit` ends the shell.
The dedicated server loads the user's tmux configuration when present and applies
it to an existing server if the file changes. Ctrl+Q is rebound afterward.
The plugin config directory can set `close_key` to a tmux root key, a
`prefix+` key, or `none`. Reopening applies the new binding without restarting
the shell and removes the previous tracked plugin binding. The popup reads
Herdr's action binding and mirrors it inside tmux so the same key shows and
hides the popup. Keep the old tmux socket name across the plugin rename to
preserve active shell sessions.
Each popup refreshes its session-specific tmux status label from the source
pane ID and title, including when attaching to an older shell session.
The indicator is presentation metadata (`display_agent`) guarded by the agent
label, so it drops when another agent takes the pane; a `pane.agent_detected`
event hook reapplies it when that pane still has a shell. A tmux
`session-closed` hook clears it. The tmux server's global environment comes
from whichever popup first started it, so the hook carries its own Herdr socket
and plugin state directory instead of relying on that environment.

Run the automated tests from the repository root:

```sh
python3 -m unittest discover -s shellbox/tests
```

For a host check, link the working tree with `herdr plugin link` and use a
throwaway project in a separate pane. With Lens closed, invoke the action, check
`pwd`, set a shell variable, press the configured toggle key, and reopen it from the same pane.
Verify that its directory and variable persist. Invoke it from another pane to
check isolation, then run `exit` in each test shell. Confirm that shell commands
never appear in the source panes. With an agent in the source pane, check that
`herdr agent get` reports the indicator in `display_agent` while the shell runs,
after the agent restarts, and no longer after `exit`. For Ctrl+H, test that its control byte detaches
an attached tmux client while Backspace leaves it attached.
