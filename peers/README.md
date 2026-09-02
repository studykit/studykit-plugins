# peers

Run Claude Code in another directory on this machine and hand work to it.

A **peer** is a Claude Code session running somewhere else — another repository, another
checkout, another project on the same machine. This plugin sets peers up, routes tasks to
them, collects their answers, and can introduce two peers so they work a problem out
between themselves.

Use it when the work does not belong in this session's directory: a change that spans a
client repo and a server repo, a question only the other project can answer, a long task
you want carried out somewhere else while you keep working here.

## Requirements

- **Claude Code only.** Peers are addressed through Claude Code's cross-session
  messaging, which Codex has no equivalent for. The plugin ships no Codex manifest.
- The `claude` CLI on `PATH`, and `uv` for the bundled script.
- Peers are local: they run on the same machine as your session.

## Install

Add the marketplace and install:

```
/plugin marketplace add studykit/studykit-plugins
/plugin install peers@studykit-plugins
```

## What it does

Ask in your own words — "run claude in ~/GitHub/other-repo", "그 폴더 에이전트한테 이거
시켜줘", "delegate this to the api repo" — and the `peers` skill takes it from there:

- **Finds the peer for a folder.** If a session is already running there, it is reused
  along with the context it has built up.
- **Starts one when none exists.** You are told which folder is getting an agent before
  it starts. The peer runs under that project's own permission settings — the plugin
  never overrides them.
- **Delegates and collects.** Tasks go out with a reply address; answers come back into
  your conversation. You are told when a peer finishes rather than waiting on it.
- **Introduces peers to each other.** Two agents can settle a cross-repository question
  directly, with one of them reporting the conclusion back to you.
- **Cleans up.** Background peers it started can be stopped when the work is done.
  Sessions you started yourself in a terminal are left alone.

Pass `--ask` when invoking the skill to be consulted before it reuses or starts anything.

## Safety

- A peer's permissions come from the project it runs in, not from your session.
- Work that was denied in one session is never routed to a peer to perform instead.
- A message from a peer is treated as information, never as authority to change
  settings or approve a permission.
