#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check that every entry point named in the roster resolves to a real file.

Contributor tooling. It is not installed, not on any runtime path, and no hook or agent calls
it.

``AUDIT_AGENTS`` is Python and the entry points it names are markdown, so this is the only
place the two can be compared at all — and the failure it catches is silent at runtime. A
dispatch to a ``subagent_type`` that matches no agent, or an invocation of a skill that does
not exist, finds nothing rather than raising; guard fails open, so the audit simply does not
happen and nothing says so.

Checked here rather than in ``guard_core`` because it is a property of the source tree, not
something a hook could act on: a runtime check would have nothing useful to do with the answer.

    uv run dev/check-entries.py

This repository has no CI, so nothing runs it on its own. It belongs in a repo-local
pre-commit hook and in the manual-testing recipe; see this plugin's ``AGENTS.md``.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent


def problems() -> list[str]:
    sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))
    try:
        from guard_core.agents import AUDIT_AGENTS  # noqa: PLC0415
    except ImportError as e:
        return [f"could not import the roster: {e}"]

    out = []
    for key, spec in AUDIT_AGENTS.items():
        for field in ("turn_entry", "report_entry"):
            name = getattr(spec, field)
            if not name:
                continue
            agent = PLUGIN_ROOT / "agents" / f"{name}.md"
            skill = PLUGIN_ROOT / "skills" / name / "SKILL.md"
            target = agent if agent.is_file() else skill if skill.is_file() else None
            if target is None:
                out.append(f"{key}.{field} = {name!r} — no agents/{name}.md and no "
                           f"skills/{name}/SKILL.md")
                continue
            # The frontmatter `name:` and the filename must agree. They diverge silently: the
            # host registers a definition under its frontmatter name, while the roster, the
            # router's report and the closeout section all use the path.
            body = target.read_text()
            if not (m := re.search(r"^name:\s*(\S+)\s*$", body, re.MULTILINE)):
                out.append(f"{key}.{field} = {name!r} — {target.name} has no `name:`")
            elif m.group(1) != name:
                out.append(f"{key}.{field} = {name!r} — but {target.name} declares "
                           f"`name: {m.group(1)}`")
    return out


def main() -> int:
    if found := problems():
        print("check-entries: the roster names entry points that do not resolve:",
              file=sys.stderr)
        for line in found:
            print(f"  {line}", file=sys.stderr)
        return 1
    print("check-entries: every roster entry point resolves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
