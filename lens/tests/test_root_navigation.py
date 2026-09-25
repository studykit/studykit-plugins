import curses
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from terminal_input import Mouse
import ui
from ui import Navigator


class RootNavigationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.first = self.base / "first"
        self.second = self.base / "한글 project"
        for root in (self.first, self.second):
            root.mkdir()
            (root / "file.md").write_text(f"# {root.name}\n")
        (self.first / "child").mkdir()
        (self.first / "child" / "nested.txt").write_text("nested")
        self.nav = Navigator(self.first, "source-pane", False, "")

    def enter_path(self, path):
        self.nav.key("\x0f", None)
        self.nav.key("\x15", None)
        for char in str(path):
            self.nav.key(char, None)
        self.nav.key("\n", None)

    def test_editor_opens_folders_without_a_line(self):
        self.nav.editor = "vim +{line}"
        opened = []
        self.nav.run_terminal = lambda screen, command, cwd: opened.append(command) or Mock(returncode=0)
        for name, expected in ((".", self.first), ("..", self.base), ("child", self.first / "child")):
            self.nav.selected = [row.path for row in self.nav.items].index(name)
            with patch("core.shutil.which", return_value="/bin/vim"):
                self.nav.edit(None)
            self.assertEqual(opened[-1], ["vim", str(expected.absolute())])
        self.nav.key("e", None)  # e edits from the files panel, like Ctrl+E.
        self.assertEqual(len(opened), 4)
        self.nav.load("file.md")
        self.nav.preview_focus = True
        self.nav.key("e", None)  # And from the preview, on the previewed file.
        self.assertEqual(opened[-1][-1], str((self.first / "file.md").absolute()))
        self.assertEqual(len(opened), 5)

    def test_relative_root_resets_stale_file_state_and_leaves_cwd_unchanged(self):
        cwd = Path.cwd()
        self.nav.load("file.md")
        self.nav.prepare_preview(80)
        self.nav.query = self.nav.search_before = "old"
        self.nav.expanded.add("child")
        self.nav.preview_focus = True
        self.nav.scroll = self.nav.preview_scroll = self.nav.horizontal = 10
        self.enter_path("../한글 project")
        self.assertEqual(self.nav.root, self.second)
        self.assertEqual(self.nav.index.root, self.second)
        self.assertEqual(self.nav.query, "")
        self.assertEqual(self.nav.expanded, set())
        self.assertEqual(self.nav.active, "")
        self.assertEqual(self.nav.source_text, "")
        self.assertFalse(self.nav.previewable)
        self.assertFalse(self.nav.preview_focus)
        self.assertIsNone(self.nav.rendered)
        self.assertIsNone(self.nav.syntax)
        self.assertIsNone(self.nav.root_draft)
        self.assertEqual((self.nav.scroll, self.nav.preview_scroll, self.nav.horizontal), (0, 0, 0))
        self.assertEqual(Path.cwd(), cwd)
        self.assertEqual(self.nav.pane_id, "source-pane")
        self.nav.load("file.md")
        self.assertIn("한글 project", self.nav.source_text)

    def test_selected_folder_prefills_dialog_and_enter_changes_root(self):
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "child")
        self.nav.key("\x0f", None)
        self.assertEqual(self.nav.root_draft, str(self.first / "child"))
        self.nav.key("\n", None)
        self.assertEqual(self.nav.root, self.first / "child")
        self.assertEqual(self.nav.index.files, ["nested.txt"])

    def test_parent_entry_and_click_keep_previous_folder_selected(self):
        for key in ("\n", Mouse(3, ui.ROOT_ROW, "click")):
            with self.subTest(key=key):
                self.nav.change_root(self.first / "child")
                if key == "\n":
                    self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "..")
                self.nav.key(key, None)
                self.assertEqual(self.nav.root, self.first)
                self.assertEqual(self.nav.items[self.nav.selected].path, "child")

    def test_tree_backspace_does_not_change_root(self):
        self.nav.change_root(self.first / "child")
        for key in ("\x7f", curses.KEY_BACKSPACE):
            with self.subTest(key=key):
                self.nav.key(key, None)
                self.assertEqual(self.nav.root, self.first / "child")
        self.assertNotIn(("⌫", "Parent folder"), self.nav.key_groups()[1][1])

    def test_parent_action_can_be_bound_explicitly(self):
        self.nav.change_root(self.first / "child")
        self.nav.bindings = {"P": "parent"}
        self.nav.key("P", None)
        self.assertEqual(self.nav.root, self.first)

    def test_invalid_empty_file_and_scan_failure_keep_previous_state(self):
        self.nav.load("file.md")
        before = self.nav.export_state()
        old_index = self.nav.index
        for path in ("", "missing", "file.md"):
            self.enter_path(path)
            self.assertEqual(self.nav.export_state(), before)
            self.assertIs(self.nav.index, old_index)
            self.assertIsNotNone(self.nav.root_draft)
            self.assertIn("Could not change root", self.nav.root_error)
            self.nav.key("\x1b", None)
        with patch("ui.scan", side_effect=PermissionError("Denied")):
            self.assertFalse(self.nav.change_root(self.second))
        self.assertEqual(self.nav.export_state(), before)
        with patch("ui.os.scandir", side_effect=PermissionError("Denied")):
            self.assertFalse(self.nav.change_root(self.second))
        self.assertEqual(self.nav.export_state(), before)

    def test_cancel_and_modal_priority_preserve_view(self):
        self.nav.preview_focus = True
        self.nav.load("file.md")
        before = self.nav.export_state()
        self.nav.key("\x0f", None)
        draft = self.nav.root_draft
        for key in ("\x13", "\x14", "\x12", Mouse(3, ui.ROOT_ROW, "click"), "\x0f"):
            self.nav.key(key, None)
        self.assertEqual(self.nav.root_draft, draft)
        self.nav.key("\x17", None)  # C-w kills the last path part, as on the command line.
        self.nav.key("\x19", None)  # C-y puts it back.
        self.assertEqual(self.nav.root_draft, draft)
        self.nav.key("\x1b", None)
        self.assertEqual(self.nav.export_state(), before)
        self.assertIsNone(self.nav.root_draft)

    def test_search_and_preview_backspace_keep_their_existing_meaning(self):
        self.nav.key("/", None)
        for key in ("a", "b", "\x7f", "\x0f", "\x14"):
            self.nav.key(key, None)
        self.assertEqual(self.nav.query, "a")
        self.assertEqual(self.nav.root, self.first)
        self.assertIsNone(self.nav.root_draft)
        self.nav.key("\x1b", None)
        self.nav.preview_focus = True
        self.nav.key("\x7f", None)
        self.assertEqual(self.nav.root, self.first)

    def test_path_editing_and_home_expansion(self):
        self.nav.key("\x0f", None)
        self.nav.key("\x15", None)
        for key in ("a", "c", curses.KEY_LEFT, "b"):
            self.nav.key(key, None)
        self.assertEqual(self.nav.root_draft, "abc")
        self.nav.key(curses.KEY_DC, None)
        self.nav.key(curses.KEY_HOME, None)
        self.nav.key("x", None)
        self.nav.key(curses.KEY_END, None)
        self.nav.key("\x7f", None)
        self.assertEqual(self.nav.root_draft, "xa")
        self.nav.key("\x1b", None)
        with patch.dict(os.environ, {"HOME": str(self.base)}):
            self.enter_path("~/한글 project")
        self.assertEqual(self.nav.root, self.second)

    def test_symlink_and_empty_directory(self):
        (self.base / "alias").symlink_to(self.second, target_is_directory=True)
        self.enter_path(self.base / "alias")
        self.assertEqual(self.nav.root, self.second)
        empty = self.base / "empty"
        empty.mkdir()
        self.enter_path(empty)
        self.assertEqual(self.nav.root, empty)
        self.assertEqual([row.path for row in self.nav.items], [".", ".."])
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "..")
        self.nav.key("\n", None)
        self.assertEqual(self.nav.root, self.base)

    def test_filesystem_root_parent_is_noop(self):
        self.nav.root = Path(self.first.anchor)
        with patch("ui.scan") as scan:
            self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "..")
            self.nav.key("\n", None)
        scan.assert_not_called()
        self.assertIn("Already", self.nav.message)

    def test_git_root_and_repository_switch(self):
        for root in (self.first, self.second):
            subprocess.run(["git", "-C", str(root), "init", "-q"], check=True, capture_output=True)
        self.nav.change_root(self.first / "child")
        self.nav.key("t", None)
        self.assertEqual(self.nav.root, self.first)
        self.assertEqual(self.nav.index.repository, self.first)
        self.enter_path(self.second)
        self.assertEqual(self.nav.index.repository, self.second)
        self.assertEqual(self.nav.index.status, {"file.md": "??"})
        self.nav.change_root(self.base)
        self.nav.key("t", None)
        self.assertEqual(self.nav.root, self.base)
        self.assertIn("not inside a Git", self.nav.message)

    def test_changing_root_keeps_a_preview_still_under_it(self):
        self.nav.change_root(self.first / "child")
        self.nav.load("nested.txt")
        self.nav.preview_focus = True
        self.nav.change_root(self.first)
        self.assertEqual((self.nav.active, self.nav.preview_focus), ("child/nested.txt", True))
        self.nav.change_root(self.second)
        self.assertEqual((self.nav.active, self.nav.preview_focus), ("", False))

    def test_resize_state_retains_changed_root(self):
        self.nav.change_root(self.second)
        self.nav.load("file.md")
        state = self.nav.export_state()
        restored = Navigator(Path(state["root"]), "source-pane", False, "")
        restored.restore_state(state)
        self.assertEqual(restored.root, self.second)
        self.assertIn("한글 project", restored.source_text)

    def test_modal_draw_and_path_click(self):
        self.nav.key(Mouse(10, ui.ROOT_ROW, "click"), None)
        self.assertIsNotNone(self.nav.root_draft)
        screen = Mock()
        for dimensions in ((44, 160), (20, 50), (10, 30)):
            screen.getmaxyx.return_value = dimensions
            self.nav.draw(screen)
        self.assertTrue(any("CHANGE ROOT" in str(call) for call in screen.addstr.call_args_list))

    def test_parent_entry_enter_click_and_changes_mode(self):
        for key in ("\n", Mouse(10, self.nav.content_top + 1, "click")):
            for changes in (False, True):
                self.nav.change_root(self.first / "child")
                self.nav.changes = changes
                self.nav.rebuild()
                self.nav.selected = 1
                self.assertEqual(self.nav.items[1].path, "..")
                with patch.object(self.nav, "show_diff") as diff:
                    self.nav.key(key, None)
                self.assertEqual(self.nav.root, self.first)
                self.assertFalse(self.nav.preview_focus)
                diff.assert_not_called()

    def test_enter_makes_a_folder_the_root_and_click_folds_it(self):
        rows = [row.path for row in self.nav.items]
        self.assertEqual(rows[:2], [".", ".."])
        self.nav.selected = rows.index("child")
        self.nav.key(Mouse(10, self.nav.content_top + self.nav.selected, "click"), None)
        self.assertEqual(self.nav.root, self.first)
        self.assertIn("child", self.nav.expanded)
        self.nav.key("\n", None)
        self.assertEqual(self.nav.root, self.first / "child")
        self.assertEqual(self.nav.items[self.nav.selected].path, "nested.txt")
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "..")
        self.nav.key("\n", None)
        self.assertEqual(self.nav.root, self.first)

    def test_space_folds_folders_but_not_dot_rows(self):
        rows = [row.path for row in self.nav.items]
        self.nav.selected = rows.index("child")
        self.nav.key(" ", None)
        self.assertIn("child", self.nav.expanded)
        self.nav.key(" ", None)
        self.assertNotIn("child", self.nav.expanded)
        for index in (0, 1):
            self.nav.selected = index
            self.nav.key(" ", None)
            self.assertEqual(self.nav.root, self.first)
            self.assertEqual(self.nav.expanded, set())

    def test_dot_row_opens_the_root_folder(self):
        self.nav.selected = 0
        self.nav.key("\n", None)
        self.assertEqual(self.nav.root, self.first)
        self.assertIn("o opens it", self.nav.message)
        with patch("ui.subprocess.Popen") as popen, patch("ui.opener_command", return_value=["open", "x"]) as opener:
            popen.return_value.wait.return_value = 0
            popen.return_value.communicate.return_value = (b"", b"")
            popen.return_value.returncode = 0
            self.nav.key("o", None)
        self.assertEqual(opener.call_args.args[1].resolve(), self.first)

    def test_parent_entry_is_not_searchable_or_previewable(self):
        self.nav.selected = 0
        self.nav.key(" ", None)
        self.assertFalse(self.nav.preview_focus)
        self.assertEqual(self.nav.active, "")
        self.nav.query = "file"
        self.nav.rebuild()
        self.assertNotIn("..", [row.path for row in self.nav.items])
        self.nav.query = "missing"
        self.nav.rebuild()
        self.assertEqual(self.nav.items, [])


if __name__ == "__main__":
    unittest.main()
