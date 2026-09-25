from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import markdown_preview as md
import obsidian_embeds as embeds


OTHER = """---
tags: x
---
# Other

Intro text.

## Section A

Alpha line.

```md
## Not a heading
```

### Deeper

Still A.

## Section B

Beta paragraph
continues here ^para

- item one
- item two ^item

- l1
- l2

^list
"""


class EmbedTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.outer = Path(temp.name)
        self.root = self.outer / "vault"
        for folder in (".obsidian", "notes/deep", "assets", ".trash"):
            (self.root / folder).mkdir(parents=True)
        (self.root / "notes" / "Other.md").write_text(OTHER)
        (self.root / "notes" / "deep" / "Other.md").write_text("# Deeper other\n")
        (self.root / ".trash" / "Gone.md").write_text("# Gone\n")
        (self.root / "assets" / "pic.png").write_bytes(b"\x89PNG\r\n\x1a\n")
        (self.outer / "Secret.md").write_text("# Secret\n")
        self.main = self.root / "Main.md"
        self.vault = embeds.Vault(embeds.vault_root(self.main, self.outer), self.main)

    def lines(self, source, width=60):
        self.main.write_text(source)
        return ["".join(span.text for span in line).rstrip() for line in md.render(source, width, vault=self.vault)]

    def test_vault_root_is_the_folder_holding_obsidian_settings(self):
        self.assertEqual(self.vault.root, self.root.resolve())
        (self.outer / "plain").mkdir()
        self.assertEqual(embeds.vault_root(self.outer / "plain" / "a.md", self.outer), self.outer.resolve())

    def test_targets_resolve_by_path_then_by_name_nearest_the_root(self):
        self.assertEqual(self.vault.find("Other"), (self.root / "notes" / "Other.md").resolve())
        self.assertEqual(self.vault.find("deep/Other"), (self.root / "notes" / "deep" / "Other.md").resolve())
        self.assertEqual(self.vault.find("notes/Other.md"), (self.root / "notes" / "Other.md").resolve())
        self.assertEqual(self.vault.find("PIC.png"), (self.root / "assets" / "pic.png").resolve())
        for missing in ("Gone", "../Secret", "/../Secret", "Nothing", ""):
            self.assertIsNone(self.vault.find(missing), missing)

    def test_whole_notes_headings_and_blocks(self):
        text = "\n".join(self.lines("![[Other]]"))
        self.assertIn("╭─ Other", text)
        self.assertIn("Intro text.", text)
        self.assertNotIn("tags: x", text)  # Frontmatter stays out of an embed.
        self.assertNotIn("^para", text)
        self.assertNotIn("^list", text)
        section = "\n".join(self.lines("![[Other#section a]]"))
        self.assertIn("Alpha line.", section)
        self.assertIn("Not a heading", section)  # A fenced ## does not end the section.
        self.assertIn("Still A.", section)  # Deeper headings belong to it.
        self.assertNotIn("Beta", section)
        self.assertIn("Beta paragraph continues here", "\n".join(self.lines("![[Other#Other#Section B]]")))
        block = "\n".join(self.lines("![[Other#^para]]"))
        self.assertIn("Beta paragraph continues here", block)
        self.assertNotIn("Section B", block)
        item = "\n".join(self.lines("![[Other#^item]]"))
        self.assertIn("item two", item)
        self.assertNotIn("item one", item)
        listed = "\n".join(self.lines("![[Other#^list]]"))
        self.assertIn("l1", listed)
        self.assertIn("l2", listed)
        self.assertNotIn("item two", listed)

    def test_aliases_title_the_panel_and_several_embeds_stack(self):
        text = "\n".join(self.lines("![[Other#^item|The item]]\n![[Other#^para]]"))
        self.assertIn("╭─ The item", text)
        self.assertIn("╭─ Other#^para", text)

    def test_inline_missing_and_unsupported_embeds_keep_placeholders(self):
        (self.root / "doc.pdf").write_bytes(b"%PDF")
        text = self.lines("See ![[Other]] here.\n\n![[Nothing]]\n\n![[doc.pdf]]\n\n![[Other#Missing]]")
        self.assertIn("See [Embed: Other] here.", text)
        self.assertIn("[Embed: Nothing]", text)
        self.assertIn("[Embed: doc.pdf]", text)
        self.assertIn("[Embed: Other#Missing]", text)

    def test_cycles_stop_at_the_repeated_note(self):
        (self.root / "A.md").write_text("A body\n\n![[B]]\n")
        (self.root / "B.md").write_text("B body\n\n![[A]]\n")
        text = "\n".join(self.lines("![[A]]", 80))
        self.assertEqual(text.count("A body"), 1)
        self.assertEqual(text.count("B body"), 1)
        self.assertIn("[Embed: A]", text)

    def test_images_become_diagram_keys_with_their_size(self):
        self.main.write_text("![[pic.png|120x80]]\n\n![[pic.png]]")
        keys = md.diagram_blocks(self.main.read_text(), self.vault)
        path = str((self.root / "assets" / "pic.png").resolve())
        self.assertEqual([key[1].split("\n")[:3] for key in keys], [[path, "120", "80"], [path, "0", "0"]])
        self.assertEqual({key[0] for key in keys}, {"image"})
        # Until the image is drawn, or where images cannot be shown, the label stays.
        self.assertIn("[Embed: pic.png · 120x80]", self.lines(self.main.read_text()))

    def test_block_ids_are_hidden_without_a_vault(self):
        lines = ["".join(span.text for span in line).rstrip() for line in md.render("Text ^abc\n\n^def\n\nNext", 40)]
        self.assertEqual([line for line in lines if line], ["Text", "Next"])


if __name__ == "__main__":
    unittest.main()
