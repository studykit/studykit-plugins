#!/usr/bin/env python3
"""Map working directories to live Claude sessions on this machine.

`ListAgents` is the address book — it names every live session and whether it is
busy — but it does not report each session's working directory. `claude agents
--json` does. This script exists solely to close that gap: it answers "which
live peer serves folder X", and starts one when none does.

It deliberately never passes `--permission-mode`. A started peer resolves its
permissions from the target project's own settings, the same as a session the
user starts by hand; forcing a mode here would silently override that choice.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

REGISTRATION_TIMEOUT_S = 30.0
POLL_INTERVAL_S = 0.5


class PeerError(RuntimeError):
    """A failure worth reporting to the caller verbatim."""


def live_sessions() -> list[dict[str, Any]]:
    try:
        completed = subprocess.run(
            ["claude", "agents", "--json"],
            capture_output=True,
            text=True,
            check=True,
        )
    except FileNotFoundError as exc:
        raise PeerError("`claude` is not on PATH; peers requires the Claude Code CLI") from exc
    except subprocess.CalledProcessError as exc:
        raise PeerError(f"`claude agents --json` failed: {exc.stderr.strip()}") from exc

    try:
        sessions = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise PeerError(f"`claude agents --json` returned non-JSON output: {exc}") from exc

    self_id = os.environ.get("CLAUDE_CODE_SESSION_ID")
    for session in sessions:
        session["self"] = bool(self_id) and session.get("sessionId") == self_id
    return sessions


def canonical(path: str | os.PathLike[str]) -> str:
    """Resolve symlinks so that /tmp and /private/tmp compare equal."""
    return str(Path(path).expanduser().resolve())


def sessions_for(folder: str, sessions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    target = canonical(folder)
    return [s for s in sessions if not s["self"] and canonical(s.get("cwd", "")) == target]


def default_name(folder: str, taken: set[str]) -> str:
    stem = re.sub(r"[^a-zA-Z0-9._-]+", "-", Path(canonical(folder)).name).strip("-").lower()
    stem = stem or "peer"
    if stem not in taken:
        return stem
    suffix = 2
    while f"{stem}-{suffix}" in taken:
        suffix += 1
    return f"{stem}-{suffix}"


def format_row(session: dict[str, Any]) -> str:
    marker = "self " if session["self"] else ""
    # The id is labelled because it is NOT the bracketed ref `ListAgents` prints, and the
    # two are easy to confuse: a SendMessage to `name [session-id]` does not resolve.
    return (
        f"{marker}{session.get('name')}  ·  {session.get('kind')}  ·  "
        f"{session.get('status')}  ·  {session.get('cwd')}  ·  "
        f"session:{session.get('sessionId', '')[:8]}"
    )


def emit(rows: list[dict[str, Any]], as_json: bool) -> None:
    if as_json:
        json.dump(rows, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return
    if not rows:
        print("(none)")
        return
    for row in rows:
        print(format_row(row))


def cmd_list(args: argparse.Namespace) -> int:
    sessions = live_sessions()
    if not args.include_self:
        sessions = [s for s in sessions if not s["self"]]
    emit(sessions, args.json)
    return 0


def cmd_resolve(args: argparse.Namespace) -> int:
    folder = canonical(args.folder)
    if not Path(folder).is_dir():
        raise PeerError(f"not a directory: {args.folder}")
    emit(sessions_for(folder, live_sessions()), args.json)
    return 0


def cmd_start(args: argparse.Namespace) -> int:
    folder = canonical(args.folder)
    if not Path(folder).is_dir():
        raise PeerError(f"not a directory: {args.folder}")

    sessions = live_sessions()
    taken = {s.get("name", "") for s in sessions}
    name = args.name or default_name(folder, taken)
    if name in taken:
        raise PeerError(f"a live session is already named {name!r}; pass --name to choose another")

    # `--bg` is the only launch that works without a terminal. An interactive
    # launch stops on the workspace-trust prompt the first time a folder is
    # used, which no unattended caller can answer.
    command = ["claude", "--bg", "-n", name]
    if args.prompt:
        command.append(args.prompt)

    try:
        subprocess.run(command, cwd=folder, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as exc:
        raise PeerError(f"failed to start a peer in {folder}: {exc.stderr.strip()}") from exc

    deadline = time.monotonic() + REGISTRATION_TIMEOUT_S
    while time.monotonic() < deadline:
        match = [s for s in live_sessions() if s.get("name") == name]
        if match:
            emit(match, args.json)
            return 0
        time.sleep(POLL_INTERVAL_S)

    raise PeerError(
        f"peer {name!r} did not register within {REGISTRATION_TIMEOUT_S:.0f}s; "
        "check `claude agents` for its state"
    )


def cmd_stop(args: argparse.Namespace) -> int:
    matches = [s for s in live_sessions() if not s["self"] and s.get("name") == args.name]
    if not matches:
        raise PeerError(f"no live peer named {args.name!r}")
    if len(matches) > 1:
        raise PeerError(f"{len(matches)} live sessions are named {args.name!r}; stop them by id")

    peer = matches[0]
    # `claude stop` only accepts background sessions, and an interactive peer is
    # a terminal a person is sitting in front of. Refuse rather than try.
    if peer.get("kind") != "background":
        raise PeerError(
            f"{args.name!r} has kind {peer.get('kind')!r}, not 'background' — it is a terminal "
            "its owner may be sitting in front of; leave it to them"
        )

    session_id = peer.get("sessionId", "")
    try:
        subprocess.run(["claude", "stop", session_id[:8]], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as exc:
        raise PeerError(f"failed to stop {args.name!r}: {exc.stderr.strip()}") from exc
    print(f"stopped {args.name} ({session_id[:8]})")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Shared rather than top-level so `<command> --json` works; a flag defined in both
    # places would have the subparser's default silently overwrite the top-level value.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", help="emit raw JSON instead of one line per session")

    p_list = subparsers.add_parser(
        "list", parents=[common], help="list every live peer session with its working directory"
    )
    p_list.add_argument("--include-self", action="store_true", help="also list this session")
    p_list.set_defaults(func=cmd_list)

    p_resolve = subparsers.add_parser(
        "resolve", parents=[common], help="list live peers whose working directory is FOLDER"
    )
    p_resolve.add_argument("folder")
    p_resolve.set_defaults(func=cmd_resolve)

    p_start = subparsers.add_parser(
        "start", parents=[common], help="start a background peer in FOLDER and wait for it to register"
    )
    p_start.add_argument("folder")
    p_start.add_argument("--name", help="peer name (default: the folder's name, de-duplicated)")
    p_start.add_argument("--prompt", help="opening prompt for the new peer")
    p_start.set_defaults(func=cmd_start)

    p_stop = subparsers.add_parser("stop", parents=[common], help="stop a background peer by name")
    p_stop.add_argument("name")
    p_stop.set_defaults(func=cmd_stop)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return int(args.func(args))
    except PeerError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
