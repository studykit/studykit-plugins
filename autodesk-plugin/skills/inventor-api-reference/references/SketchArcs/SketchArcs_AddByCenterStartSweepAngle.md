# SketchArcs.AddByCenterStartSweepAngle Method

Parent Object: [SketchArcs](../SketchArcs/SketchArcs.md)

## Description

Method that creates a new sketch arc using the input point and angles.

## Syntax

SketchArcs.**AddByCenterStartSweepAngle**( ***CenterPoint*** As Object, ***Radius*** As Double, ***StartAngle*** As Double, ***SweepAngle*** As Double ) As [SketchArc](../SketchArc/SketchArc.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CenterPoint | Object | Input object that defines the center point. This can be either a SketchPoint or Point2d object. In the case where a SketchPoint object is input, the center point of the arc will be attached to the sketch point. |
| Radius | Double | Input Double that defines the radius of the arc in centimeters. |
| StartAngle | Double | Input Double that defines the start angle in radians. The start angle is defined with respect to the sketch x-axis. |
| SweepAngle | Double | Input Double that defines the sweep angle in radians. The sweep is in a counter-clockwise direction from the start. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creates an Arc Length Dimension Constraint](../../sample-programs/ArcLengthDimConstraint_Sample.md) | Demonstrates creating an arc length dimension constraint. |

## Version

Introduced in version 5
