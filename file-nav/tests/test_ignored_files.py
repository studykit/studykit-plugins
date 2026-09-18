from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import core
from ui import Navigator


class IgnoredFileTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.root = self.base / "project"
        self.root.mkdir()
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)
        (self.root / ".gitignore").write_text("sources/**\ncache/\nnode_modules/\n")
        (self.root / "visible.txt").write_text("visible")
        (self.root / "sources" / "repo").mkdir(parents=True)
        (self.root / "sources" / "empty").mkdir()
        (self.root / "sources" / "repo" / "ignored.py").write_text("print('preview only')")
        (self.root / "cache").mkdir()
        (self.root / "cache" / "hidden.txt").write_text("cache")

    def navigator(self):
        return Navigator(self.root, "pane", False, "")

    def test_default_hidden_and_explicit_inclusion_preserve_git_state(self):
        before = (self.root / ".gitignore").read_bytes()
        hidden = core.scan(self.root)
        shown = core.scan(self.root, include_ignored=True)
        self.assertNotIn("sources/repo/ignored.py", hidden.files)
        self.assertIn("sources/repo/ignored.py", shown.files)
        self.assertIn("cache/hidden.txt", shown.files)
        self.assertEqual(shown.status, hidden.status)
        self.assertEqual((self.root / ".gitignore").read_bytes(), before)
        self.assertNotIn("sources/repo/ignored.py", shown.status)
        self.assertIn("sources/empty", shown.directories)
        rows = core.rows(shown.files, {"sources"}, directories=shown.directories)
        self.assertTrue(any(row.path == "sources/empty" and row.directory for row in rows))

    def test_nested_repositories_and_worktree_metadata(self):
        nested = self.root / "sources" / "repo"
        subprocess.run(["git", "init", "-q", str(nested)], check=True, capture_output=True)
        (self.root / "sources" / "empty" / ".git").write_text("gitdir: nowhere")
        shown = core.scan(self.root, include_ignored=True)
        self.assertIn("sources/repo/ignored.py", shown.files)
        self.assertFalse(any(".git" in Path(name).parts for name in shown.files + shown.directories))
        self.assertEqual(core.preview(shown, "sources/repo/ignored.py"), "print('preview only')")

    def test_no_directory_symlink_traversal_or_outside_preview(self):
        outside = self.base / "outside"
        outside.mkdir()
        (outside / "secret.txt").write_text("outside")
        (self.root / "sources" / "link").symlink_to(outside, target_is_directory=True)
        (self.root / "sources" / "file-link").symlink_to(outside / "secret.txt")
        shown = core.scan(self.root, include_ignored=True)
        self.assertNotIn("sources/link/secret.txt", shown.files)
        with self.assertRaisesRegex(ValueError, "outside"):
            core.preview(shown, "sources/file-link")

    def test_toggle_search_preview_and_hide_clear_stale_content(self):
        nav = self.navigator()
        self.assertNotIn("sources", [row.path for row in nav.items])
        nav.key("\x08", None)
        self.assertTrue(nav.include_ignored)
        self.assertIn("sources", [row.path for row in nav.items])
        nav.query = "ignored.py"
        nav.rebuild()
        nav.key(" ", None)
        self.assertEqual(nav.active, "sources/repo/ignored.py")
        self.assertIn("preview only", nav.source_text)
        nav.preview_focus = True
        nav.key("\x08", None)
        self.assertFalse(nav.include_ignored)
        self.assertEqual(nav.active, "")
        self.assertEqual(nav.source_text, "")
        self.assertFalse(nav.preview_focus)
        self.assertEqual(nav.items, [])

    def test_control_h_replaces_control_v_without_changing_root(self):
        nav = self.navigator()
        nav.key("\x16", None)
        self.assertFalse(nav.include_ignored)
        nav.key("\x08", None)
        self.assertTrue(nav.include_ignored)
        self.assertEqual(nav.root, self.root)
        nav.key("\x16", None)
        self.assertTrue(nav.include_ignored)
        nav.key("\x08", None)
        self.assertFalse(nav.include_ignored)
        self.assertEqual(nav.root, self.root)

    def test_control_h_still_deletes_text_in_search_and_path_input(self):
        nav = self.navigator()
        nav.key("/", None)
        nav.key("a", None)
        nav.key("\x08", None)
        self.assertEqual(nav.query, "")
        self.assertFalse(nav.include_ignored)
        nav.key("\x1b", None)
        nav.key("\x0f", None)
        path = nav.root_draft
        nav.key("\x08", None)
        self.assertEqual(nav.root_draft, path[:-1])
        self.assertFalse(nav.include_ignored)

    def test_enable_leaves_changes_mode_but_ignored_files_are_not_changes(self):
        nav = self.navigator()
        nav.changes = True
        nav.key("\x08", None)
        self.assertFalse(nav.changes)
        nav.key("\x07", None)
        self.assertTrue(nav.changes)
        self.assertNotIn("sources", [row.path for row in nav.items])

    def test_toggle_failure_is_atomic(self):
        nav = self.navigator()
        before = nav.export_state()
        index = nav.index
        with patch("ui.scan", side_effect=OSError("unreadable")):
            nav.key("\x08", None)
        self.assertEqual(nav.export_state(), before)
        self.assertIs(nav.index, index)
        self.assertIn("unreadable", nav.message)

    def test_resize_refresh_and_root_changes_preserve_toggle(self):
        nav = self.navigator()
        nav.key("\x08", None)
        nav.load("sources/repo/ignored.py")
        nav.refresh()
        self.assertIn("sources/repo/ignored.py", nav.index.files)
        state = nav.export_state()
        restored = self.navigator()
        restored.restore_state(state)
        self.assertTrue(restored.include_ignored)
        self.assertEqual(restored.source_text, nav.source_text)
        nav.change_root("sources")
        self.assertTrue(nav.include_ignored)
        self.assertIn("repo/ignored.py", nav.index.files)

    def test_toggle_does_not_override_input_modals(self):
        for start, finish in (("/", "\x1b"), ("\x0f", "\x1b"), ("\x17", "\x1b")):
            nav = self.navigator()
            nav.key(start, None)
            nav.key("\x08", None)
            self.assertFalse(nav.include_ignored)
            nav.key(finish, None)

    def test_bounded_extra_traversal_and_non_git_dependencies(self):
        outside = self.base / "plain"
        (outside / "node_modules").mkdir(parents=True)
        for i in range(10):
            (outside / "node_modules" / f"{i}.js").write_text("code")
        self.assertEqual(core.scan(outside).files, [])
        with patch("core.MAX_FILES", 5):
            shown = core.scan(outside, include_ignored=True)
        self.assertLessEqual(len(shown.files) + len(shown.directories), 5)
        self.assertIn("node_modules", shown.directories)
        self.assertTrue(shown.files)
        self.assertIn("limited", shown.note)

    def test_toggle_status_is_visible_in_header(self):
        nav = self.navigator()
        screen = Mock()
        screen.getmaxyx.return_value = (30, 120)
        for state in ("hidden", "shown"):
            screen.reset_mock()
            nav.draw(screen)
            self.assertTrue(any(f"Ignored: {state} (^H)" in call.args[2]
                                for call in screen.addstr.call_args_list))
            nav.key("\x08", None)

    def test_budget_visits_sibling_sources_before_deep_cache(self):
        root = self.base / "breadth"
        directory = root / "a-cache"
        for _ in range(12):
            directory /= "deep"
        directory.mkdir(parents=True)
        (root / "sources").mkdir()
        (root / "sources" / "first.py").write_text("source")
        with patch("core.MAX_FILES", 8):
            shown = core.scan(root, include_ignored=True)
        self.assertIn("sources/first.py", shown.files)
        self.assertLessEqual(len(shown.files) + len(shown.directories), 8)


if __name__ == "__main__":
    unittest.main()
