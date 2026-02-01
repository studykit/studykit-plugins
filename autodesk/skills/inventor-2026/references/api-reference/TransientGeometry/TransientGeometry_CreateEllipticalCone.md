# TransientGeometry.CreateEllipticalCone Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new EllipticalCone object. The object created is a transient mathematical object and is not displayed graphically

## Syntax

TransientGeometry.**CreateEllipticalCone**( ***BasePoint*** As [Point](../Point/Point.md), ***AxisVector*** As [UnitVector](../UnitVector/UnitVector.md), ***MajorAxisVector*** As [Vector](../Vector/Vector.md), ***MinorMajorRatio*** As Double, ***HalfAngle*** As Double, ***IsExpanding*** As Boolean ) As [EllipticalCone](../EllipticalCone/EllipticalCone.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BasePoint | [Point](../Point/Point.md) | Input Point object that specifies the base of the elliptical cone. |
| AxisVector | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector object that specifies the direction of the axis of the elliptical cone. |
| MajorAxisVector | [Vector](../Vector/Vector.md) | Input Vector object that specifies the direction of the major axis of the elliptical cone. |
| MinorMajorRatio | Double | Input Double that specifies the ratio of the minor and major axes of the elliptical cone. |
| HalfAngle | Double | Input Double that specifies the taper angle of the elliptical cone. This is the angle measured from the axis to the side of the elliptical cone. |
| IsExpanding | Boolean | Input Boolean that if the taper of the elliptical cone is expanding outwards or inwards in the direction of the axis vector. If True and the HalfAngle is positive, then the elliptical cone is expanding outward along the axis vector. |

## Version

Introduced in version 4
