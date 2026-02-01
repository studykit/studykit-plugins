# DrawingDocument.ProcessViewSelection Method

Parent Object: [DrawingDocument](../DrawingDocument/DrawingDocument.md)

## Description

Process object selection according to the context of the document referenced by the containing view.

## Syntax

DrawingDocument.**ProcessViewSelection**( ***Selection*** As [GenericObject](../GenericObject/GenericObject.md), ***ContainingView*** As [DrawingView](../DrawingView/DrawingView.md), ***SelectedObject*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Selection | [GenericObject](../GenericObject/GenericObject.md) | Input GenericObject obtained from the SelectSet.Item property. |
| ContainingView | [DrawingView](../DrawingView/DrawingView.md) | Output DrawingView object that returns the drawing view in the context of which the selection was made. |
| SelectedObject | Object | Output GenericObject that returns the object in the context of the document referenced by the containing view. |

## Version

Introduced in version 10
