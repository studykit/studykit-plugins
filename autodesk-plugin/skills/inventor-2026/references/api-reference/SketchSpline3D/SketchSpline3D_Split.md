# SketchSpline3D.Split Method

Parent Object: [SketchSpline3D](../SketchSpline3D/SketchSpline3D.md)

## Description

Method that splits the spline at the specified location. After the split, the original object (the one on which this method was called) represents the part of the spline associated with the original start point. The SketchSpline3D object returned by this method represents the part of the spline associated with the original end point. The curvature of the final result may differ from the original spline.

## Syntax

SketchSpline3D.**Split**( ***FitPoint*** As Variant ) As [SketchSpline3D](../SketchSpline3D/SketchSpline3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FitPoint | Variant | Input Variant value that specifies the location at which to split the spline. This can be either a numeric value indicating the index of the fit point (the indices corresponding to the fit points in order from the start to the end of the spline, where the first fit point has an index of 1) or it can be an existing fit point. |

## Version

Introduced in version 8
