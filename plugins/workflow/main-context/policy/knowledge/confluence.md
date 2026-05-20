## confluence knowledge

Confluence knowledge documents are provider-backed pages. Workflow scripts
do not currently support Confluence knowledge writes. Resolve authoring
paths for read-time guidance with
`"$WORKFLOW" authoring_resolver.py --type <type> --role knowledge --json`
(see `../authoring.md`), but report the write limitation to the user
rather than attempting a provider write.

Do not use GitHub `wiki/` paths for this project.
