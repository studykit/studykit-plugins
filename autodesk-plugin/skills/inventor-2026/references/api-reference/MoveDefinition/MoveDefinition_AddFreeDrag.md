# MoveDefinition.AddFreeDrag Method

Parent Object: [MoveDefinition](../MoveDefinition/MoveDefinition.md)

## Description

Method that creates a free drag operation on the associated move body feature.

## Syntax

MoveDefinition.**AddFreeDrag**( ***XOffset*** As Variant, ***YOffset*** As Variant, ***ZOffset*** As Variant ) As [FreeDragMoveOperation](../FreeDragMoveOperation/FreeDragMoveOperation.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| XOffset | Variant | Input Variant that defines the x offset of the move operation. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| YOffset | Variant | Input Variant that defines the y offset of the move operation. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| ZOffset | Variant | Input Variant that defines the z offset of the move operation. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Move Feature Creation](../../sample-programs/MoveBodyFeatures_Sample.md) | Demonstrates the creation of a Move feature. |

## Version

Introduced in version 2013
