# /// script
# requires-python = ">=3.10"
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Package entry point: run as `uv run --script issue/__main__.py`.

Under ``--script`` uv installs the PEP 723 deps but puts this file's own
directory (``scripts/issue``) on ``sys.path[0]``, so the absolute
``issue.*`` package imports below would not resolve. Prepend the parent
(``scripts``) so ``import issue`` finds the package.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from issue.dispatch import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
