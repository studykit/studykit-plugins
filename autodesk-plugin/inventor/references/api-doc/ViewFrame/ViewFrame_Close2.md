# ViewFrame.Close2 Method

Parent Object: [ViewFrame](../ViewFrame/ViewFrame.md)

## Description

Method that closes this view frame. Close a ViewFrame may cause documents to close, use the argument to specify the documents to save if necessary. This does nothing if try to close the default ViewFrame.

## Syntax

ViewFrame.**Close2**( [***SaveDocuments***] As Boolean, [***DocumentsToSave***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SaveDocuments | Boolean | Optional input Boolean value to specify whether to save the documents. |
| DocumentsToSave | Variant | Optional input ObjectCollection including the documents to save. This is ignored if the SaveDocuments is specified as False. If the SaveDocuments is set to True and this is not specified then all the documents being closed in this ViewFrame will be saved.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |