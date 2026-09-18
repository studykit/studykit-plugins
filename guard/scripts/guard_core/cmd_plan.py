"""Print configured operational knowledge directories for audit callers.

The `knowledge-dirs` CLI exposes existing directories in configured order. User-supplied
reviewers may consume them; Guard does not choose their review procedure.
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
    reported on stderr. Callers decide how to proceed without a knowledge directory.
    """
    project_dir = _cli_project_dir()
    config = _load_config(project_dir)
    dirs = _knowledge_dirs(project_dir, config)
    for path in dirs:
        print(path)
    _trace(project_dir, None, "knowledge-dirs", "printed", count=str(len(dirs)))
    return 0
