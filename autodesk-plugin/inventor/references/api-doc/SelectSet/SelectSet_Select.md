# SelectSet.Select Method

Parent Object: [SelectSet](../SelectSet/SelectSet.md)

## Description

Method that adds an entity to the select set.

## Syntax

SelectSet.**Select**( ***Entity*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | Input Autodesk Inventor object that is valid to be selected. This method will fail in the case where an unselectable object is provided. For example, you can't select a Document or Matrix object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |
| [Copy a sketch](../../sample-programs/CopySketch_Sample.md) | This sample demonstrates copying the contents of a sketch into another sketch via the API. |
| [Break alignment of a section view](../../sample-programs/SectionDrawingView_Sample.md) | Sample showing how to break the alignment of a drawing section view by calling the DrawingBreakViewAlignment command. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |