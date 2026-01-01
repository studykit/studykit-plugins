# DrawingSketches.Item Property

Parent Object: [DrawingSketches](../DrawingSketches/DrawingSketches.md)

## Description

Returns the specified DrawingSketch object from the collection.

## Syntax

DrawingSketches.**Item**( ***Index*** As Variant ) As [DrawingSketch](../DrawingSketch/DrawingSketch.md)

## Property Value

This is a read only property whose value is a [DrawingSketch](../DrawingSketch/DrawingSketch.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the sketch name. If an out of range index or a name of a non-existent sketch is specified, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Moving sketch entities to a new layer](../../sample-programs/Layer_Sample.md) | This sample demonstrates the creation of a new layer and moving sketch entities onto this newly created layer. |

## Version

Introduced in version 5.3
