# SketchPoint3DProxy.ConnectTo Method

Parent Object: [SketchPoint3DProxy](../SketchPoint3DProxy/SketchPoint3DProxy.md)

## Description

Method that connects this sketch point to the input point. Valid inputs are SketchPoint3D, SketchPoint, Vertex or WorkPoint. This method is the UI equivalent of 'Add Coincident Constraint'. The point being constrained is the sketch point on which this method is called and the input point is the constraining point. This method will fail if a coincident constraint exists between this sketch point and a vertex; i.e. this sketch point must be underconstrained.

## Syntax

SketchPoint3DProxy.**ConnectTo**( ***ConstrainingPoint*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ConstrainingPoint | Object | Input SketchPoint3D, Vertex or Workpoint to use as the constraining point. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |