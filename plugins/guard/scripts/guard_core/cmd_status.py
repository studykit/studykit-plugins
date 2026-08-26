"""``toggle`` and ``status`` — the session mute, and the indicator that makes it visible.

``toggle`` (UserPromptExpansion, for ``/guard:toggle [on|off]``) arms or mutes the automatic
audit for THIS SESSION — ``audit_paused`` in the session state, never guard.local.json, so it
cannot change what the project does by default. A session STARTS muted
(``state._read_state``), which makes ``on`` the common direction: it clears the pause and is
the only thing that ever does. An empty argument flips. While muted, ``stop`` recommends
nothing and ``user-prompt`` names no answer file, but the pending target and the answer file
are still recorded — the Codex adapter reads that marker. The hook does the work and blocks
the expansion, so its message reaches the user directly and no model is invoked to relay a
sentence the hook has already finished (see ``emit._emit_expansion``); the command file
exists to make the matcher reachable at all, and its body never runs.

``status`` (CLI, stdin JSON) is the other half, and starting muted is what makes it
load-bearing rather than a convenience: the mute is a feature only because it is visible, and
now it is the state every session opens in. It prints one short field — ``guard <n>`` armed /
``guard off`` muted / ``guard · on`` and ``guard ·`` for the two states of a project with
nothing switched on — or NOTHING on any failure, because its stdout goes straight into the
user's status bar. The mute decides the word in EVERY branch, including the last pair: a
toggle that leaves the segment unchanged cannot be told from a toggle that did not fire.
A plugin cannot own the main ``statusLine``, so the user composes this segment into theirs
(``/guard:statusline`` offers to do it). It reads only the small config and state files,
nothing else: it runs on every assistant message. Not a hook event.

``toggle-cli`` (CLI, argv) is the same mute for a shell prompt rather than for the model's
slash command. It exists because ``/guard:toggle`` costs a turn: typing it into Claude Code
sends a prompt, and the answer comes back as a blocked expansion. From a terminal the user
already has, flipping guard should not enter the conversation at all. The two verbs share
``_parse_toggle_arg``, ``_apply_toggle`` and ``_mute_sentence``, so the accepted words and
the resulting sentence cannot drift between them; what differs is only where the session id
comes from (``CLAUDE_CODE_SESSION_ID`` rather than the payload), how the answer leaves
(stdout rather than a blocked expansion), and which command the sentence names as the way
to arm guard.
"""

from __future__ import annotations

import json
import os
import sys

from pathlib import Path

from .config import _load_config, _switch_on
from .paths import _cli_project_dir, _project_dir, _trace
from .payload import _read_payload, _session_id
from .emit import _emit_expansion
from .agents import AUDIT_AGENTS
from .state import _audit_paused, _read_state, _write_state


# Status-line colours. Dim for the state guard chose not to shout about, green for armed,
# yellow for muted — the one state the user set and can forget. Kept as constants because a
# status line that emits a stray escape sequence garbles the user's terminal row.
_ANSI_RESET = "\033[0m"


_ANSI_ARMED = "\033[32m"


_ANSI_MUTED = "\033[33m"


_ANSI_IDLE = "\033[2m"


def _shell_arm_hint() -> str:
    """How to arm guard from THIS shell, as the user's own wrapper is named.

    The wrapper sets ``GUARD_TOGGLE_NAME`` so a user who installed it under another name
    is not told to run a command their shell does not have. Falls back to the name the
    installer suggests.
    """
    name = os.environ.get("GUARD_TOGGLE_NAME", "").strip()
    return f"{name} on" if name else "guard on"


def _parse_toggle_arg(arg: str) -> str | None:
    """Map a user's word to ``on`` / ``off`` / ``flip``, or None if it is not one.

    One vocabulary for both entry points. The synonyms are here rather than at each call
    site because a word accepted by the slash command and rejected by the shell one is a
    difference the user has no way to predict.
    """
    arg = arg.strip().lower()
    if arg in ("", "flip", "toggle"):
        return "flip"
    if arg in ("on", "resume", "enable", "arm", "unmute"):
        return "on"
    if arg in ("off", "pause", "disable", "mute"):
        return "off"
    return None


def _mute_sentence(state: dict, paused: bool, arm_hint: str) -> str:
    """The one description of a session's mute, for reporting it and for changing it.

    Split from ``_apply_toggle`` because the CLI's ``status`` verb reports without writing,
    and the copy it used to keep drifted from this one. A reader comparing ``guard on`` with
    ``guard status`` saw two answers and no way to tell which reflected the state.

    One line each, and every branch opens with ON or OFF. The old wording buried the new
    state mid-sentence ("no longer muted, but ..."), which reads as a toggle that did not
    fire — the flip is the one thing the user is checking for here.

    ON or OFF, and nothing about the roster. Neither the names nor a count belongs here:
    which agents run is the router's answer, decided per turn against what the turn actually
    contains, so anything stated at toggle time describes a different question than the one
    the user will see answered. A roster restated here is also a second copy to drift.
    ``/guard:settings`` is where the switches live.

    The one exception is having nothing switched on, which is not a roster detail but a
    different outcome — the turn-reading agents cannot run at all — and saying so is what
    stops `guard on` from promising an audit that will not come.
    """
    if paused:
        return f"guard: audits OFF for this session. `{arm_hint}` to arm."
    if any(_switch_on(state, k) for k in AUDIT_AGENTS):
        return "guard: audits ON for this session."
    # Not "nothing will run": `ext-docs-auditor` has no switch, so a turn that writes a
    # saved reference is still named at Stop with every agent off. Overstating the silence
    # here is how a user reads that dispatch as guard ignoring their settings.
    return ("guard: audits ON for this session, but no agent is switched on — only saved "
            "references are checked. `/guard:settings` to switch one on.")


def _apply_toggle(project_dir: Path, session_id: str, action: str, arm_hint: str) -> str:
    """Write the mute for one session and return the sentence describing the result.

    The message is the product, not a side effect: both callers show it verbatim, so the
    branches below are the only place either one decides what the user is told.

    ``arm_hint`` is how the CALLER's user arms guard — `/guard:toggle on` from the slash
    command, `guard on` from the shell. It is a parameter because the sentence is shown to
    someone who just typed one of the two, and naming the other interface is advice they
    cannot follow where they are standing.
    """
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    paused = (not _audit_paused(state)) if action == "flip" else (action == "off")

    state["audit_paused"] = paused
    _write_state(project_dir, session_id, state)
    return _mute_sentence(state, paused, arm_hint)


def cmd_toggle() -> int:
    """UserPromptExpansion for `/guard:toggle [on|off]`. Mute or unmute this session.

    The hook does the work rather than telling the model to: `command_args` carries the
    argument (hooks docs, excerpt in the refs dir as `claude-code-statusline.md`), so no
    argument means flip, `on`/`off` set it outright, and the outcome does not depend on a
    model reading a procedure correctly. Nothing here is addressed to a model — the
    expansion is blocked, so every string below is read by a person.

    Session state only. It cannot touch guard.local.json, which is what makes this safe to
    reach for mid-conversation: it cannot change what any other session does. And since every
    session starts muted, an `off` here is not undone by the next session either — there is
    nothing this can leave behind. `on` means auditing on, so it CLEARS the pause — the
    user's vocabulary is about guard, not about the flag's name.
    """
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None:
        return 0
    # Not silent, unlike every other guard failure. A hook that prints nothing lets the model
    # report the mute it was asked for and never got — the same shape as the crashed toggle
    # this project has already seen narrated as success. The two neighbouring branches (no
    # session id, unrecognised argument) say so out loud for the same reason.
    if project_dir is None:
        _emit_expansion(
            "guard: no project directory resolved — nothing changed."
        )
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        _emit_expansion("guard: no usable session id, so there is no session to mute.")
        return 0

    raw = payload.get("command_args")
    raw = raw if isinstance(raw, str) else ""
    action = _parse_toggle_arg(raw)
    if action is None:
        _emit_expansion(
            f"guard: `{raw.strip().lower()}` is not an argument — use `on`, `off`, or "
            "nothing to flip. Nothing changed."
        )
        return 0

    msg = _apply_toggle(project_dir, session_id, action, "/guard:toggle on")
    _emit_expansion(msg)
    _trace(project_dir, session_id, "toggle", "set", arg=action)
    return 0


