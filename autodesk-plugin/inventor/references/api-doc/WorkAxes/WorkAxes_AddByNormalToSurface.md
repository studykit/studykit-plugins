# WorkAxes.AddByNormalToSurface Method

Parent Object: [WorkAxes](../WorkAxes/WorkAxes.md)

## Description

Method that creates a new work axis that passes through the point and is normal to the input surface. This method is not currently supported when creating a work axis within an assembly.

## Syntax

WorkAxes.**AddByNormalToSurface**( ***Surface*** As Object, ***Point*** As Object, [***Construction***] As Boolean ) As [WorkAxis](../WorkAxis/WorkAxis.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Surface | Object | Input object that represents a surface entity. This object can be a Face (planar or non-planar), a WorkPlane or a PlanarSketch object. |
| Point | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, SketchPoint, or SketchPoint3D object. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work axis as a construction axis or not. The default is False which indicates to create a standard work axis, not a construction work axis. A construction work axis is hidden from the user and is not displayed graphically or listed in the browser. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |