from pathlib import Path
import curses
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import command_line
from core import application_command, opener_command
from ui import Navigator


class OpenerCommandTests(unittest.TestCase):
    def test_platform_defaults_and_configured_placeholder(self):
        path = Path("/tmp/a b.txt")
        with patch("core.shutil.which", return_value="/bin/x"):
            self.assertEqual(opener_command("", path, "darwin"), ["open", str(path)])
            self.assertEqual(opener_command("", path, "linux"), ["xdg-open", str(path)])
            self.assertEqual(opener_command("open -a Finder", path), ["open", "-a", "Finder", str(path)])
            self.assertEqual(opener_command("code {file} -n", path), ["code", str(path), "-n"])
        with patch("core.shutil.which", return_value=None), self.assertRaises(ValueError):
            opener_command("", path, "linux")

    def test_application_command_per_platform(self):
        path = Path("/tmp/a.txt")
        self.assertEqual(application_command("Visual Studio Code", path, "darwin"),
                         ["open", "-a", "Visual Studio Code", str(path)])
        with patch("core.shutil.which", return_value="/bin/x"):
            self.assertEqual(application_command("code -n", path, "linux"), ["code", "-n", str(path)])
        with patch("core.shutil.which", return_value=None), self.assertRaises(ValueError):
            application_command("nope", path, "linux")


class LaunchTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        (self.root / "docs").mkdir()
        (self.root / "docs" / "guide.pdf").write_text("pdf")
        self.nav = Navigator(self.root, "pane", False, "")
        self.nav.body = 10
        self.nav.opener = "true"

    def launched(self, *keys):
        with patch("ui.subprocess.Popen", wraps=__import__("subprocess").Popen) as popen:
            for key in keys:
                self.nav.key(key, None)
        return [call.args[0][-1] for call in popen.call_args_list]

    def test_o_opens_the_selected_folder_or_the_previewed_file(self):
        index = next(i for i, row in enumerate(self.nav.items) if row.path == "docs")
        self.nav.selected = index
        self.assertEqual(self.launched("o"), [str(self.root / "docs")])
        self.assertEqual(self.nav.message, "Opened docs")
        self.nav.expanded.add("docs")
        self.nav.rebuild()
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "docs/guide.pdf")
        self.nav.activate()
        self.assertTrue(self.nav.preview_focus)
        self.assertEqual(self.launched("o"), [str(self.root / "docs" / "guide.pdf")])

    def test_command_takes_a_path_and_reports_failures(self):
        self.assertEqual(self.launched(*":launch docs\n"), [str(self.root / "docs")])
        self.launched(*":launch missing\n")
        self.assertIn("No such file", self.nav.message)
        self.nav.opener = "false"
        self.launched(*":xdg-open docs\n")
        self.assertIn("status 1", self.nav.message)

    def test_shift_o_lists_applications_and_filters_them(self):
        apps = ["Preview", "TextEdit", "Visual Studio Code"]
        with patch("command_line.applications", return_value=apps):
            self.nav.key("O", None)
        self.assertEqual(self.nav.app_choices(), apps)
        for key in "t":
            self.nav.key(key, None)
        # "t" starts TextEdit and appears inside "Visual Studio Code"; prefixes come first.
        self.assertEqual(self.nav.app_choices(), ["TextEdit", "Visual Studio Code"])
        self.nav.key(curses.KEY_DOWN, None)
        with patch("ui.application_command", return_value=["true"]) as build:
            self.nav.key("\n", None)
        self.assertIsNone(self.nav.app_picker)
        self.assertEqual(build.call_args.args[0], "Visual Studio Code")
        self.assertIn("with Visual Studio Code", self.nav.message)
        with patch("command_line.applications", return_value=apps):
            self.launched(*":with\n")
        self.assertEqual(self.nav.app_choices()[0], "Visual Studio Code")  # Recent first.
        self.nav.key("\x1b", None)
        self.assertIsNone(self.nav.app_picker)

    def test_typed_name_without_a_match_is_used_as_is(self):
        with patch("command_line.applications", return_value=[]):
            self.nav.key("O", None)
        for key in "mytool":
            self.nav.key(key, None)
        with patch("ui.application_command", return_value=["true"]) as build:
            self.nav.key("\n", None)
        self.assertEqual(build.call_args.args[0], "mytool")

if __name__ == "__main__":
    unittest.main()
