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

from workflow_config import (
    CONFIG_NAME,
    WorkflowConfigError,
    load_workflow_config,
    normalize_provider,
    validate_provider_for_role,
)
from workflow_env import (
    WorkflowEnvError,
    detect_shell_runtime,
    workflow_project_dir_from_env,
    workflow_session_id_from_env,
)
from workflow_providers import CACHE_POLICY_DEFAULT, CACHE_POLICY_REFRESH
from workflow_session_state import (
    read_authoring_resolution,
    record_authoring_resolution,
)

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
AUTHORING_DIR = PLUGIN_ROOT / "authoring"

ISSUE_TYPES = {"task", "bug", "spike", "epic", "review"}
KNOWLEDGE_TYPES = {"spec", "architecture", "domain", "context", "nfr", "ci"}
DUAL_TYPES = {"usecase", "research"}
ALL_TYPES = ISSUE_TYPES | KNOWLEDGE_TYPES | DUAL_TYPES
AUTHORING_SCOPES = {"content", "comment"}

PRD_COMPONENT_TYPES = {"context", "usecase", "nfr", "spec", "domain"}

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
    "accepts."
)

ISSUE_PROVIDER_FILES = {
    "github": "providers/github-issue-convention.md",
    "jira": "providers/jira-issue-convention.md",
}

ISSUE_PROVIDER_RELATIONSHIP_FILES = {
    "github": "providers/github-issue-relationships.md",
    "jira": "providers/jira-issue-relationships.md",
}

KNOWLEDGE_PROVIDER_FILES = {
    "github": "providers/github-knowledge-convention.md",
    "confluence": "providers/confluence-page-convention.md",
}

ISSUE_PROVIDER_TYPE_PATTERNS = {
    "github": "providers/github-issue-{artifact_type}-authoring.md",
    "jira": "providers/jira-issue-{artifact_type}-authoring.md",
}

KNOWLEDGE_PROVIDER_TYPE_PATTERNS = {
    "github": "providers/github-knowledge-{artifact_type}-authoring.md",
    "confluence": "providers/confluence-page-{artifact_type}-authoring.md",
}

KNOWLEDGE_PROVIDER_PRD_FILES = {
    "github": "providers/github-knowledge-prd-paths.md",
}

PROVIDER_EXTRA_FILES = {
    ("issue", "github"): ("providers/github-issue-anti-patterns.md",),
    ("issue", "jira"): ("providers/jira-issue-anti-patterns.md",),
}


def _anchor_scope_suffix(scope: str) -> str:
    return "-comment" if scope == "comment" else ""


def reading_list_anchor(artifact_type: str, role: str, scope: str) -> str:
    return f"{artifact_type}-{role}{_anchor_scope_suffix(scope)}-reading-list"


def notes_anchor(artifact_type: str, role: str, scope: str) -> str:
    return f"{artifact_type}-{role}{_anchor_scope_suffix(scope)}-notes"


@dataclass(frozen=True)
class Resolution:
    """Resolved authoring contract set."""

    artifact_type: str
    role: str
    provider: str | None
    scope: str
    files: tuple[Path, ...]
    notes: tuple[str, ...] = ()

    @property
    def reading_list_anchor(self) -> str:
        return reading_list_anchor(self.artifact_type, self.role, self.scope)

    @property
    def notes_anchor(self) -> str:
        return notes_anchor(self.artifact_type, self.role, self.scope)

    def to_markdown(self) -> str:
        sections: list[str] = []
        reading_lines = [f"## {self.reading_list_anchor}"]
        reading_lines.extend(f"- {path}" for path in self.files)
        sections.append("\n".join(reading_lines))
        if self.notes:
            notes_lines = [f"## {self.notes_anchor}"]
            notes_lines.extend(f"- {note}" for note in self.notes)
            sections.append("\n".join(notes_lines))
        return "\n\n".join(sections) + "\n"


