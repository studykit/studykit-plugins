# Peer lifecycle

How peers are found, started, named and stopped, and the constraints behind each choice.

## The script

`scripts/peer_sessions.py` uses only the standard library; run it with `uv run`.

Take the script's path from SKILL.md, which is skill content and has the skill-directory
placeholder substituted for a real path before it reaches you. This file is not — it is
read as ordinary text, so a placeholder written here would stay literal and resolve to
nothing.

| Command | What it does |
| --- | --- |
| `list [--include-self]` | Every live peer with its working directory |
| `resolve <folder>` | Live peers whose working directory is `<folder>` |
| `start <folder> [--name N] [--prompt P]` | Start a background peer and wait for it to register |
| `stop <name>` | Stop a background peer |

Every command takes `--json` after it (`resolve <folder> --json`), which emits the raw
session objects instead of one line each — use it when a decision depends on a field the
text form drops, such as `startedAt`.

Failures print `error: <reason>` to stderr and exit non-zero. Report the reason; do not
retry a start that failed for a stated reason.

## Why a separate script exists

`ListAgents` is the address book, and it is the right tool for "who is out there". It
does not report each peer's working directory, so it cannot answer "which peer serves
this folder" — the question every delegation starts from. `claude agents --json` carries
`cwd`, and the script exists to join the two.

The script canonicalises both sides of the comparison, so `/tmp/x` matches a session
whose registry entry reads `/private/tmp/x`.

`resolve` regularly returns more than one peer — a repository someone is actively working
in holds two or three sessions at once. There is no rule for picking among them, because
the right answer depends on who owns each: prefer a `background` peer this skill started,
and ask the user before messaging anything `interactive`.

## The `session:` id is not a messaging address

Each row ends with `session:<8 hex chars>` — the first characters of the CLI's session id,
which is what `claude attach` and `claude stop` take. It is not what `SendMessage` uses.

`ListAgents` prints its own bracketed `[ref]` for disambiguating a duplicated name, and
the two are unrelated values for the same session: one appears as `session:e21cd349` in
this script's output and `[793e66]` in `ListAgents`. Addressing a peer as
`name [session-id]` fails with "no agent named … is reachable". The name alone is the
address; reach for the `[ref]` only when `ListAgents` or an error shows one.

The current session appears in the registry too. It is identified by
`CLAUDE_CODE_SESSION_ID` and excluded from every result unless `--include-self` is
passed — delegating to oneself is a loop, not a delegation.

## Starting

`start` launches `claude --bg` in the target directory, then polls the registry until the
new name appears (30s, then it gives up and says so).

**`--bg` is not a preference.** An interactive start in a directory Claude Code has not
been used in before stops on the workspace-trust prompt and never reaches a usable state.
No unattended launcher can answer that prompt. `--bg` starts without showing it.

That is a convenience with a cost: the trust prompt exists so a person decides before an
agent gets read, write and execute rights in a folder. An unattended start skips the
question. This is why the skill names the folder to the user before starting a peer there
— it moves the decision back to where the prompt would have put it.

## Naming

Without `--name`, the peer takes the folder's own name, lowercased, with unusual
characters replaced — `~/GitHub/news-markdown` becomes `news-markdown`. A collision with
a live name gets a `-2`, `-3` suffix.

Folder-derived names are what makes a peer recognisable in `ListAgents` weeks later. Pass
`--name` only when the default would be misleading — two checkouts of the same repository,
or a peer dedicated to one long task.

`start` refuses a `--name` that a live session already holds, rather than creating a
second session that the bare name cannot address.

## Permissions

The script never passes `--permission-mode`. A peer resolves permissions from the target
project's own settings, exactly as a session the user starts by hand in that directory
would.

This matters more than it looks. Passing a mode would silently override the user's
configured default — including a project that deliberately runs in `plan` or restricted
mode. Leaving it alone means the peer's authority is whatever the user already decided
for that project, and it stays visible in the place they configured it.

A consequence worth stating to the user: a peer in a project configured for
`bypassPermissions` will edit and run commands there without asking. That is the
project's setting, not something the delegation introduced, but the user may not have it
in mind when naming a folder.

## Stopping

`stop` ends a background peer and keeps its conversation; it can be resumed later with
`claude attach <id>`.

It refuses anything that is not `kind: background`. An `interactive` peer is a terminal a
person may be using — there is no CLI verb to stop one, and there should not be one here.
If an interactive peer needs to end, that is its owner's call.

Leaving a background peer running is often right: the next delegation to that folder
reuses its context instead of rebuilding it. Stop one when the work is finished and the
folder is unlikely to come up again, or when the user asks.

## What is not usable for results

`claude logs <id>` returns the session's raw ANSI terminal capture — cursor addressing,
spinner frames, redraws. It is readable by a person watching, and it is not a transcript.
Results come back over `SendMessage` and nowhere else.
