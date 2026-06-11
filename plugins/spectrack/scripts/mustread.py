#!/usr/bin/env python3
# /// script
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
    WorkflowEnvError,
    detect_shell_runtime,
    workflow_project_dir_from_env,
    workflow_session_id_from_env,
)
from session_state import (
    read_authoring_resolution,
    record_authoring_resolution,
)

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
AUTHORING_DIR = PLUGIN_ROOT / "authoring"

ISSUE_TYPES = {"task", "bug", "spike", "epic", "review"}
KNOWLEDGE_TYPES = {"spec", "architecture", "domain", "context", "nfr", "ci", "decision-index"}
DUAL_TYPES = {"usecase", "research"}
ALL_TYPES = ISSUE_TYPES | KNOWLEDGE_TYPES | DUAL_TYPES
AUTHORING_SCOPES = {"content", "comment"}
REVIEW_TARGETS = ALL_TYPES - {"review"}

PRD_COMPONENT_TYPES = {"context", "usecase", "nfr", "spec", "domain"}

DECOMPOSITION_TYPES = {"task", "epic"}

PLAN_MODE_TYPES = {"task", "bug"}

PLAN_MODE_TRIGGER_NOTE = (
    "Enter plan mode before drafting the body when the change is not yet "
    "implemented. Skip plan mode for retroactive issues that track work "
    "already done."
)

TASK_AUDIT_TYPES = {"task"}

TASK_AUDIT_TRIGGER_NOTE = (
    "After the body file is drafted, before invoking the publish script, "
    "ask the user via AskUserQuestion whether to run the task-size-auditor "
    "subagent against the draft. Spawn task-size-auditor only when the user "
    "accepts. Skip this step entirely for retroactive issues that track "
    "work already done."
)

RESOLUTION_AUDIT_TYPES = {"task", "bug"}

RESOLUTION_AUDIT_TRIGGER_NOTE = (
    "After the body file is drafted, before invoking the publish script, "
    "ask the user via AskUserQuestion whether to run the resolution-auditor "
    "subagent against the draft. Pass it the draft body file path and the "
    "artifact type; it validates the recorded root cause and proposed "
    "approach against the actual code and git history (for retroactive "
    "issues, against the change that already landed) and writes its verdict "
    "to a sidecar file beside the draft. Spawn resolution-auditor only when "
    "the user accepts. If the verdict is `ok`, continue to publish. If it is "
    "`wrong-cause`, `ineffective-approach`, or `weak-diagnosis`, do not "
    "publish: revise the draft's recorded cause and approach to address the "
    "sidecar's Actionable section (rewrite the cause/approach, or settle the "
    "named execution-contingent claim), then re-run resolution-auditor "
    "against the revised draft. Repeat until the verdict is `ok`, up to 3 "
    "audit rounds total; if it is still not `ok` after the third round, stop "
    "and surface the latest sidecar to the user. A `unverifiable` verdict is "
    "not a re-plan trigger — surface it and let the user decide."
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


def render_cache_hit_reference(
    reading_anchor: str,
    notes_anchor: str | None = None,
) -> str:
    lines = [f'- See `<reading anchor="{reading_anchor}">` above.']
    if notes_anchor is not None:
        lines.append(
            f'- See `<notes anchor="{notes_anchor}">` above — '
            "triggers apply to this call too."
        )
    lines.append(
        "- If the anchor body is no longer in context, rerun this command "
        "with `--raw` to re-emit it."
    )
    return "\n".join(lines) + "\n"


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
    artifact_type: str, target: str | None, scope: str
) -> tuple[list[str], list[str]]:
    convention = "providers/issue/github/convention.md"
    relationships = "providers/issue/github/relationships.md"
    anti_patterns = "providers/issue/github/anti-patterns.md"
    match (scope, target):
        case ("comment", _):
            return [convention], []
        case (_, str()):
            return [
                convention,
                relationships,
                "providers/issue/github/review.md",
                anti_patterns,
            ], []
        case _:
            parts = [
                convention,
                relationships,
                f"providers/issue/github/{artifact_type}.md",
                anti_patterns,
            ]
            if artifact_type == "usecase":
                parts.append("providers/knowledge/github/actors.md")
            notes = (
                [RETROACTIVE_PUBLISH_STATE_GITHUB]
                if artifact_type in PLAN_MODE_TYPES
                else []
            )
            return parts, notes


def _resolve_authoring_github_knowledge(
    artifact_type: str, target: str | None, scope: str
) -> tuple[list[str], list[str]]:
    convention = "providers/knowledge/github/convention.md"
    match (scope, target):
        case ("comment", _):
            return [convention], []
        case _:
            parts = [
                convention,
                f"providers/knowledge/github/{artifact_type}.md",
            ]
            if artifact_type == "usecase":
                parts.append("providers/knowledge/github/actors.md")
            return parts, []


def _resolve_authoring_jira_issue(
    artifact_type: str, target: str | None, scope: str
) -> tuple[list[str], list[str]]:
    convention = "providers/issue/jira/convention.md"
    relationships = "providers/issue/jira/relationships.md"
    anti_patterns = "providers/issue/jira/anti-patterns.md"
    match (scope, target):
        case ("comment", _):
            return [convention], []
        case (_, str()):
            return [
                convention,
                relationships,
                "providers/issue/jira/review.md",
                anti_patterns,
            ], []
        case _:
            parts = [
                convention,
                relationships,
                f"providers/issue/jira/{artifact_type}.md",
                anti_patterns,
            ]
            notes = (
                [RETROACTIVE_PUBLISH_STATE_JIRA]
                if artifact_type in PLAN_MODE_TYPES
                else []
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
    side: str, artifact_type: str, target: str | None, scope: str
) -> list[str]:
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
            parts.extend([
                "contracts/issue/body.md",
                "contracts/issue/common.md",
                "contracts/issue/review.md",
            ])
            return parts
        case (_, None, "issue"):
            parts = ["contracts/issue/body.md", "contracts/issue/common.md"]
        case _:  # (_, None, "knowledge")
            parts = ["contracts/knowledge/body.md"]

    if artifact_type in PRD_COMPONENT_TYPES:
        parts.append("contracts/prd.md")
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


def _common_notes(
    side: str, artifact_type: str, target: str | None, scope: str
) -> list[str]:
    if scope == "comment" or target is not None or side != "issue":
        return []
    notes: list[str] = []
    if artifact_type == "usecase":
        notes.append(USECASE_INTERVIEW_NOTE)
    if artifact_type in PLAN_MODE_TYPES:
        notes.append(PLAN_MODE_TRIGGER_NOTE)
    if artifact_type in TASK_AUDIT_TYPES:
        notes.append(TASK_AUDIT_TRIGGER_NOTE)
    if artifact_type in RESOLUTION_AUDIT_TYPES:
        notes.append(RESOLUTION_AUDIT_TRIGGER_NOTE)
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
) -> Resolution:
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

    parts = _common_parts(side, artifact_type, target, scope)
    provider_parts: list[str] = []
    provider_notes: list[str] = []
    helper_side = "issue" if target is not None else side
    match (provider, helper_side):
        case ("github", "issue"):
            provider_parts, provider_notes = _resolve_authoring_github_issue(
                artifact_type, target, scope
            )
        case ("github", "knowledge"):
            provider_parts, provider_notes = _resolve_authoring_github_knowledge(
                artifact_type, target, scope
            )
        case ("jira", "issue"):
            provider_parts, provider_notes = _resolve_authoring_jira_issue(
                artifact_type, target, scope
            )
        case _:
            pass

    for part in provider_parts:
        if part not in parts:
            parts.append(part)

    notes = _common_notes(side, artifact_type, target, scope) + provider_notes

    return Resolution(
        artifact_type=artifact_type,
        side=side,
        provider=provider,
        scope=scope,
        target=target,
        files=absolute_authoring_paths(parts),
        notes=tuple(notes),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
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
        "--project",
        type=Path,
        default=workflow_project_dir_from_env(),
        help="project path used to find .spectrack/config.yml",
    )
    parser.add_argument("--require-config", action="store_true", help="fail when .spectrack/config.yml is absent")
    parser.add_argument(
        "--raw",
        action="store_true",
        help="force full markdown re-emission, overwriting the stored entry",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        resolution = resolve_authoring(
            args.type,
            side=args.side,
            target=args.target,
            provider=args.provider,
            project=args.project,
            require_config=args.require_config,
            scope=args.scope,
        )
    except ResolverError as exc:
        print(f"authoring resolver error: {exc}", file=sys.stderr)
        return 2

    runtime, session_id = _resolve_session()
    if not session_id:
        print(resolution.to_markdown(), end="")
        return 0

    anchor = resolution.reading_anchor
    current_key = _resolution_key(resolution)
    use_cache_hit = False
    if not args.raw:
        existing = read_authoring_resolution(
            args.project, runtime, session_id, tag="reading", anchor=anchor
        )
        if existing is not None and _keys_equal(existing.get("key"), current_key):
            use_cache_hit = True

    if use_cache_hit:
        notes_anchor_value = (
            resolution.notes_anchor if resolution.notes else None
        )
        print(
            render_cache_hit_reference(
                resolution.reading_anchor,
                notes_anchor_value,
            ),
            end="",
        )
        return 0

    print(resolution.to_markdown(), end="")
    record_authoring_resolution(
        args.project,
        runtime,
        session_id,
        tag="reading",
        anchor=anchor,
        key=current_key,
    )
    if resolution.notes:
        record_authoring_resolution(
            args.project,
            runtime,
            session_id,
            tag="notes",
            anchor=resolution.notes_anchor,
            key=current_key,
        )
    return 0


def _resolve_session() -> tuple[str, str]:
    runtime = detect_shell_runtime()
    if runtime.session_id:
        return runtime.name, runtime.session_id
    try:
        session_id = workflow_session_id_from_env()
    except WorkflowEnvError:
        return "", ""
    return runtime.name, session_id


def _resolution_key(resolution: Resolution) -> dict[str, str | None]:
    return {
        "type": resolution.artifact_type,
        "side": resolution.side,
        "provider": resolution.provider,
        "scope": resolution.scope,
        "target": resolution.target,
    }


def _keys_equal(left: object, right: dict[str, str | None]) -> bool:
    if not isinstance(left, dict):
        return False
    fields = ("type", "side", "provider", "scope", "target")
    return all(left.get(field) == right.get(field) for field in fields)


if __name__ == "__main__":
    raise SystemExit(main())
