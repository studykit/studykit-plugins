## github knowledge

Knowledge documents live as repository Markdown files under `wiki/`.

1. Choose the target file before requesting authoring paths.
2. Resolve the authoring paths with
   `"$WORKFLOW" authoring_resolver.py --type <type> --role knowledge --json`
   (see `../authoring.md`).
3. Read the returned files.
4. Edit the target file directly in the working tree.

There is no provider-backed knowledge write script; the file is the source
of truth. Commit the changes through normal version control.
