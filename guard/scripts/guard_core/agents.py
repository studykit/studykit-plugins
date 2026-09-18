"""Markdown inclusion scope and disjoint storage buckets for edited paths."""

from __future__ import annotations

from pathlib import Path
from typing import NamedTuple

class DocScope(NamedTuple):
    """Optional included directories for ordinary Markdown."""

    include: tuple[Path, ...]


_AGENT_DOC_NAMES = frozenset({"agents.md", "claude.md"})


def _in_doc_scope(target: Path, doc_scope: DocScope | None) -> bool:
    """Whether ordinary Markdown belongs to the configured document directories."""
    if doc_scope is None:
        return False
    if not doc_scope.include:
        return True
    return any(d == target.parent or d in target.parents for d in doc_scope.include)


def _edited_bucket(target: Path, refs_dir: Path | None = None,
                   doc_scope: DocScope | None = None) -> str | None:
    if refs_dir is not None and target.suffix.lower() == ".md" and (
            target.parent == refs_dir or refs_dir in target.parents):
        return "edited_refs"
    if target.name.lower() in _AGENT_DOC_NAMES:
        return "edited_agent_docs"
    if target.suffix.lower() == ".md" and _in_doc_scope(target, doc_scope):
        return "edited_docs"
    return None if target.suffix.lower() == ".md" else "edited_files"
