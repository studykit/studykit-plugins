# SketchControlPointSpline3DProxy.ControlPolygonSide Property

Parent Object: [SketchControlPointSpline3DProxy](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy.md)

## Description

Read-only property that returns the SketchLine3D object that represents a side of the control polygon. The indices correspond to the control polygon edges in order from the start to the end of the spline.

## Syntax

SketchControlPointSpline3DProxy.**ControlPolygonSide**( ***Index*** As Long ) As [SketchLine3D](../SketchLine3D/SketchLine3D.md)

## Property Value

This is a read only property whose value is a [SketchLine3D](../SketchLine3D/SketchLine3D.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | The index of the control polygon side to return. An Index of 1 returns the first edge, with the last side being ControlPointCount -1 since there is one less side than number of control points. |

## Version

Introduced in version 2014
