# WorkPlanes.AddByThreePoints Method

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Method that creates a new work plane based on the three input points. The three input points must be unique non-coincident points. Point1 to Point2 defines the positive X axis and Point3 defines the positive Y direction. This method is not currently supported when creating a work plane within an assembly.

## Syntax

WorkPlanes.**AddByThreePoints**( ***Point1*** As Object, ***Point2*** As Object, ***Point3*** As Object, [***Construction***] As Boolean ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point1 | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, or SketchPoint object. |
| Point2 | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, or SketchPoint object. |
| Point3 | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, or SketchPoint object. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work plane as a construction plane or not. The default is False, which indicates to create a standard work plane, not a construction work plane. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction:  * Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. * If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |