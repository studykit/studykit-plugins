# SketchControlPointSplineProxy.ControlPoint Property

Parent Object: [SketchControlPointSplineProxy](../SketchControlPointSplineProxy/SketchControlPointSplineProxy.md)

## Description

Read-only property that returns the SketchPoint at the specified index. The indices correspond to the control points in order from the start to the end of the spline. An Index of 1 returns the first SketchPoint. The ControlPointCount property returns the total number of control points for the spline. Deleting the returned sketch point will delete the control point from the spline.

## Syntax

SketchControlPointSplineProxy.**ControlPoint**( ***Index*** As Long ) As [SketchPoint](../SketchPoint/SketchPoint.md)

## Property Value

This is a read only property whose value is a [SketchPoint](../SketchPoint/SketchPoint.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | The index of the control point to return. The first control point has in index of 1. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |