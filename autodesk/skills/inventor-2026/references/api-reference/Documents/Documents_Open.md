# Documents.Open Method

Parent Object: [Documents](../Documents/Documents.md)

## Description

Method that opens the specified Inventor document.

## Remarks

Programmatic changes to the "Defer Updates" setting made through the kDrawingDeferUpdateDesignTrackingProperties iProperty of a drawing document opened in Autodesk Inventor will not affect the open drawing document and will be overwritten upon save of that document. However, changes to the "Defer Updates" setting made through the DrawingSettings.DeferUpdates property of the API, or through the Autodesk Inventor Document Settings dialog, will be honored for the open drawing document. When opening non-Inventor DWG files, this method honors the application option to decide between open and import.

## Syntax

Documents.**Open**( ***FullDocumentName*** As String, [***OpenVisible***] As Boolean ) As [Document](../Document/Document.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullDocumentName | String | Input String that specifies the full document name of the document to open. If only the FullFileName is specified for part and assembly documents, the master document within the file is opened. |
| OpenVisible | Boolean | Optional input Boolean that specifies whether to open the document as visible. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |
| [Adding iPart occurrences to an assembly](../../sample-programs/AddiPartMember_Sample.md) | This sample demonstrates adding iPart occurrences to an assembly. |
| [Create a Configuration Table](../../sample-programs/CustomTables_AddConfigurationTable_Sample.md) | This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document. |
| [Adding Representation views](../../sample-programs/DrawingViews_AddBaseView_Sample.md) | This sample demonstrates how to create a base view by specifying various representations. |
| [Create flat pattern drawing view](../../sample-programs/DrawingViews_AddBaseView2_Sample.md) | This sample demonstrates the creation of a flat pattern base view in a drawing. |
| [Create base view with representations](../../sample-programs/DrawingViews_AddBaseView3_Sample.md) | This sample demonstrates how to create a base view by specifying various representations. |
| [Open assembly using last model state](../../sample-programs/GetLastActiveModelState_Sample.md) | This sample demonstrates how to open an assembly document in its last active model state. |
| [Create sheet with multiple views](../../sample-programs/SheetFormat_Sample.md) | This sample demonstrates the creation of a drawing sheet based on a particular sheet format containing the definition for multiple views. |
| [Copying a title block definition](../../sample-programs/TitleBlockDefinition_CopyTo_Sample.md) | This sample demonstrates copying a title block definition from one drawing to another and replacing the existing title blocks in the drawing with the new title block. |

## Version

Introduced in version 4
