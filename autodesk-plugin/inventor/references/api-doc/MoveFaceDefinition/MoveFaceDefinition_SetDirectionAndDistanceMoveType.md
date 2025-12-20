# MoveFaceDefinition.SetDirectionAndDistanceMoveType Method

Parent Object: [MoveFaceDefinition](../MoveFaceDefinition/MoveFaceDefinition.md)

## Description

Method that sets the move face type to kDirectionAndDistanceMoveType. The move is defined using a direction and a distance along the direction.

## Syntax

MoveFaceDefinition.**SetDirectionAndDistanceMoveType**( ***Distance*** As Variant, ***Direction*** As Object, [***DirectionReversed***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Distance | Variant | Defines the distance to move along the specified direction. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Direction | Object | Specifies the entity defining the direction for the move. This can either be a WorkAxis, a linear Edge, or a planar Face object. |
| DirectionReversed | Boolean | Specifies whether the direction defined by the entity in the Direction argument should be reversed. Defaults to False indicating that the direction is not reversed. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |