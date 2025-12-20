# PartsListRow.Item Property

Parent Object: [PartsListRow](../PartsListRow/PartsListRow.md)

## Description

Returns the specified PartsListCells object from the collection. This is the default property of the PartsListCells collection object.

## Syntax

PartsListRow.**Item**( ***Index*** As Variant ) As [PartsListCell](../PartsListCell/PartsListCell.md)

## Property Value

This is a read only property whose value is a [PartsListCell](../PartsListCell/PartsListCell.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the PartsListCell to return. This can be either a numeric value indicating the index of the item in the collection, a string indicating the title of a column header, or a PartsListColumn object. If an out of range index, a non-existent column header title, or an invalid PartsListColumn object is specified, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Parts List Edit](../../sample-programs/PartsLists_Edit_Sample.md) | This sample illustrates editing the contents of the parts list. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |