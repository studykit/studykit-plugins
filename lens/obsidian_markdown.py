"""Obsidian preview tokens; no link following or execution. Embeds are resolved by
obsidian_embeds; these rules only parse them."""
from __future__ import annotations

import re


WIKILINK = re.compile(r"!?\[\[([^\[\]\n]+)\]\]")
CALLOUT = re.compile(r"^\[!([\w-]+)\][+-]?(?:[ \t]+(.*))?$")
TASK = re.compile(r"^\[([ xX])\](?:[ \t]+|$)")


def wikilink(state, silent):
    match = WIKILINK.match(state.src, state.pos, state.posMax)
    if not match:
        return False
    target, _, alias = match[1].replace(r"\|", "|").partition("|")
    target, alias = target.strip(), alias.strip()
    if not target:
        return False
    if not silent:
        embedded = match[0].startswith("!")
        token = state.push("obsidian_embed" if embedded else "wikilink",
                           "embed" if embedded else "wikilink", 0)
        token.meta = {"target": target, "alias": alias}
        if embedded:
            if re.fullmatch(r"\d+(?:x\d+)?", alias):
                label = f"{target} · {alias}"
            else:
                label = f"{alias} — {target}" if alias else target
            token.content = f"[Embed: {label}]"
        else:
            token.content = alias or target
    state.pos = match.end()
    return True


def highlight(state, silent):
    # Use markdown-it's delimiter pairing, so escaped markers, inline code,
    # emphasis, and links retain their normal boundaries inside highlights.
    from markdown_it.rules_inline.state_inline import Delimiter

    if silent or state.src[state.pos] != "=":
        return False
    scanned = state.scanDelims(state.pos, True)
    token = state.push("text", "", 0)
    token.content = "=" * scanned.length
    if scanned.length == 2:
        state.delimiters.append(Delimiter(
            marker=ord("="), length=0, token=len(state.tokens) - 1, end=-1,
            open=scanned.can_open, close=scanned.can_close,
        ))
    state.pos += scanned.length
    return True


def pair_highlights(state):
    groups = [state.delimiters]
    groups.extend(meta["delimiters"] for meta in state.tokens_meta
                  if meta and "delimiters" in meta)
    for delimiters in groups:
        for opener in delimiters:
            if opener.marker != ord("=") or opener.end == -1:
                continue
            closer = delimiters[opener.end]
            for index, nesting, kind in ((opener.token, 1, "mark_open"),
                                         (closer.token, -1, "mark_close")):
                token = state.tokens[index]
                token.type, token.tag, token.nesting = kind, "mark", nesting
                token.content = ""


def frontmatter(state, start_line, end_line, silent):
    if start_line != 0 or state.parentType != "root" or state.tShift[0] != 0:
        return False
    if state.src[state.bMarks[0]:state.eMarks[0]].strip() != "---":
        return False
    for closing in range(1, end_line):
        line = state.src[state.bMarks[closing]:state.eMarks[closing]]
        if line.rstrip() in ("---", "..."):
            if not silent:
                token = state.push("frontmatter", "pre", 0)
                token.content = state.getLines(1, closing, 0, False)
                token.map = [0, closing + 1]
                state.line = closing + 1
            return True
    return False


def blocks(state):
    from markdown_it.token import Token

    result = []
    quote_stack = []
    i = 0
    while i < len(state.tokens):
        token = state.tokens[i]
        if token.type == "blockquote_open":
            first = state.tokens[i + 1:i + 4]
            match = None
            if [item.type for item in first] == ["paragraph_open", "inline", "paragraph_close"]:
                heading, _, body = first[1].content.partition("\n")
                match = CALLOUT.fullmatch(heading)
            quote_stack.append(bool(match))
            if match:
                kind = match[1].lower()
                token.type, token.tag = "callout_open", "aside"
                token.meta = {"kind": kind}
                title_open = Token("callout_title_open", "p", 1)
                title_open.meta = {"kind": kind}
                title = Token("inline", "", 0)
                title.content = kind.upper()
                if match[2]:
                    title.content += " · " + match[2]
                result.extend((token, title_open, title, Token("callout_title_close", "p", -1)))
                if body:
                    first[1].content = body
                    result.extend(first)
                i += 4
                continue
        elif token.type == "blockquote_close":
            if quote_stack.pop():
                token.type, token.tag = "callout_close", "aside"
        result.append(token)
        i += 1
    state.tokens = result


