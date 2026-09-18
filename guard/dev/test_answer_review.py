#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Answer preparation and settings migration regressions, without native dispatch."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


PLUGIN = Path(__file__).resolve().parents[1]
SCRIPT = PLUGIN / "skills/answer/scripts/review.py"
CLI = PLUGIN / "scripts/guard_hook.py"
RETIRED = ("claims-auditor", "deferrals-auditor", "clarity-auditor")


class AnswerReviewTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="guard-answer-review-")
        self.addCleanup(temporary.cleanup)
        self.project = Path(temporary.name).resolve()
        self.env = {key: value for key, value in os.environ.items()
                    if not key.startswith(("GUARD_", "CLAUDE_", "CODEX_", "HERDR_"))}
        self.env["PYTHONDONTWRITEBYTECODE"] = "1"

    def config(self, host, action, **extra):
        path = self.project / f".{host}/guard.local.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps({"answer_review": action, **extra}))
        return path

    def run_script(self, script, args, env=None, error=False):
        result = subprocess.run([sys.executable, str(script), *args], cwd=self.project,
                                env=env or self.env, text=True, capture_output=True, timeout=15)
        self.assertEqual(result.returncode, 1 if error else 0, result.stdout + result.stderr)
        return result

    def prepare(self, host, document=None, error=False):
        args = ["--host", host, "--project", str(self.project)]
        if document is not None:
            args.append(str(document))
        return json.loads(self.run_script(SCRIPT, args, error=error).stdout)

    def cli(self, host, *args):
        env = dict(self.env, GUARD_HOST=host, GUARD_PROJECT_DIR=str(self.project),
                   GUARD_SETTINGS_SKILL="1")
        return self.run_script(CLI, list(args), env=env)

    def test_unset_has_no_reviewer_or_side_effects_even_with_old_switches(self):
        for host in ("claude", "codex"):
            self.assertEqual(self.prepare(host), {"status": "no_reviewer"})
            self.assertFalse((self.project / f".{host}").exists())
            path = self.config(host, {}, **{key: "on" for key in RETIRED})
            before = path.read_bytes()
            self.assertEqual(self.prepare(host), {"status": "no_reviewer"})
            self.assertEqual(path.read_bytes(), before)
            self.assertEqual(list(path.parent.iterdir()), [path])

    def test_exact_agent_or_skill_and_host_isolation_without_session(self):
        self.env.update(GUARD_HOST="claude", GUARD_PROJECT_DIR="/wrong-project",
                        CLAUDE_CODE_SESSION_ID="other", CODEX_THREAD_ID="other")
        for kind in ("agent", "skill"):
            for host in ("claude", "codex"):
                self.config(host, {"kind": kind, "name": f"user:{host}-review"})
            for host in ("claude", "codex"):
                result = self.prepare(host)
                self.assertEqual(result["reviewer"], {"kind": kind, "name": f"user:{host}-review"})
                self.assertEqual(result["answer_dir"], str(self.project / f".{host}/answers"))
                self.assertFalse(Path(result["answer_dir"]).exists())

    def test_document_preparation_is_read_only_and_resolves_relative_paths(self):
        document = self.project / "answer with spaces.md"
        document.write_text("# Answer\nEvidence — 검토\n")
        for host in ("claude", "codex"):
            path = self.config(host, {"kind": "skill", "name": "user-review"})
            before = {p: p.read_bytes() for p in (document, path)}
            result = self.prepare(host, document.name)
            self.assertEqual(result["document_path"], str(document))
            self.assertEqual({p: p.read_bytes() for p in before}, before)
            self.assertEqual(list(path.parent.iterdir()), [path])

    def test_invalid_or_recursive_reviewers_never_fall_back(self):
        for host in ("claude", "codex"):
            for action in ({"kind": "unknown", "name": "a"}, {"kind": "agent"},
                           {"kind": "skill", "name": "guard:answer"},
                           {"kind": "skill", "name": "answer"}):
                self.config(host, action)
                self.assertEqual(self.prepare(host, error=True)["status"], "error")
                self.assertFalse((self.project / f".{host}/answers").exists())

    def test_missing_empty_directory_and_invalid_encoding_documents_fail(self):
        empty = self.project / "empty.md"
        empty.write_text(" \n")
        binary = self.project / "binary.md"
        binary.write_bytes(b"\xff")
        for host in ("claude", "codex"):
            self.config(host, {"kind": "agent", "name": "reviewer"})
            for document in ("missing.md", empty, self.project, binary):
                self.assertEqual(self.prepare(host, document, error=True)["status"], "error")

    def test_settings_register_clear_and_preserve_retired_values_until_unset(self):
        for host in ("claude", "codex"):
            path = self.config(host, {}, **{key: "on" for key in RETIRED})
            action = {"kind": "skill", "name": "user:review"}
            self.cli(host, "settings", "set", "answer_review", json.dumps(action))
            shown = self.cli(host, "settings", "show").stdout
            self.assertIn("answer_review: skill:user:review", shown)
            self.assertIn("retired in v0.153.0", shown)
            before = path.read_bytes()
            bad = {"kind": "skill", "name": "guard:answer"}
            self.assertIn("cannot review itself", self.cli(
                host, "settings", "set", "answer_review", json.dumps(bad)).stderr)
            for key in RETIRED:
                self.assertIn("retired", self.cli(host, "settings", "set", key, "off").stderr)
            self.assertEqual(path.read_bytes(), before)
            self.cli(host, "settings", "unset", "answer_review")
            self.assertEqual(self.prepare(host), {"status": "no_reviewer"})
            self.assertTrue(all(json.loads(path.read_text())[key] == "on" for key in RETIRED))
            for key in RETIRED:
                self.cli(host, "settings", "unset", key)
            self.assertFalse(any(key in json.loads(path.read_text()) for key in RETIRED))

    def test_file_checkpoint_survives_retired_state_fields(self):
        document = self.project / "guide.md"
        document.write_text("# Guide\n")
        source = self.project / "code.py"
        source.write_text("# Comment\n")
        for host in ("claude", "codex"):
            self.config(host, {}, **{"doc-auditor": "on", "comment-corrector": "on",
                "doc_review_rules": [{"glob": "*.md", "action": {
                    "kind": "skill", "name": "my-doc-review"}}]})
            path = self.project / f".{host}/guard/state/session.json"
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({**{key: "on" for key in RETIRED},
                "doc-auditor": "on", "comment-corrector": "on",
                "edited_docs": [str(document)], "edited_files": [str(source)],
                "plan_audited_hash": "preserve-plan", "pending_verify_prompt_id": "preserve-turn"}))
            result = json.loads(self.cli(host, "file-checkpoint", "show",
                                        "--session", "session", "--host", host).stdout)
            self.assertIn("my-doc-review", [group["name"] for group in result["groups"]])
            self.assertIn(str(document), result["files"])
            if host == "claude":
                self.assertIn("guard:comment-corrector", [g["name"] for g in result["groups"]])
            state = json.loads(path.read_text())
            self.assertFalse(any(key in state for key in RETIRED))
            self.assertEqual(state["plan_audited_hash"], "preserve-plan")
            self.assertEqual(state["pending_verify_prompt_id"], "preserve-turn")

    def test_candidates_returns_only_migration_notice(self):
        result = self.cli("claude", "candidates", "--doc")
        self.assertEqual(result.stdout, "")
        self.assertIn("retired", result.stderr)
        self.assertIn("answer_review", result.stderr)


if __name__ == "__main__":
    unittest.main()
