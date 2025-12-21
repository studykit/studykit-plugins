# IntersectionCurveProxy.Edit Method

Parent Object: [IntersectionCurveProxy](../IntersectionCurveProxy/IntersectionCurveProxy.md)

## Description

Method that edits all of the inputs used to compute the intersection curve. This method is more efficient than setting each of the individual properties since this will result in a single compute rather than computing after each property edit.

## Syntax

IntersectionCurveProxy.**Edit**( ***EntityOne*** As Object, ***EntityTwo*** As Object ) As [IntersectionCurve](../IntersectionCurve/IntersectionCurve.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Input object that defines the first entity. This can be one of the following: SurfaceBody, Face, WorkPlane or 2D sketch curve object. If a 2D sketch curve is specified, the sketch curves connected with the sketch curve might be automatically included for intersection operation. |
| EntityTwo | Object | Input object that defines the second entity or set of entities being intersected by the first entity. This can be one of the following: SurfaceBody, Face, Faces, FaceCollection, WorkPlane or 2D sketch curve object with the following restrictions:   * If the EntityOne is a WorkPlane then EntityTwo cannot be a WorkPlane. * If a Faces or FaceCollection object is provided, all the Face objects in the collection must belong to the same SurfaceBody. * If EntityOne is a 2D sketch curve, then EntityTwo must also be a 2D sketch curve in a different 2D sketch. The 2D sketch curves connected with the one specified as EntityTwo might be automatically included for intersection operation. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |