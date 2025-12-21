# OrientedBox.PutOrientedBoxData Method

Parent Object: [OrientedBox](../OrientedBox/OrientedBox.md)

## Description

Method that sets the corner point and edges data that define this OrientedBox.

## Syntax

OrientedBox.**PutOrientedBoxData**( ***CornerPoint*** As [Point](../Point/Point.md), ***DirectionOne*** As [Vector](../Vector/Vector.md), ***DirectionTwo*** As [Vector](../Vector/Vector.md), ***DirectionThree*** As [Vector](../Vector/Vector.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CornerPoint | [Point](../Point/Point.md) | Input Point object that defines a corner point of the oriented box. |
| DirectionOne | [Vector](../Vector/Vector.md) | Input Vector object that defines the first direction of the oriented box starting from the corner point. |
| DirectionTwo | [Vector](../Vector/Vector.md) | Input Vector object that defines the second edge of the oriented box starting from the corner point. If this vector is not perpendicular to the DirectionOne, an error will occur. |
| DirectionThree | [Vector](../Vector/Vector.md) | Input Vector object that defines the third edge of the oriented box starting from the corner point. If this vector is not perpendicular to the DirectionOne and DirectionTwo, an error will occur. |

## Version

Introduced in version 2016