def cmd_toggle_cli() -> int:
    """CLI for the shell wrapper: ``toggle-cli [on|off|status]``. Prints one line.

        guard_hook.py toggle-cli          — flip this session
        guard_hook.py toggle-cli on       — arm it
        guard_hook.py toggle-cli off      — mute it
        guard_hook.py toggle-cli status   — report without changing anything

    Same mute, same session, same words as `/guard:toggle` — see `_apply_toggle`. The
    session id comes from `CLAUDE_CODE_SESSION_ID`, which Claude Code sets in every Bash
    tool subprocess to the value the hook payload carries
    (`wiki/ref/claude-code-session-id-env.md`). That equality is the whole basis for this
    verb: it is what lets a shell command address the same `state/<sid>.json` the Stop hook
    will read at the end of the turn.

    `status` is here rather than in the `status` verb because that one is the status-LINE
    segment: it reads a JSON payload on stdin and prints ANSI for a terminal row. A person
    asking "is guard on right now" from a prompt wants a sentence, and wants it without
    constructing a payload.

    Never silent, unlike most of guard. Every other failure path in this plugin fails open
    because the alternative is blocking the user's session; here the user is standing at a
    prompt waiting to be told what happened, and a command that prints nothing and exits 0
    reads as "done" — which is the one outcome this must never fake. Exit code carries the
    same information for scripting: 0 only when the state was read or written as asked.
    """
    argv = sys.argv[2:]
    raw = argv[0] if argv else ""

    session_id = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    if not session_id:
        print("guard: no CLAUDE_CODE_SESSION_ID in this environment — this only works in "
              "a shell Claude Code launched. Nothing changed.", file=sys.stderr)
        return 1
    # Reuse the payload's own validation: the id is interpolated into a state filename.
    if _session_id({"session_id": session_id}) is None:
        print("guard: CLAUDE_CODE_SESSION_ID is not a usable session id. Nothing changed.",
              file=sys.stderr)
        return 1

    project_dir = _cli_project_dir()

    if raw.strip().lower() in ("status", "show"):
        state = _read_state(project_dir, session_id, _load_config(project_dir))
        print(_mute_sentence(state, _audit_paused(state), _shell_arm_hint()))
        _trace(project_dir, session_id, "toggle-cli", "show")
        return 0

    action = _parse_toggle_arg(raw)
    if action is None:
        print(f"guard: `{raw.strip().lower()}` is not an argument — use `on`, `off`, "
              "`status`, or nothing to flip. Nothing changed.", file=sys.stderr)
        return 1

    # The state file is the only record of the mute, so a write that silently failed would
    # leave the user with a sentence saying the flip happened. `_write_state` swallows
    # OSError by design (guard fails open in hooks), so confirm by reading back rather
    # than trusting it. `flip` has to resolve its target BEFORE the write — comparing the
    # result against a state re-read afterwards would compare it with itself and pass for
    # any outcome at all.
    config = _load_config(project_dir)
    before = _audit_paused(_read_state(project_dir, session_id, config))
    expected = (not before) if action == "flip" else (action == "off")

    msg = _apply_toggle(project_dir, session_id, action, _shell_arm_hint())

    verify = _read_state(project_dir, session_id, config)
    if _audit_paused(verify) is not expected:
        print("guard: could not write the session state — the mute is unchanged.",
              file=sys.stderr)
        _trace(project_dir, session_id, "toggle-cli", "write_failed", arg=action)
        return 1
    print(msg)
    _trace(project_dir, session_id, "toggle-cli", "set", arg=action)
    return 0


def cmd_status() -> int:
    """Status-line segment: is guard auditing this session? Reads stdin, prints one field.

    A plugin cannot install the MAIN status line — only `agent` and `subagentStatusLine` are
    honored in a plugin's settings.json — so this prints a segment the user composes into
    whatever status line they already run. The excerpt is saved in the refs dir as
    `claude-code-statusline.md`.

    Two documented constraints shape the body. It runs on every assistant message, debounced
    at 300ms, and a newer update cancels the one in flight: so it reads only the small
    config and state JSON files and does nothing else — no git, no transcript, no subprocess.
    And its stdout goes
    straight into the user's status bar: so every failure prints NOTHING rather than an
    error message, because a status line is the one place guard must never shout from.
    """
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, ValueError, OSError, UnicodeDecodeError):
        return 0
    if not isinstance(payload, dict):
        return 0

    # The status-line payload names the launch directory, which is where guard's state hangs
    # off. `CLAUDE_PROJECT_DIR` is the fallback so the same command works when a user wires
    # it into a script that does not forward the JSON.
    ws = payload.get("workspace")
    root = ws.get("project_dir") if isinstance(ws, dict) else None
    for cand in (root, payload.get("cwd"), os.environ.get("CLAUDE_PROJECT_DIR")):
        if isinstance(cand, str) and cand.strip():
            root = cand.strip()
            break
    else:
        return 0
    session_id = _session_id(payload)
    if not isinstance(root, str) or session_id is None:
        return 0

    try:
        project_dir = Path(root)
        state = _read_state(project_dir, session_id, _load_config(project_dir))
    except Exception:
        return 0

    armed = [k for k in AUDIT_AGENTS if _switch_on(state, k)]
    # The mute is a feature only because it is visible, so it decides the WORD in every
    # branch — including the one where no agent is switched on. Ordering `armed` ahead of
    # the mute, or letting the empty-roster case print the same dot either way, makes
    # `/guard:toggle` a command with no observable effect on a project that has switched
    # nothing on: the state flips and the segment does not move. That is indistinguishable
    # from a broken toggle, which is how it was read.
    if not armed:
        # Nothing switched on for this project. Still not an error and still not worth
        # shouting about, so it keeps the dim dot — but the dot follows the mute, so the
        # toggle remains legible here too.
        word = "guard ·" if _audit_paused(state) else "guard · on"
        print(f"{_ANSI_IDLE}{word}{_ANSI_RESET}")
    elif _audit_paused(state):
        # Muted with agents configured is the state worth a colour: the user chose it and
        # can forget it, and unlike the branch above there is something being held back.
        print(f"{_ANSI_MUTED}guard off{_ANSI_RESET}")
    else:
        print(f"{_ANSI_ARMED}guard {len(armed)}{_ANSI_RESET}")
    return 0
