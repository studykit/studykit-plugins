# Document.Save2 Method

Parent Object: [Document](../Document/Document.md)

## Description

Method that saves the document and the specified dependent documents.

## Remarks

If the document has never been saved, calling this method prompts the user for a file name just like the Save method. Calling Document.Save2 without specifying any arguments results in the dirty dependents getting saved. The "Save Dependents" dialog is not displayed (the Save method does display the dialog).

## Syntax

Document.**Save2**( [***SaveDependents***] As Boolean, [***DocumentsToSave***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SaveDependents | Boolean | Optional input Boolean that specifies whether or not to save dependent documents that have been dirtied. Defaults to True indicating that the dependents will be saved. If the DependentsToSave argument is not specified, all dirty dependents are saved. If the argument is specified as False, only this document will be saved. The argument is ignored if the document doesn't have any dependents needing save. |
| DocumentsToSave | Variant | Optional input ObjectCollection that contains the Document objects to save. Use the Document.AllReferencedDocuments property to iterate over all dependent documents and find the ones that need to be saved (i.e. Dirty property returns True). If the SaveDependents argument is True and this argument is not specified, all dirty documents are saved. The argument is ignored if the document doesn't have any dependents needing save.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010