def render_cache_hit_reference(
    reading_list_anchor: str,
    notes_anchor: str | None = None,
) -> str:
    lines = [f"- See `{reading_list_anchor}` above."]
    if notes_anchor is not None:
        lines.append(
            f"- See `{notes_anchor}` above — triggers apply to this call too."
        )
    return "\n".join(lines) + "\n"


class ResolverError(ValueError):
    """Raised when authoring cannot be resolved safely."""


def normalize_type(value: str) -> str:
    normalized = value.strip().lower().replace("_", "-")
    if normalized == "use-case":
        normalized = "usecase"
    if normalized not in ALL_TYPES:
        raise ResolverError(f"unsupported artifact type: {value}")
    return normalized


def normalize_role(value: str | None, artifact_type: str) -> str:
    if value is None:
        if artifact_type in ISSUE_TYPES:
            return "issue"
        if artifact_type in KNOWLEDGE_TYPES:
            return "knowledge"
        raise ResolverError(
            f"artifact type '{artifact_type}' can be issue or knowledge; specify --role"
        )

    normalized = value.strip().lower().replace("_", "-")
    if normalized in {"page", "wiki", "doc", "document"}:
        normalized = "knowledge"
    if normalized not in {"issue", "knowledge"}:
        raise ResolverError(f"unsupported artifact role: {value}")

    if artifact_type in ISSUE_TYPES and normalized != "issue":
        raise ResolverError(f"artifact type '{artifact_type}' is issue-backed")
    if artifact_type in KNOWLEDGE_TYPES and normalized != "knowledge":
        raise ResolverError(f"artifact type '{artifact_type}' is knowledge-backed")
    return normalized


def normalize_scope(value: str | None) -> str:
    if value is None:
        return "content"
    normalized = value.strip().lower().replace("_", "-")
    if normalized in {"body", "edit", "full"}:
        normalized = "content"
    if normalized in {"comments", "comment-only", "comment-only-work"}:
        normalized = "comment"
    if normalized not in AUTHORING_SCOPES:
        raise ResolverError(f"unsupported authoring scope: {value}")
    return normalized


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


