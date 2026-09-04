"""``toggle-cli`` and ``status`` — the session mute, and the indicator that makes it visible.

``toggle-cli`` (CLI, argv) arms or mutes guard for THIS SESSION —
``audit_paused`` in the session state, never guard.local.json, so it cannot change what the
project does by default. The state a session opens in is the project's ``audit-turn`` setting,
MUTED when the file says nothing (``state._read_state``), which makes ``on`` the common
direction: one stretch of work that wants guard, with the setting left alone. An empty
argument flips, and ``status`` reports without writing. While muted, ``stop`` says nothing,
``user-prompt`` names no answer file, and ``candidates`` tells an invoked audit that the
session is muted — but the pending target and the answer file are still recorded, so arming
guard and asking still reaches the turn.

The shell is the ONLY way in, through the ``guard`` wrapper the SessionStart hook puts on
``PATH``. There was a ``/guard:toggle`` slash command beside it and it was removed: flipping
guard is not something to say to the model. The command cost a turn — typing it sent a
prompt, and the answer came back as a blocked expansion — and it also cost a command file
and a ``UserPromptExpansion`` matcher that had to stay in step with each other. From a
terminal the user already has, the same flip touches the conversation not at all.

``status`` (CLI, stdin JSON) is the other half, and it is load-bearing rather than a
convenience: the mute is a feature only because it is visible. SessionStart says which state
the session opened in and the toggle prints its own result, but both scroll away — this field
is the only place the answer is still legible at the moment a user wonders. It prints one short field — ``guard <will
run>/<switched on>``, so ``guard 3/3`` armed, ``guard 0/3`` muted, ``guard 0/0`` for a project
with nothing switched on, each followed by ``· ⚑`` when the plan gate is armed and ``· ⚐``
when it is not — or NOTHING on any failure, because its stdout goes straight into the user's
status bar. The mute decides the word in EVERY branch, including the last pair: a
toggle that leaves the segment unchanged cannot be told from a toggle that did not fire.
A plugin cannot own the main ``statusLine``, so the user composes this segment into theirs
(``/guard:statusline`` offers to do it). It reads only the small config and state files,
nothing else: it runs on every assistant message. Not a hook event.
"""

from __future__ import annotations

import json
import os
import sys

from pathlib import Path

from .config import _load_config, _parse_switch, _switch_on
from .paths import _cli_project_dir, _trace
from .payload import _session_id
from .agents import AUDIT_AGENTS
from .state import _audit_paused, _plan_audit_paused, _read_state, _write_state


# Status-line colours, and one rule behind both halves: GREEN MEANS ARMED. The fraction is
# green while the session is auditing and dim while it is muted; the flag is green while the
# plan gate is armed and dim while it is not. Two independent switches, the same vocabulary,
# so a glance at the field counts the green rather than decoding two conventions. Kept as
# constants because a status line that emits a stray escape sequence garbles the user's
# terminal row.
_ANSI_RESET = "\033[0m"


