"""The turn's answer file, and the user's request saved beside it.

``turns/<sid>/<pid>.md`` is the turn's ANSWER. guard names the path at the start of the turn
and the main agent writes the substance there; the agents audit it and the correctors edit it
in place, so the corrected file is what the user is shown. guard fills it in only if the turn
left it empty (``_write_turn_response``).

``turns/<sid>/<pid>.request.md`` is the user's REQUEST for that turn, verbatim, written by
guard at UserPromptSubmit. It goes to the ROUTER and to nothing else: never audited, never
corrected, never handed to an audit agent. It is there so triage can tell the part of an
answer the user asked for from the part nobody asked for (``_write_turn_request``).
"""

from __future__ import annotations

from pathlib import Path

from .paths import _state_root


def _turn_record_file(project_dir: Path, session_id: str, prompt_id: str) -> Path:
    """The file the turn is passed between agents in. Written by guard, then extended.

    The turn goes through a file rather than through the dispatch text, and that is the
    whole coordination mechanism here. A routed turn has up to five readers — the router,
    then whichever agents it names — and pasting the turn into each dispatch means writing
    it out that many times, in a message the main agent composes itself, which is exactly
    where a turn quietly becomes a paraphrase of the turn. One file, read by everyone.

    The file is the ANSWER, not a record of it. guard names the path at the start of the
    turn, the main agent writes the substance there, the agents audit and correct it in
    place, and the corrected file is what the user is shown — so the same text never has to
    be printed twice, once flawed and once fixed. guard writes it only as a fallback, when
    the turn ended with nothing there. What surrounds the response — this turn's tool
    activity, what an earlier turn established — lives in the transcript, and an agent that
    needs any of it runs `transcript turn|find|index` and gets its own extract file. That
    keeps the author of the turn out of the record of the turn, which is the property the
    whole design rests on. The one exception is the user's request, which guard copies into
    a sibling file for the router alone (`_turn_request_file`): the router has `Read` and no
    way to extract, and materiality is the one judgment that cannot be made from the answer
    by itself.
    """
    return _state_root(project_dir) / "turns" / session_id / f"{prompt_id}.md"


# Section headings in the turn record. Fixed strings, because both the instruction that
# asks for a section and the agent definitions that say which section to read name them.
# Header on the copy GUARD writes, and only on that copy. The normal case is the main agent
# authoring this file during the turn — the file IS the answer, not a transcript of it — so
# there is no heading at all then. guard writes only when the turn ended with nothing there,
# and then the header is the honest label: this is a fallback, taken from the payload after
# the fact, and whatever the reply actually said is what the user already read.
TURN_FALLBACK_HEADER = (
    "<!-- guard: the turn ended without this file being written, so guard filled it in from "
    "the response it was handed. Audit it as the answer; corrections still go here. -->"
)


def _write_turn_response(project_dir: Path, session_id: str, prompt_id: str,
                         response: str) -> Path | None:
    """Fill in the answer file IF the turn left it empty. Returns the path, or None.

    Not an overwrite, ever. The main agent is asked at the start of the turn to write its
    answer here, and by Stop that file may already hold the answer plus whatever a corrector
    has done to it — clobbering it with the payload copy would throw away the corrections
    and replace the working document with a snapshot of an earlier state.

    So this is the fallback for a turn that ignored the ask, and it matters that there is
    one: the agents are pointed at this file by path, and with no file at all the dispatch
    would name something that is not there.

    Best-effort, and a failure is silent: the recommendation goes out anyway and the main
    agent is asked to create the file. A guard that refused to recommend because it could
    not write a scratch file would be failing closed on its own plumbing.
    """
    path = _turn_record_file(project_dir, session_id, prompt_id)
    try:
        if path.exists() and path.stat().st_size > 0:
            return path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"{TURN_FALLBACK_HEADER}\n\n{response.rstrip()}\n",
                        encoding="utf-8")
    except OSError:
        return None
    return path


def _turn_request_file(project_dir: Path, session_id: str, prompt_id: str) -> Path:
    """The file holding the user's request for this turn. For the ROUTER only.

    A sibling of the answer file rather than a section inside it, and that separation is the
    point. Put in the answer file, the user's own sentences become text the correctors edit —
    `korean-corrector` would rewrite the user's Korean, in a file the user is then shown —
    and text the auditors weigh as part of the answer. Kept apart, the request can be handed
    to the one agent whose judgment needs it and withheld from every agent that would act on
    it. It also lands in the same per-session directory, so the SessionStart sweep reaps it
    with the answer it belongs to and there is no second tree to keep bounded.
    """
    return _state_root(project_dir) / "turns" / session_id / f"{prompt_id}.request.md"


# Header on the request file. guard writes this file itself, so unlike the answer file it
# always carries a header — and the header has work to do: the router is told the file is
# the user's words and not the answer, at the top of the file it is reading, where a
# dispatch line naming the path cannot say it.
TURN_REQUEST_HEADER = (
    "<!-- guard: the user's request for this turn, verbatim, as guard received it at "
    "UserPromptSubmit. NOT part of the answer: nothing audits it, nothing corrects it, and "
    "no audit agent is given it. It exists so the router can tell what the user asked for "
    "from what the answer volunteered. -->"
)


def _write_turn_request(project_dir: Path, session_id: str, prompt_id: str,
                        prompt: str) -> Path | None:
    """Save the user's request verbatim for the router. Returns the path, or None.

    Verbatim is the requirement, not a nicety: the router's job is to judge what the user
    asked for, and a condensed or paraphrased request is one guard's own summarizer has
    already decided the answer to. This is the only place guard keeps a copy of a prompt, and
    it is kept for one reader.

    Best-effort and silent on failure, like `_write_turn_response`: the router falls back to
    judging materiality from the answer alone, which is what it did before this file existed.
    A guard that skipped an audit because it could not write a scratch file would be failing
    closed on its own plumbing.
    """
    path = _turn_request_file(project_dir, session_id, prompt_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"{TURN_REQUEST_HEADER}\n\n{prompt.strip()}\n", encoding="utf-8")
    except OSError:
        return None
    return path
