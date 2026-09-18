"""File-review switches and classification of edited paths."""

from __future__ import annotations

from pathlib import Path
from typing import NamedTuple

from .config import _doc_glob_matches


class DocScope(NamedTuple):
    """Included document directories plus directory and glob exclusions."""

    include: tuple[Path, ...]
    exclude: tuple[Path, ...]
    exclude_globs: tuple[str, ...] = ()
    project_dir: Path | None = None


SETTABLE_AGENTS = ("comment-corrector", "doc-auditor")


# Source files whose comments `comment-corrector` can judge. Deliberately not "every
# file the turn touched": the agent judges comments against the code under them, and a
# markdown or JSON edit gives it nothing to judge. Extension-based rather than
# content-sniffing because this runs on every edit and must stay a set lookup.
_SOURCE_SUFFIXES = frozenset({
    ".py", ".pyi", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".go", ".rs",
    ".java", ".kt", ".kts", ".c", ".h", ".cc", ".cpp", ".hpp", ".cs", ".rb", ".php",
    ".swift", ".scala", ".sh", ".bash", ".zsh", ".lua", ".sql", ".m", ".mm", ".dart",
    ".ex", ".exs", ".vue", ".svelte", ".zig",
})


# Filenames `agents-md-auditor` can judge. Matched on the name, not the suffix: what makes
# one of these auditable is that a coding agent loads it as standing instruction, and that
# is a property of the name the host looks for, not of it being markdown. Every other
# markdown file in a repository is prose nobody is instructed by, and auditing one against
# what an instruction file may contain would flag an ordinary document for having content.
#
# Lowercased before the lookup, since a repository may spell either one in any case and the
# host resolves them case-insensitively on macOS and Windows regardless.
#
# Every other markdown file in a repository is prose nobody is instructed by, and auditing
# one against what an instruction file may contain would flag an ordinary document for
# having content. Those go to `doc-auditor` instead, on a bar of their own — which is why
# this set stays exactly these two names and does not grow.
_AGENT_DOC_NAMES = frozenset({"agents.md", "claude.md"})


def _in_doc_scope(target: Path, doc_scope: DocScope | None) -> bool:
    """Whether this markdown file is one of the project's documents.

    Scope is CONFIGURED, and both halves are needed for different reasons. ``exclude`` is
    the load-bearing one: a repository keeps markdown that is not a document — scratch
    directories, vendored trees, a handover log — and a project that already audits some
    corner of its docs another way has to be able to say so, or two audits fault the same
    file for opposite reasons. ``include``, when set, narrows to those directories and is
    the safer shape for a repository whose non-document markdown outnumbers its documents.

    Empty ``include`` means the whole project, which is the honest default: a project that
    turned this audit on meant its documents, and guessing which subset from directory names
    would be guard deciding what counts as documentation for a repository it has never read.
    """
    if doc_scope is None or _excluded_document(target, doc_scope):
        return False
    if not doc_scope.include:
        return True
    return any(d == target.parent or d in target.parents for d in doc_scope.include)


def _excluded_document(target: Path, doc_scope: DocScope | None) -> bool:
    """Whether directory or glob exclusions remove this Markdown from every review bucket."""
    if doc_scope is None:
        return False
    if any(d == target.parent or d in target.parents for d in doc_scope.exclude):
        return True
    if doc_scope.project_dir is not None:
        try:
            relative = target.relative_to(doc_scope.project_dir).as_posix()
        except ValueError:
            return True
        if any(_doc_glob_matches(relative, pattern) for pattern in doc_scope.exclude_globs):
            return True
    return False


# Which state list a PostToolUse target belongs in, if any.
#
# ORDER IS LOAD-BEARING here, unlike the two name-based tests below it, which are disjoint by
# construction (`_SOURCE_SUFFIXES` holds no `.md`). The refs test is by LOCATION and it comes
# first, because the refs directory's own index is named `AGENTS.md` and its shim `CLAUDE.md`:
# by name alone both go to the agent-doc auditor, which would fault the index of a reference
# library for not being a map of the project's deeper docs — a finding that is wrong about a
# file that is doing its job. Inside the refs directory, every markdown file is the refs
# auditor's, index included: a row describing local reasoning is the same violation as a
# section of it.
#
# `edited_docs` comes LAST, and it is the open-ended one: it takes whatever markdown the
# three tests above left, inside the configured scope. Every bucket before it is closed —
# a location, a suffix set, two filenames — so putting the open test last is what keeps
# them disjoint without another exclusion list to maintain. A refs file and an `AGENTS.md`
# are both markdown and both already spoken for by the time it is reached.
#
# `refs_dir` and `doc_scope` are passed in rather than resolved here so this stays a pure
# function of its arguments; the caller already has the project dir and the config it takes
# to resolve them.
def _edited_bucket(target: Path, refs_dir: Path | None = None,
                   doc_scope: DocScope | None = None) -> str | None:
    if target.suffix.lower() == ".md" and _excluded_document(target, doc_scope):
        return None
    if refs_dir is not None and target.suffix.lower() == ".md" and (
            target.parent == refs_dir or refs_dir in target.parents):
        return "edited_refs"
    if target.suffix.lower() in _SOURCE_SUFFIXES:
        return "edited_files"
    if target.name.lower() in _AGENT_DOC_NAMES:
        return "edited_agent_docs"
    if target.suffix.lower() == ".md" and _in_doc_scope(target, doc_scope):
        return "edited_docs"
    return None
