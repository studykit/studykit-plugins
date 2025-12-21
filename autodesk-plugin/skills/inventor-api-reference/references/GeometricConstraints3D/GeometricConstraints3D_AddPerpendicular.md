# GeometricConstraints3D.AddPerpendicular Method

Parent Object: [GeometricConstraints3D](../GeometricConstraints3D/GeometricConstraints3D.md)

## Description

Method that creates a new perpendicular constraint between the two input entities. This method will fail if the constraint overconstrains the sketch.

## Remarks

The constraint can currently be applied between a 3D sketch line and another 3D sketch line, a work axis, linear edge, work plane or a surface (face).

## Syntax

GeometricConstraints3D.**AddPerpendicular**( ***EntityOne*** As Object, ***EntityTwo*** As Object, [***Reserved1***] As Boolean, [***Reserved2***] As Boolean ) As [PerpendicularConstraint3D](../PerpendicularConstraint3D/PerpendicularConstraint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Object that specifies the first entity to be constrained. |
| EntityTwo | Object | Object that specifies the second entity to be constrained. |
| Reserved1 | Boolean | This argument is reserved for future use and is currently ignored. |
| Reserved2 | Boolean | This argument is reserved for future use and is currently ignored.   This is an optional argument whose default value is True. |

## Version

Introduced in version 11
