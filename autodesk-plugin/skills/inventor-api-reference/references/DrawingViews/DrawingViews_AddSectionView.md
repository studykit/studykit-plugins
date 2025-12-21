# DrawingViews.AddSectionView Method

Parent Object: [DrawingViews](../DrawingViews/DrawingViews.md)

## Description

Method that creates a section drawing view.

## Syntax

DrawingViews.**AddSectionView**( ***ParentView*** As [DrawingView](../DrawingView/DrawingView.md), ***SectionLineSketch*** As [DrawingSketch](../DrawingSketch/DrawingSketch.md), ***Position*** As [Point2d](../Point2d/Point2d.md), ***ViewStyle*** As [DrawingViewStyleEnum](../DrawingViewStyleEnum.md), [***Scale***] As Variant, [***ShowLabel***] As Boolean, [***Name***] As String, [***Reserved***] As Boolean, [***FullDepth***] As Boolean, [***SectionDepth***] As Variant ) As [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentView | [DrawingView](../DrawingView/DrawingView.md) | Input DrawingView object that specifies the base parent view of the projected view. |
| SectionLineSketch | [DrawingSketch](../DrawingSketch/DrawingSketch.md) | Input DrawingSketch object that contains the profile that will be used to define the section line of the view. The DrawingSketch should be associated with the parent DrawingView (i.e. from parent DrawingView.Sketches). The choice between the projected and aligned methods is made automatically based on the following rules. The method can be changed after creation using SectionDrawingView.UseAlignedMethod property.   1. One line - Full Section View - Projected method 2. Two perpendicular lines - Half Section View - Projected method 3. Two non-perpendicular lines - Aligned Section View 4. Three or more lines - Offset Section View - Projected method |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the placement point of the view on the sheet. |
| ViewStyle | [DrawingViewStyleEnum](../DrawingViewStyleEnum.md) | Input DrawingViewStyleEnum the specifies the display style of the geometry within the view. |
| Scale | Variant | Optional input Double that specifies the drawing view scale factor. If this argument is not specified, the scale is derived from the ParentView. |
| ShowLabel | Boolean | Optional input Boolean that specifies whether to display or hide the view label. The default is True indicating that the label will be displayed.   This is an optional argument whose default value is True. |
| Name | String | Optional input String that defines the editable portion of the drawing view name that is displayed within the browser.   This is an optional argument whose default value is "". |
| Reserved | Boolean | Optional input Boolean reserved for future use.   This is an optional argument whose default value is True. |
| FullDepth | Boolean | Optional input Boolean that specifies whether to use full section depth. A value of True indicates full section depth. If False, the SectionDepth argument needs to be supplied.   This is an optional argument whose default value is True. |
| SectionDepth | Variant | Input Variant that defines the section depth. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document.   This is an optional argument whose default value is null. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |