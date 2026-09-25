import curses
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import command_line
import git_history
import view_state
from ui import Navigator


class GitHistoryTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.git("init", "-q")
        self.git("config", "user.name", "History Test")
        self.git("config", "user.email", "history@example.invalid")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True).stdout

    def commit(self, subject):
        self.git("add", "-A")
        self.git("commit", "-qm", subject)

    def fixture(self):
        (self.root / "old name.txt").write_text("before\n")
        self.commit("add file")
        self.git("mv", "old name.txt", "new name.txt")
        self.commit("rename file")
        (self.root / "new name.txt").write_text("after\n")
        self.commit("edit file")

    def test_project_and_file_history_follow_rename(self):
        self.fixture()
        project, more = git_history.commits(self.root)
        self.assertFalse(more)
        self.assertEqual([entry.subject for entry in project], ["edit file", "rename file", "add file"])
        file, more = git_history.commits(self.root, path="new name.txt")
        self.assertFalse(more)
        self.assertEqual([entry.path for entry in file], ["new name.txt", "new name.txt", "old name.txt"])
        rename = git_history.changed_files(self.root, file[1].oid)
        self.assertEqual((rename[0].status, rename[0].previous, rename[0].path),
                         ("R100", "old name.txt", "new name.txt"))
        self.assertIn("rename from old name.txt", git_history.patch(self.root, file[1].oid, rename[0]))
        self.assertIn("+before", git_history.patch(self.root, file[2].oid,
                                                  git_history.changed_files(self.root, file[2].oid)[0]))

    def test_history_ui_navigation_and_return_to_files(self):
        self.fixture()
        nav = Navigator(self.root, "pane", False, "")
        nav.run_command("git.history", None)
        self.assertEqual(nav.history_mode, "project")
        self.assertEqual(nav.history_commits[0].subject, "edit file")
        self.assertEqual([title for title, _ in nav.key_groups()], ["History", "Current panel"])
        self.assertIn(("Enter l", "Show details"), nav.key_groups()[1][1])
        nav.key("\n", None)
        self.assertTrue(nav.history_right_focus)
        self.assertIn(("Enter l", "Show file diff"), nav.key_groups()[1][1])
        nav.key("\n", None)
        self.assertTrue(nav.history_patch)
        self.assertIn(("j k ↑ ↓", "Scroll diff"), nav.key_groups()[1][1])
        self.assertIn("+after", "\n".join(nav.history_lines()[0]))
        nav.key("\x1b", None)
        self.assertFalse(nav.history_patch)
        nav.key("\x1b", None)
        self.assertFalse(nav.history_right_focus)
        nav.key("\x1b", None)
        self.assertEqual(nav.history_mode, "")
        self.assertEqual(nav.items[2].path, "new name.txt")
        nav.selected = 2
        nav.key("H", None)
        self.assertEqual(nav.history_mode, "file")
        self.assertIn("+after", "\n".join(nav.history_lines()[0]))
        nav.key("j", None)
        self.assertEqual(nav.history_commits[nav.history_selected].subject, "rename file")
        self.assertIn("rename from old name.txt", "\n".join(nav.history_lines()[0]))
        nav.key("j", None)
        self.assertEqual(nav.history_commits[nav.history_selected].path, "old name.txt")
        self.assertIn("+before", "\n".join(nav.history_lines()[0]))
        nav.key("\x07", None)
        self.assertEqual(nav.history_mode, "file")  # Ctrl+G never closes Lens or history.
        nav.key("\x1b", None)
        self.assertEqual(nav.history_mode, "")
        self.assertEqual(view_state.normalize(nav.export_state(), self.root)["history_path"], "")

    def test_git_commands_are_grouped_without_old_aliases(self):
        names = command_line.candidates("git.", self.root, [])[1]
        self.assertEqual(names, ["git.changes", "git.diff", "git.file-history", "git.history",
                                 "git.ignored", "git.root"])
        self.assertIn("git.file-history", command_line.describe("git"))
        for old in ("git-root", "history", "history-file", "changes", "diff", "ignored"):
            self.assertIsNone(command_line.lookup(old))

    def test_git_prefix_shows_available_commands_and_opens_history(self):
        self.fixture()
        nav = Navigator(self.root, "pane", False, "")
        nav.key("g", None)
        self.assertEqual(nav.key_group, "git")
        self.assertEqual([key for key, _, _ in nav.git_group_keys()], ["p", "r", "c", "i"])
        screen = Mock()
        screen.getmaxyx.return_value = (40, 120)
        nav.draw(screen)
        self.assertIn("Project history", [call.args[2] for call in screen.addstr.call_args_list])
        nav.key("f", None)
        self.assertEqual(nav.history_mode, "")
        self.assertIn("Unknown Git key", nav.message)
        nav.key("g", None)
        nav.key("p", None)
        self.assertEqual(nav.history_mode, "project")
        nav.key("g", None)
        self.assertEqual(nav.key_group, "")
        self.assertEqual(nav.history_selected, 0)
        self.assertEqual(nav.git_group_keys(), ())
        nav.key(curses.KEY_END, None)
        self.assertEqual(nav.history_selected, 2)
        nav.key("g", None)
        self.assertEqual(nav.history_selected, 0)
        self.assertEqual(nav.history_mode, "project")
        self.assertEqual(nav.key_group, "")
        nav.key("\x1b", None)
        nav.selected = next(i for i, row in enumerate(nav.items) if row.path == "new name.txt")
        nav.key("g", None)
        self.assertEqual([key for key, _, _ in nav.git_group_keys()], ["p", "f", "r", "c", "i", "d"])
        nav.key("f", None)
        self.assertEqual(nav.history_mode, "file")
        nav.key("g", None)
        self.assertEqual(nav.key_group, "")
        self.assertEqual(nav.history_mode, "file")

    def test_history_paging_and_saved_view(self):
        self.fixture()
        with patch.object(git_history, "PAGE_SIZE", 2):
            page, more = git_history.commits(self.root, path="new name.txt")
            self.assertEqual([entry.subject for entry in page], ["edit file", "rename file"])
            self.assertTrue(more)
            later, more = git_history.commits(self.root, offset=2, path="new name.txt")
            self.assertEqual([entry.path for entry in later], ["old name.txt"])
            self.assertFalse(more)
            nav = Navigator(self.root, "pane", False, "")
            nav.selected = 2
            nav.run_command("git.file-history", None)
            nav.key("j", None)
            nav.key("j", None)
            self.assertEqual(nav.history_selected, 2)
            state = nav.export_state()
            restored = Navigator(self.root, "pane", False, "", initial_state=state)
            self.assertEqual((restored.history_mode, restored.history_selected), ("file", 2))
            self.assertEqual(restored.history_commits[2].path, "old name.txt")
            screen = Mock()
            screen.getmaxyx.return_value = (30, 120)
            restored.draw(screen)
            labels = [call.args[2] for call in screen.addstr.call_args_list]
            self.assertTrue(any("HISTORY · new name.txt" in label for label in labels))
            self.assertTrue(any("+before" in label for label in labels))

    def test_unusual_file_names_in_history(self):
        for name in ("COMMIT", "\nleading.txt"):
            (self.root / name).write_text("content\n")
        self.commit("unusual names")
        for name in ("COMMIT", "\nleading.txt"):
            entries, more = git_history.commits(self.root, path=name)
            self.assertFalse(more)
            self.assertEqual(entries[0].path, name)
            self.assertIn("+content", git_history.patch(self.root, entries[0].oid,
                                                          next(item for item in git_history.changed_files(self.root, entries[0].oid)
                                                               if item.path == name)))

    def test_long_commit_message_can_scroll_before_file_list(self):
        (self.root / "file.txt").write_text("content\n")
        self.git("add", ".")
        self.git("commit", "-qm", "long message", "-m", "\n".join(f"line {i}" for i in range(30)))
        nav = Navigator(self.root, "pane", False, "")
        nav.run_command("git.history", None)
        nav.history_right_focus = True
        nav.body = 8
        nav.key(curses.KEY_NPAGE, None)
        self.assertEqual(nav.history_right_scroll, 8)
        screen = Mock()
        screen.getmaxyx.return_value = (15, 120)
        nav.draw(screen)
        self.assertEqual(nav.history_right_scroll, 8)
        nav.key("j", None)
        nav.draw(screen)
        self.assertGreater(nav.history_right_scroll, 8)


if __name__ == "__main__":
    unittest.main()
