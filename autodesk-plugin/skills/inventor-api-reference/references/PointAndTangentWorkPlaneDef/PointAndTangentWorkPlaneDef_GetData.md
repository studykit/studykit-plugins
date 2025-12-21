# PointAndTangentWorkPlaneDef.GetData Method

Parent Object: [PointAndTangentWorkPlaneDef](../PointAndTangentWorkPlaneDef/PointAndTangentWorkPlaneDef.md)

## Description

Method that gets all of the data defining a work that passes through a point and is tangent to the input face.

## Syntax

PointAndTangentWorkPlaneDef.**GetData**( ***Point*** As Object, ***Face*** As [Face](../Face/Face.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | Object | Output object that represents a point. This object can be a Vertex, WorkPoint, or SketchPoint, or SketchPoint3D object. The work plane passes through this point. |
| Face | [Face](../Face/Face.md) | Output Face object that indicates the tangent surface. This face will be a cylinder, cone, sphere or a bspline surface. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |