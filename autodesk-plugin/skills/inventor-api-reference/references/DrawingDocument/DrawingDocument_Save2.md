# DrawingDocument.Save2 Method

Parent Object: [DrawingDocument](../DrawingDocument/DrawingDocument.md)

## Description

Method that saves the document and the specified dependent documents.

## Syntax

DrawingDocument.**Save2**( [***SaveDependents***] As Boolean, [***DocumentsToSave***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SaveDependents | Boolean | Optional input Boolean that specifies whether or not to save dependent documents that have been dirtied. Defaults to True indicating that the dependents will be saved. If the DependentsToSave argument is not specified, all dirty dependents are saved. If the argument is specified as False, only this document will be saved. The argument is ignored if the document doesn't have any dependents needing save. |
| DocumentsToSave | Variant | Optional input ObjectCollection that contains the Document objects to save. Use the Document.AllReferencedDocuments property to iterate over all dependent documents and find the ones that need to be saved (i.e. Dirty property returns True). If the SaveDependents argument is True and this argument is not specified, all dirty documents are saved. The argument is ignored if the document doesn't have any dependents needing save.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |