# CustomTables.AddExcelTable Method

Parent Object: [CustomTables](../CustomTables/CustomTables.md)

## Description

Method that creates a new custom table based on an excel file. The newly created CustomTable is returned.

## Syntax

CustomTables.**AddExcelTable**( ***ExcelFileName*** As String, ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), [***Title***] As String, [***StartCell***] As String, [***ColumnHeaderRow***] As Long ) As [CustomTable](../CustomTable/CustomTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ExcelFileName | String | Input String that specifies the full file name of the excel file. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that defines the placement point of the table on the sheet. |
| Title | String | Optional input String that specifies the title (or the header) of the table. |
| StartCell | String | Optional input String that specifies the start cell of the data in the excel file. If not specified, the cell 'A2' is used as the start cell.   This is an optional argument whose default value is "A2". |
| ColumnHeaderRow | Long | Optional input Long that specifies the header row in the excel file. If not specified, the first row in the excel file is assumed to be the header row.   This is an optional argument whose default value is 1. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a drawing Excel Table](../../sample-programs/CustomTables_AddExcelTable_Sample.md) | This sample demonstrates the creation of a table based on an Excel file in a drawing. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |