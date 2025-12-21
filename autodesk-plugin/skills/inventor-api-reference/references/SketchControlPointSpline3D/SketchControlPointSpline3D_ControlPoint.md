# SketchControlPointSpline3D.ControlPoint Property

Parent Object: [SketchControlPointSpline3D](../SketchControlPointSpline3D/SketchControlPointSpline3D.md)

## Description

Read-only property that returns the SketchPoint3D at the specified index. The indices correspond to the control points in order from the start to the end of the spline. The ControlPointCount property returns the total number of control points for the spline. Deleting the returned sketch point will delete the control point from the spline.

## Syntax

SketchControlPointSpline3D.**ControlPoint**( ***Index*** As Long ) As [SketchPoint3D](../SketchPoint3D/SketchPoint3D.md)

## Property Value

This is a read only property whose value is a [SketchPoint3D](../SketchPoint3D/SketchPoint3D.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | The index of the control point to return. The first control point has an index of 1. |

## Version

Introduced in version 2014
