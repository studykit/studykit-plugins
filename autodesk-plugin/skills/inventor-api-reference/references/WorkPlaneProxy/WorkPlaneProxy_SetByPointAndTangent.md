# WorkPlaneProxy.SetByPointAndTangent Method

Parent Object: [WorkPlaneProxy](../WorkPlaneProxy/WorkPlaneProxy.md)

## Description

Method that redefines the work plane to pass through the input point and tangent to the input surface.

## Syntax

WorkPlaneProxy.**SetByPointAndTangent**( ***Point*** As Object, ***Face*** As [Face](../Face/Face.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | Object | Input object that represents a point. This object can be a Vertex, WorkPoint, SketchPoint3D or SketchPoint object. The input point must lie on the input surface. |
| Face | [Face](../Face/Face.md) | Input Face object that indicates the tangent surface. This face must either be a cylinder, a cone that is positioned such that a valid tangent exists, a sphere or a bspline surface. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |