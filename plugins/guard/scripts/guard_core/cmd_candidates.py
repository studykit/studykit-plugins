"""``candidates`` — the CLI verb the ROUTER runs to learn which agents it may name.

Not a hook event. The Stop hook used to print this list into ``additionalContext``, which
put it in the MAIN AGENT's context on every routed turn even though the main agent has no
use for it: it dispatches the router and then follows whatever sections the report names,
and the roster it was handed in between is a detail of a decision it does not make. So the
hook prints the command instead of the answer, and the router — the one reader — runs it and
gets the list first-hand.

The list is derived, not stored. ``_eligible_agents`` is the same function ``cmd_stop``
calls, over the same session state, so the two cannot disagree about which switches are on;
what this verb adds is the turn-reading filter, because the file-reading agents are
dispatched around the router (see ``cmd_stop``) and naming one to the router would be
offering it a key its caller never opens.

Its only argument is which dispatch path is asking (``--doc`` for the document router,
nothing for the turn router). Neither router is told a session id: it comes from
``CLAUDE_CODE_SESSION_ID``, which a
subagent's Bash carries as its PARENT session's id — verified in 2.1.239: a subagent's
`echo $CLAUDE_CODE_SESSION_ID` printed the main session's id, not one of its own. That is
what makes this verb usable from the router at all, since guard's state and turn
directories are named by the main session's id and a router reading its own would find an
unconfigured project with every switch off. The env var is documented for Bash tool
subprocesses and to match the hook payload's ``session_id``
(`wiki/ref/claude-code-session-id-env.md`).
"""

from __future__ import annotations

import os
import sys

from .config import _agent_mode, _load_config
from .paths import _cli_project_dir, _trace
from .agents import (AUDIT_AGENTS, REPORT_PATH, TURN_PATH, _eligible_agents,
                     _path_entry)
from .state import _audit_paused, _read_state


def cmd_candidates() -> int:
    """Print what the router may name, one ``entry=mode`` per line.

        candidates            # the turn path, for `turn-router`
        candidates --doc      # the document path, for `report-router`

    Read-only: it touches no state and honors no write marker, because it answers a question
    the router is entitled to ask and changes nothing by asking. Prints in ``AUDIT_AGENTS``
    order, which is the order the router's report must preserve — the read-only auditors
    before the correctors, so a corrector never rewrites a sentence an auditor was about to
    flag. That ordering therefore lives in one place, the roster, and reaches the router as
    the order of the lines rather than as a rule it has to be told.

    Three shapes that print no keys, and they must not look alike on stderr. No session id
    is an installation problem. A muted session is the user having switched guard off, which
    is an answer. An empty list is a real answer too, and one the router should never see on
    the routed path, since the hook prints this command only when at least one turn-reading
    agent is eligible — so each is called out rather than left as silence the router would
    have to interpret.

    On the ``--continue`` / bare ``--resume`` carve-out in the reference above, the env var
    may carry the startup id while the hooks carry the resumed one. That surfaces here as an
    empty roster for a session whose state lives under the other id, which is why the empty
    case is explicit: the router is told the lookup came back empty rather than being handed
    silence it could read as "nothing is on".
    """
    argv = sys.argv[2:]
    path = REPORT_PATH if argv and argv[0].strip() == "--doc" else TURN_PATH
    session_id = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    project_dir = _cli_project_dir()
    if not session_id:
        print("guard candidates: no CLAUDE_CODE_SESSION_ID in this environment — cannot "
              "tell which session's switches to read.", file=sys.stderr)
        _trace(project_dir, None, "candidates", "no_session")
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    # The mute, honored here as well as in `cmd_stop`. On the routed path this is dead
    # weight — a muted session returns before the router is ever dispatched, so this verb
    # is not reached — but the document path (`inputs --file`) has no Stop hook in front of
    # it, and its router asks this command what is on. Without this, `guard off` would
    # silence the turn audit and leave the document audit running, which is not what a
    # switch labelled off means.
    if _audit_paused(state):
        print("guard candidates: this session is muted (`guard off`) — nothing is eligible.",
              file=sys.stderr)
        _trace(project_dir, session_id, "candidates", "paused")
        return 0
    # The file lists are deliberately empty. Only the turn-reading agents are routed, and
    # `_eligible_agents` gates a file-reading one on having a file of its own kind — so
    # passing nothing is what makes those ineligible here, which is exactly the filter this
    # verb wants. Reading the recorded lists instead would let a file-reading agent through
    # to a router whose caller opens no section for it.
    # `routed` drops `korean-corrector`: the translator's report hands it over, so offering it
    # here would ask the router to judge a translation that does not exist while it reads.
    eligible = [k for k in _eligible_agents(state, [], [])
                if AUDIT_AGENTS[k].reads == "turn" and AUDIT_AGENTS[k].routed]
    if not eligible:
        print("guard candidates: no turn-reading agent is switched on for this session.",
              file=sys.stderr)
        _trace(project_dir, session_id, "candidates", "none")
        return 0

    # Key to entry-point name, once, here — see `_path_entry`. What the line names is what
    # the caller invokes, which is an agent for most rows and a skill for `clarity-auditor`;
    # which tool to reach for is the router's report template's business, not this verb's. An audit
    # with no entry on this path drops out, and on `--doc` that is most of them: the Korean
    # pair writes and checks a translation a document never gets, and this is what replaces
    # the paragraph the document router used to need telling it to refuse those two by name.
    named = [(k, e) for k in eligible if (e := _path_entry(k, path))]
    if not named:
        print(f"guard candidates: nothing on the {path} path is switched on for this "
              "session.", file=sys.stderr)
        _trace(project_dir, session_id, "candidates", "none_on_path", path=path)
        return 0
    for key, entry in named:
        # A switch-free agent has no config key to read a mode from, so its mode is the one
        # in the roster. Reading `_agent_mode` for it would return the OFF default and print
        # a line the router is told to ignore. The mode is the AUDIT's, so it is read from
        # the key even though the line prints the entry point.
        fixed = AUDIT_AGENTS[key].fixed_mode
        print(f"{entry}={fixed or _agent_mode(state, key)}")
    _trace(project_dir, session_id, "candidates", "listed", path=path,
           eligible=",".join(e for _, e in named))
    return 0
