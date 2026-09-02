# peers — contributor notes

Claude-only plugin. Peers are reached through Claude Code's `ListAgents` / `SendMessage`
cross-session surface, which Codex has no equivalent for, so there is no `.codex-plugin/`
manifest and no adapter layer to keep host-neutral. If Codex ever gains cross-session
messaging, the split to make is skill body (portable) against addressing (host-specific).

## Why the plugin shells out instead of using the Agent SDK

The Agent SDK looks like the right foundation and is not. A session it drives does
register as a live peer, but it lives only as long as the Python process holding the
connection — so a short-lived command cannot leave a peer running, which is the whole
point. Its `list_sessions()` enumerates on-disk transcripts (no `pid`, no `kind`, no
`status`), so it cannot tell a live peer from a finished one either.

Both were measured rather than assumed; the evidence, along with the launch-mode and
permission-inheritance findings the design rests on, is saved in this repository's
reference directory under `claude-code-live-session-registry-and-agent-sdk`.

## Testing

Peer behavior cannot be verified by reading the script's output alone — the questions
that matter are whether a started peer registers, whether a message reaches it, and
whether its reply comes back. Test the round trip against a throwaway directory:

1. `start` a peer there and confirm it appears in `ListAgents` under the expected name.
2. `SendMessage` it a task naming a reply address, with `notify_when_idle: true`.
3. Confirm the reply arrives as a `<cross-session-message>` in this session.
4. `stop` it and confirm it leaves the registry.

Run the script directly for the resolve/naming cases (symlinked paths such as
`/tmp` against `/private/tmp`, self-exclusion, a duplicate `--name`); those need no live
peer.

Do not test in this repository. A peer started here joins the same registry as the
session doing the testing, under a name derived from the same folder.
