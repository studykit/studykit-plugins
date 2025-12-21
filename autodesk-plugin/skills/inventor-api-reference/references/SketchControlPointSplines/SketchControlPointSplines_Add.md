# SketchControlPointSplines.Add Method

Parent Object: [SketchControlPointSplines](../SketchControlPointSplines/SketchControlPointSplines.md)

## Description

Method that creates a control point spline based on the set of input points that define the vertices of the control polygon. A closed spline is created when the start and end points have the same coordinate.

## Syntax

SketchControlPointSplines.**Add**( ***ControlPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md) ) As [SketchControlPointSpline](../SketchControlPointSpline/SketchControlPointSpline.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ControlPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | A collection of the points that defines the position of the control points. The inputs can be combination of Point2d and SketchPoint objects. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Control point, equation, and intersection curve creation.](../../sample-programs/AdvancedCurveCreation_Sample.md) | This sample demonstrates several new curve creation techniques introduced in Inventor 2014. It creates a new part and then create a 2d control point spline and a 2d equation curve. Surfaces are created from these two curves by extruding them. A 3d intersection curve is created between the extrusions. A 3d control point spline and 3d equation curve are also created. |

## Version

Introduced in version 2014
