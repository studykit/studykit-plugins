## filesystem issue writes

The configured issue provider is `filesystem`. Workflow issues are local
Markdown artifacts edited directly at the paths the authoring resolver
returns. There is no provider-backed publish, comment, update, or
relationship script.

## Flow

1. Read and edit the resolver-returned files directly in the working
   tree.
2. Commit the changes through normal version control.

There is no body-file temp flow and no cache freshness check on the
filesystem path. Do not call provider issue scripts on this project.
