#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["PyYAML", "python-frontmatter"]
# ///
"""Resolve workflow authoring contracts for workflow artifacts.

The resolver is intentionally small and deterministic. It returns absolute
paths to plugin-bundled authoring files so agents do not guess which files to
read before writing workflow artifacts.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from config import (
    CONFIG_NAME,
    WorkflowConfigError,
    load_workflow_config,
    normalize_provider,
    validate_provider_for_role,
)
from env import (
    detect_shell_runtime,
    workflow_project_dir_from_env,
)

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
AUTHORING_DIR = PLUGIN_ROOT / "authoring"

ISSUE_TYPES = {"task", "bug", "spike", "epic", "review"}
KNOWLEDGE_TYPES = {"spec", "architecture", "domain", "context", "nfr", "ci", "decision-index"}
DUAL_TYPES = {"usecase", "research"}
ALL_TYPES = ISSUE_TYPES | KNOWLEDGE_TYPES | DUAL_TYPES
AUTHORING_SCOPES = {"content", "comment"}
REVIEW_TARGETS = ALL_TYPES - {"review"}

# Canonical GitHub issue-type labels, ordered. Each issue carries exactly one
# of these labels; setup pre-creates any that are missing in the repository and
# records the merged label set into .spectrack/config.yml. This is the single
# source of truth for the type-label vocabulary and its color/description
# metadata — GitHub membership checks derive their name set from here.
GITHUB_TYPE_LABEL_SPECS: tuple[dict[str, str], ...] = (
    {"name": "task", "color": "1d76db", "description": "SpecTrack task issue"},
    {"name": "bug", "color": "d73a4a", "description": "SpecTrack bug issue"},
    {"name": "spike", "color": "5319e7", "description": "SpecTrack spike issue"},
    {"name": "epic", "color": "a2eeef", "description": "SpecTrack epic issue"},
    {"name": "review", "color": "0e8a16", "description": "SpecTrack review issue"},
    {"name": "usecase", "color": "fbca04", "description": "SpecTrack use case issue"},
    {"name": "research", "color": "bfdadc", "description": "SpecTrack research issue"},
)
GITHUB_TYPE_LABEL_NAMES: frozenset[str] = frozenset(
    spec["name"] for spec in GITHUB_TYPE_LABEL_SPECS
)

PRD_COMPONENT_TYPES = {"context", "usecase", "nfr", "spec", "domain"}

DECOMPOSITION_TYPES = {"task", "epic"}

PLAN_MODE_TYPES = {"task", "bug"}

# Issue types whose bodies carry assertions about runtime behavior, so they read
# the runtime-grounded-claim rule. Other issue types only need body conventions
# (folded into issue/common.md).
RUNTIME_GROUNDED_TYPES = {"task", "bug", "spike"}

# Authoring intent for task/bug content. Unlike side/scope/target, the
# resolver cannot infer it from the artifact — the author decides which one
# applies (capturing not-yet-done work / recording already-done work).
# It is therefore required (no default) for task/bug content authoring and
# rejected on every other surface.
AUTHORING_MODES = ("backlog", "retroactive")

BACKLOG_TRIGGER_NOTE = (
    "Backlog mode: this is the open, not-yet-done spec. Record at least "
    "Description; add Context, Acceptance Criteria, and — for a bug — "
    "Reproduction to whatever level of detail is useful, from a brief "
    "capture to a complete spec (both are valid). Do not work out a cause, "
    "an approach, or implementation steps in the body — those are decided "
    "against the current code when the item is picked up for implementation. "
    "Publish in the backend's open/unresolved state."
)

RETROACTIVE_TRIGGER_NOTE = (
    "Retroactive mode: the work already landed, so the body states facts, "
    "not intent. Description says what changed and why; record "
    "the diagnosed cause when relevant and how it was actually done; "
    "Acceptance Criteria records the checks that ran and their outcomes. "
    "Publish together with the transition to the backend's resolved state."
)

RETROACTIVE_PUBLISH_STATE_GITHUB = (
    "Retroactive issues that track work already done should be "
    "published in the closed state."
)

RETROACTIVE_PUBLISH_STATE_JIRA = (
    "Retroactive issues that track work already done should be "
    "published in the resolved state."
)

USECASE_SKILL_PATH = PLUGIN_ROOT / "skills" / "usecase" / "SKILL.md"

USECASE_INTERVIEW_NOTE = (
    "Workflow `usecase` issues are interview-derived, not hand-authored. To "
    "produce them, conduct the Socratic, one-question-at-a-time use-case "
    f"interview: read `{USECASE_SKILL_PATH}` and follow its body as the "
    "procedure, treating the user's idea/topic as its `$ARGUMENTS`. If you are "
    "already executing that interview, ignore this note and continue."
)

RESEARCH_RECORDING_NOTE = (
    "Recording phase: this research issue is the working record of the "
    "investigation — capture the question, evidence, and findings here. When "
    "findings across one or more research issues are stable, consolidate them "
    "into the curated report: `spectrack mustread --type research --side "
    "knowledge`. Do not write the curated report before its research issue(s) "
    "exist."
)

RESEARCH_CONSOLIDATION_NOTE = (
    "Consolidation phase: the curated report summarizes and references existing "
    "research issues — do not run fresh investigation here. If a new question "
    "arises, open a new research issue first: `spectrack mustread --type "
    "research --side issue`."
)


def _anchor_scope_suffix(scope: str) -> str:
    return "-comment" if scope == "comment" else ""


def reading_anchor(
    artifact_type: str, side: str, scope: str, target: str | None
) -> str:
    if artifact_type == "review" and target is not None:
        return f"{target}-{side}-review{_anchor_scope_suffix(scope)}"
    return f"{artifact_type}-{side}{_anchor_scope_suffix(scope)}"


def notes_anchor(
    artifact_type: str, side: str, scope: str, target: str | None
) -> str:
    return reading_anchor(artifact_type, side, scope, target)


@dataclass(frozen=True)
class Resolution:
    """Resolved authoring contract set."""

    artifact_type: str
    side: str
    provider: str | None
    scope: str
    target: str | None
    files: tuple[Path, ...]
    notes: tuple[str, ...] = ()
    mode: str | None = None

    @property
    def reading_anchor(self) -> str:
        return reading_anchor(
            self.artifact_type, self.side, self.scope, self.target
        )

    @property
    def notes_anchor(self) -> str:
        return notes_anchor(
            self.artifact_type, self.side, self.scope, self.target
        )

    def to_markdown(self) -> str:
        sections: list[str] = []
        reading_lines = [f'<reading anchor="{self.reading_anchor}">']
        reading_lines.append(f"Base: {AUTHORING_DIR}")
        reading_lines.extend(
            f"- {path.relative_to(AUTHORING_DIR)}" for path in self.files
        )
        reading_lines.append("</reading>")
        sections.append("\n".join(reading_lines))
        if self.notes:
            notes_lines = [f'<notes anchor="{self.notes_anchor}">']
            notes_lines.extend(f"- {note}" for note in self.notes)
            notes_lines.append("</notes>")
            sections.append("\n".join(notes_lines))
        return "\n\n".join(sections) + "\n"


class ResolverError(ValueError):
    """Raised when authoring cannot be resolved safely."""


def validate_type(value: str) -> None:
    if value not in ALL_TYPES:
        raise ResolverError(f"unsupported artifact type: {value}")


def validate_side(value: str) -> None:
    if value not in {"issue", "knowledge"}:
        raise ResolverError(f"unsupported artifact side: {value}")


def validate_scope(value: str) -> None:
    if value not in AUTHORING_SCOPES:
        raise ResolverError(f"unsupported authoring scope: {value}")


def validate_target(value: str, artifact_type: str) -> None:
    if artifact_type != "review":
        raise ResolverError("--target is only valid with --type review")
    if value == "review":
        raise ResolverError("--target review is not supported")
    if value not in REVIEW_TARGETS:
        raise ResolverError(f"unsupported target type: {value}")


def resolve_side(
    value: str | None, artifact_type: str, target: str | None = None
) -> str:
    """Resolve the side axis (issue or knowledge).

    When ``target`` is set the side refers to the target's side (the
    artifact being reviewed). Otherwise the side refers to the
    artifact_type being authored. Defaults from type for single-side
    types; dual-side types require an explicit value.
    """
    effective_type = target if target is not None else artifact_type
    if value is None:
        if effective_type in ISSUE_TYPES:
            return "issue"
        if effective_type in KNOWLEDGE_TYPES:
            return "knowledge"
        raise ResolverError(
            f"artifact type '{effective_type}' can be issue or knowledge; specify --side"
        )
    validate_side(value)
    if effective_type in ISSUE_TYPES and value != "issue":
        raise ResolverError(f"artifact type '{effective_type}' is issue-backed")
    if effective_type in KNOWLEDGE_TYPES and value != "knowledge":
        raise ResolverError(f"artifact type '{effective_type}' is knowledge-backed")
    return value


def _resolve_authoring_github_issue(
    artifact_type: str, target: str | None, scope: str, mode: str | None
) -> tuple[list[str], list[str]]:
    match (scope, target):
        case ("comment", _):
            return [], []
        case (_, str()):
            return [], []
        case _:
            if mode == "backlog":
                return [], []
            parts: list[str] = []
            if artifact_type == "usecase":
                parts.append("providers/knowledge/github/convention.md")
            notes = (
                [RETROACTIVE_PUBLISH_STATE_GITHUB] if mode == "retroactive" else []
            )
            return parts, notes


def _resolve_authoring_github_knowledge(
    artifact_type: str, target: str | None, scope: str
) -> tuple[list[str], list[str]]:
    # Every knowledge type renders through the single GitHub convention: the
    # provider layer carries only github-Markdown-specific rules, while section
    # structure and per-type rules live in the shared knowledge contracts.
    return ["providers/knowledge/github/convention.md"], []


def _resolve_authoring_jira_issue(
    artifact_type: str, target: str | None, scope: str, mode: str | None
) -> tuple[list[str], list[str]]:
    convention = "providers/issue/jira/convention.md"
    match (scope, target):
        case ("comment", _):
            return [convention], []
        case (_, str()):
            return [convention], []
        case _:
            if mode == "backlog":
                return [convention], []
            parts = [convention]
            notes = (
                [RETROACTIVE_PUBLISH_STATE_JIRA] if mode == "retroactive" else []
            )
            return parts, notes


def absolute_authoring_paths(parts: Iterable[str]) -> tuple[Path, ...]:
    paths: list[Path] = []
    for rel in parts:
        path = (AUTHORING_DIR / rel).resolve()
        if not path.exists():
            raise ResolverError(f"authoring file does not exist: {path}")
        paths.append(path)
    return tuple(paths)


def authoring_relative_path(path: Path, *, plugin_root: Path | None = None) -> str | None:
    root = (plugin_root or PLUGIN_ROOT).expanduser().resolve()
    authoring_dir = (root / "authoring").resolve()
    resolved = path.expanduser()
    if not resolved.is_absolute():
        resolved = Path.cwd() / resolved
    resolved = resolved.resolve()
    try:
        relative = resolved.relative_to(authoring_dir)
    except ValueError:
        return None
    if not resolved.is_file():
        return None
    return relative.as_posix()


def is_authoring_file(path: Path, *, plugin_root: Path | None = None) -> bool:
    return authoring_relative_path(path, plugin_root=plugin_root) is not None


def _common_parts(
    side: str, artifact_type: str, target: str | None, scope: str, mode: str | None
) -> list[str]:
    # Research authoring is consolidated into a single self-contained, side-agnostic
    # contract. Content-scope research reads only that file (plus any provider parts);
    # comment scope and review targets fall through to the shared rules below.
    if artifact_type == "research" and target is None and scope != "comment":
        return ["contracts/research.md"]
    match (scope, target, side):
        case ("comment", _, _):
            return []
        case (_, str() as t, s):
            parts = [
                f"contracts/quality/{t}-{s}-criteria.md"
                if t in DUAL_TYPES
                else f"contracts/quality/{t}-criteria.md"
            ]
            if t == "usecase":
                parts.extend([
                    "contracts/usecase-abstraction-guard.md",
                    "contracts/quality/actors-criteria.md",
                ])
            parts.append("contracts/issue/common.md")
            return parts
        case (_, None, "issue"):
            parts = ["contracts/issue/common.md"]
            if artifact_type in RUNTIME_GROUNDED_TYPES:
                parts.append("contracts/issue/runtime-grounded-claims.md")
        case _:  # (_, None, "knowledge")
            parts = ["contracts/knowledge/body.md"]

    if artifact_type in PRD_COMPONENT_TYPES:
        parts.append("contracts/prd.md")
    if artifact_type == "review":
        return parts
    if artifact_type in DUAL_TYPES:
        parts.append(f"contracts/{artifact_type}.md")
        parts.append(f"contracts/{side}/{artifact_type}.md")
    else:
        parts.append(f"contracts/{side}/{artifact_type}.md")
    if artifact_type in DECOMPOSITION_TYPES:
        parts.append("contracts/issue/decomposition-patterns.md")
    if artifact_type == "usecase":
        parts.extend([
            "contracts/usecase-abstraction-guard.md",
            "contracts/knowledge/actors.md",
        ])
    return parts


def _mode_applies(
    side: str, artifact_type: str, target: str | None, scope: str
) -> bool:
    """Whether ``--mode`` governs this authoring surface.

    Mode only shapes direct task/bug body authoring. Comment scope, review
    targets, and the knowledge side never carry an implementation intent.
    """
    return (
        scope != "comment"
        and target is None
        and side == "issue"
        and artifact_type in PLAN_MODE_TYPES
    )


def _resolve_mode(
    value: str | None,
    side: str,
    artifact_type: str,
    target: str | None,
    scope: str,
) -> str | None:
    if not _mode_applies(side, artifact_type, target, scope):
        if value is not None:
            raise ResolverError(
                "--mode only applies to task/bug content authoring"
            )
        return None
    if value is None:
        raise ResolverError(
            "task/bug content authoring requires --mode "
            "(backlog or retroactive)"
        )
    if value not in AUTHORING_MODES:
        raise ResolverError(f"unsupported authoring mode: {value}")
    return value


def _common_notes(
    side: str,
    artifact_type: str,
    target: str | None,
    scope: str,
    mode: str | None,
    runtime: str,
) -> list[str]:
    if scope == "comment" or target is not None:
        return []
    # Research threads its two-phase workflow through the notes channel: the
    # issue is the working record, the knowledge report consolidates it. Each
    # phase points at the command for the next, so the flow is discoverable by
    # walking it rather than documented up front.
    if artifact_type == "research":
        return [
            RESEARCH_RECORDING_NOTE
            if side == "issue"
            else RESEARCH_CONSOLIDATION_NOTE
        ]
    if side != "issue":
        return []
    notes: list[str] = []
    if artifact_type == "usecase":
        notes.append(USECASE_INTERVIEW_NOTE)
    if artifact_type in PLAN_MODE_TYPES:
        if mode == "backlog":
            notes.append(BACKLOG_TRIGGER_NOTE)
        elif mode == "retroactive":
            notes.append(RETROACTIVE_TRIGGER_NOTE)
    return notes


def resolve_authoring(
    artifact_type: str,
    *,
    side: str | None = None,
    target: str | None = None,
    provider: str | None = None,
    project: Path | None = None,
    require_config: bool = False,
    scope: str = "content",
    mode: str | None = None,
    runtime: str | None = None,
) -> Resolution:
    if runtime is None:
        runtime = detect_shell_runtime().name
    validate_type(artifact_type)
    if target is not None:
        validate_target(target, artifact_type)
    validate_scope(scope)
    side = resolve_side(side, artifact_type, target)

    if target is not None and scope == "comment":
        raise ResolverError(
            "--target does not apply to comment scope; "
            "quality-criteria files only describe content-level review"
        )

    mode = _resolve_mode(mode, side, artifact_type, target, scope)

    config_provider: str | None = None
    if project is not None or require_config:
        try:
            config = load_workflow_config(project or Path.cwd(), require=require_config)
        except WorkflowConfigError as exc:
            raise ResolverError(str(exc)) from exc
        if config is not None:
            config_provider = config.provider_for_role(side)

    provider = normalize_provider(provider) or config_provider
    if provider is not None:
        try:
            validate_provider_for_role(side, provider)
        except WorkflowConfigError as exc:
            raise ResolverError(str(exc)) from exc

    parts = _common_parts(side, artifact_type, target, scope, mode)
    provider_parts: list[str] = []
    provider_notes: list[str] = []
    helper_side = "issue" if target is not None else side
    match (provider, helper_side):
        case ("github", "issue"):
            provider_parts, provider_notes = _resolve_authoring_github_issue(
                artifact_type, target, scope, mode
            )
        case ("github", "knowledge"):
            provider_parts, provider_notes = _resolve_authoring_github_knowledge(
                artifact_type, target, scope
            )
        case ("jira", "issue"):
            provider_parts, provider_notes = _resolve_authoring_jira_issue(
                artifact_type, target, scope, mode
            )
        case _:
            pass

    for part in provider_parts:
        if part not in parts:
            parts.append(part)

    notes = (
        _common_notes(side, artifact_type, target, scope, mode, runtime)
        + provider_notes
    )

    return Resolution(
        artifact_type=artifact_type,
        side=side,
        provider=provider,
        scope=scope,
        target=target,
        files=absolute_authoring_paths(parts),
        notes=tuple(notes),
        mode=mode,
    )


# Pre-call policy the resolver cannot infer from its flags: how to choose the
# mode/side arguments, the workflow type vocabulary, and how a non-workflow
# type is handled. Kept here so `--help` is the single source and the injected
# SessionStart/SubagentStart context can stay a thin pointer to it.
_HELP_EPILOG = """\
Choosing --mode (required for task/bug content authoring):
  retroactive  The change has already landed (implemented, committed, or
               merged) — pick it even when the user never says the word. The
               body records facts: what changed, the diagnosed cause when
               relevant, how it was actually done, and the checks that ran.
               The issue publishes in the backend's closed/resolved state.
  backlog      The work is not yet done; the issue is the open spec. Record at
               least Description; add Context, Acceptance Criteria, and — for a
               bug — Reproduction to any useful level of detail. Do not work
               out a cause, an approach, or implementation steps in the body;
               those are settled against the current code when the item is
               picked up. Publishes in the backend's open/unresolved state.

