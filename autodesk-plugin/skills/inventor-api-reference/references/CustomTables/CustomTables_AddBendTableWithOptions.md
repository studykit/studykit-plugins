# CustomTables.AddBendTableWithOptions Method

Parent Object: [CustomTables](../CustomTables/CustomTables.md)

## Description

Method that creates a new bend table. The newly created CustomTable is returned.

## Syntax

CustomTables.**AddBendTableWithOptions**( ***SheetMetalFileName*** As String, ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), [***Options***] As Variant ) As [CustomTable](../CustomTable/CustomTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SheetMetalFileName | String | Input String that specifies the full file name of the sheet metal file to create the bend table from. The input file name must be that of a sheet metal file with at least one flat pattern created in it, else an error will occur. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that defines the placement point of the table on the sheet. |
| Options | Variant | Optional input NameValueMap that specifies more options to create the bend table. Valid options are: Name = “Title”. Value = String that specifies the title (or the header) of the table. Name = “Columns”. Value = Array of Strings that specifies the columns of the bend table. The strings can be any or all of the following in any order: “BEND ID”, “BEND DIRECTION”, “BEND ANGLE”, “BEND RADIUS”，“BEND ALT RADIUS” and “ BEND KFACTOR”. If not specified, the default columns “BEND ID”, “BEND DIRECTION”, “BEND ANGLE” and “BEND RADIUS” are created. Name = “BendIDNumericFormat”. Value = Boolean that specifies whether the format of the Bend ID is alphabetic or numeric. If not specified, a value of True is used indicating that numeric format will be used. Name = “BendIDPrefix”. Value = String that specifies a prefix for the Bend IDs. |

## Version

Introduced in version 2022