def resolve_authoring(
    artifact_type: str,
    *,
    role: str | None = None,
    provider: str | None = None,
    project: Path | None = None,
    require_config: bool = False,
    scope: str = "content",
) -> Resolution:
    normalized_type = normalize_type(artifact_type)
    normalized_role = normalize_role(role, normalized_type)
    normalized_scope = normalize_scope(scope)

    config_provider: str | None = None
    if project is not None or require_config:
        try:
            config = load_workflow_config(project or Path.cwd(), require=require_config)
        except WorkflowConfigError as exc:
            raise ResolverError(str(exc)) from exc
        if config is not None:
            config_provider = config.provider_for_role(normalized_role)

    normalized_provider = normalize_provider(provider) or config_provider
    if normalized_provider is not None:
        try:
            validate_provider_for_role(normalized_role, normalized_provider)
        except WorkflowConfigError as exc:
            raise ResolverError(str(exc)) from exc

    parts: list[str] = []
    if normalized_scope == "comment":
        if normalized_role == "issue" and normalized_provider in ISSUE_PROVIDER_FILES:
            parts.append(ISSUE_PROVIDER_FILES[normalized_provider])
        if normalized_role == "knowledge" and normalized_provider in KNOWLEDGE_PROVIDER_FILES:
            parts.append(KNOWLEDGE_PROVIDER_FILES[normalized_provider])
        return Resolution(
            artifact_type=normalized_type,
            role=normalized_role,
            provider=normalized_provider,
            scope=normalized_scope,
            files=absolute_authoring_paths(parts),
        )

    if normalized_role == "issue":
        parts.append("common/issue-body.md")
        parts.append("common/issue-authoring.md")
    else:
        parts.append("common/knowledge-body.md")
    if normalized_type in PRD_COMPONENT_TYPES:
        parts.append("common/prd-authoring.md")
    parts.append(f"common/{normalized_type}-authoring.md")
    if normalized_role == "issue" and normalized_type in PLAN_MODE_TYPES:
        parts.append("common/plan-mode-authoring.md")

    if normalized_role == "issue" and normalized_provider in ISSUE_PROVIDER_FILES:
        parts.append(ISSUE_PROVIDER_FILES[normalized_provider])
        parts.append(ISSUE_PROVIDER_RELATIONSHIP_FILES[normalized_provider])
        parts.append(
            ISSUE_PROVIDER_TYPE_PATTERNS[normalized_provider].format(
                artifact_type=normalized_type
            )
        )
    if normalized_role == "knowledge" and normalized_provider in KNOWLEDGE_PROVIDER_FILES:
        parts.append(KNOWLEDGE_PROVIDER_FILES[normalized_provider])
        parts.append(
            KNOWLEDGE_PROVIDER_TYPE_PATTERNS[normalized_provider].format(
                artifact_type=normalized_type
            )
        )
        if (
            normalized_type in PRD_COMPONENT_TYPES
            and normalized_provider in KNOWLEDGE_PROVIDER_PRD_FILES
        ):
            parts.append(KNOWLEDGE_PROVIDER_PRD_FILES[normalized_provider])
    if normalized_provider is not None:
        parts.extend(PROVIDER_EXTRA_FILES.get((normalized_role, normalized_provider), ()))

    notes_list: list[str] = []
    if normalized_role == "issue" and normalized_type in PLAN_MODE_TYPES:
        notes_list.append(PLAN_MODE_TRIGGER_NOTE)
    if normalized_role == "issue" and normalized_type in TASK_AUDIT_TYPES:
        notes_list.append(TASK_AUDIT_TRIGGER_NOTE)
    notes = tuple(notes_list)

    return Resolution(
        artifact_type=normalized_type,
        role=normalized_role,
        provider=normalized_provider,
        scope=normalized_scope,
        files=absolute_authoring_paths(parts),
        notes=notes,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--type", required=True, help="workflow artifact type")
    parser.add_argument("--role", help="issue or knowledge; required for usecase/research")
    parser.add_argument("--provider", help="provider override, such as github, jira, or confluence")
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
        help="project path used to find .workflow/config.yml",
    )
    parser.add_argument("--require-config", action="store_true", help="fail when .workflow/config.yml is absent")
    parser.add_argument(
        "--cache-policy",
        choices=(CACHE_POLICY_DEFAULT, CACHE_POLICY_REFRESH),
        default=CACHE_POLICY_DEFAULT,
        help="session-state cache policy; refresh forces full emission",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        resolution = resolve_authoring(
            args.type,
            role=args.role,
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

    anchor = resolution.reading_list_anchor
    current_key = _resolution_key(resolution)
    use_cache_hit = False
    if args.cache_policy != CACHE_POLICY_REFRESH:
        existing = read_authoring_resolution(
            args.project, runtime, session_id, anchor
        )
        if existing is not None and _keys_equal(existing.get("key"), current_key):
            use_cache_hit = True

    if use_cache_hit:
        notes_anchor_value = (
            resolution.notes_anchor if resolution.notes else None
        )
        print(
            render_cache_hit_reference(
                resolution.reading_list_anchor, notes_anchor_value
            ),
            end="",
        )
        return 0

    rendered = resolution.to_markdown()
    print(rendered, end="")
    body_lines = rendered.rstrip("\n").splitlines() if rendered else []
    record_authoring_resolution(
        args.project,
        runtime,
        session_id,
        anchor=anchor,
        key=current_key,
        body=body_lines,
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
        "role": resolution.role,
        "provider": resolution.provider,
        "scope": resolution.scope,
    }


def _keys_equal(left: object, right: dict[str, str | None]) -> bool:
    if not isinstance(left, dict):
        return False
    fields = ("type", "role", "provider", "scope")
    return all(left.get(field) == right.get(field) for field in fields)


if __name__ == "__main__":
    raise SystemExit(main())
