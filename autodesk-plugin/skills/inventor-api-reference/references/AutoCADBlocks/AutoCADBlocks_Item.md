# AutoCADBlocks.Item Property

Parent Object: [AutoCADBlocks](../AutoCADBlocks/AutoCADBlocks.md)

## Description

Returns the specified AutoCADBlock object from the collection.

## Syntax

AutoCADBlocks.**Item**( ***Index*** As Variant ) As [AutoCADBlock](../AutoCADBlock/AutoCADBlock.md)

## Property Value

This is a read only property whose value is an [AutoCADBlock](../AutoCADBlock/AutoCADBlock.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Specifies the AutoCADBlock to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the AutoCADBlock name. If an out of range index or a name of a non-existent AutoCADBlock is provided, an error will occur. |

## Version

Introduced in version 2011
