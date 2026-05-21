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
    cache_refreshed: bool | None = None
    provider_kind: str = "github"
    issue_file: str = "issue.md"
    comments: tuple[str, ...] = ()

    def to_json(self, basedir: str = "") -> dict[str, Any]:
        issue_dir = ensure_trailing_slash(self.issue_dir.strip())
        relative_dir = issue_dir[len(basedir):] if basedir and issue_dir.startswith(basedir) else issue_dir
        payload: dict[str, Any] = {
            "issue": f"{relative_dir}{self.issue_file}",
            "title": self.title,
            "state": self.state,
            "cache_refreshed": self.cache_refreshed,
        }
        if self.comments:
            payload["comments"] = [
                comment[len(basedir):] if basedir and comment.startswith(basedir) else comment
                for comment in self.comments
            ]
        return payload


def cache_refreshed_from_payload(payload: Mapping[str, Any], *, default: bool | None = None) -> bool | None:
    cache_data = payload.get("cache")
    if isinstance(cache_data, Mapping):
        hit = cache_data.get("hit")
        if isinstance(hit, bool):
            return not hit
    return default


_FLATTEN_PROVIDER_DROPS = frozenset(
    {
        "operation",
        "cache",
        "verified",
        "role",
        "kind",
        "repository",
        "site",
        "issue",
        "key",
        "cache_refreshed",
    }
)


def flatten_provider_envelope(
    provider_payload: Mapping[str, Any],
    *,
    project: Path,
    issue_file: Path | None = None,
) -> dict[str, Any]:
    """Flatten a workflow issue provider response to the CLI envelope.

    Returns ``{issue, cache_refreshed, ...verb-specific extras}``. Drops the
    provider wrapper fields (``operation``, ``role``, ``kind``,
    ``repository``/``site``, ``verified``), the inner ``cache`` block, and
    the bare-ref ``issue``/``key`` strings. Freshness-drift fields
    (``status``, ``reason``, ``message``, ``reread_required``,
    ``reread_paths``) pass through untouched.

    ``issue_file`` defaults to ``provider_payload["cache"]["issue_file"]``;
    the relationships flow passes it explicitly because that provider
    response does not carry a ``cache`` block.
    """

    if issue_file is None:
        cache_block = provider_payload.get("cache")
        if isinstance(cache_block, Mapping):
            file_str = cache_block.get("issue_file")
            if file_str:
                issue_file = Path(str(file_str))
        if issue_file is None:
            reread_paths = provider_payload.get("reread_paths")
            if isinstance(reread_paths, (list, tuple)) and reread_paths:
                issue_file = Path(str(reread_paths[0]))

    issue_path = display_project_path(issue_file, project) if issue_file else ""
    flat: dict[str, Any] = {
        "issue": issue_path,
        "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
    }
    for key, value in provider_payload.items():
        if key in _FLATTEN_PROVIDER_DROPS:
            continue
        flat[key] = value
    return flat


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
        suffix = " (refreshed)" if context.cache_refreshed is True else ""
        lines.append(f"- {issue_ref} → `{issue_path}`{suffix}")
        for comment_path in context.comments:
            relative = comment_path[len(shared_base):] if shared_base and comment_path.startswith(shared_base) else comment_path
            lines.append(f"  - `{relative}`")
    return "\n".join(lines)


def format_issue_cache_json(
    contexts: Sequence[IssueFetchContext],
) -> dict[str, Any]:
    """Build compact JSON for provider issue fetch output."""

    basedir = shared_basedir(contexts)
    return {
        "basedir": basedir,
        "issues": [context.to_json(basedir) for context in contexts],
    }


def shared_basedir(contexts: Sequence[IssueFetchContext]) -> str:
    """Return the directory shared by every context's issue_dir."""

    bases: list[str] = []
    for context in contexts:
        issue_dir = ensure_trailing_slash(context.issue_dir.strip())
        suffix = f"{context.number}/"
        if not issue_dir.endswith(suffix):
            return ""
        bases.append(issue_dir[: -len(suffix)])
    if not bases:
        return ""
    first = bases[0]
    if any(base != first for base in bases):
        return ""
    return first


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
