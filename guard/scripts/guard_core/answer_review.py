"""Select the user's answer reviewer without creating or modifying a document."""

from pathlib import Path
from typing import Any

from .config import CONFIG_REL, _answer_review_action, _load_config


def prepare_review(project_dir: Path, document: Path | None = None) -> dict[str, Any]:
    action, configured = _answer_review_action(_load_config(project_dir))
    if configured and action is None:
        raise ValueError("answer_review must specify an agent or skill other than answer")
    if action is None:
        return {"status": "no_reviewer"}
    result: dict[str, Any] = {
        "status": "review",
        "reviewer": {"kind": action.kind, "name": action.name},
        # Deliverables live outside the swept Guard state directory.
        "answer_dir": str((project_dir / Path(CONFIG_REL).parent / "answers").resolve()),
    }
    if document is not None:
        resolved = document.resolve(strict=True)
        if not resolved.read_text(encoding="utf-8").strip():
            raise ValueError("The answer document is empty")
        result["document_path"] = str(resolved)
    return result
