# ParameterTable.FileName Property

Parent Object: [ParameterTable](../ParameterTable/ParameterTable.md)

## Description

Gets/Sets the File Name of this linked table. Fails if this table is embedded. Setting a new File Name may add new parameters, update existing ones, and may turn some to DriverLost.

## Syntax

ParameterTable.**FileName**() As String

## Property Value

This is a read/write property whose value is a String.

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