# TransientGeometry.CreateEllipticalCylinder Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new EllipticalCylinder object. The object created is a transient mathematical object and is not displayed graphically

## Syntax

TransientGeometry.**CreateEllipticalCylinder**( ***BasePoint*** As [Point](../Point/Point.md), ***AxisVector*** As [UnitVector](../UnitVector/UnitVector.md), ***MajorAxisVector*** As [Vector](../Vector/Vector.md), ***MinorMajorRatio*** As Double ) As [EllipticalCylinder](../EllipticalCylinder/EllipticalCylinder.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BasePoint | [Point](../Point/Point.md) | Input Point object that specifies the base of the elliptical cylinder. |
| AxisVector | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector object that specifies the direction of the axis of the elliptical cylinder. |
| MajorAxisVector | [Vector](../Vector/Vector.md) | Input Vector object that specifies the direction of the major axis of the elliptical cylinder. |
| MinorMajorRatio | Double | Input Double that specifies the ratio of the minor and major axes of the elliptical cylinder. |

## Version

Introduced in version 4
