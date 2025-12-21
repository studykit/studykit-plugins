# SketchArcs3D.AddByCenterStartSweepAngle Method

Parent Object: [SketchArcs3D](../SketchArcs3D/SketchArcs3D.md)

## Description

Method that creates a new sketch arc using the input point and angles.

## Syntax

SketchArcs3D.**AddByCenterStartSweepAngle**( ***CenterPoint*** As Object, ***Normal*** As [UnitVector](../UnitVector/UnitVector.md), ***ReferenceVector*** As [UnitVector](../UnitVector/UnitVector.md), ***Radius*** As Double, ***StartAngle*** As Double, ***SweepAngle*** As Double ) As [SketchArc3D](../SketchArc3D/SketchArc3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CenterPoint | Object | Input object that defines the center point. This can currently only be a Point object. |
| Normal | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector that defines the normal direction for the arc. |
| ReferenceVector | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector that defines the reference vector. The ReferenceVector is the direction that is used to measure the start and the end angles of the arc. In other words, the ReferenceVector represents the zero angle and the start and end angles are measure with respect to this vector. |
| Radius | Double | Input Double that defines the radius of the arc in centimeters. |
| StartAngle | Double | Input Double that defines the start angle in radians. The start angle is defined with respect to the sketch x-axis. |
| SweepAngle | Double | Input Double that defines the sweep angle in radians. The sweep is in a counter-clockwise direction from the start. |

## Version

Introduced in version 2008
