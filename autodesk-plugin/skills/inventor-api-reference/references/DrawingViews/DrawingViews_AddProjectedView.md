# DrawingViews.AddProjectedView Method

Parent Object: [DrawingViews](../DrawingViews/DrawingViews.md)

## Description

Method that creates a projected .

## Syntax

DrawingViews.**AddProjectedView**( ***ParentView*** As [DrawingView](../DrawingView/DrawingView.md), ***Position*** As [Point2d](../Point2d/Point2d.md), ***ViewStyle*** As [DrawingViewStyleEnum](../DrawingViewStyleEnum.md), [***Scale***] As Variant ) As [DrawingView](../DrawingView/DrawingView.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentView | [DrawingView](../DrawingView/DrawingView.md) | Input object that specifies the base parent view of the projected view. |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the placement point of the view on the sheet. |
| ViewStyle | [DrawingViewStyleEnum](../DrawingViewStyleEnum.md) | Input DrawingViewStyleEnum the specifies the display style of the geometry within the view. |
| Scale | Variant | Optional input Variant that specifies the drawing view scale factor. If this argument is not specified, the scale is derived from the ParentView. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |