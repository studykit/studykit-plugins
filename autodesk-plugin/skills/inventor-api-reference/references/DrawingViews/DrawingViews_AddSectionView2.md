# DrawingViews.AddSectionView2 Method

Parent Object: [DrawingViews](../DrawingViews/DrawingViews.md)

## Description

Method that creates a section drawing view.

## Syntax

DrawingViews.**AddSectionView2**( ***ParentView*** As [DrawingView](../DrawingView/DrawingView.md), ***SectionLineSketch*** As [DrawingSketch](../DrawingSketch/DrawingSketch.md), ***Position*** As [Point2d](../Point2d/Point2d.md), ***ViewStyle*** As [DrawingViewStyleEnum](../DrawingViewStyleEnum.md), [***Scale***] As Variant, [***ShowLabel***] As Boolean, [***Name***] As String, [***FullDepth***] As Boolean, [***SectionDepth***] As Variant, [***MoreOptions***] As Variant ) As [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentView | [DrawingView](../DrawingView/DrawingView.md) | Input DrawingView object that specifies the base parent view of the projected view. |
| SectionLineSketch | [DrawingSketch](../DrawingSketch/DrawingSketch.md) | Input DrawingSketch object that contains the profile that will be used to define the section line of the view. The choice between the projected and aligned methods is made automatically based on the following rules. The method can be changed after creation using SectionDrawingView.UseAlignedMethod property.  1. One line - Full Section View - Projected method. 2. Two perpendicular lines - Half Section View - Projected method 3. Two non-perpendicular lines - Aligned Section View. 4. Three or more lines - Offset Section View - Projected method. |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the placement point of the view on the sheet. |
| ViewStyle | [DrawingViewStyleEnum](../DrawingViewStyleEnum.md) | Input DrawingViewStyleEnum the specifies the display style of the geometry within the view. Valid values are kHiddenLineDrawingViewStyle, kHiddenLineRemovedDrawingViewStyle, kShadedDrawingViewStyle, kShadedHiddenLineDrawingViewStyle and kFromBaseDrawingViewStyle. |
| Scale | Variant | Optional input Double that specifies the drawing view scale factor. If this argument is not specified, the scale is derived from the ParentView. |
| ShowLabel | Boolean | Optional input Boolean that specifies whether to display or hide the view label. The default is True indicating that the label will be displayed.   This is an optional argument whose default value is True. |
| Name | String | Optional input String that defines the editable portion of the drawing view name that is displayed within the browser.   This is an optional argument whose default value is "". |
| FullDepth | Boolean | Optional input Boolean that specifies whether to use full section depth. A value of True indicates full section depth. If False, the SectionDepth argument needs to be supplied.   This is an optional argument whose default value is True. |
| SectionDepth | Variant | Optional input Variant that defines the section depth. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document.   This is an optional argument whose default value is null. |
| MoreOptions | Variant | Optional input NameValueMap that specifies more options for creating the section view.    Valid options include:    Name = TargetSheet. Value = Sheet object that specifies the target Sheet to place the section view. If not specifies this will default to the Sheet the ParentView is located on.    Name = PositionOnTargetSheet. Value = Point2d object that specifies the position of the section view on target sheet. This is ignored when the TargetSheet is not specified. If this is specified the Positon argument is used to determine the section line direction.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025.1
