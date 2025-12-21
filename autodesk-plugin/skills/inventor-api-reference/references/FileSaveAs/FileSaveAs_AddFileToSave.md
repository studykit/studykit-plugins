# FileSaveAs.AddFileToSave Method

Parent Object: [FileSaveAs](../FileSaveAs/FileSaveAs.md)

## Description

Adds a document, taken from within this tree, to the set of documents to be saved. Please note: Saving of files in Apprentice is not allowed on files that require migration (any file that has not already been migrated to the same version of the Apprentice server). The current document's NeedsMigrating property must return False before the FileSaveAs object can successfully be returned.

## Syntax

FileSaveAs.**AddFileToSave**( ***Document*** As Unknown, ***TargetFileName*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Document | Unknown | Input object that specifies the to be saved. |
| TargetFileName | String | Input String that specifies the name of the file to be saved. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |