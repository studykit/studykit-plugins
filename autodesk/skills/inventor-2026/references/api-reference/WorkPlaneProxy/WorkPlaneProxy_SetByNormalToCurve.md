# WorkPlaneProxy.SetByNormalToCurve Method

Parent Object: [WorkPlaneProxy](../WorkPlaneProxy/WorkPlaneProxy.md)

## Description

Method that redefines the work plane to pass through the input point and normal to the input curve.

## Syntax

WorkPlaneProxy.**SetByNormalToCurve**( ***CurveEntity*** As Object, ***Point*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CurveEntity | Object | Input object that represents a curve entity. This object can be an Edge, 3D sketch entity, 2D sketch entity or a WorkAxis. For an Edge or 3D sketch entity the geometry must be a Spline, Arc, Circle, EllipticalArc, or Ellipse. For a 2D sketch entity, the geometry must be a Spline2d, Arc2d, Circle2d, EllipticalArc2d, or Ellipse2d. |
| Point | Object | Input object that represents a point, The point must lie on the curve, as described below. This object can be a WorkPoint, Vertex, SketchPoint, or SketchPoint3D object. If the input curve is a 2D sketch entity, the point must be a SketchPoint that meets one of the following conditions: start or end point of the curve, one of the fit points of a spline, or constrained to the curve with a coincident constraint. If the input curve is a 3D curve, the point must be related to the curve. For a 3D point to be related to a 3D curve, it can be the start, mid, or end point of the curve. |

## Version

Introduced in version 2008
