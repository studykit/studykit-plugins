# MoveDefinition.AddMoveAlongRay Method

Parent Object: [MoveDefinition](../MoveDefinition/MoveDefinition.md)

## Description

Method that creates a move along ray operation on the associated move body feature.

## Syntax

MoveDefinition.**AddMoveAlongRay**( ***DirectionEntity*** As Object, ***UseNaturalEntityDirection*** As Boolean, ***Offset*** As Variant ) As [MoveAlongRayMoveOperation](../MoveAlongRayMoveOperation/MoveAlongRayMoveOperation.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DirectionEntity | Object | Input entity that specifies the direction of the move. Valid input includes linear edges, planar faces, work axes, and work planes. |
| UseNaturalEntityDirection | Boolean | Input Boolean that specifies if the movement direction of the bodies uses the natural direction of the direction entity. If True it uses the natural direction. If False the direction is reversed. |
| Offset | Variant | Input Variant that defines the offset value of the move operation. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Move Feature Creation](../../sample-programs/MoveBodyFeatures_Sample.md) | Demonstrates the creation of a Move feature. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |