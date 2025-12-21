# FileManager.GetFullDocumentName Method

Parent Object: [FileManager](../FileManager/FileManager.md)

## Description

Returns the full document name which is a unique identifier for an open Document. The returned string is the full file name concatenated with the model state name for a part or assembly document.

## Syntax

FileManager.**GetFullDocumentName**( ***FullFileName*** As String, [***ModelStateName***] As String ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String that specifies the Inventor file on disk. |
| ModelStateName | String | Optional input String that specifies the name of the model state within the file. This argument is ignored for presentation and drawing documents. If an assembly or partt document has multiple model states and this argument is not specified, the full document name of the primary document is returned. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding Representation views](../../sample-programs/DrawingViews_AddBaseView_Sample.md) | This sample demonstrates how to create a base view by specifying various representations. |
| [Create flat pattern drawing view](../../sample-programs/DrawingViews_AddBaseView2_Sample.md) | This sample demonstrates the creation of a flat pattern base view in a drawing. |
| [Create base view with representations](../../sample-programs/DrawingViews_AddBaseView3_Sample.md) | This sample demonstrates how to create a base view by specifying various representations. |
| [Open assembly using last model state](../../sample-programs/GetLastActiveModelState_Sample.md) | This sample demonstrates how to open an assembly document in its last active model state. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |