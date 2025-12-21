# iAssemblyTableRow.Item Property

Parent Object: [iAssemblyTableRow](../iAssemblyTableRow/iAssemblyTableRow.md)

## Description

Returns the specified iAssemblyTableCell object from the collection.

## Syntax

iAssemblyTableRow.**Item**( ***Index*** As Variant ) As [iAssemblyTableCell](../iAssemblyTableCell/iAssemblyTableCell.md)

## Property Value

This is a read only property whose value is an [iAssemblyTableCell](../iAssemblyTableCell/iAssemblyTableCell.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Value that specifies the iAssemblyTableCell to return. This can be either a numeric value indicating the index of a column where the first column has an index of 1 or it can be a string indicating the heading of a particular column. The heading is obtained using the Heading property on an iAssemblyTableColumn object. If an out of range index or a heading of a non-existent column is provided, an error will occur. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |