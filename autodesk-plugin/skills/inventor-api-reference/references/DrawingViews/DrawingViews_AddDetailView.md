# DrawingViews.AddDetailView Method

Parent Object: [DrawingViews](../DrawingViews/DrawingViews.md)

## Description

Method that creates a detail drawing view. This method fails if the parent sheet is not active.

## Syntax

DrawingViews.**AddDetailView**( ***ParentView*** As [DrawingView](../DrawingView/DrawingView.md), ***Position*** As [Point2d](../Point2d/Point2d.md), ***ViewStyle*** As [DrawingViewStyleEnum](../DrawingViewStyleEnum.md), ***CircularFence*** As Boolean, ***FenceCenterOrCornerOne*** As [Point2d](../Point2d/Point2d.md), ***FenceRadiusOrCornerTwo*** As Variant, [***AttachPoint***] As Variant, [***Scale***] As Variant, [***ShowLabel***] As Boolean, [***Name***] As String, [***Reserved***] As Boolean ) As [DetailDrawingView](../DetailDrawingView/DetailDrawingView.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentView | [DrawingView](../DrawingView/DrawingView.md) | DrawingView object that specifies the base parent view of the projected view. |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the placement point of the view on the sheet. |
| ViewStyle | [DrawingViewStyleEnum](../DrawingViewStyleEnum.md) | DrawingViewStyleEnum the specifies the display style of the geometry within the view. |
| CircularFence | Boolean | Boolean that specifies whether to use a circular fence or a rectangular fence. Specify True for circular and False for rectangular. |
| FenceCenterOrCornerOne | [Point2d](../Point2d/Point2d.md) | Point2d object that specifies the center point for a circular fence or the first corner for a rectangular fence. |
| FenceRadiusOrCornerTwo | Variant | Specifies the radius of a circular fence or input Point2d object that specifies the second corner for a rectangular fence. |
| AttachPoint | Variant | Optional input GeometryIntent object that specifies the geometry to attach the detail view to. If not specified, the detail view is unattached and can be moved around. |
| Scale | Variant | Optional input Double that specifies the drawing view scale factor. If this argument is not specified, the scale is derived from the ParentView.   This is an optional argument whose default value is null. |
| ShowLabel | Boolean | Optional input Boolean that specifies whether to display or hide the view label. The default is True indicating that the label will be displayed.   This is an optional argument whose default value is True. |
| Name | String | Optional input String that defines the editable portion of the drawing view name that is displayed within the browser.   This is an optional argument whose default value is "". |
| Reserved | Boolean | Optional input Boolean reserved for future use.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add detail drawing view](../../sample-programs/DrawingViews_AddDetailView_Sample.md) | This sample demonstrates the creation of a detail drawing view with an attach point. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |