# SheetFormats.Add Method

Parent Object: [SheetFormats](../SheetFormats/SheetFormats.md)

## Description

Method that creates a new SheetFormat. The newly created SheetFormat is returned.

## Syntax

SheetFormats.**Add**( ***Sheet*** As [Sheet](../Sheet/Sheet.md), ***Name*** As String ) As [SheetFormat](../SheetFormat/SheetFormat.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Sheet | [Sheet](../Sheet/Sheet.md) | Input Sheet object that specifies the sheet to be used as the template for creating the sheet format. |
| Name | String | Input String that defines the name of the sheet format. The name must be unique with respect to all other SheetFormats in the document or an error will occur. |

## Version

Introduced in version 2009
