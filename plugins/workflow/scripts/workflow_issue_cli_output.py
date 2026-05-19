#!/usr/bin/env python3
"""Issue CLI output helpers."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class IssueFetchContext:
    """Concise context for one provider issue cache read."""

    number: str
    issue_dir: str
    title: str
    state: str
    cache_hit: bool | None = None
    provider_kind: str = "github"
    issue_file: str = "issue.md"

    def to_json(self) -> dict[str, Any]:
        payload = {
            "issue": self.number,
            "issue_dir": self.issue_dir,
            "title": self.title,
            "state": self.state,
            "cache_hit": self.cache_hit,
        }
        if self.issue_file != "issue.md":
            payload["issue_file"] = self.issue_file
        return payload


def cache_hit_from_payload(payload: Mapping[str, Any], *, default: bool | None = None) -> bool | None:
    cache_data = payload.get("cache")
    if isinstance(cache_data, Mapping):
        hit = cache_data.get("hit")
        if isinstance(hit, bool):
            return hit
    return default


def format_issue_cache_context(
    contexts: Sequence[IssueFetchContext],
    *,
    include_details: bool = True,
) -> str:
    """Render issue cache context using project-relative cache issue files."""

    _ = include_details
    shared_base = shared_issue_dir_base(contexts)
    lines = ["## Workflow issue cache", ""]
    if shared_base is not None:
        lines.append(f"Base: `{shared_base}`")
    for context in contexts:
        issue_path = issue_file_relative_to_base(context, shared_base)
        issue_ref = f"#{context.number}" if context.provider_kind == "github" else context.number
        suffix = " (refreshed)" if context.cache_hit is False else ""
        lines.append(f"- {issue_ref} → `{issue_path}`{suffix}")
    return "\n".join(lines)


def format_issue_cache_json(
    contexts: Sequence[IssueFetchContext],
    *,
    provider_kind: str,
    cache_policy: str,
    repository: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build compact JSON for provider issue fetch output."""

    payload: dict[str, Any] = {
        "operation": "cache_fetch",
        "role": "issue",
        "kind": provider_kind,
        "cache_policy": cache_policy,
        "issues": [context.to_json() for context in contexts],
    }
    if repository is not None:
        payload["repository"] = dict(repository)
    return payload


def format_issue_cache_context_from_payload(payload: dict[str, object]) -> str:
    """Render plain output from the JSON payload without re-reading cache files."""

    contexts: list[IssueFetchContext] = []
    for item in payload.get("issues", []):
        if not isinstance(item, dict):
            continue
        cache_hit = item.get("cache_hit")
        contexts.append(
            IssueFetchContext(
                number=str(item.get("issue") or ""),
                issue_dir=str(item.get("issue_dir") or ""),
                title=str(item.get("title") or ""),
                state=str(item.get("state") or ""),
                cache_hit=cache_hit if isinstance(cache_hit, bool) else None,
                provider_kind=str(payload.get("kind") or "github"),
                issue_file=str(item.get("issue_file") or "issue.md"),
            )
        )

    return format_issue_cache_context(contexts)


def display_project_path(path: Path, project: Path, *, trailing_slash: bool = False) -> str:
    resolved = path.expanduser().resolve(strict=False)
    try:
        display = resolved.relative_to(project.expanduser().resolve(strict=False)).as_posix()
    except ValueError:
        display = str(resolved)
    if trailing_slash and not display.endswith("/"):
        display += "/"
    return display


def shared_issue_dir_base(contexts: Sequence[IssueFetchContext]) -> str | None:
    """Return a shared issue directory prefix for multi-issue displays."""

    if len(contexts) <= 1:
        return None

    bases: list[str] = []
    for context in contexts:
        issue_dir = ensure_trailing_slash(context.issue_dir.strip())
        suffix = f"{context.number}/"
        if not issue_dir.endswith(suffix):
            return None
        bases.append(issue_dir[: -len(suffix)])

    if not bases:
        return None
    first = bases[0]
    if not first or any(base != first for base in bases):
        return None
    return first


def issue_file_relative_to_base(context: IssueFetchContext, base: str | None) -> str:
    issue_dir = ensure_trailing_slash(context.issue_dir.strip())
    issue_file = f"{issue_dir}{context.issue_file}"
    if base is None or not issue_dir.startswith(base):
        return issue_file
    relative = f"{issue_dir[len(base) :]}{context.issue_file}"
    return relative or issue_file


def ensure_trailing_slash(value: str) -> str:
    if not value or value.endswith("/"):
        return value
    return f"{value}/"
