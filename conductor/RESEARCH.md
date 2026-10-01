# Sending messages into running Claude Code sessions

Research for a program that manages many agent sessions: can it send a message into a Claude
Code session that is already open? Checked 2026-10-02 against Claude Code 2.1.286, Python
`claude-agent-sdk` 0.2.163 (PyPI latest, GitHub `main` `db750b2`) and TypeScript
`@anthropic-ai/claude-agent-sdk` 0.3.286 (npm latest).

## Answer

The Agent SDK has no call for it, but Claude Code documents one: each session's **inbox socket**
(cross-session messaging). A script may post to it. Channels are a second, research-preview route
that only works for sessions started with `--channels`.

## Agent SDK (Python and TypeScript)

- `query()` / `ClaudeSDKClient` start their own CLI process; streaming input sends messages only
  to that process.
- `resume` / `fork_session` start a **new** process from the saved transcript. They do not reach a
  running process, so they don't answer this question.
- `list_sessions`, `get_session_info`, `get_session_messages`, `rename`/`tag`/`delete`/`fork_session`
  work on transcripts.
- The SDK has only the **receiving** side of peer messages: `UserMessage.origin` /
  `MessageOrigin` with `kind: "peer"`, `from`, `name`, `body`, `verifiedPeerPid`
  (`types.py`; `sdk.d.ts` `SDKMessageOrigin`). It has no API to send one.
- `@anthropic-ai/claude-agent-sdk/bridge` (alpha) is a transport for claude.ai (CCR) hosted
  sessions, not local ones.

## Inbox socket (cross-session messaging)

Source: <https://code.claude.com/docs/en/cross-session-messaging.md> → "The session's inbox
socket"; <https://code.claude.com/docs/en/env-vars.md>.

- Requires Claude Code v2.1.224+ (macOS/Linux). On by default; nothing to enable.
- Every session except bare mode binds one, including `claude -p` and background sessions.
- Path: `/status` → `Peer address` (`uds:` prefix), or `CLAUDE_CODE_MESSAGING_SOCKET`, exported to
  hooks (from `SessionStart` on) and Bash commands. Locally each running session also has
  `~/.claude/sessions/<pid>.json` with `sessionId`, `cwd`, `kind`, `status`, `name`,
  `messagingSocketPath` (e.g. `/tmp/cc-socks/<pid>.sock`), `peerProtocol: 1`, `peerFeatures`.
  That file is undocumented — observed, not a contract.
- `claude agents --json` lists active sessions (interactive and background) with `pid`,
  `sessionId`, `cwd`, `kind`, `name`, `status`/`state`.
- Auth: an optional first line `{"type":"auth","token":"<CLAUDE_CODE_MESSAGING_TOKEN>"}` on
  macOS/Linux (required on Windows). The socket is restricted to the OS user.
- A connection must send a complete line within 30 s.
- Delivery: an idle session starts a new turn with the message; a busy one reads it between tool
  calls. Plain text only, about 1M characters max; bursts and repeats are throttled; at most 50
  queued.
- The receiver applies `crossSessionInbound` (`accept` / `hold` / `refuse`). With no value set, a
  session that bypasses permissions holds unattributed messages for approval (dialog, expires after
  `dialogExpiry`, default 5 min). For unattended workers set `crossSessionInbound: accept`, e.g. in
  `--settings`.
- "Own-child" messages, from the session's own hooks or Bash, are delivered when no
  `crossSessionInbound` applies. On macOS this is verified by process evidence while the poster runs,
  otherwise by the token.
- Incoming messages are marked as from another session: they can't approve prompts, change
  configuration, or run slash commands.

**Not documented:** the JSON shape of the message line after the auth line. Find it with a spike.

## Channels

Source: <https://code.claude.com/docs/en/channels.md>,
<https://code.claude.com/docs/en/channels-reference.md>.

- An MCP server pushes events into the running session and can receive replies (two-way).
- The session must be started with `--channels <server>`; being in `.mcp.json` is not enough. So
  this does not reach a session that is already open.
- Research preview. Team/Enterprise orgs need `channelsEnabled` from an admin.

## Hooks

Source: <https://code.claude.com/docs/en/hooks.md> → "Run hooks in the background".

- `async: true`: output (`additionalContext`, `systemMessage`) is delivered on the **next** turn; it
  doesn't wake an idle session.
- `asyncRewake: true`: runs in the background and wakes Claude on exit code 2, showing the hook's
  stderr as a system reminder. Documented for "a long-running background failure"; `timeout` is
  still enforced (default 600 s). It could be a message path, but the inbox socket fits better.
- Useful role: a `SessionStart` hook can register `CLAUDE_CODE_MESSAGING_SOCKET` and `session_id`
  with the manager, so the manager knows every session's address.

## Open

- [ ] Spike: the message line format on the inbox socket, and delivery from a non-child process
  into an idle interactive session.
- [ ] Whether a token sent by a non-child process counts as "own-child".