_ANSI_ARMED = "\033[32m"


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

    One vocabulary for every entry point: the on/off words come from ``config``, which is
    also what the ``audit-turn`` / ``audit-plan`` settings are read with, because a word the
    config file accepts and this command rejects is a difference the user has no way to
    predict. ``flip`` is this command's alone — a setting has no "the other one".
    """
    arg = arg.strip().lower()
    if arg in ("", "flip", "toggle"):
        return "flip"
    parsed = _parse_switch(arg)
    if parsed is None:
        return None
    return "on" if parsed else "off"


def _mute_sentence(state: dict, paused: bool) -> str:
    """The one description of a session's mute, for reporting it and for changing it.

    Split from ``_apply_toggle`` because the ``status`` verb reports without writing,
    and the copy it used to keep drifted from this one. A reader comparing ``guard on`` with
    ``guard status`` saw two answers and no way to tell which reflected the state.

    One line each, and every branch opens with ON or OFF. The old wording buried the new
    state mid-sentence ("no longer muted, but ..."), which reads as a toggle that did not
    fire — the flip is the one thing the user is checking for here.

    ON or OFF, and nothing about the roster. Neither the names nor a count belongs here:
    which agents run is the router's answer, decided against what the turn actually contains
    when the user asks for an audit, so anything stated at toggle time describes a different
    question than the one the user will see answered. A roster restated here is also a second
    copy to drift. ``/guard:settings`` is where the switches live.

    The one exception is having nothing switched on, which is not a roster detail but a
    different outcome — the turn-reading agents cannot run at all — and saying so is what
    stops `guard on` from promising an audit that could not run.

    "ON" means armed, not running. Nothing audits a turn until the user invokes
    ``/guard:audit-turn``; what arming does is give that invocation a turn to work on. The
    sentence stays short rather than teaching that here — the session was told at
    ``SessionStart``, and this is a line printed at a shell prompt.
    """
    if paused:
        return f"guard: audits OFF for this session. `{_shell_arm_hint()}` to arm."
    if any(_switch_on(state, k) for k in AUDIT_AGENTS):
        return "guard: audits ON for this session — `/guard:audit-turn` to audit a turn."
    # Not "nothing will run": `ext-docs-auditor` has no switch, so a turn that writes a
    # saved reference is still named at Stop with every agent off. Overstating the silence
    # here is how a user reads that dispatch as guard ignoring their settings.
    return ("guard: audits ON for this session, but no agent is switched on — nothing to "
            "audit a turn with, and only saved references are checked. `/guard:settings` to "
            "switch one on.")


def _apply_toggle(project_dir: Path, session_id: str, action: str) -> str:
    """Write the mute for one session and return the sentence describing the result.

    The message is the product, not a side effect: the caller shows it verbatim, so the
    branches below are the only place anything decides what the user is told.
    """
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    paused = (not _audit_paused(state)) if action == "flip" else (action == "off")

    state["audit_paused"] = paused
    _write_state(project_dir, session_id, state)
    return _mute_sentence(state, paused)


def cmd_toggle_cli() -> int:
    """CLI for the shell wrapper: ``toggle-cli [on|off|status]``. Prints one line.

        guard_hook.py toggle-cli          — flip this session
        guard_hook.py toggle-cli on       — arm it
        guard_hook.py toggle-cli off      — mute it
        guard_hook.py toggle-cli status   — report without changing anything

    The mute, and the only way to reach it — see `_apply_toggle`. The
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
        print(_mute_sentence(state, _audit_paused(state)))
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

    msg = _apply_toggle(project_dir, session_id, action)

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

    Two switches, one field: the fraction is the turn audit, and the trailing flag is the
    plan gate — filled `⚑` armed, outline `⚐` muted. They are separate settings with separate commands and separate defaults, and
    this is the only place either one is visible without being asked for.

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
    # The plan gate is a SECOND switch, with its own default and its own command
    # (`guard-plan`), so it needs its own mark — and a mark rather than a word because this
    # field shares one terminal row with everything else the user's status line carries.
    # Presence against absence is enough to read it, but only because the mark is appended in
    # EVERY branch below: a `guard-plan` flip that left some segment unchanged would be the
    # unobservable toggle the next comment is about.
    # Filled flag armed, OUTLINE flag muted — the mark is always there, never absent. An
    # absent mark cannot be told from a guard that does not report plan audits at all, which
    # is exactly the reader who most needs to know the gate exists: someone who has never run
    # `guard-plan` and would otherwise never learn there is a switch. The two glyphs are the
    # same shape at the same width, so the field neither moves nor grows when it flips.
    #
    # Both are ordinary Unicode, deliberately: a private-use Nerd Font glyph has no fallback,
    # and this segment is composed into status lines whose font guard cannot know. U+2690 and
    # U+2691 have identical coverage in the fonts a terminal falls back to.
    #
    # It carries its OWN colour, closed before the fraction's begins. The two switches are
    # independent — `guard` cannot move the plan gate and `guard-plan` cannot move the
    # turn audit — so one colour spanning both would state a single verdict about two
    # settings: a green fraction beside a dim flag has to be able to say "auditing, gate off",
    # and one span over both cannot. Green armed, dim muted — the same vocabulary the fraction
    # uses, so the field is read by counting the green.
    if _plan_audit_paused(state):
        flag = f"{_ANSI_IDLE} · ⚐{_ANSI_RESET}"
    else:
        flag = f"{_ANSI_IDLE} · {_ANSI_RESET}{_ANSI_ARMED}⚑{_ANSI_RESET}"
    # One shape everywhere: agents that can run on the next finished turn over agents
    # switched on. `guard off` used to hold the muted case, and it read as a claim about guard
    # itself — which the neighbouring "nothing switched on" state, also nothing running for an
    # entirely different reason, then contradicted. The fraction cannot be read that way, and
    # it says what a bare count never did: how many switches are set at all.
    #
    # The numerator is only ever 0 or the whole denominator, because the mute is what governs
    # it. That is the fraction working, not a wasted digit: `guard` moves the
    # numerator and `/guard:settings` moves the denominator, so which command a reader needs
    # is legible from the field.
    #
    # ONE CORNER LOSES THE TEXTUAL DIFFERENCE: with nothing switched on, both mute states are
    # `0/0`, and only the colour separates them. That is a deliberate trade for one grammar
    # over a special case — but it is also the whole reason the colours below are not
    # decoration. Before touching them, note that a mute nobody can see is the failure that
    # killed the gate this mute replaced: `guard` must remain observable in every
    # state, and here the colour is the only thing carrying it.
    # Each half closes its own colour before the next opens — nesting the flag's spans inside
    # the fraction's left a reset in the middle of an open span, which renders correctly today
    # and is one edit away from not.
    #
    # The numbers AND the colour carry the mute, and the redundancy is the point. `0/N` muted
    # against `N/N` armed stays legible where colour cannot go — a log, a screenshot, a
    # terminal configured differently — while the colour is what makes the flip visible at a
    # glance in the row itself. It also covers the one case the numbers cannot: a project with
    # nothing switched on reads `0/0` either way, since there is no count for the numerator to
    # move, and green-versus-dim is then the only thing separating a muted session from an
    # armed one. Do not tint that pair identically.
    if _audit_paused(state):
        turn = f"{_ANSI_IDLE}guard 0/{len(armed)}{_ANSI_RESET}"
    elif not armed:
        # Armed, but nothing switched on: green because the session IS auditing, and `0/0`
        # because no turn-reading agent can run. Not a contradiction — `ext-docs-auditor` has
        # no switch, so a turn that writes a saved reference is still checked from here.
        turn = f"{_ANSI_ARMED}guard 0/0{_ANSI_RESET}"
    else:
        turn = f"{_ANSI_ARMED}guard {len(armed)}/{len(armed)}{_ANSI_RESET}"
    print(f"{turn}{flag}")
    return 0
