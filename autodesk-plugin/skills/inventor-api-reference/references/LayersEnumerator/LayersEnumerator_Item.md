# LayersEnumerator.Item Property

Parent Object: [LayersEnumerator](../LayersEnumerator/LayersEnumerator.md)

## Description

Returns the specified Layer object from the collection.

## Syntax

LayersEnumerator.**Item**( ***Index*** As Variant ) As [Layer](../Layer/Layer.md)

## Property Value

This is a read only property whose value is a [Layer](../Layer/Layer.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the Layer to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the internal name of a Layer. If an out of range index or a name of a non-existent Layer is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Moving sketch entities to a new layer](../../sample-programs/Layer_Sample.md) | This sample demonstrates the creation of a new layer and moving sketch entities onto this newly created layer. |

## Version

Introduced in version 10
