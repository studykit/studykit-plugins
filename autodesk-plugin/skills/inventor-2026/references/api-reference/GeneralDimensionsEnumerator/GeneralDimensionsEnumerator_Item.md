# GeneralDimensionsEnumerator.Item Property

Parent Object: [GeneralDimensionsEnumerator](../GeneralDimensionsEnumerator/GeneralDimensionsEnumerator.md)

## Description

Returns the specified DrawingStandardStyle object from the collection.

## Syntax

GeneralDimensionsEnumerator.**Item**( ***Index*** As Long ) As [GeneralDimension](../GeneralDimension/GeneralDimension.md)

## Property Value

This is a read only property whose value is a [GeneralDimension](../GeneralDimension/GeneralDimension.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Value that specifies the GeneralDimension to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the GeneralDimension name. If an out of range index or a name of a non-existent GeneralDimension is provided, an error will occur. |

## Version

Introduced in version 9
