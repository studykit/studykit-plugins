# RevisionTableRow.Item Property

Parent Object: [RevisionTableRow](../RevisionTableRow/RevisionTableRow.md)

## Description

Returns the specified Cell object from the collection.

## Syntax

RevisionTableRow.**Item**( ***Index*** As Variant ) As [RevisionTableCell](../RevisionTableCell/RevisionTableCell.md)

## Property Value

This is a read only property whose value is a [RevisionTableCell](../RevisionTableCell/RevisionTableCell.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the RevisionTableCell to return. This can be either a numeric value indicating the index of the item in the collection, a string indicating the title of a column header, or a RevisionTableColumn object. If an out of range index, a non-existent column header title, or an invalid RevisionTableColumn object is specified, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Query revision table](../../sample-programs/RevisionTable_Sample.md) | This sample illustrates querying the contents of the revision table. |

## Version

Introduced in version 10
