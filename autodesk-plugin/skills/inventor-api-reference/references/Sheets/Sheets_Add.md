# Sheets.Add Method

Parent Object: [Sheets](../Sheets/Sheets.md)

## Description

Method that creates a new Sheet.

## Syntax

Sheets.**Add**( [***Size***] As [DrawingSheetSizeEnum](../DrawingSheetSizeEnum.md), [***Orientation***] As [PageOrientationTypeEnum](../PageOrientationTypeEnum.md), [***SheetName***] As String, [***Width***] As Variant, [***Height***] As Variant ) As [Sheet](../Sheet/Sheet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Size | [DrawingSheetSizeEnum](../DrawingSheetSizeEnum.md) | Optional input enum value that defines the size of sheet to create. If kCustomDrawingSheetSize is used the Width and Height arguments must be specified. If not specified, the default value kCDrawingSheetSize is used. |
| Orientation | [PageOrientationTypeEnum](../PageOrientationTypeEnum.md) | Optional input PageOrientationTypeEnum that defines if the sheet will be landscape or portrait orientation. If not specified or if specified as kDefaultPageOrientation, the sheet will be created with a landscape orientation.   This is an optional argument whose default value is 10242. |
| SheetName | String | Optional input String that defines the editable portion of the name that is displayed within the browser. If not specified, a default name is assigned to the sheet.   This is an optional argument whose default value is "". |
| Width | Variant | Optional input Double that defines the width of the sheet. This value is used when the Size argument is kCustomDrawingSheetSize, otherwise it is ignored. The size is defined in centimeters.   This is an optional argument whose default value is null. |
| Height | Variant | Optional input Double that defines the height of the sheet. This value is used when the Size argument is kCustomDrawingSheetSize, otherwise it is ignored. The size is defined in centimeters.   This is an optional argument whose default value is null. |

## Version

Introduced in version 9
