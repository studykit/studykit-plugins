"""Locate Guard's installed plugin root for shell-wrapper exports.

The old per-Stop dispatch builders lived here. Edited-file reviews now use the explicit
``audit-files`` checkpoint, leaving only the installation-path helper shared by SessionStart.
"""

from __future__ import annotations

from pathlib import Path


# The CLI behind Guard's shell wrappers and the marker that finds the plugin root. It is
# present in every install at a fixed place and is the one file Guard cannot run without.
CLI_REL = "scripts/guard_hook.py"
_PLUGIN_ROOT_MAX_DEPTH = 5


def _plugin_root() -> Path:
    """Find the plugin root by marker rather than by counting parent directories."""
    here = Path(__file__).resolve()
    for parent in here.parents[:_PLUGIN_ROOT_MAX_DEPTH]:
        if (parent / CLI_REL).is_file():
            return parent
    # Partial install or test tree: fall back to the shipped layout,
    # ``<root>/scripts/guard_core/dispatch.py``.
    return here.parent.parent.parent
