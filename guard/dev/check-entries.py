#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check that every entry point named in the roster resolves to a real definition.

Contributor tooling. It is not installed, not on any runtime path, and no hook or agent calls
it.

``AUDIT_AGENTS`` is Python and the entry points it names are markdown, so this is the only
place the two can be compared at all — and the failure it catches is silent at runtime. A
dispatch to a ``subagent_type`` that matches no agent, or an invocation of a skill that does
not exist, finds nothing rather than raising; guard fails open, so the audit simply does not
happen and nothing says so.

One entry is a USER-LEVEL agent rather than one this plugin ships (``EXTERNAL_ENTRIES``), and
it is checked differently — see the note there.

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

# Entry points that resolve to a USER-LEVEL agent instead of one this plugin ships. They are
# installed into the user's own agent directory, so they are dispatched by the bare name with no
# `guard:` prefix and there is no `agents/<name>.md` to find. Two checks replace the file lookup:
# the definition must exist in this repository's `global/agents/`, which is where that directory
# is populated from, and the plugin must NOT also carry a copy — a shadow copy is invisible at
# runtime (the bare name still resolves to the user-level one) and would drift silently.
#
# Nothing here can verify the user actually installed them. That is why the dispatch text in
# `agents/report-router.md` and `skills/answer/SKILL.md` says what to do when the name resolves
# to nothing: hand over the English rather than translate in the main session.
EXTERNAL_ENTRIES = frozenset({"korean-translator"})

# Where `global/install.sh` links from. Resolved relative to this plugin rather than to the
# checkout root so the failure is a missing file rather than a wrong-looking path.
GLOBAL_AGENTS = PLUGIN_ROOT.parent / "global" / "agents"


def _declares_name(target: Path, name: str) -> str | None:
    """``None`` if ``target`` declares ``name:`` in its frontmatter, else what is wrong.

    The frontmatter `name:` and the filename must agree. They diverge silently: the host
    registers a definition under its frontmatter name, while the roster, the router's report
    and the dispatch text all use the path.
    """
    body = target.read_text()
    if not (m := re.search(r"^name:\s*(\S+)\s*$", body, re.MULTILINE)):
        return f"{target.name} has no `name:`"
    if m.group(1) != name:
        return f"but {target.name} declares `name: {m.group(1)}`"
    return None


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
            if name in EXTERNAL_ENTRIES:
                if agent.is_file():
                    out.append(f"{key}.{field} = {name!r} — user-level entry, but the plugin "
                               f"also ships agents/{name}.md; the bare name resolves to the "
                               f"user's copy, so this one is dead and will drift")
                external = GLOBAL_AGENTS / f"{name}.md"
                if not external.is_file():
                    out.append(f"{key}.{field} = {name!r} — user-level entry with no "
                               f"{external} to install from")
                elif (wrong := _declares_name(external, name)):
                    out.append(f"{key}.{field} = {name!r} — {wrong}")
                continue
            skill = PLUGIN_ROOT / "skills" / name / "SKILL.md"
            target = agent if agent.is_file() else skill if skill.is_file() else None
            if target is None:
                out.append(f"{key}.{field} = {name!r} — no agents/{name}.md and no "
                           f"skills/{name}/SKILL.md")
                continue
            if wrong := _declares_name(target, name):
                out.append(f"{key}.{field} = {name!r} — {wrong}")
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
