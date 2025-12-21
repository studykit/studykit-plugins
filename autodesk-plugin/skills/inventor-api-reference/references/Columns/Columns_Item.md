# Columns.Item Property

Parent Object: [Columns](../Columns/Columns.md)

## Description

Returns the specified Column object from the collection.

## Syntax

Columns.**Item**( ***Index*** As Variant ) As [Column](../Column/Column.md)

## Property Value

This is a read only property whose value is a [Column](../Column/Column.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the Column to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string that corresponds to the title of a column header. If an out of range index or a name of a non-existent Column is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Custom Table - create](../../sample-programs/CustomTables_Sample.md) | This sample demonstrates how to create a custom table. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |