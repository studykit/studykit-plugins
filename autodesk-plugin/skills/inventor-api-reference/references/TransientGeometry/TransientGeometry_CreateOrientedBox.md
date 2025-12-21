# TransientGeometry.CreateOrientedBox Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new oriented box object.

## Syntax

TransientGeometry.**CreateOrientedBox**( [***CornerPoint***] As Variant, [***DirectionOne***] As Variant, [***DirectionTwo***] As Variant, [***DirectionThree***] As Variant ) As [OrientedBox](../OrientedBox/OrientedBox.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CornerPoint | Variant | Optional input Point object that defines a corner point of the oriented box. The below DirectionOne/ DirectionTwo/DirectionThree arguments define the oriented box directions with this corner point as starting point. If not specified the origin point will be used. |
| DirectionOne | Variant | Optional input Vector object that specifies the first direction and length. If not specified a default vector(1,0,0) will be used.   This is an optional argument whose default value is null. |
| DirectionTwo | Variant | Optional input Vector object that specifies the second direction and length. If not specified a default vector(0,1,0) will be used. If this vector is not perpendicular to the DirectionOne, an error will occur.   This is an optional argument whose default value is null. |
| DirectionThree | Variant | Optional input Vector object that specifies the third direction and length. If not specified (Vector(0,0,1) a default vector(0,0,1) will be used. If this vector is not perpendicular to the DirectionOne and DirectionTwo, an error will occur.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2016
