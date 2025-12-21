# iAssemblyTableRows.Item Property

Parent Object: [iAssemblyTableRows](../iAssemblyTableRows/iAssemblyTableRows.md)

## Description

Returns an item from the collection.

## Syntax

iAssemblyTableRows.**Item**( ***Index*** As Variant ) As [iAssemblyTableRow](../iAssemblyTableRow/iAssemblyTableRow.md)

## Property Value

This is a read only property whose value is an [iAssemblyTableRow](../iAssemblyTableRow/iAssemblyTableRow.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Value that specifies the iAssemblyTableRow to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the member name. If an out of range index or a name of a non-existent iAssemblyTableRow is provided, an error will occur. This index value is not the same as the index value indicated in the user interface dialog. Rows in the dialog may be re-ordered. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |