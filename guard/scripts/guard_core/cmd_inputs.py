"""``inputs`` — the CLI verb an agent runs to locate the turn it was sent to work on.

Not a hook event. The Stop hook used to print the closeout path, the turn directory, the
answer file and the transcript into ``additionalContext``, which put four absolute paths in
the MAIN AGENT's context on every turn so that it could copy them into a dispatch. Every one
of them is derivable from the turn id, and the main agent derives none of them — it relays
them, which is a step that can only lose fidelity.

So the dispatch carries the turn id — or nothing at all, when the user asked for the audit
themselves and named no turn — and whoever was sent runs this verb to get the rest.
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
from pathlib import Path

from .config import _load_config
from .paths import _cli_project_dir, _knowledge_dirs, _trace
from .state import _read_state
from .turnrec import (_turn_record_file, _turn_request_file,
                      _turn_translation_file)
from .dispatch import _closeout_path


def cmd_inputs() -> int:
    """Print the per-turn paths for one turn, one ``key: value`` per line.

        inputs [<turn-id>]

    The turn id is the only argument because it is the only thing the caller knows that
    this process cannot work out — and it is optional, because for the commonest audit the
    caller does not know it either: the user asks for the turn they just read, so an omitted
    id resolves to the last turn guard recorded. Everything printed is derived from that id
    plus the session: the answer file and the request file from ``turnrec``'s layout, the
    closeout file from the plugin root, the transcript from what the Stop hook recorded.

    Absolute paths, and the turn directory is NOT factored out into a placeholder the way
    the old dispatch text did it. That form existed to save characters in the main agent's
    context; here the reader is the agent that will open the file, and handing it a path it
    must assemble is how a Read fails on a path nobody typed wrong.

    The request file is printed only when it exists. It is written at UserPromptSubmit and
    a turn guard never saw a prompt for has none — the router is required to judge from the
    answer alone then, and a path to a missing file would have it Read, fail, and guess at
    why.

    ``turn`` is printed unconditionally and first. It used to appear only alongside a
    transcript, as half of a "history is here" pair; now it is also the ANSWER to a bare
    invocation, and a caller that resolved its target here must be able to see which turn it
    got rather than infer it from a path.

    Fail-open, like every other verb: a missing session id or an unreadable state file
    prints a reason on stderr and exits 0. The agent that called this is told to say what it
    could not reach rather than stall, and an agent that stalls here stalls the turn.
    """
    argv = sys.argv[2:]
    # `--file` is the document form: a file that is not a turn — one no turn produced and no
    # `Stop` ever saw. The turn id is the only thing this verb
    # cannot derive, so when there is no turn the caller supplies the one path in its place
    # and the rest is derived the same way. It lives here rather than in a verb of its own
    # because it answers the same question — where is the thing I was sent to work on — and a
    # second verb would be a second place for the layout to be spelled out.
    if argv and argv[0].strip() == "--file":
        return _inputs_for_file(argv[1:])
    prompt_id = argv[0].strip() if argv else ""

    session_id = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    project_dir = _cli_project_dir()
    if not session_id:
        print("guard inputs: no CLAUDE_CODE_SESSION_ID in this environment — cannot tell "
              "which session's turn to locate.", file=sys.stderr)
        _trace(project_dir, None, "inputs", "no_session")
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    # No turn id: the turn the user means is the last one guard recorded, and the `Stop`
    # hook records it on every human turn whatever the switches say. This is what lets the
    # audit entry points be invoked bare — `/guard:audit-turn` with nothing after it — so a
    # user who wants the turn they just read checked does not have to find an id first, and
    # a forked skill, which has no conversation to read one from, does not have to be handed
    # one. guard's own control turns never become this target (`cmd_stop`), so the marker
    # still points at the answer even after the user has asked about it.
    if not prompt_id:
        pending = state.get("pending_verify_prompt_id")
        prompt_id = pending.strip() if isinstance(pending, str) else ""
    if not prompt_id:
        print("guard inputs: no turn id given and none recorded for this session — "
              "`inputs <turn-id>` or `inputs --file <path>`.", file=sys.stderr)
        _trace(project_dir, session_id, "inputs", "no_pending")
        return 0

    answer = _turn_record_file(project_dir, session_id, prompt_id).resolve()
    # Printed whether or not history is available, and first, because the caller may not have
    # supplied it: a bare invocation resolved the turn HERE, and everything the caller then
    # says about it — the id it passes to an audit, the id it names in its report — has to be
    # this one rather than one it guessed at.
    print(f"turn: {prompt_id}")
    print(f"closeout: {_closeout_path()}")
    print(f"answer file: {answer}")
    # Derived, and printed whether or not the file is there. The caller is the party that knows
    # whether this turn was delivered in Korean — it either had the translation written an hour
    # ago or it did not — and `korean-translator` may not derive a path of its own, so the
    # rewrite after a correction needs this path named rather than reconstructed.
    print("translation file: "
          f"{_turn_translation_file(project_dir, session_id, prompt_id).resolve()}")
    request = _turn_request_file(project_dir, session_id, prompt_id).resolve()
    if request.is_file():
        print(f"request file: {request}")

    # One line per configured directory, in the order the user wrote them — precedence, and
    # a single line holding several paths would have to be split on a separator that a real
    # path may contain. Absent entirely when the project has configured none, which is the
    # normal case and is why the reader is told to treat absence as "no knowledge base"
    # rather than as a lookup that failed.
    for kdir in _knowledge_dirs(project_dir, config):
        print(f"knowledge dir: {kdir}")

    transcript = state.get("transcript_path")
    if isinstance(transcript, str) and transcript:
        print(f"transcript: {transcript}")
    else:
        print("guard inputs: no transcript recorded for this session — history is "
              "unavailable; judge on what you have.", file=sys.stderr)
    _trace(project_dir, session_id, "inputs", "printed", prompt_id=prompt_id)
    return 0


def _inputs_for_file(argv: list[str]) -> int:
    """``inputs --file <path>`` — the same keys, for a document with no turn behind it.

    Three fields are absent and each absence is a fact, not a gap:

    - no **request file**, because nobody typed a prompt that produced this document. The
      materiality call the router makes from a request is simply unavailable here.
    - no **closeout**. guard's turn closeout is written around a turn: findings go into the
      answer file, the reply is short and in the user's language, and the file the user reads
      is opened at the end. A document has no reply and nothing to open. The document router carries its own,
      much shorter, dispatch instructions instead — including the translation, which a document
      does get when its reader reads another language.
    - no **transcript** and no **turn**, and this one is easy to get wrong. A document reaching
      this path was not written in the MAIN session's transcript — the case it was built for was
      a brief written inside a subagent's own conversation — so handing that path over would
      offer history that cannot hold the document's provenance, and an agent would spend a
      search on it before finding out. The document is audited as what it says.

    Unlike the turn form, the path here comes from the caller rather than from guard's own
    layout, so it is checked: a missing file is reported and nothing is printed, because an
    agent handed a path that does not open reads it as an empty document and audits nothing.

    Fail-open like every other verb — a bad path is a reason on stderr and exit 0.
    """
    project_dir = _cli_project_dir()
    if not argv or not argv[0].strip():
        print("guard inputs: no path given — `inputs --file <path>`.", file=sys.stderr)
        _trace(project_dir, None, "inputs", "file_no_path")
        return 0
    target = Path(argv[0].strip()).expanduser()
    try:
        target = target.resolve()
    except OSError:
        target = target.absolute()
    if not target.is_file():
        print(f"guard inputs: no file at {target} — nothing to audit.", file=sys.stderr)
        _trace(project_dir, None, "inputs", "file_missing")
        return 0

    # `file:`, not `answer file:`. Only the document router reads this form, and calling a
    # brief an "answer" would invite it to reason about a turn that does not exist.
    print(f"file: {target}")
    config = _load_config(project_dir)
    for kdir in _knowledge_dirs(project_dir, config):
        print(f"knowledge dir: {kdir}")
    _trace(project_dir, None, "inputs", "file_printed", file=target.name)
    return 0
