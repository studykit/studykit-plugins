"""``pre-fetch`` — PreToolUse, sending the main session's network reads to the fetcher.

The problem this exists for. When ``ext-docs-fetcher`` is on, this project's rule is that a
page the session cites gets saved, so the citation stays inspectable after the page changes.
Stating that rule as session context and asking the main agent to honour it is what guard did
before, and a standing sentence is exactly the kind of instruction that survives one turn and
then quietly stops applying: nothing reports that it was skipped, and the answer that skipped
it looks like every other answer. A denied tool call cannot be skipped.

So the sentence becomes a rule the host applies, and the reason string carries what the
sentence used to say — which agent to dispatch instead.

Two limits, both deliberate, and both about not blocking a party that has no way forward.

**Only the main conversation.** Inside a subagent this hook fails open. A subagent cannot
dispatch another agent — the host filters ``Agent`` out of every subagent's tool list
(measured; see wiki/ref/claude-code-skill-fork-context.md) — so denying its fetch would leave
it with the tool gone and the replacement unreachable. That includes ``ext-docs-fetcher``
itself, which is the one subagent that must fetch; the main-conversation test covers it
without naming it, and a test by name would be a second place to keep the agent's name
correct.

**Only when the switch is on.** ``ext-docs-fetcher`` off means the project did not ask for
this, and guard's standing invariant is that installing it changes nothing until a switch is
turned on. This is the one hook where that matters most: every other one reports on work
already done, and this one stops work from happening.

Fail open everywhere else too, like the rest of guard's hooks: an unreadable payload, a
missing project dir, a config that will not load all return silently and let the host's
normal permission flow decide.
"""

from __future__ import annotations

import json
import sys

from .agents import _agent_id
from .config import _HOST_IS_CODEX, _load_config, _switch_on
from .paths import _project_dir, _trace
from .payload import _read_payload, _session_id
from .state import _read_state


# The network tools this redirects. `WebSearch` is here for the same reason as `WebFetch`:
# a session that may search but not fetch reads the result snippets and answers from those,
# which is the unattributed-summary failure the refs directory exists to prevent — and it
# leaves no page to save.
_FETCH_TOOLS = frozenset({"WebFetch", "WebSearch"})

_AGENT = "ext-docs-fetcher"


def _deny(reason: str) -> None:
    json.dump({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }, sys.stdout)


def cmd_pre_fetch() -> int:
    """PreToolUse on the network tools. Deny the main conversation; name the agent instead."""
    payload = _read_payload()
    if payload is None:
        return 0
    tool = payload.get("tool_name")
    if tool not in _FETCH_TOOLS:
        return 0

    # Codex ships no fetcher, so a deny there would forbid a tool and name no replacement.
    if _HOST_IS_CODEX:
        return 0

    project_dir = _project_dir()
    if project_dir is None:
        return 0

    # Traced on every network call, not only on a deny — whether this hook fires at all, and
    # whether the host populated `agent_type` when it did, is what a deny-only trace cannot
    # tell apart from "the session never fetched". `_trace` writes only when GUARD_TRACE is set.
    _trace(project_dir, None, "pre-fetch", "seen",
           agent=payload.get("agent_type"), tool=tool)

    # `agent_type` is absent in the main conversation and carries the plugin-scoped name
    # inside a subagent, so its presence IS the "am I a subagent" test.
    if payload.get("agent_type") is not None:
        return 0

    config = _load_config(project_dir)
    session_id = _session_id(payload)
    # The live mode, not the file's: `/guard:settings` can turn this off mid-session, and a
    # hook that read only the config would keep denying after the user switched it off.
    cfg = _read_state(project_dir, session_id, config) if session_id else config
    if not _switch_on(cfg, _AGENT):
        return 0

    _trace(project_dir, session_id, "pre-fetch", "deny", tool=tool)
    _deny(
        f"guard: this project saves copies of the documentation it cites, so {tool} from the "
        f"main session is blocked. Dispatch {_agent_id(_AGENT)} with the user's question "
        "verbatim and wait for it: it reports the local path of what is already saved, "
        "fetches and saves the primary source when nothing is, and says which of the two it "
        "did — or reports none. Read the files it names yourself."
    )
    return 0
