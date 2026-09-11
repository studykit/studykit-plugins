import contextlib
import importlib.util
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("handover", Path(__file__).parents[1] / "hooks/handover_hook.py")
hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook)


class LifecycleTests(unittest.TestCase):
    def test_session_record_requires_matching_end_and_clear_consumes_once(self):
        for reason in ("clear",):
            with self.subTest(reason=reason), tempfile.TemporaryDirectory() as directory:
                project = Path(directory).resolve()
                handover = project / "handover.md"
                handover.write_text("Resume test work.")
                with patch.object(hook, "state_dir", return_value=project / "state"), patch.dict(os.environ, {"CLAUDE_PROJECT_DIR": str(project), "CLAUDE_ENV_FILE": ""}):
                    hook.write_json(hook.session_path(project, "old"), {"handover_file": str(handover)})
                    self.assertFalse(hook.handoff_path(project).exists())
                    hook.on_end({"session_id": "old", "reason": "other"})
                    self.assertFalse(hook.handoff_path(project).exists())
                    hook.on_end({"cwd": str(project), "session_id": "unrelated", "reason": reason})
                    self.assertFalse(hook.handoff_path(project).exists())
                    hook.on_end({"cwd": str(project), "session_id": "old", "reason": reason})
                    self.assertFalse(hook.session_path(project, "old").exists())
                    with contextlib.redirect_stdout(io.StringIO()) as output:
                        hook.on_start({"cwd": str(project), "session_id": "new", "source": "startup"})
                    self.assertEqual(output.getvalue(), "")
                    self.assertTrue(hook.handoff_path(project).exists())
                    with contextlib.redirect_stdout(io.StringIO()) as output:
                        hook.on_start({"cwd": str(project), "session_id": "new", "source": "clear"})
                    self.assertIn(str(handover), json.loads(output.getvalue())["hookSpecificOutput"]["additionalContext"])
                    with contextlib.redirect_stdout(io.StringIO()) as output:
                        hook.on_start({"cwd": str(project), "session_id": "newer", "source": "clear"})
                    self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
