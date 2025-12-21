# SketchSpline3DProxy.Disconnect Method

Parent Object: [SketchSpline3DProxy](../SketchSpline3DProxy/SketchSpline3DProxy.md)

## Description

Method that removes an existing fit point from the spline. This method can have the effect of deleting the sketch point if it is not associated with any other sketch entity.

## Syntax

SketchSpline3DProxy.**Disconnect**( ***FitPoint*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FitPoint | Variant | Input Variant value that specifies the point to disconnect. This can be either a numeric value indicating the index of the fit point (the indices corresponding to the fit points in order from the start to the end of the spline, where the first fit point has an index of 1) or it can be an existing fit point. |

## Version

Introduced in version 8

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |