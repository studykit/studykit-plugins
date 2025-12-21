# WorkPlanes.AddByNormalToCurve Method

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Method that creates a new work plane that passes through the point and is normal to the input curve. The point must lie on the curve, as described below. This method is not currently supported when creating a work plane within an assembly.

## Syntax

WorkPlanes.**AddByNormalToCurve**( ***CurveEntity*** As Object, ***Point*** As Object, [***Construction***] As Boolean ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CurveEntity | Object | Input object that represents a curve entity. This object can be an Edge, 3D sketch entity, or a 2D sketch entity. For an Edge or 3D sketch entity the geometry must be a Spline, Arc, Circle, EllipticalArc, or Ellipse. For a 2D sketch entity, the geometry must be a Spline2d, Arc2d, Circle2d, EllipticalArc2d, or Ellipse2d. |
| Point | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, SketchPoint, or SketchPoint3D object. If the input curve is a 2D sketch entity, the point must be a SketchPoint that meets one of the following conditions: start or end point of the curve, one of the fit points of a spline, or constrained to the curve with a coincident constraint. If the input curve is a 3D curve, the point must be related to the curve. For a 3D point to be related to a 3D curve, it can be the start, mid, or end point of the curve. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work plane as a construction plane or not. The default is False which indicates to create a standard work plane, not a construction work plane. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction:  * Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. * If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |