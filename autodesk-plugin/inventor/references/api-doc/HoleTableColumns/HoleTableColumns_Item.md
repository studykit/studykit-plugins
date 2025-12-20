# HoleTableColumns.Item Property

Parent Object: [HoleTableColumns](../HoleTableColumns/HoleTableColumns.md)

## Description

Returns the specified Column object from the collection.

## Syntax

HoleTableColumns.**Item**( ***Index*** As Variant ) As [HoleTableColumn](../HoleTableColumn/HoleTableColumn.md)

## Property Value

This is a read only property whose value is a [HoleTableColumn](../HoleTableColumn/HoleTableColumn.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the HoleTableColumn to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string that corresponds to the title of a column header. If an out of range index or a name of a non-existent HoleTableColumn is provided, an error will occur. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |