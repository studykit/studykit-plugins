# DefaultBorder Object

Derived from: [Border](../Border/Border.md) Object

## Description

The DefaultBorder object represents an instance of the default border.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DefaultBorder/DefaultBorder_Delete.md) | Method that deletes the title block from the sheet. |
| [GetResultText](../DefaultBorder/DefaultBorder_GetResultText.md) | Method that returns the text that is currently displayed for a specific text box. This is useful for text boxes that use input form other sources to define their content, i.e. properties and prompted text. The string displayed within this text box is returned. |
| [SetPromptResultText](../DefaultBorder/DefaultBorder_SetPromptResultText.md) | Method that sets the text that was supplied for a specified border that contains prompted text. The string displayed within this border is changed. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DefaultBorder/DefaultBorder_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BottomMargin](../DefaultBorder/DefaultBorder_BottomMargin.md) | Property that returns the space between the bottom edge of the sheet and the border line. The distance is specified in centimeters. |
| [Centermarks](../DefaultBorder/DefaultBorder_Centermarks.md) | Property that returns if center marks are displayed on the border. A value of True indicates center marks are displayed. |
| [Definition](../DefaultBorder/DefaultBorder_Definition.md) | Property returning the border definition object that this border is an instance of. |
| [DelimitZonesByLines](../DefaultBorder/DefaultBorder_DelimitZonesByLines.md) | Property that returns if delimit zones are indicated by lines or arrowheads. A value of True indicates lines are used and False specifies arrowheads. |
| [HorizontalZoneCount](../DefaultBorder/DefaultBorder_HorizontalZoneCount.md) | Property that returns the number of horizontal zones to be created for the border. |
| [HorizontalZoneLabelMode](../DefaultBorder/DefaultBorder_HorizontalZoneLabelMode.md) | Property that returns the label style for the horizontal labels. Valid values are kBorderLabelModeAlphabetical, kBorderLabelModeNumeric, and kBorderLabelModeNone. |
| [LabelFromBottomRight](../DefaultBorder/DefaultBorder_LabelFromBottomRight.md) | Property that returns whether the zone numbers begin at the bottom-right or top-left corner. A value of True indicates the bottom-right corner and False specifies the top-left. |
| [LeftMargin](../DefaultBorder/DefaultBorder_LeftMargin.md) | Property that returns the space between the left edge of the sheet and the border line. The distance is specified in centimeters. |
| [Name](../DefaultBorder/DefaultBorder_Name.md) | Gets and sets the name of the border instance. |
| [Parent](../DefaultBorder/DefaultBorder_Parent.md) | Property returning the parent sheet object. |
| [RangeBox](../DefaultBorder/DefaultBorder_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [RightMargin](../DefaultBorder/DefaultBorder_RightMargin.md) | Property that returns the space between the right edge of the sheet and the border line. The distance is specified in centimeters. |
| [TopMargin](../DefaultBorder/DefaultBorder_TopMargin.md) | Property that returns the space between the top edge of the sheet and the border line. The distance is specified in centimeters. |
| [Type](../DefaultBorder/DefaultBorder_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [VerticalZoneCount](../DefaultBorder/DefaultBorder_VerticalZoneCount.md) | Property that returns the number of vertical zones to be created for the border. |
| [VerticalZoneLabelMode](../DefaultBorder/DefaultBorder_VerticalZoneLabelMode.md) | Property that returns the label style for the vertical labels. Valid values are kBorderLabelModeAlphabetical, kBorderLabelModeNumeric, and kBorderLabelModeNone. |

## Accessed From

[Sheet.AddDefaultBorder](../Sheet/Sheet_AddDefaultBorder.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Border Insert](../../sample-programs/Sheet_AddDefaultBorder_Sample.md) | This sample illustrates inserting a default border. |
| [Border Insert Default](../../sample-programs/Sheet_AddDefaultBorder2_Sample.md) | This sample illustrates inserting a default border using the default values. |

## Version

Introduced in version 5.3
