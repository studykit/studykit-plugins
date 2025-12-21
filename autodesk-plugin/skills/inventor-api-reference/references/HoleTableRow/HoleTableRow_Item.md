# HoleTableRow.Item Property

Parent Object: [HoleTableRow](../HoleTableRow/HoleTableRow.md)

## Description

Returns the specified Cell object from the collection.

## Syntax

HoleTableRow.**Item**( ***Index*** As Variant ) As [HoleTableCell](../HoleTableCell/HoleTableCell.md)

## Property Value

This is a read only property whose value is a [HoleTableCell](../HoleTableCell/HoleTableCell.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the HoleTableCell to return. This can be either a numeric value indicating the index of the item in the collection, a string indicating the title of a column header, or a HoleTableColumn object. If an out of range index, a non-existent column header title, or an invalid HoleTableColumn object is specified, an error occurs. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |