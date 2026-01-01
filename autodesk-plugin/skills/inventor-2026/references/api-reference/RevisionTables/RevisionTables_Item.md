# RevisionTables.Item Property

Parent Object: [RevisionTables](../RevisionTables/RevisionTables.md)

## Description

Returns the specified RevisionTable object from the collection.

## Syntax

RevisionTables.**Item**( ***Index*** As Variant ) As [RevisionTable](../RevisionTable/RevisionTable.md)

## Property Value

This is a read only property whose value is a [RevisionTable](../RevisionTable/RevisionTable.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the RevisionTable to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the RevisionTable name. If an out of range index or a name of a non-existent RevisionTable is provided, an error will occur . |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Query revision table](../../sample-programs/RevisionTable_Sample.md) | This sample illustrates querying the contents of the revision table. |

## Version

Introduced in version 10
