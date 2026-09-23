from concurrent.futures import Future
from pathlib import Path
import subprocess
import sys
import tempfile
from threading import Event
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import core
from ui import Navigator


class DeferredStatusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.git("init", "-q")
        self.git("config", "user.name", "Navigator Test")
        self.git("config", "user.email", "navigator@example.invalid")
        for name in ("a.txt", "b.txt", "gone.txt"):
            (self.root / name).write_text("before\n")
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        (self.root / "b.txt").write_text("after\n")
        self.git("rm", "-q", "gone.txt")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args],
                              check=True, capture_output=True)

    def navigator(self, **kwargs):
        return Navigator(self.root, "source", False, "", defer_status=True, **kwargs)

    def complete(self, nav, status=None, error=None, index=None):
        result = Future()
        if error:
            result.set_exception(error)
        else:
            result.set_result(status if status is not None else core.read_status(nav.root, nav.index.repository))
        nav.status_job = (index or nav.index, result)
        nav.poll_status()

    def test_initial_listing_does_not_run_status_and_later_adds_staged_deletion(self):
        with patch("core.git", wraps=core.git) as git:
            nav = self.navigator()
        self.assertFalse(any(call.args[1] == "status" for call in git.call_args_list))
        self.assertIn("b.txt", nav.index.files)
        self.assertNotIn("gone.txt", nav.index.files)
        self.assertTrue(nav.index.status_pending)
        self.assertEqual(nav.index.status, {})
        self.complete(nav)
        self.assertFalse(nav.index.status_pending)
        self.assertEqual(nav.index.status["b.txt"], " M")
        self.assertEqual(nav.index.status["gone.txt"], "D ")
        self.assertIn("gone.txt", [row.path for row in nav.items])

    def test_query_starts_after_draw_and_close_does_not_wait(self):
        started, release = Event(), Event()
        def slow_status(*args):
            started.set()
            release.wait(5)
            return {}
        nav = self.navigator()
        def draw(screen):
            self.assertFalse(started.is_set())
            self.assertIn("b.txt", nav.index.files)
        def read(screen):
            self.assertTrue(started.wait(2))
            nav.key("j", screen)
            self.assertEqual(nav.items[nav.selected].path, "a.txt")
            return "\x03"
        with patch("ui.read_status", side_effect=slow_status), \
                patch("curses.curs_set"), patch("ui.theme", return_value={}), \
                patch("terminal_input.enable"), patch("terminal_input.disable"), \
                patch("terminal_input.sync_size"), patch("terminal_input.read", side_effect=read), \
                patch.object(nav, "draw", side_effect=draw):
            try:
                nav.run(Mock())
                self.assertFalse(nav.status_job[1].done())
            finally:
                release.set()
                if nav.status_job:
                    nav.status_job[1].result(timeout=2)

    def test_refresh_discards_old_result_even_for_same_root(self):
        nav = self.navigator()
        previous = nav.index
        nav.refresh()
        self.complete(nav, {"stale.txt": "??"}, index=previous)
        self.assertNotIn("stale.txt", nav.index.files)
        self.assertTrue(nav.index.status_pending)
        self.complete(nav)
        self.assertEqual(nav.index.status["b.txt"], " M")

    def test_control_r_discovers_new_files_and_reloads_preview_and_git_status(self):
        (self.root / ".gitignore").write_text("ignored.txt\n")
        nav = self.navigator()
        nav.start_status()
        nav.status_job[1].result(timeout=2)
        nav.poll_status()
        nav.load("a.txt")
        (self.root / "new.txt").write_text("new file\n")
        (self.root / "ignored.txt").write_text("ignored file\n")
        (self.root / "a.txt").write_text("updated preview\n")
        self.assertNotIn("new.txt", nav.index.files)
        self.assertNotIn("a.txt", nav.index.status)
        nav.key("\x12", None)
        self.assertIn("new.txt", [row.path for row in nav.items])
        self.assertNotIn("ignored.txt", nav.index.files)
        self.assertEqual(nav.source_text, "updated preview\n")
        self.assertTrue(nav.index.status_pending)
        nav.start_status()
        nav.status_job[1].result(timeout=2)
        nav.poll_status()
        self.assertEqual(nav.index.status["new.txt"], "??")
        self.assertEqual(nav.index.status["a.txt"], " M")
        nav.key("\x07", None)
        self.assertIn("new.txt", [row.path for row in nav.items])
        self.git("add", ".")
        self.git("commit", "-qm", "all changes saved")
        nav.key("\x12", None)
        nav.start_status()
        nav.status_job[1].result(timeout=2)
        nav.poll_status()
        self.assertEqual(nav.index.status, {})
        self.assertEqual([row.path for row in nav.items], [".."])

    def test_root_change_keeps_one_worker_and_discards_previous_root(self):
        nav = self.navigator()
        old = nav.index
        pending = Future()
        nav.status_job = (old, pending)
        (self.root / "nested").mkdir()
        (self.root / "nested" / "new.txt").write_text("new")
        self.assertTrue(nav.change_root("nested"))
        with patch("ui.read_status") as status:
            nav.start_status()
            status.assert_not_called()
        pending.set_result({"stale.txt": "??"})
        nav.poll_status()
        self.assertNotIn("stale.txt", nav.index.files)
        nav.start_status()
        nav.status_job[1].result(timeout=2)
        nav.poll_status()
        self.assertEqual(nav.index.status, {"new.txt": "??"})

    def test_status_failure_keeps_files_usable_and_can_be_retried(self):
        nav = self.navigator()
        files = list(nav.index.files)
        self.complete(nav, error=subprocess.TimeoutExpired("git", 15))
        self.assertEqual(nav.index.files, files)
        self.assertFalse(nav.index.status_pending)
        self.assertTrue(nav.index.status_error)
        nav.start_status()
        self.assertIsNone(nav.status_job)
        nav.key("/", None)
        nav.key("b", None)
        self.assertEqual([row.path for row in nav.items], ["b.txt"])
        nav.refresh()
        self.assertTrue(nav.index.status_pending)
        self.assertEqual(nav.index.status_error, "")

    def test_completion_preserves_current_view_and_preview(self):
        nav = self.navigator()
        nav.query = "b.txt"
        nav.rebuild()
        nav.load("b.txt")
        nav.preview_focus = True
        before = nav.export_state()
        self.complete(nav)
        self.assertEqual(nav.export_state(), before)
        self.assertEqual(nav.source_text, "after\n")

    def test_changes_view_restores_selection_after_status_without_losing_checkpoint(self):
        state = {"root": str(self.root), "changes": True, "selected": "gone.txt", "scroll": 1}
        nav = self.navigator(initial_state=state)
        self.assertEqual([row.path for row in nav.items], [".."])
        self.assertEqual(nav.export_state()["selected"], "gone.txt")
        self.assertEqual(nav.export_state()["scroll"], 1)
        self.complete(nav)
        self.assertEqual([row.path for row in nav.items], ["..", "b.txt", "gone.txt"])
        self.assertEqual(nav.items[nav.selected].path, "gone.txt")
        self.assertEqual(nav.scroll, 1)

    def test_input_overrides_selection_waiting_for_status(self):
        nav = self.navigator(initial_state={"root": str(self.root), "changes": True, "selected": "gone.txt"})
        nav.key("\x07", None)
        nav.key("j", None)
        self.complete(nav)
        self.assertEqual(nav.items[nav.selected].path, "a.txt")

    def test_close_and_refresh_keep_selection_waiting_for_status(self):
        nav = self.navigator(initial_state={"root": str(self.root), "changes": True,
                                            "selected": "gone.txt", "scroll": 1})
        nav.refresh()
        self.assertFalse(nav.key("\x03", None))
        self.assertEqual(nav.export_state()["selected"], "gone.txt")
        self.assertEqual(nav.export_state()["scroll"], 1)
        self.complete(nav)
        self.assertEqual(nav.items[nav.selected].path, "gone.txt")

    def test_pending_header_distinguishes_unknown_status_from_clean(self):
        nav = self.navigator()
        screen = Mock()
        screen.getmaxyx.return_value = (30, 120)
        nav.draw(screen)
        self.assertTrue(any("Git: loading" in call.args[2] for call in screen.addstr.call_args_list))
        self.complete(nav)
        screen.reset_mock()
        nav.draw(screen)
        self.assertFalse(any("Git: loading" in call.args[2] for call in screen.addstr.call_args_list))

    def test_non_git_root_has_no_background_job(self):
        with tempfile.TemporaryDirectory() as directory:
            nav = Navigator(Path(directory), "source", False, "", defer_status=True)
            nav.start_status()
            self.assertIsNone(nav.status_job)
            self.assertFalse(nav.index.status_pending)

    def test_late_status_merge_respects_entry_limit_and_empty_directories(self):
        index = core.Index(self.root, ["a.txt"], {}, self.root, directories=["empty"])
        with patch("core.MAX_FILES", 3):
            core.apply_status(index, {"b.txt": "??", "c.txt": "??", "empty": "??"})
        self.assertEqual(index.files, ["a.txt", "b.txt"])
        self.assertEqual(index.directories, ["empty"])
        self.assertIn("limited", index.note)


if __name__ == "__main__":
    unittest.main()
