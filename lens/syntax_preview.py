"""Highlight already-bounded source text with Pygments; never execute the file."""
from __future__ import annotations

from pathlib import Path

from markdown_preview import ESCAPES, Span, Style
from theme_colors import resolve as resolve_theme


MAX_TOKENS = 100_000


def token_style(token_type, colors):
    from pygments.token import Token, Keyword, Name, String, Number, Comment, Operator, Generic, Error

    tokens = {
        Keyword: "mauve", Name.Function: "blue", Name.Class: "yellow",
        Name.Namespace: "blue", Name.Decorator: "mauve", Name.Builtin: "teal",
        Name.Tag: "accent", Name.Attribute: "peach", String: "green", Number: "peach",
        Comment: "subtext0", Operator: "teal", Generic.Heading: "accent",
        Generic.Subheading: "accent", Generic.Deleted: "red", Generic.Inserted: "green",
        Error: "red", Token: "text",
    }
    matched = token_type
    while matched not in tokens:
        matched = matched.parent
    return Style(foreground=colors[tokens[matched]],
                 bold=token_type in Generic.Strong or token_type in Generic.Heading,
                 italic=token_type in Generic.Emph,
                 underline=token_type in Error)


def render(text: str, filename: str, colors=None):
    from pygments import lex
    from pygments.lexers import get_lexer_for_filename
    from pygments.lexers.special import TextLexer
    from pygments.util import ClassNotFound

    # Normalize display whitespace before tokenization so tabs crossing token
    # boundaries retain their columns, while terminal controls cannot be styled.
    text = ESCAPES.sub("", text).replace("\r\n", "\n").replace("\r", "\n").expandtabs(4)
    text = "".join(char for char in text if char.isprintable() or char == "\n")
    if not text:
        return None
    try:
        lexer = get_lexer_for_filename(Path(filename).name, text[:8192],
                                       stripnl=False, stripall=False, ensurenl=False)
    except ClassNotFound:
        return None
    if isinstance(lexer, TextLexer):
        return None
    colors = colors or resolve_theme()
    lines = [[]]
    styles = {}
    for count, (token, value) in enumerate(lex(text, lexer), 1):
        if count > MAX_TOKENS:
            raise ValueError("Syntax preview exceeded the token limit")
        if token not in styles:
            styles[token] = token_style(token, colors)
        style = styles[token]
        for offset, part in enumerate(value.split("\n")):
            if offset:
                lines.append([])
            if not part:
                continue
            if lines[-1] and lines[-1][-1].style == style:
                previous = lines[-1][-1]
                lines[-1][-1] = Span(previous.text + part, style)
            else:
                lines[-1].append(Span(part, style))
    if text.endswith("\n") and len(lines) > 1 and not lines[-1]:
        lines.pop()
    return lexer.name, lines
