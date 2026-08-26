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

It takes NO argument. The session id comes from ``CLAUDE_CODE_SESSION_ID``, which a
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
from .agents import AUDIT_AGENTS, _eligible_agents
from .state import _audit_paused, _read_state


def cmd_candidates() -> int:
    """Print the turn-reading agents the router may name, one ``key=mode`` per line.

        candidates

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
    eligible = [k for k in _eligible_agents(state, [], [])
                if AUDIT_AGENTS[k].reads == "turn"]
    if not eligible:
        print("guard candidates: no turn-reading agent is switched on for this session.",
              file=sys.stderr)
        _trace(project_dir, session_id, "candidates", "none")
        return 0
    for key in eligible:
        print(f"{key}={_agent_mode(state, key)}")
    _trace(project_dir, session_id, "candidates", "listed", eligible=",".join(eligible))
    return 0
