# Markdown footnotes (extended syntax)

Source: <https://www.markdownguide.org/extended-syntax/#footnotes>. Fetched 2026-08-13.

Saved because guard's `refs_format: footnote` injects this syntax into the session, so
the shipped text must rest on an inspectable copy rather than recollection.

## Reference syntax

> Add a caret and an identifier inside brackets (`[^1]`)

## Definition syntax

> Add the footnote using another caret and number inside brackets with a colon and text
> (`[^1]: My footnote.`)

## Identifiers are NOT required to be numbers

> Identifiers can be numbers or words, but they can't contain spaces or tabs.

Word-label example from the guide:

```
[^bignote]

[^bignote]: Here's one with multiple paragraphs and code.
```

## The label does not control the displayed number

> Identifiers only correlate the footnote reference with the footnote itself — in the
> output, footnotes are numbered sequentially.

So a word label is purely an authoring convenience: the renderer numbers footnotes 1, 2,
3 by order of appearance regardless of the label used. Choosing `[^judge]` over `[^3]`
costs the reader nothing in the rendered output and removes the need to renumber when
the prose is edited.

## Placement limits

Footnotes need not sit at the end of the document, but they cannot be placed inside
lists, blockquotes, or tables.
