# WorkPlane.SetByThreePoints Method

Parent Object: [WorkPlane](../WorkPlane/WorkPlane.md)

## Description

Method that redefines the work plane to be based on the three input points.

## Remarks

The three input points must be unique non-coincident points. Point1 to Point2 defines the positive X axis and Point3 defines the positive Y direction. This method is not valid when the work plane exists in an Assembly component definition.

## Syntax

WorkPlane.**SetByThreePoints**( ***Point1*** As Object, ***Point2*** As Object, ***Point3*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point1 | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, SketchPoint, or SketchPoint3D object. |
| Point2 | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, SketchPoint, or SketchPoint3D object. |
| Point3 | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, SketchPoint, or SketchPoint3D object. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |