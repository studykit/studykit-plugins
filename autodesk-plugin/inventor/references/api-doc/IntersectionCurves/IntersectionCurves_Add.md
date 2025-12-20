# IntersectionCurves.Add Method

Parent Object: [IntersectionCurves](../IntersectionCurves/IntersectionCurves.md)

## Description

Creates a new intersection curve.

## Syntax

IntersectionCurves.**Add**( ***EntityOne*** As Object, ***EntityTwo*** As Object ) As [IntersectionCurve](../IntersectionCurve/IntersectionCurve.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Input object that defines the first entity. This can be one of the following: SurfaceBody, Face, WorkPlane or 2D sketch curve object. If a 2D sketch curve is specified, then sketch curves connected with the sketch curve might be automatically included for intersection operation. |
| EntityTwo | Object | Input object that defines the second entity or set of entities being intersected by the first entity. This can be one of the following: SurfaceBody, Face, Faces, FaceCollection, WorkPlane or 2D sketch curve object with the following restrictions: * If the EntityOne is a WorkPlane then EntityTwo cannot be a WorkPlane. * If a Faces or FaceCollection object is provided, all the Face objects in the collection must belong to the same SurfaceBody. * If EntityOne is a 2D sketch curve, then EntityTwo must also be a 2D sketch curve in a different 2D sketch. The 2D sketch curves connected with the one specified as EntityTwo might be automatically included for intersection operation. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Control point, equation, and intersection curve creation.](../../sample-programs/AdvancedCurveCreation_Sample.md) | This sample demonstrates several new curve creation techniques introduced in Inventor 2014. It creates a new part and then create a 2d control point spline and a 2d equation curve. Surfaces are created from these two curves by extruding them. A 3d intersection curve is created between the extrusions. A 3d control point spline and 3d equation curve are also created. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |