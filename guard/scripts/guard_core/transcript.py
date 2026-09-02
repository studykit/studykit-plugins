"""Reading the host's transcript, and the ``transcript`` CLI verb over it.

guard reads the transcript for two unrelated purposes and they must stay apart. At Stop it
reads a single record to learn how the turn was *opened* (``_turn_identity``) — never its
content, which is the main agent's to write. Separately, ``cmd_transcript`` slices turns out
of the file on an audit agent's request: ``index`` / ``turn`` / ``find``, bounded by
``--since`` / ``--until`` / ``--last``. It writes an extract FILE and prints only its path
plus a one-line summary, so nothing lands in a context that did not ask for it. Only on an
agent's request, never on a schedule. Not a hook event.

Extracts go to ``extracts/<dir>/…`` and are swept with the rest of the session's state.
``<dir>`` is the transcript filename's stem unless the caller passes ``--session``, and no
caller does; Claude Code names that file after the session, so in practice it reads as a
session id without being one by contract. Nothing reads these back by name — the subcommand
prints the path it wrote — so the sweep keys on the directory's mtime instead.
"""

from __future__ import annotations

import json
import re
import sys

from pathlib import Path
from typing import Any

from .paths import _cli_project_dir, _state_root, _trace


# guard's own control commands, e.g. "/guard:settings claims-auditor off", "/settings",
# "/guard:claims-auditor". `settings` is a forked skill and each per-agent command a
# UserPromptExpansion — either way the turn is a relay, not real work to log/judge. The
# name is `settings`, not `config`, precisely so the bare form does NOT match Claude Code's
# built-in `/config` command (which the optional `(guard:)?` would otherwise capture,
# making guard treat every `/config` as its own control command). `(?=\s|$)` rather than
# `\b`: the name must END here, not merely hit a word boundary — `\b` would also accept a
# longer hyphenated name (`/settings-export` matching `settings`, `/claims-auditor-extra`
# matching `claims-auditor`), which is how another plugin's command becomes guard's.
# `comment-corrector` is deliberately ABSENT: that skill's relayed findings are claims about
# real files and about edits made to them, so its turn stays auditable like any other work.
# `statusline` is absent for the same reason: it reports what is in the user's settings files
# and proposes an edit to them, which is checkable work, not a relay of guard's own state.
# `reader-profile` is here for a different reason from the rest: its turn is an interview
# about the user, so the "answer" is the user's own words read back to them, and auditing
# that would have guard grading the user on how they described themselves.
_CONTROL_CMD_RE = re.compile(
    r"^/(guard:)?(settings|reader-profile|claims-auditor|deferrals-auditor"
    r"|clarity-auditor|korean-corrector)(?=\s|$)",
    re.IGNORECASE)


# In the transcript, a slash command is expanded to
# "<command-name>/guard:settings</command-name>" (see session b30dbaec). Pull the command
# name out of that tag; a raw typed form ("/guard:settings claims-auditor off") is handled by
# the fallback in _turn_command_name.
_COMMAND_NAME_RE = re.compile(r"<command-name>\s*(/?[^<\n]+?)\s*</command-name>", re.IGNORECASE)


def _message_of(record: Any) -> dict[str, Any]:
    msg = record.get("message") if isinstance(record, dict) else None
    return msg if isinstance(msg, dict) else {}


def _turn_command_name(user_text: str) -> str:
    """The slash command that opened the turn, normalized (leading '/' stripped,
    lowercased), or '' when the turn was not opened by a slash command.

    Slash commands reach the transcript expanded as
    ``<command-name>/guard:settings</command-name>``; a raw typed form
    (``/guard:settings claims-auditor off``) is handled by the fallback.
    """
    text = user_text.strip()
    m = _COMMAND_NAME_RE.search(text)
    if m:
        name = m.group(1).strip()
    elif text.startswith("/"):
        name = text.split()[0]
    else:
        return ""
    return name.lstrip("/").lower()


def _is_control_command_name(name: str) -> bool:
    """True when a normalized command name is one of guard's own control commands
    (``settings``/``reader-profile``/``*-auditor``/``korean-corrector``, with or without
    the ``guard:`` prefix)."""
    return bool(name) and bool(_CONTROL_CMD_RE.match("/" + name))


# Text the host injects into a `user` record that is not the user talking: hook output,
# slash-command envelopes, `!` command echoes, the compaction caveat. Matched as a prefix
# on the record's text. Without this filter the record's "user request" is whatever the
# host happened to prepend, which is both wrong and the kind of wrong an auditor cannot
# detect — it has no other copy of the request to compare against. The same list drives
# hindsight's transcript renderer (`hindsight/skills/review/scripts/render.py`).
# The envelope a user `!` command's input arrives in. It is also the record that ANCHORS
# such a turn, which is what `_turn_identity` keys its Stop skip on.
_BASH_TAG = "<bash-input>"


_INJECTED_PREFIXES = (
    "<system-reminder", "<command-name>", "<command-message>", "<command-args",
    "<local-command", "<bash-input", "<bash-stdout", "<bash-stderr", "Caveat:",
    "<task-notification", "<user-prompt-submit-hook>",
)


# Caps on the tool activity guard slices into a turn record. Generous, because the record
# is a file rather than context — but not unbounded: whoever is dispatched Reads the whole
# file, so an uncapped 5MB transcript turn would arrive in an auditor's context intact.
# Per-result first, so one runaway command cannot crowd out ten useful ones, then a total.
TOOL_RESULT_MAX_CHARS = 4000


TOOL_ACTIVITY_MAX_CHARS = 30000


def _transcript_records(path: Path):
    """Yield the transcript's records as dicts, in file order. Malformed lines skipped.

    Streamed with ``errors="replace"``: these files reach several megabytes, and one
    undecodable byte must not cost the whole read.
    """
    try:
        fh = path.open(encoding="utf-8", errors="replace")
    except OSError:
        return
    with fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except (json.JSONDecodeError, ValueError):
                continue
            if isinstance(rec, dict):
                yield rec


def _turn_slice(transcript_path: Any, prompt_id: Any) -> dict[str, Any] | None:
    """Everything guard can read about one turn from the transcript. None when it cannot.

    Returns ``{origin_kind, command_name, user, assistant, tools}``. A turn is
    anchored on the FIRST record whose top-level ``promptId`` equals ``prompt_id``, and the
    slice runs to the next record carrying a DIFFERENT non-empty promptId. That positional
    rule is not a convenience: only ``user`` records carry a promptId at all — the assistant
    records, and the ``tool_use`` blocks inside them, carry none — so a filter on promptId
    would drop precisely the tool activity this exists to collect. Verified on a real
    4.8MB, 21-turn transcript: promptIds occur in contiguous runs, one run per turn.

    Skipped: ``isMeta`` (guard's own injected feedback), ``isSidechain`` (a subagent's
    records, which are not this turn's activity even when they share the file), and user
    text that is really host-injected envelope (``_INJECTED_PREFIXES``), which a user `!`
    command's input and output are: neither is the user asking for anything.

    Fail-open throughout: an unreadable transcript, a malformed line, or a prompt_id absent
    from the file yields None or a partial slice, never a raise.
    """
    if not isinstance(transcript_path, str) or not isinstance(prompt_id, str) or not prompt_id:
        return None
    path = Path(transcript_path)
    if not path.is_file():
        return None

    user = ""
    assistant: list[str] = []
    tools: list[dict[str, str]] = []
    origin_kind = ""
    command_name = ""
    in_turn = False

    for rec in _transcript_records(path):
        rec_pid = rec.get("promptId")
        if not in_turn:
            if rec_pid != prompt_id:
                continue
            in_turn = True
            origin = rec.get("origin")
            if isinstance(origin, dict):
                origin_kind = str(origin.get("kind") or "")
            anchor = _message_of(rec).get("content")
            command_name = _turn_command_name(anchor if isinstance(anchor, str) else "")
        elif isinstance(rec_pid, str) and rec_pid and rec_pid != prompt_id:
            break

        if rec.get("isMeta") is True or rec.get("isSidechain") is True:
            continue

        content = _message_of(rec).get("content")
        if isinstance(content, str):
            if not user and not content.lstrip().startswith(_INJECTED_PREFIXES):
                user = content
            continue
        if not isinstance(content, list):
            continue
        for part in content:
            if not isinstance(part, dict):
                continue
            ptype = part.get("type")
            if ptype == "text":
                txt = str(part.get("text", "")).strip()
                if txt:
                    assistant.append(txt)
            elif ptype == "tool_use":
                name = part.get("name", "tool")
                inp = part.get("input")
                cmd = inp.get("command") if isinstance(inp, dict) else None
                if not isinstance(cmd, str) or not cmd:
                    cmd = f"[{name}] {json.dumps(inp, ensure_ascii=False)[:400]}"
                tools.append({"command": cmd, "output": ""})
            elif ptype == "tool_result":
                res = part.get("content")
                if isinstance(res, list):
                    res = " ".join(str(x.get("text", "")) for x in res if isinstance(x, dict))
                out = str(res if res is not None else "")
                for t in reversed(tools):
                    if not t["output"]:
                        t["output"] = out
                        break
                else:
                    tools.append({"command": "[tool_result]", "output": out})

    if not in_turn:
        return None
    return {
        "origin_kind": origin_kind,
        "command_name": command_name,
        "user": user,
        "assistant": "\n\n".join(assistant),
        "tools": tools,
    }


def _extract_dir(project_dir: Path, session_id: str) -> Path:
    return _state_root(project_dir) / "extracts" / (session_id or "unknown")


def _write_extract(path: Path, body: str) -> bool:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
        return True
    except OSError:
        return False


def _render_turn(turn: dict[str, Any], turn_id: str) -> str:
    """One turn as an extract file reads: request, tool activity, response. Verbatim.

    Verbatim is the whole point of extracting with a script instead of asking an agent to
    write down what happened. A copy made by the turn's own author gets tidied, and a
    tidied turn is one where the claim actually made is no longer the claim being audited.
    Truncation is marked in place so a reader can tell a short command from a cut one.
    """
    parts: list[str] = []
    for t in turn.get("tools", []):
        if not isinstance(t, dict):
            continue
        out = str(t.get("output", ""))
        if len(out) > TOOL_RESULT_MAX_CHARS:
            out = out[:TOOL_RESULT_MAX_CHARS] + "\n…(output truncated by guard)"
        parts.append(f"$ {t.get('command', '')}\n→ {out}")
    activity = "\n\n".join(parts).strip()
    if len(activity) > TOOL_ACTIVITY_MAX_CHARS:
        # Keep the TAIL: the later calls are the ones the response was written from.
        activity = ("…(earlier tool activity in this turn omitted by guard)\n"
                    + activity[-TOOL_ACTIVITY_MAX_CHARS:])
    return "\n\n".join([
        f"# Turn {turn_id}",
        "## The user's request",
        (str(turn.get("user", "")).strip() or "(not in the transcript)"),
        "## Tool activity",
        (activity or "(none)"),
        "## What the assistant said",
        (str(turn.get("assistant", "")).strip() or "(not in the transcript)"),
    ]) + "\n"


def _turn_index(path: Path) -> list[dict[str, str]]:
    """Every turn in the transcript, in order: its id, when it started, its opening line.

    An index, not content — small enough that an agent can read it whole and then ask for
    the two or three turns that look relevant. Turns opened by a host-injected envelope
    (a task-notification, a hook relay) are labelled as such rather than dropped: an agent
    looking for where a number came from is better served by seeing the gap.
    """
    out: list[dict[str, str]] = []
    for rec in _transcript_records(path):
        pid = rec.get("promptId")
        if not isinstance(pid, str) or not pid:
            continue
        if out and out[-1]["turn"] == pid:
            continue
        content = _message_of(rec).get("content")
        text = content if isinstance(content, str) else ""
        head = " ".join(text.split())
        kind = ""
        if head.lstrip().startswith(_INJECTED_PREFIXES):
            kind = " [host-injected]"
            head = head[:80]
        out.append({
            "turn": pid,
            "at": str(rec.get("timestamp") or ""),
            "head": (head[:160] or "(no text)") + kind,
        })
    return out


def _turn_window(order: list[str], since: str, until: str, last: str) -> set[str]:
    """Which turn ids an extraction may look at, given the caller's window.

    A session transcript runs to megabytes and hundreds of turns, and an agent auditing
    the turn that just finished has no use for turn 3. Bounding the scan is therefore an
    input, not an optimization: without it `find` returns matches from an hour ago with
    equal prominence, and the agent pays to read them.

    ``since``/``until`` are turn ids, inclusive on both ends; an id that is not in the
    transcript is ignored rather than treated as empty, since the alternative is an
    extraction that silently returns nothing. ``last`` keeps the N most recent turns of
    whatever survives, so `--until <the audited turn> --last 10` reads as "the ten turns
    ending at this one" — which is the shape an auditor actually asks for.
    """
    lo, hi = 0, len(order)
    if since and since in order:
        lo = order.index(since)
    if until and until in order:
        hi = order.index(until) + 1
    window = order[lo:hi]
    try:
        n = int(last)
    except (TypeError, ValueError):
        n = 0
    if n > 0:
        window = window[-n:]
    return set(window)


def cmd_transcript() -> int:
    """Extract part of the session transcript INTO A FILE and print only its path.

    Argv::

        transcript index|turn|find --transcript P
                   [--turn ID] [--pattern RE]
                   [--since ID] [--until ID] [--last N] [--out F]

    Written for the audit agents, not for the main session. An agent auditing a claim needs
    to know what the session actually ran and said — often several turns back — and there
    are three bad ways to give it that. Asking the main agent to write it down makes the
    turn's own author the source for the record of the turn. Having guard accumulate every
    turn into a file, forever, pays for a full record on every turn to serve the few that
    are ever audited. Printing the extract to stdout puts it in the CALLER's context, which
    is the cost this whole design exists to avoid.

    So: the extract goes to a file, stdout carries the path and a one-line summary, and the
    agent Reads what it asked for — or hands the path to another agent, which is the cheap
    way for two of them to look at the same evidence.

    Fail-open like every other subcommand: an unreadable transcript, an unknown turn, or a
    bad pattern prints a one-line reason and exits 0. An agent that cannot get an extract
    must say so and judge on what it has, not stall.
    """
    argv = sys.argv[2:]
    op = argv[0].lower() if argv else ""
    opts: dict[str, str] = {}
    i = 1
    while i < len(argv) - 1:
        if argv[i].startswith("--"):
            opts[argv[i][2:]] = argv[i + 1]
            i += 2
        else:
            i += 1

    if op not in ("index", "turn", "find"):
        print("guard transcript: expected `index`, `turn`, or `find`.", file=sys.stderr)
        return 0
    tpath = opts.get("transcript", "")
    path = Path(tpath) if tpath else None
    if path is None or not path.is_file():
        print(f"guard transcript: no readable transcript at {tpath or '(none given)'}",
              file=sys.stderr)
        return 0

    project_dir = _cli_project_dir()
    session_id = opts.get("session", "") or path.stem
    out = Path(opts["out"]) if opts.get("out") else None
    rows = _turn_index(path)
    order = [r["turn"] for r in rows]
    window = _turn_window(order, opts.get("since", ""), opts.get("until", ""),
                          opts.get("last", ""))

    if op == "index":
        shown = [r for r in rows if r["turn"] in window]
        body = "# Turns in this session\n\n" + "\n".join(
            f"- `{r['turn']}` {r['at']} — {r['head']}" for r in shown) + "\n"
        dest = out or _extract_dir(project_dir, session_id) / "index.md"
        if not _write_extract(dest, body):
            print(f"guard transcript: could not write {dest}", file=sys.stderr)
            return 0
        print(f"{dest}\n{len(shown)} of {len(rows)} turns, oldest first.")
        _trace(project_dir, session_id, "transcript", "index", turns=len(shown))
        return 0

    if op == "turn":
        turn_id = opts.get("turn", "")
        turn = _turn_slice(str(path), turn_id)
        if turn is None:
            print(f"guard transcript: turn {turn_id or '(none given)'} is not in "
                  f"{path.name}", file=sys.stderr)
            return 0
        body = _render_turn(turn, turn_id)
        dest = out or _extract_dir(project_dir, session_id) / f"turn-{turn_id}.md"
        if not _write_extract(dest, body):
            print(f"guard transcript: could not write {dest}", file=sys.stderr)
            return 0
        print(f"{dest}\n{len(turn.get('tools', []))} tool calls, {len(body)} chars.")
        _trace(project_dir, session_id, "transcript", "turn", turn=turn_id,
               tools=len(turn.get("tools", [])))
        return 0

    pattern = opts.get("pattern", "")
    try:
        rx = re.compile(pattern, re.IGNORECASE)
    except (re.error, TypeError):
        print(f"guard transcript: {pattern!r} is not a valid regex", file=sys.stderr)
        return 0
    hits: list[str] = []
    seen: set[str] = set()
    current = ""
    for rec in _transcript_records(path):
        pid = rec.get("promptId")
        if isinstance(pid, str) and pid:
            current = pid
        if current not in window or rec.get("isSidechain") is True:
            continue
        blob = json.dumps(_message_of(rec).get("content"), ensure_ascii=False)
        m = rx.search(blob)
        if m:
            lo = max(0, m.start() - 200)
            hits.append(f"- turn `{current}`: …{blob[lo:m.end() + 200]}…")
            seen.add(current)
    body = (f"# Matches for `{pattern}`\n\n"
            f"Searched {len(window)} of {len(order)} turns.\n\n"
            + ("\n".join(hits) if hits else "(no match)") + "\n")
    dest = out or _extract_dir(project_dir, session_id) / "find.md"
    if not _write_extract(dest, body):
        print(f"guard transcript: could not write {dest}", file=sys.stderr)
        return 0
    print(f"{dest}\n{len(hits)} matches across {len(seen)} turns; "
          f"searched {len(window)} of {len(order)}.")
    _trace(project_dir, session_id, "transcript", "find", hits=len(hits))
    return 0


def _turn_identity(transcript_path: Any, prompt_id: Any) -> dict[str, Any] | None:
    """What KIND of turn this is, read from the transcript anchor. Never its content.

    Returns ``{origin_kind, command_name, bash_input}``, or None (fail-open) when the
    transcript is unreadable or the prompt_id is not in it. Every user of it is a skip,
    not an audit:

    - ``origin_kind`` — a typed prompt is ``"human"``. Anything else that opens a turn is
      machinery reporting in, and each such kind arrives with a fresh promptId and
      ``promptSource`` "system": ``"task-notification"`` for a background subagent's
      completion (NOT ``isMeta``, so otherwise indistinguishable from a typed prompt) and
      ``"peer"`` for an inbound ``SendMessage`` from a subagent or another session
      (``isMeta``). Both observed in 2.1.239. Recommending an audit on either is
      self-perpetuating, because guard's own dispatch is what produces them: the audit
      agents are background tasks, and they message the session back.
    - ``command_name`` — the slash command that opened the turn, so a turn opened by
      one of guard's own control commands can be skipped.
    - ``bash_input`` — the turn was opened by a user `!` command rather than a prompt.
      Such a turn carries no ``origin`` at all (verified in 2.1.239, session 6bc60bbf), so
      the ``origin_kind`` skip above lets it through; see `cmd_stop` for why it must not.

    Only the ANCHOR record is examined; records derived from the turn carry
    ``promptId=None`` and nothing about them changes the turn's kind. Kept separate from
    ``_turn_slice`` because the skips must be decided before guard does any work, and
    reading one record is cheaper than slicing a turn out of a multi-megabyte file.
    """
    if not isinstance(transcript_path, str) or not isinstance(prompt_id, str) or not prompt_id:
        return None
    path = Path(transcript_path)
    if not path.is_file():
        return None
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except (json.JSONDecodeError, ValueError):
            continue
        if not isinstance(rec, dict) or rec.get("promptId") != prompt_id:
            continue
        origin = rec.get("origin")
        content = _message_of(rec).get("content")
        text = content if isinstance(content, str) else ""
        return {
            "origin_kind": str(origin.get("kind") or "") if isinstance(origin, dict) else "",
            "command_name": _turn_command_name(text),
            "bash_input": text.lstrip().startswith(_BASH_TAG),
        }
    return None
