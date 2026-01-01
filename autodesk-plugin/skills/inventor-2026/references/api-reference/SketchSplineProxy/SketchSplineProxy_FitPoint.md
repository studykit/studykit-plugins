# SketchSplineProxy.FitPoint Property

Parent Object: [SketchSplineProxy](../SketchSplineProxy/SketchSplineProxy.md)

## Description

Property that returns the SketchPoint at the specified index. The indices correspond to the fit points in order from the start to the end of the spline. An Index of 1 returns the first SketchPoint. The FitPointCount property returns the total number of fits points for the spline.

## Syntax

SketchSplineProxy.**FitPoint**( ***Index*** As Long ) As [SketchPoint](../SketchPoint/SketchPoint.md)

## Property Value

This is a read only property whose value is a [SketchPoint](../SketchPoint/SketchPoint.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long value that specifies the index of the SketchPoint to return. |

## Version

Introduced in version 6
