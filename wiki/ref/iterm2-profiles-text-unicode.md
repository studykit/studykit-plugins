# iTerm2 — Preferences › Profiles › Text (Unicode & font settings)

Source: <https://iterm2.com/documentation-preferences-profiles-text.html>
Retrieved: 2026-08-26

Quoted from the page. Nothing here is paraphrase; where the page is silent, this file says so
rather than filling the gap.

## Normalization

> This affects how text is processed on input. Most users will want no normalization. HFS+
> normalization preserves the fullwidth attribute of composed characters.

The page documents the setting's effect but does not publish a mapping from the stored value
to a normalization form. Do not assume which value means none / NFC / NFD / HFS+ without
checking the UI popup.

## Non-ASCII font

> All non-ASCII text (many accented Latin letters, non-Latin text, less-common symbols, and
> thousands of miscellaneous unicode characters) will be drawn with this font.

The page presents this as the effect of the setting when it is in use. It does not state, on
this page, what is used instead when the accompanying "use a different font for non-ASCII
text" checkbox is off.

## Ambiguous-width characters

> Some characters (e.g., Chinese ideograms) are double-width, and take two cells to display.
> Other characters (e.g., Latin letters) are single width and take only one cell to display.

## Unicode version 9+

> Unicode version 9 offers better formatting for Emoji. If your applications have been
> updated to use these tables, you should enable this setting.
