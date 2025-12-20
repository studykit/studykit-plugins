# MeasureTools.GetAngle Method

Parent Object: [MeasureTools](../MeasureTools/MeasureTools.md)

## Description

Method that returns the angle between the input entities. The input entities must all belong to the same document, unless they are transient objects.

## Syntax

MeasureTools.**GetAngle**( ***EntityOne*** As Object, ***EntityTwo*** As Object, [***EntityThree***] As Variant ) As Double

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Object that specifies the first entity. Valid inputs include Face, Edge, Vertex, transient objects (Point, Plane, Cylinder, etc.), work features, 2d and 3d sketch entities, DrawingViewCurve and GeometryIntent objects. Proxy object inputs are supported for assembly documents. For spherical and circular entity inputs, the center is assumed. For cylindrical and conical inputs, the axis is assumed. For toroidal inputs, the axis is assumed, unless the third argument of the method is also supplied in which case the center is assumed. For position inputs (such as Vertex, WorkPoint, Point, etc.) to be valid, all three inputs to the method should be supplied and they must all be position inputs (this implies a 3-point angle measurement). |
| EntityTwo | Object | Input object that specifies the second entity. Valid inputs include Face, Edge, Vertex, transient objects (Point, Plane, Cylinder, etc.), work features, 2d and 3d sketch entities, DrawingViewCurve and GeometryIntent objects. Proxy object inputs are supported for assembly documents. For spherical and circular entity inputs, the center is assumed. For cylindrical and conical inputs, the axis is assumed. For toroidal inputs, the axis is assumed, unless the third argument of the method is also supplied in which case the center is assumed. For position inputs (such as Vertex, WorkPoint, Point, etc.) to be valid, all three inputs to the method should be supplied and they must all be position inputs (this implies a 3-point angle measurement). |
| EntityThree | Variant | Optional input object that specifies the third entity for a 3-point angle measurement. Valid inputs include spherical & toroidal Face, Vertex, transient objects defining a position (Point, Sphere, etc.), work points, 2d & 3d sketch points, and GeometryIntent objects. Proxy object inputs are supported for assembly documents. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |