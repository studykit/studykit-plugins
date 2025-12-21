# WorkPlanes.AddByPointAndTangent Method

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Method that creates a new work plane through the input point and tangent to the input surface. The input point must lie on the input surface. This method is not currently supported when creating a work plane within an assembly.

## Syntax

WorkPlanes.**AddByPointAndTangent**( ***Point*** As Object, ***Face*** As [Face](../Face/Face.md), [***Construction***] As Boolean ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | Object | Input object that represents a point. This object can be a Vertex, WorkPoint, SketchPoint3D, or SketchPoint object. |
| Face | [Face](../Face/Face.md) | Input Face object that indicates the tangent surface. This face must either be a cylinder, a cone that is positioned such that a valid tangent exists, a sphere, or a bspline surface. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work plane as a construction plane or not. The default is False, which indicates to create a standard work plane, not a construction work plane. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |