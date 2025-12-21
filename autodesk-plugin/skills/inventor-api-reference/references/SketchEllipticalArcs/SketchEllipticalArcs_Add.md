# SketchEllipticalArcs.Add Method

Parent Object: [SketchEllipticalArcs](../SketchEllipticalArcs/SketchEllipticalArcs.md)

## Description

Method that creates a new sketch elliptical arc.

## Syntax

SketchEllipticalArcs.**Add**( ***CenterPoint*** As Object, ***MajorAxisVector*** As [UnitVector2d](../UnitVector2d/UnitVector2d.md), ***MajorRadius*** As Double, ***MinorRadius*** As Double, ***StartAngle*** As Double, ***SweepAngle*** As Double ) As [SketchEllipticalArc](../SketchEllipticalArc/SketchEllipticalArc.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CenterPoint | Object | Input object that defines the center point. This can be either a SketchPoint or Point2d object. In the case where a SketchPoint object is input, the ellipse will be attached to the point. |
| MajorAxisVector | [UnitVector2d](../UnitVector2d/UnitVector2d.md) | Input UnitVector2d that defines the direction of the major axis. |
| MajorRadius | Double | Input Double that defines the major radius in centimeters. |
| MinorRadius | Double | Input Double that defines the minor radius in centimeters. |
| StartAngle | Double | Input Double that defines the start angle in radians. The start angle is defined with respect to the major axis. |
| SweepAngle | Double | Input Double that defines the sweep angle in radians. The sweep is in a counter-clockwise direction from the start angle. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sketch elliptical arc](../../sample-programs/SketchEllipticalArc_Sample.md) | This sample demonstrates creating an elliptical arc in a sketch and dimensioning its minor radius. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |