# BOMRowsEnumerator.Item Property

Parent Object: [BOMRowsEnumerator](../BOMRowsEnumerator/BOMRowsEnumerator.md)

## Description

Returns an item in the collection.

## Syntax

BOMRowsEnumerator.**Item**( ***Index*** As Long ) As [BOMRow](../BOMRow/BOMRow.md)

## Property Value

This is a read only property whose value is a [BOMRow](../BOMRow/BOMRow.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Value that specifies the BOMRow to return. This is a numeric value indicating the index of the item in the collection. If an out of range index is input, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |

## Version

Introduced in version 11
