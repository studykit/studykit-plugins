import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import herdr_main
from ui import Navigator


class ToggleKeyTests(unittest.TestCase):
    def config(self, text):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        path = Path(temp.name) / "config.toml"
        path.write_text(text)
        return {"HERDR_CONFIG_PATH": str(path), "HERDR_PLUGIN_ID": "studykit.lens"}

    def test_toggle_bindings_accept_modified_punctuation_and_expand_the_prefix(self):
        env = self.config('''[keys]
prefix = "ctrl+s"
[[keys.command]]
key = "prefix+d"
command = "studykit.lens.changes"
[[keys.command]]
key = "ctrl+;"
command = "studykit.lens.toggle"
[[keys.command]]
key = "l"
command = "studykit.lens.toggle"
''')
        # The bare "l" binding is dropped: it would close Lens mid-search.
        self.assertEqual(herdr_main.toggle_keys(env), [("ctrl+;",)])
        self.assertEqual(herdr_main.toggle_keys(self.config('[[keys.command]]\nkey = "prefix+a"\n'
                                                            'command = "studykit.lens.toggle"\n')),
                         [("\x02", "a")])  # Herdr's default prefix is Ctrl+B.

    def test_navigator_closes_on_the_sequence_only(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        nav = Navigator(Path(temp.name), "pane", False, "", close_keys=[("\x13", "\x01")])
        self.assertTrue(nav.key("\x13", None))
        self.assertTrue(nav.key("j", None))  # Not the binding: the key still works.
        self.assertEqual(nav.close_typed, ())
        self.assertTrue(nav.key("\x13", None))
        self.assertFalse(nav.key("\x01", None))

    def test_direct_modified_punctuation_closes_popup(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        nav = Navigator(Path(temp.name), "pane", False, "", close_keys=[("ctrl+;",)])
        self.assertFalse(nav.key("ctrl+;", None))


class ToggleActionTests(unittest.TestCase):
    def test_toggle_closes_a_focused_navigator(self):
        env = {"HERDR_ENV": "1", "HERDR_PLUGIN_ID": "studykit.lens",
               "HERDR_PLUGIN_CONTEXT_JSON": json.dumps({"focused_pane_id": "w:p2", "tab_id": "w:t"})}
        replies = {"focus": {"plugin_pane": {"plugin_id": "studykit.lens", "entrypoint": "navigator"}},
                   "close": {}}
        with patch("herdr_main.call", side_effect=lambda env, method, /, **params: replies[method.split(".")[-1]]) as call:
            self.assertEqual(herdr_main.main(env, "toggle"), 0)
        self.assertEqual(call.call_args.args[1:], ("plugin.pane.close",))
        self.assertEqual(call.call_args.kwargs, {"pane_id": "w:p2"})

    def test_toggle_opens_when_no_navigator_is_open(self):
        env = {"HERDR_ENV": "1", "HERDR_PLUGIN_ID": "studykit.lens",
               "HERDR_PLUGIN_CONTEXT_JSON": json.dumps({"focused_pane_id": "w:p1", "tab_id": "w:t"})}
        with patch("herdr_main.call", side_effect=RuntimeError("plugin_pane_not_found")), \
                patch("herdr_main.source", return_value=("w:p1", Path("/tmp"))), \
                patch("herdr_main.open_panel") as open_panel:
            self.assertEqual(herdr_main.main(env, "toggle"), 0)
        self.assertEqual(open_panel.call_args.args[1], "w:p1")


if __name__ == "__main__":
    unittest.main()
