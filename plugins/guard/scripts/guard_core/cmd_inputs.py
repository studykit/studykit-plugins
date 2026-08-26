"""``inputs`` — the CLI verb an agent runs to locate the turn it was sent to work on.

Not a hook event. The Stop hook used to print the playbook path, the turn directory, the
answer file and the transcript into ``additionalContext``, which put four absolute paths in
the MAIN AGENT's context on every routed turn so that it could copy them into a dispatch.
Every one of them is derivable from the turn id, and the main agent derives none of them —
it relays them, which is a step that can only lose fidelity.

So the dispatch carries the turn id, and whoever was sent runs this verb to get the rest.
The paths are then read by the party that opens them, produced by the code that owns the
layout (``turnrec``, ``dispatch``) rather than re-spelled by a caller.

Like ``candidates``, it takes the session from ``CLAUDE_CODE_SESSION_ID``, which a
subagent's Bash carries as its PARENT session's id — that is what lets a subagent reach
state written under the main session's id (`wiki/ref/claude-code-session-id-env.md`).

The transcript is the one field guard cannot derive: it is the host's path, handed to the
Stop hook in its payload, so ``cmd_stop`` records it in session state and this verb reads it
back. A session whose state has no transcript yet prints every other field and says so on
stderr, because an agent that needs history must be able to tell "no transcript" from "I
built the path wrong".
"""

from __future__ import annotations

import os
import sys

from .config import _load_config
from .paths import _cli_project_dir, _trace
from .state import _read_state
from .turnrec import _turn_record_file, _turn_request_file
from .dispatch import _playbook_path


def cmd_inputs() -> int:
    """Print the per-turn paths for one turn, one ``key: value`` per line.

        inputs <turn-id>

    The turn id is the only argument because it is the only thing the caller knows that
    this process cannot work out. Everything printed is derived from it plus the session:
    the answer file and the request file from ``turnrec``'s layout, the playbook from the
    plugin root, the transcript from what the Stop hook recorded.

    Absolute paths, and the turn directory is NOT factored out into a placeholder the way
    the old dispatch text did it. That form existed to save characters in the main agent's
    context; here the reader is the agent that will open the file, and handing it a path it
    must assemble is how a Read fails on a path nobody typed wrong.

    The request file is printed only when it exists. It is written at UserPromptSubmit and
    a turn guard never saw a prompt for has none — the router is required to judge from the
    answer alone then, and a path to a missing file would have it Read, fail, and guess at
    why.

    Fail-open, like every other verb: a missing session id or an unreadable state file
    prints a reason on stderr and exits 0. The agent that called this is told to say what it
    could not reach rather than stall, and an agent that stalls here stalls the turn.
    """
    argv = sys.argv[2:]
    if not argv or not argv[0].strip():
        print("guard inputs: no turn id given — `inputs <turn-id>`.", file=sys.stderr)
        return 0
    prompt_id = argv[0].strip()

    session_id = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    project_dir = _cli_project_dir()
    if not session_id:
        print("guard inputs: no CLAUDE_CODE_SESSION_ID in this environment — cannot tell "
              "which session's turn to locate.", file=sys.stderr)
        _trace(project_dir, None, "inputs", "no_session")
        return 0

    answer = _turn_record_file(project_dir, session_id, prompt_id).resolve()
    print(f"playbook: {_playbook_path()}")
    print(f"answer file: {answer}")
    request = _turn_request_file(project_dir, session_id, prompt_id).resolve()
    if request.is_file():
        print(f"request file: {request}")

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    transcript = state.get("transcript_path")
    if isinstance(transcript, str) and transcript:
        print(f"transcript: {transcript}")
        print(f"turn: {prompt_id}")
    else:
        print("guard inputs: no transcript recorded for this session — history is "
              "unavailable; judge on what you have.", file=sys.stderr)
    _trace(project_dir, session_id, "inputs", "printed", prompt_id=prompt_id)
    return 0
