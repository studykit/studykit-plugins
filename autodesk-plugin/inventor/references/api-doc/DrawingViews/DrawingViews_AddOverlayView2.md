# DrawingViews.AddOverlayView2 Method

Parent Object: [DrawingViews](../DrawingViews/DrawingViews.md)

## Description

Method that creates an overlay drawing view.

## Syntax

DrawingViews.**AddOverlayView2**( ***ParentView*** As [DrawingView](../DrawingView/DrawingView.md), ***ModelState*** As String, ***PositionalRepresentation*** As String, ***DesignViewRepresentation*** As String, ***DesignViewAssociative*** As Boolean, ***ViewStyle*** As [DrawingViewStyleEnum](../DrawingViewStyleEnum.md), [***ShowLabel***] As Boolean, [***Name***] As String ) As [DrawingView](../DrawingView/DrawingView.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentView | [DrawingView](../DrawingView/DrawingView.md) | Input DrawingView object that specifies the parent view of the overlay view. The parent view must be a base view, projected view or an auxiliary view of an assembly, else the method returns an error. |
| ModelState | String | Input String that specifies the model state to use for the overlay view. The input string must the name of an existing model state in the assembly referenced by the parent view. The method returns a failure if a model state with this name is not found in the referenced assembly. |
| PositionalRepresentation | String | Input String that specifies the positional representation to use for the overlay view. The input string must the name of an existing position representation in the assembly referenced by the parent view. The method returns a failure if a representation with this name is not found in the referenced assembly. |
| DesignViewRepresentation | String | Input String that specifies the design view representation to use for the overlay view. The input string must the name of an existing design view representation in the assembly referenced by the parent view. In addition, “Nothing Visible” and “All Visible” can also be provided. The method returns a failure if a representation with this name is not found in the referenced assembly. |
| DesignViewAssociative | Boolean | Input Boolean that indicates whether to associatively apply the design view representation. If set to True, any changes to the design view in the referenced assembly will show in this view. |
| ViewStyle | [DrawingViewStyleEnum](../DrawingViewStyleEnum.md) | Input DrawingViewStyleEnum the specifies the display style of the geometry within the view. Valid values are kHiddenLineDrawingViewStyle, kHiddenLineRemovedDrawingViewStyle, kShadedDrawingViewStyle, kShadedHiddenLineDrawingViewStyle and kFromBaseDrawingViewStyle. |
| ShowLabel | Boolean | Optional input Boolean that specifies whether to display or hide the view label. The default is True indicating that the label will be displayed. |
| Name | String | Optional input String that defines the editable portion of the drawing view name that is displayed within the browser. If not specified, the name of the input positional representation is used.   This is an optional argument whose default value is "". |

## Version

Introduced in version 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |