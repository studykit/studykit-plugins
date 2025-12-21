# Layer.LineType Property

Parent Object: [Layer](../Layer/Layer.md)

## Description

Property that gets and sets the line type override. Setting the property to kDefaultLineType restores the default line type. If the property returns kCustomLineType, the GetCustomLineType method can be used to get further details about the line type.

## Syntax

Layer.**LineType**() As [LineTypeEnum](../LineTypeEnum.md)

## Property Value

This is a read/write property whose value is a [LineTypeEnum](../LineTypeEnum.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Moving sketch entities to a new layer](../../sample-programs/Layer_Sample.md) | This sample demonstrates the creation of a new layer and moving sketch entities onto this newly created layer. |

## Version

Introduced in version 10
