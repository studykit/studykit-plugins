"""``dispatch`` — the turn's dispatch text, printed for the forked audit skill.

The other half of the Stop hook. Stop decides whether a finished turn has anything to audit
and says one line: invoke ``guard:audit`` with this turn's id. That skill runs in a forked
context and this verb is what fills it in — the same text Stop used to print, built by
``dispatch.turn_dispatch_text`` from the same session state, now paid for in the fork's
context instead of the main agent's.

Three things it must do, all of them about not auditing the wrong thing:

- **Take the turn id from the caller.** It is an argument, not a lookup. The state file's
  pending marker is an inference about which turn the user means, which is the right answer
  for someone typing ``/guard:<agent>`` and the wrong one here: the hook knows exactly which
  turn ended, and an audit pointed at the neighbouring turn is a failure nothing downstream
  can detect.
- **Treat that id as a lookup key and nothing else.** It arrives through a model, so it is
  validated for shape and used to name a file under the session's own turn directory. An id
  that does not match is refused rather than joined onto a path.
- **Exit 0 with a legible line, always.** An injected command that exits non-zero aborts the
  whole skill invocation and the model never sees the body
  (``wiki/ref/claude-code-skill-injection-and-fork-probe.md`` for the mechanics), which is
  guard going silently dormant. So every failure here is a sentence the fork can relay.
"""

from __future__ import annotations

import os
import re
import sys

from .config import _load_config
from .paths import _cli_project_dir, _trace
from .state import _read_state
from .turnrec import _turn_record_file
from .dispatch import turn_dispatch_text


# The shape a turn id may have, and the rule is the id's JOB rather than its format. A
# transcript ``prompt_id`` is a UUID today, but validating for one would make guard wrong the
# day the host changes it — and would be checking the wrong thing anyway. The value's only job
# is to name one path segment under the session's own turn directory, so what has to be
# excluded is a separator or a relative step, not a non-hex character.
_TURN_ID_RE = re.compile(r"^[A-Za-z0-9._-]{1,128}$")


def _usable_turn_id(turn: str) -> bool:
    return bool(_TURN_ID_RE.match(turn)) and turn not in (".", "..")


def _arg(argv: list[str], flag: str) -> str:
    """The value of ``--flag`` in ``argv``, or empty. No error on a flag with no value."""
    if flag in argv:
        i = argv.index(flag)
        if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
            return argv[i + 1]
    return ""


def cmd_dispatch() -> int:
    argv = sys.argv[2:]
    positional = [a for a in argv if not a.startswith("--")]
    turn = _arg(argv, "--turn") or (positional[0] if positional else "")
    # `CLAUDE_CODE_SESSION_ID` is documented for Bash tool subprocesses and stated to match
    # the `session_id` in the hook payload, which is what guard's state and turn directories
    # are named by (`wiki/ref/claude-code-session-id-env.md`). So the session needs no
    # argument: passing it through the skill body would add a value the model could get
    # wrong about a fact the runtime already knows.
    session = (_arg(argv, "--session") or os.environ.get("CLAUDE_CODE_SESSION_ID") or "")
    project_dir = _cli_project_dir()

    if not turn or not _usable_turn_id(turn):
        print("guard: no usable turn id was passed to `dispatch`, so there is nothing to "
              "audit. Do not audit anything; report this line to the session that invoked "
              "you.")
        _trace(project_dir, session or None, "dispatch", "bad_turn_id", turn=turn[:80])
        return 0
    if not session:
        print("guard: the session id is not in this environment, so guard cannot find the "
              "turn's record. Do not audit anything; report this line to the session that "
              "invoked you.")
        _trace(project_dir, None, "dispatch", "no_session")
        return 0
    if not _turn_record_file(project_dir, session, turn).is_file():
        print(f"guard: no turn record for {turn} in this session, so there is nothing to "
              "audit. Do not audit anything; report this line to the session that invoked "
              "you.")
        _trace(project_dir, session, "dispatch", "no_record", prompt_id=turn)
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session, config)
    # The transcript path comes from state rather than from an argument: Stop recorded it
    # there, it is a session-long fact, and it is the same value the on-demand
    # `/guard:<agent>` path already reads from there.
    transcript = state.get("transcript_path")
    transcript = transcript if isinstance(transcript, str) else ""
    text, outcome, eligible = turn_dispatch_text(project_dir, session, turn, state, config,
                                                 transcript)
    if not eligible:
        print("guard: no agent is eligible for this turn, so there is nothing to audit. Do "
              "not audit anything; report this line to the session that invoked you.")
        _trace(project_dir, session, "dispatch", "none_eligible", prompt_id=turn)
        return 0
    print(text)
    _trace(project_dir, session, "dispatch", outcome, prompt_id=turn,
           eligible=",".join(eligible))
    return 0
