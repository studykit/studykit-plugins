# RevisionTableColumns.Item Property

Parent Object: [RevisionTableColumns](../RevisionTableColumns/RevisionTableColumns.md)

## Description

Returns the specified Column object from the collection.

## Syntax

RevisionTableColumns.**Item**( ***Index*** As Variant ) As [RevisionTableColumn](../RevisionTableColumn/RevisionTableColumn.md)

## Property Value

This is a read only property whose value is a [RevisionTableColumn](../RevisionTableColumn/RevisionTableColumn.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the RevisionTableColumn to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string that corresponds to the title of a column header. If an out of range index or a name of a non-existent RevisionTableColumn is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Query revision table](../../sample-programs/RevisionTable_Sample.md) | This sample illustrates querying the contents of the revision table. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |