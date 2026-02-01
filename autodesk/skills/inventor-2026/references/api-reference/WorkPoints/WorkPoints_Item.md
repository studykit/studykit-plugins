# WorkPoints.Item Property

Parent Object: [WorkPoints](../WorkPoints/WorkPoints.md)

## Description

Returns the specified WorkPoint object from the collection. This is the default property of the WorkPoints collection object.

## Syntax

WorkPoints.**Item**( ***Index*** As Variant ) As [WorkPoint](../WorkPoint/WorkPoint.md)

## Property Value

This is a read only property whose value is a [WorkPoint](../WorkPoint/WorkPoint.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the object to return. This can be a numeric value indicating the index of the item in the collection or it can be a string indicating the work point name. If an out of range index or a name of a non-existent work point is specified, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |

## Version

Introduced in version 4