def tasks(state):
    from markdown_it.token import Token

    for index, token in enumerate(state.tokens):
        if token.type != "inline" or index < 2 or not token.children:
            continue
        if [item.type for item in state.tokens[index - 2:index]] != ["list_item_open", "paragraph_open"]:
            continue
        match = TASK.match(token.content)
        first = token.children[0]
        if not match or first.type != "text" or not first.content.startswith(match[0]):
            continue
        checked = match[1].lower() == "x"
        box = Token("checkbox", "checked" if checked else "unchecked", 0)
        box.content = "☑ " if checked else "☐ "
        first.content = first.content[len(match[0]):]
        token.children.insert(0, box)


def install(parser):
    parser.inline.ruler.before("image", "obsidian_wikilink", wikilink)
    parser.inline.ruler.before("emphasis", "obsidian_highlight", highlight)
    parser.inline.ruler2.after("balance_pairs", "obsidian_highlight", pair_highlights)
    parser.block.ruler.before("hr", "obsidian_frontmatter", frontmatter)
    parser.core.ruler.before("inline", "obsidian_callouts", blocks)
    parser.core.ruler.after("inline", "obsidian_tasks", tasks)


def markdown_type():
    """Keep Rich optional until preview rendering is requested."""
    from rich.markdown import BlockQuote, CodeBlock, Markdown, MarkdownElement, Paragraph
    from rich.panel import Panel
    from rich.text import Text

    class Callout(BlockQuote):
        style_name = "markdown.paragraph"

        @classmethod
        def create(cls, markdown, token):
            element = cls()
            element.kind = token.meta["kind"]
            return element

        def __rich_console__(self, console, options):
            yield Panel(self.elements, padding=(0, 1),
                        border_style=console.get_style(f"markdown.callout.{self.kind}",
                                                       default="markdown.callout.note"))

    class CalloutTitle(Paragraph):
        @classmethod
        def create(cls, markdown, token):
            element = cls(justify="left")
            element.kind = token.meta["kind"]
            return element

        def on_enter(self, context):
            super().on_enter(context)
            self.text.style = context.console.get_style(
                f"markdown.callout.{self.kind}", default="markdown.callout.note")

    class EmbeddedNote(BlockQuote):
        style_name = "markdown.paragraph"

        @classmethod
        def create(cls, markdown, token):
            element = cls()
            element.title = token.meta["title"]
            return element

        def __rich_console__(self, console, options):
            yield Panel(self.elements, title=Text(self.title, style="markdown.embed"),
                        title_align="left", padding=(0, 1), border_style="markdown.hr")

    class EmbeddedImage(MarkdownElement):
        # Drawn only until the image is ready, or where images cannot be shown.
        @classmethod
        def create(cls, markdown, token):
            element = cls()
            element.label = token.content
            return element

        def __rich_console__(self, console, options):
            yield Text(self.label, style="markdown.embed")

    class Properties(CodeBlock):
        @classmethod
        def create(cls, markdown, token):
            return cls("yaml", markdown.code_theme)

        def __rich_console__(self, console, options):
            from rich.syntax import Syntax

            yield Panel(Syntax(str(self.text), "yaml", theme=self.theme, word_wrap=True),
                        title="Properties", title_align="left", padding=(0, 1),
                        border_style="markdown.hr")

    class ObsidianMarkdown(Markdown):
        inlines = Markdown.inlines | {"wikilink", "embed", "mark", "checked", "unchecked", "link", "link_url"}
        elements = {**Markdown.elements, "callout_open": Callout,
                    "callout_title_open": CalloutTitle, "frontmatter": Properties,
                    "obsidian_note_open": EmbeddedNote, "obsidian_image": EmbeddedImage}

    return ObsidianMarkdown
