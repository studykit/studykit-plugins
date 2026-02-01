# SketchControlPointSpline.ControlPolygonSide Property

Parent Object: [SketchControlPointSpline](../SketchControlPointSpline/SketchControlPointSpline.md)

## Description

Read-only property that returns the SketchLine that represents a side of the control polygon. The indices correspond to the control polygon edges in order from the start to the end of the spline. An Index of 1 returns the first edge, with the last side being ControlPointCount -1 since there is one less side than number of control points.

## Syntax

SketchControlPointSpline.**ControlPolygonSide**( ***Index*** As Long ) As [SketchLine](../SketchLine/SketchLine.md)

## Property Value

This is a read only property whose value is a [SketchLine](../SketchLine/SketchLine.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | The index of the polygon side to return. The first side has an index of 1. |

## Version

Introduced in version 2014
