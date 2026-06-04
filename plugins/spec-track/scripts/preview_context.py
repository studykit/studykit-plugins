#!/usr/bin/env python3
# /// script
# dependencies = ["PyYAML"]
# ///
"""Preview the hook-injected context for each SpecTrack surface.

The same build functions the hooks call at runtime
(``main_context.build_*``) render the text printed here, so what this
command emits is byte-for-byte what the agent actually receives — there is
no second copy of the wording to drift. Use it while authoring skills or
agents to see what is already injected before duplicating it in a doc.

Surfaces:

- ``session`` — SessionStart, main session (skills run here).
- ``subagent`` — SubagentStart base policy, plus the per-agent block when
  ``--agent`` names one (agents run here).
- ``commit`` — the commit-prefix snippet re-injected at UserPromptSubmit
  when a commit keyword fires.

The active issue provider selects provider-keyed fragments. Pass
``--provider`` to preview a specific one, or omit it to load the project's
``.spec-track/config.yml``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from config import (
    CommitRefsConfig,
    ProviderConfig,
    WorkflowConfig,
    load_workflow_config,
)
from env import workflow_project_dir_from_env
from main_context import (
    build_commit_prefix_context,
    build_session_policy_context,
    build_subagent_policy_context,
)

_PLUGIN_ROOT = Path(__file__).resolve().parents[1]
_AGENTS_DIR = _PLUGIN_ROOT / "hooks" / "context" / "subagent" / "agents"

_KNOWN_PROVIDERS = ("github", "jira", "filesystem")
_KNOWN_RUNTIMES = ("claude", "codex")
_SURFACES = ("session", "subagent", "commit", "all")


def available_agents() -> list[str]:
    """Return per-agent block names, derived from the injected fragment files."""

    return sorted(p.stem for p in _AGENTS_DIR.glob("*.md"))


def synthesize_config(provider: str) -> WorkflowConfig:
    """Build a minimal config whose only meaningful field is the issue provider.

    The build functions read just ``config.issues.kind`` to pick
    provider-keyed fragments, so a synthetic config is enough to preview any
    provider without a configured project on disk.
    """

    return WorkflowConfig(
        path=Path("<preview>"),
        root=Path.cwd(),
        version=1,
        mode="preview",
        issues=ProviderConfig(role="issue", kind=provider),
        knowledge=ProviderConfig(role="knowledge", kind=provider),
        issue_id_format="",
        commit_refs=CommitRefsConfig(enabled=True),
        raw={},
    )


def resolve_config(provider: str | None) -> WorkflowConfig:
    """Synthesize from ``--provider`` or load the project config; error if neither."""

    if provider is not None:
        return synthesize_config(provider)
    project_dir = workflow_project_dir_from_env() or Path.cwd()
    config = load_workflow_config(project_dir)
    if config is None:
        raise SystemExit(
            "no .spec-track/config.yml found from "
            f"{project_dir}; pass --provider to preview a specific provider"
        )
    return config


def banner(title: str) -> str:
    return f"{'=' * 10} {title} {'=' * 10}"


def render_surface(
    surface: str,
    config: WorkflowConfig,
    *,
    runtime: str,
    agent: str | None,
) -> list[str]:
    """Return ``[banner, rendered]`` blocks for one surface."""

    provider = config.issues.kind
    blocks: list[str] = []
    if surface in ("session", "all"):
        blocks.append(banner(f"SessionStart (main) — provider={provider} runtime={runtime}"))
        blocks.append(build_session_policy_context(
            config, plugin_root=_PLUGIN_ROOT, runtime=runtime,
        ))
    if surface in ("subagent", "all"):
        agents = available_agents() if agent == "all" else [agent]
        for name in agents:
            label = f"agent={name}" if name else "base"
            blocks.append(banner(
                f"SubagentStart ({label}) — provider={provider} runtime={runtime}"
            ))
            blocks.append(build_subagent_policy_context(
                config, plugin_root=_PLUGIN_ROOT, runtime=runtime, agent_type=name,
            ))
    if surface in ("commit", "all"):
        blocks.append(banner("UserPromptSubmit (commit-prefix)"))
        blocks.append(build_commit_prefix_context())
    return blocks


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="spec-track preview-context",
        description="Preview the context SpecTrack hooks inject on each surface.",
    )
    parser.add_argument(
        "--surface", choices=_SURFACES, default="all",
        help="Which injection surface to render (default: all).",
    )
    parser.add_argument(
        "--provider", choices=_KNOWN_PROVIDERS, default=None,
        help="Issue provider to preview. Omit to load the project's "
             ".spec-track/config.yml.",
    )
    parser.add_argument(
        "--runtime", choices=_KNOWN_RUNTIMES, default="claude",
        help="Host runtime for the launcher snippet (default: claude).",
    )
    parser.add_argument(
        "--agent", default=None,
        help="Per-agent SubagentStart block to include (name or 'all'). "
             "Omit for the base subagent policy only.",
    )
    parser.add_argument(
        "--list-agents", action="store_true",
        help="List the per-agent block names and exit.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.list_agents:
        print("\n".join(available_agents()))
        return 0
    config = resolve_config(args.provider)
    blocks = render_surface(
        args.surface, config, runtime=args.runtime, agent=args.agent,
    )
    print("\n\n".join(blocks))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