Choosing --side (dual-side types research / usecase):
  They begin on the issue side (the working record) and consolidate onto the
  knowledge side.

Workflow artifact types:
  issue      task, bug, spike, epic, review
  knowledge  architecture, ci, context, decision-index, domain, nfr, spec
  dual-side  research, usecase (both issue and knowledge sides)

Any other --type returns NONE — there is no authoring contract. On GitHub,
create the issue directly with that type (it is carried as a type label). On
Jira, use only the workflow types above unless a
providers.issues.artifact_issue_types mapping exists (see
`spectrack issue <verb> --help`).

The resolver output lists the files to read before drafting and a notes
section whose every bullet is a binding rule for the calling flow. Knowledge
pages live under wiki/ — edit the resolver-returned file and commit.
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog=_HELP_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--type", required=True, help="workflow artifact type")
    parser.add_argument(
        "--side",
        help="issue or knowledge; required for usecase/research, defaults otherwise",
    )
    parser.add_argument(
        "--target",
        help="artifact type being reviewed; only valid with --type review",
    )
    parser.add_argument("--provider", help="provider override, such as github or jira")
    parser.add_argument(
        "--scope",
        choices=sorted(AUTHORING_SCOPES),
        default="content",
        help="authoring surface to resolve; use comment for comment-only work",
    )
    parser.add_argument(
        "--mode",
        choices=AUTHORING_MODES,
        help=(
            "authoring intent; required for task/bug content authoring: "
            "backlog (open spec, not yet done) or "
            "retroactive (already done)"
        ),
    )
    parser.add_argument(
        "--project",
        type=Path,
        default=workflow_project_dir_from_env(),
        help="project path used to find .spectrack/config.yml",
    )
    parser.add_argument("--require-config", action="store_true", help="fail when .spectrack/config.yml is absent")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # Types outside SpecTrack's built-in workflow vocabulary carry no authoring
    # contract. Report NONE (rather than failing) so the calling flow knows
    # there is nothing to read and can create the artifact directly.
    if args.type not in ALL_TYPES:
        print("NONE")
        return 0

    try:
        resolution = resolve_authoring(
            args.type,
            side=args.side,
            target=args.target,
            provider=args.provider,
            project=args.project,
            require_config=args.require_config,
            scope=args.scope,
            mode=args.mode,
        )
    except ResolverError as exc:
        print(f"authoring resolver error: {exc}", file=sys.stderr)
        return 2

    print(resolution.to_markdown(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
