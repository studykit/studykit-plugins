"""The turn's text, cut out of the transcript when an audit asks for it.

``turns/<sid>/<pid>.md`` is the turn's RESPONSE — the text being audited — and
``turns/<sid>/<pid>.request.md`` is the user's request for that turn. guard writes both, from
the transcript, in ``cmd_inputs``; neither passes through the hands of the agent that wrote
the response, which is the property the whole design rests on.

Nothing here runs per turn. Until v0.122.0 the Stop hook wrote the response on every turn and
``UserPromptSubmit`` wrote the request on every prompt, against an audit that in most sessions
never came; both now happen once, when the user asks.

``<sid>`` and ``<pid>`` in all of the above are the SHORT forms — see ``_short``.
"""
from __future__ import annotations

from pathlib import Path

from .paths import _state_root

# How many leading characters of an id go into a path. The ids guard is handed are 36-char
# UUIDs, and the answer file's path is printed into the main agent's context on every turn:
# at full length the session id and the turn id together are 72 characters of hex, which
# tokenizes far worse than the English around it.
#
# A prefix rather than a hash or a counter, because a prefix stays DERIVABLE. A subagent
# holding only `CLAUDE_CODE_SESSION_ID` builds the same directory by applying the same rule,
# and the transcript's full `promptId` is matched against the short turn id by prefix
# (`transcript._turn_slice`) — so no mapping from the short form back to the long one has to
# be stored anywhere, and nothing breaks if the state file holding it were lost.
#
# 8 hex characters. A collision needs two turns in ONE session whose UUIDs share a 32-bit
# prefix; at a few hundred turns that is around one in a hundred thousand, and the cost of
# losing that bet is one turn's answer file being reused rather than anything unrecoverable.
_ID_PATH_CHARS = 8


def _short(identifier: str) -> str:
    """The path form of a session or turn id.

    Idempotent on a value that is already short, and that is what makes it safe to apply at
    every call site: an id typed back at guard — `inputs <turn-id>`, by an agent reading the
    short form guard printed — passes through unchanged, while a full UUID from a hook
    payload is cut down. Neither caller has to know which form it is holding.
    """
    return identifier[:_ID_PATH_CHARS]


def _turn_dir(project_dir: Path, session_id: str) -> Path:
    """The per-session directory the turn files live in.

    Named from the short session id. The SessionStart sweep reaps these on the directory's
    own mtime and never on its name (`cmd_session`), so shortening the name costs it
    nothing.
    """
    return _state_root(project_dir) / "turns" / _short(session_id)


def _turn_record_file(project_dir: Path, session_id: str, prompt_id: str) -> Path:
    """The file the turn's response is passed to its auditors in.

    The turn goes through a file rather than through the dispatch text, and that is the
    whole coordination mechanism here. A routed turn has up to four readers — the router,
    then whichever agents it names — and pasting the turn into each dispatch means writing
    it out that many times, in a message the main agent composes itself, which is exactly
    where a turn quietly becomes a paraphrase of the turn. One file, read by everyone.

    guard writes it, from the transcript. What surrounds the response — this turn's tool
    activity, what an earlier turn established — stays in the transcript, and an agent that
    needs any of it runs `transcript turn|find|index` and gets its own extract file. That
    keeps the author of the turn out of the record of the turn. The one exception is the
    user's request, which guard copies into a sibling file for the router alone
    (`_turn_request_file`): materiality is the one judgment that cannot be made from the
    response by itself.
    """
    return _turn_dir(project_dir, session_id) / f"{_short(prompt_id)}.md"


# Header on the response file. guard writes this file itself, always, so it always carries
# one — and the header has work to do: it tells the auditor that what it is reading was cut
# from the transcript by guard rather than written by the party being audited.
TURN_RESPONSE_HEADER = (
    "<!-- guard: the assistant's response for this turn, verbatim, cut from the transcript "
    "by guard. Not written by the session that produced it. -->"
)


def _write_turn_response(project_dir: Path, session_id: str, prompt_id: str,
                         response: str) -> Path | None:
    """Write the turn's response out for the auditors. Returns the path, or None.

    Overwrites, deliberately. guard is the only writer — nothing on this path corrects the
    file, because the turn it holds was printed to the user long before the audit ran and no
    edit here could reach it — so a second `inputs` for the same turn must produce the same
    file rather than preserve whatever the first left.

    Best-effort, and a failure is silent: the paths are printed anyway and the agents are told
    to stop and say so when the answer file is empty or missing. A guard that refused to
    resolve a turn because it could not write a scratch file would be failing closed on its
    own plumbing.
    """
    path = _turn_record_file(project_dir, session_id, prompt_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"{TURN_RESPONSE_HEADER}\n\n{response.rstrip()}\n",
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
    return _turn_dir(project_dir, session_id) / f"{_short(prompt_id)}.request.md"


# Header on the request file. guard writes this file itself, so unlike the answer file it
# always carries a header — and the header has work to do: the router is told the file is
# the user's words and not the answer, at the top of the file it is reading, where a
# dispatch line naming the path cannot say it.
TURN_REQUEST_HEADER = (
    "<!-- guard: the user's request for this turn, verbatim, cut from the transcript by "
    "guard. NOT part of the answer: nothing audits it, nothing corrects it, and no audit "
    "agent is given it. It exists so the router can tell what the user asked for from what "
    "the response volunteered. -->"
)


def _write_turn_request(project_dir: Path, session_id: str, prompt_id: str,
                        prompt: str) -> Path | None:
    """Save the user's request verbatim for the router. Returns the path, or None.

    Verbatim is the requirement, not a nicety: the router's job is to judge what the user
    asked for, and a condensed or paraphrased request is one guard's own summarizer has
    already decided the answer to. This is the only place guard keeps a copy of a prompt, and
    it is kept for one reader.

    Best-effort and silent on failure, like `_write_turn_response`: the router falls back to
    judging materiality from the response alone. A turn opened by a slash command has no
    request at all — the host's envelope is not the user talking — and that is the same case.
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
