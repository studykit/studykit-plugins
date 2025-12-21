# FileSaveAs Object

## Description

Custom interface to access management information about a particular file version.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddFileToSave](../FileSaveAs/FileSaveAs_AddFileToSave.md) | Adds a document, taken from within this tree, to the set of documents to be saved. Please note: Saving of files in Apprentice is not allowed on files that require migration (any file that has not already been migrated to the same version of the Apprentice server). The current document's NeedsMigrating property must return False before the FileSaveAs object can successfully be returned. |
| [ExecuteSave](../FileSaveAs/FileSaveAs_ExecuteSave.md) | Executes the Save operation on each of the documents specified via the AddFileToSave method. |
| [ExecuteSaveAs](../FileSaveAs/FileSaveAs_ExecuteSaveAs.md) | Executes the Save As operation on each of the documents specified via the AddFileToSave method. |
| [ExecuteSaveCopyAs](../FileSaveAs/FileSaveAs_ExecuteSaveCopyAs.md) | Executes the Save Copy As operation on each of the documents specified via the AddFileToSave method. |

## Accessed From

[ApprenticeServer.FileSaveAs](../ApprenticeServer/ApprenticeServer_FileSaveAs.md), [ApprenticeServerComponent.FileSaveAs](../ApprenticeServerComponent/ApprenticeServerComponent_FileSaveAs.md)

## Version

Introduced in version 4
