# CustomTables.AddCSVTable Method

Parent Object: [CustomTables](../CustomTables/CustomTables.md)

## Description

Method that creates a new custom table based on a CSV (comma delimited) file. The newly created CustomTable is returned.

## Syntax

CustomTables.**AddCSVTable**( ***CSVFileName*** As String, ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), [***Title***] As String, [***UseFirstRowForHeaders***] As Boolean ) As [CustomTable](../CustomTable/CustomTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CSVFileName | String | Input String that specifies the full file name of the CSV (comma delimited) file. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that defines the placement point of the table on the sheet. |
| Title | String | Optional input String that specifies the title (or the header) of the table. |
| UseFirstRowForHeaders | Boolean | Optional input Boolean that specifies whether to use the first row for column headers. If not specified, this argument defaults to True.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |