# Sheet.AddDefaultBorder Method

Parent Object: [Sheet](../Sheet/Sheet.md)

## Description

Method that adds an instance of the default border to the sheet. This method is the equivalent of inserting the 'Default Border' border. A border created using the default border is created 'on the fly' by Autodesk Inventor using the supplied input. It is not based on an existing border definition.

## Syntax

Sheet.**AddDefaultBorder**( [***HorizontalZoneCount***] As Variant, [***HorizontalZoneLabelMode***] As Variant, [***VerticalZoneCount***] As Variant, [***VerticalZoneLabelMode***] As Variant, [***LabelFromBottomRight***] As Variant, [***DelimitByLines***] As Variant, [***Centermarks***] As Variant, [***TopMargin***] As Variant, [***BottomMargin***] As Variant, [***LeftMargin***] As Variant, [***RightMargin***] As Variant, [***TextStyle***] As Variant, [***TextLayer***] As Variant, [***LineLayer***] As Variant ) As [DefaultBorder](../DefaultBorder/DefaultBorder.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HorizontalZoneCount | Variant | Optional value that specifies the number of horizontal zones to be created for the border. If not supplied it will default to a standard value, which varies depending on the width of the sheet. |
| HorizontalZoneLabelMode | Variant | Optional input BorderLabelModeEnum value that specifies label style for the horizontal labels. Valid values are kBorderLabelModeAlphabetical, kBorderLabelModeNumeric, and kBorderLabelModeNone. If not specified, it will default to kBorderLabelModeNumeric.     This is an optional argument whose default value is null. |
| VerticalZoneCount | Variant | Optional value that specifies the number of vertical zones to be created for the border. If not supplied it will default to a standard value, which varies depending on the height of the sheet.     This is an optional argument whose default value is null. |
| VerticalZoneLabelMode | Variant | Optional input BorderLabelModeEnum value that specifies label style for the vertical labels. Valid values are kBorderLabelModeAlphabetical, kBorderLabelModeNumeric, and kBorderLabelModeNone. If not specified, it will default to kBorderLabelModeAlphabetical.     This is an optional argument whose default value is null. |
| LabelFromBottomRight | Variant | Optional input Variant that indicates whether the zone numbers should begin at the bottom\-right or top\-left corner. A value of True indicates the bottom\-right corner and False specifies the top\-left. If not specified, it will default to True.     This is an optional argument whose default value is null. |
| DelimitByLines | Variant | Optional input Boolean input that indicates if delimit zones should be indicated by lines or arrowheads. A value of True indicates lines and False specifies arrowheads. If not specified, it will default to True.     This is an optional argument whose default value is null. |
| Centermarks | Variant | Optional input Boolean that specifies whether to a incorporate center marks into the border. A value of True will add center marks. If not specified, it will default to True.     This is an optional argument whose default value is null. |
| TopMargin | Variant | Optional Double input that specifies the space between the top edge of the sheet and the border line. The distance is specified in centimeters. If not specified, it defaults to a value appropriate for the current active standard.     This is an optional argument whose default value is null. |
| BottomMargin | Variant | Optional Double input that specifies the space between the bottom edge of the sheet and the border line. The distance is specified in centimeters. If not specified, it defaults to a value appropriate for the current active standard.     This is an optional argument whose default value is null. |
| LeftMargin | Variant | Optional Double input that specifies the space between the left edge of the sheet and the border line. The distance is specified in centimeters. If not specified, it defaults to a value appropriate for the current active standard.     This is an optional argument whose default value is null. |
| RightMargin | Variant | Optional input Variant that specifies the space between the right edge of the sheet and the border line. The distance is specified in centimeters. If not specified, it defaults to a value appropriate for the current active standard.     This is an optional argument whose default value is null. |
| TextStyle | Variant | Optional input TextStyle object that specifies the text style for the zone labels.     This is an optional argument whose default value is null. |
| TextLayer | Variant | Optional input Layer object that specifies the layer for the zone labels.     This is an optional argument whose default value is null. |
| LineLayer | Variant | Optional input Layer object that specifies the layer for the border geometry.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Border Insert](../../sample-programs/Sheet_AddDefaultBorder_Sample.md) | This sample illustrates inserting a default border. |
| [Border Insert Default](../../sample-programs/Sheet_AddDefaultBorder2_Sample.md) | This sample illustrates inserting a default border using the default values. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |