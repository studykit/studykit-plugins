# ParameterTables.AddExcelTable Method

Parent Object: [ParameterTables](../ParameterTables/ParameterTables.md)

## Description

Method that creates a new ParameterTable object, given an existing Excel document as input. Returns the resulting ParameterTable object. The first sheet in the Excel document is used.

## Syntax

ParameterTables.**AddExcelTable**( ***ExcelDocument*** As String, ***StartCell*** As String, ***Link*** As Boolean ) As [ParameterTable](../ParameterTable/ParameterTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ExcelDocument | String | Input String value that contains the full path to the Excel document. |
| StartCell | String | Input String value that specifies the beginning cell to begin importing from, for example "A1". |
| Link | Boolean | Input Boolean value that specifies whether the Excel document is to be embedded or linked. True indicates it should be linked. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Table Parameters](../../sample-programs/ParameterTables_Sample.md) | This sample demonstrates how to access the Parameters object, and from it in turn the TableParameters collection that represents the collection of parameters that have been linked/embedded from an external spreadsheet. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |