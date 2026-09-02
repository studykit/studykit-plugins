"""``knowledge-dirs`` — the CLI verb the design review runs.

Not a hook event. It is called by the ``guard:audit-plan`` skill, which reviews the
implementation plan the main agent is about to present for approval.

The plan itself needs no verb here. In plan mode the host writes the plan to a file and
tells the main agent where — and the skill runs in that agent's own context, so the path is
already in hand and goes straight into each dispatch. Guard writing a second copy would add
the one step the review cannot afford: a model transcribing the plan, which is where a plan
becomes a paraphrase of the plan.

``knowledge-dirs`` prints the project's configured knowledge directories, one absolute path
per line, in configured order. Only ``design-environment`` consumes them, but the SKILL is
what reads this: the agent is dispatched with the paths rather than resolving them, so a
project with none dispatches the agent anyway and the agent falls back to its other sources
without having to tell "unset" apart from "lookup failed".
"""

from __future__ import annotations

from .config import _load_config
from .paths import _cli_project_dir, _knowledge_dirs, _trace


def cmd_knowledge_dirs() -> int:
    """Print the project's knowledge directories, one absolute path per line.

        knowledge-dirs

    Configured order is preserved and is precedence — the reader is told to start at the
    front. Only directories that exist are printed (``_knowledge_dirs``), so a typo in the
    config drops that entry rather than sending an agent to a path that is not there.

    Printing NOTHING is a normal, frequent result: most projects configure none. It is not
    reported on stderr, because unlike ``candidates`` there is no ambiguity to resolve — the
    skill dispatches the environment critic either way, and that agent's own definition says
    what to do when it has no knowledge base. A warning here would be a line the caller has
    to decide to ignore on every review.
    """
    project_dir = _cli_project_dir()
    config = _load_config(project_dir)
    dirs = _knowledge_dirs(project_dir, config)
    for path in dirs:
        print(path)
    _trace(project_dir, None, "knowledge-dirs", "printed", count=str(len(dirs)))
    return 0
