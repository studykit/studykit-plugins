## filesystem knowledge

Knowledge documents are local repository files at paths the authoring
resolver returns.

1. Resolve the authoring paths with
   `"$WORKFLOW" authoring_resolver.py --type <type> --role knowledge --json`
   (see `../authoring.md`).
2. Read and edit the returned files directly in the working tree.
3. Commit through normal version control.

Do not call `wiki/` or Confluence provider commands on this project.
