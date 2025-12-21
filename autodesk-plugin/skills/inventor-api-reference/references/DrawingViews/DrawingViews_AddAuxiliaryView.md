# DrawingViews.AddAuxiliaryView Method

Parent Object: [DrawingViews](../DrawingViews/DrawingViews.md)

## Description

Method that creates an auxiliary drawing view.

## Syntax

DrawingViews.**AddAuxiliaryView**( ***ParentView*** As [DrawingView](../DrawingView/DrawingView.md), ***OrientationEdge*** As [DrawingCurve](../DrawingCurve/DrawingCurve.md), ***Position*** As [Point2d](../Point2d/Point2d.md), ***ViewStyle*** As [DrawingViewStyleEnum](../DrawingViewStyleEnum.md), [***Scale***] As Variant, [***ShowLabel***] As Boolean, [***Name***] As String ) As [DrawingView](../DrawingView/DrawingView.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentView | [DrawingView](../DrawingView/DrawingView.md) | Input DrawingView object that specifies the parent view of the auxiliary view. |
| OrientationEdge | [DrawingCurve](../DrawingCurve/DrawingCurve.md) | Input DrawingCurve object that specifies the orientation of the auxiliary view. This must be a linear DrawingCurve from the parent view, else the method returns an error. |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the placement point of the view on the sheet. |
| ViewStyle | [DrawingViewStyleEnum](../DrawingViewStyleEnum.md) | Input DrawingViewStyleEnum the specifies the display style of the geometry within the view. Valid values are kHiddenLineDrawingViewStyle, kHiddenLineRemovedDrawingViewStyle, kShadedDrawingViewStyle, kShadedHiddenLineDrawingViewStyle and kFromBaseDrawingViewStyle. |
| Scale | Variant | Optional input that specifies the drawing view scale factor. This can be either specified as a Double or a String. **Examples:** 2.0, "5:1", "1/2", etc.  If this argument is not specified, the scale is derived from the ParentView. |
| ShowLabel | Boolean | Optional input Boolean that specifies whether to display or hide the view label. The default is True indicating that the label will be displayed.   This is an optional argument whose default value is True. |
| Name | String | Optional input String that defines the editable portion of the drawing view name that is displayed within the browser.   This is an optional argument whose default value is "". |

## Version

Introduced in version 2010
