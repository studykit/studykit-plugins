# SketchSplineProxy.InsertFitPoint Method

Parent Object: [SketchSplineProxy](../SketchSplineProxy/SketchSplineProxy.md)

## Description

Method that inserts a new fit point into the spline.

## Syntax

SketchSplineProxy.**InsertFitPoint**( ***FitPoint*** As Object, [***TargetIndex***] As Long, [***InsertBefore***] As Boolean ) As [SketchPoint](../SketchPoint/SketchPoint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FitPoint | Object | Input object that specifies the position of the new fit point. This can be either a SketchPoint or Point2d object. In the case where a Point2d object is input, a SketchPoint will be created at that location. |
| TargetIndex | Long | Input Long that specifies the existing fit point to insert the new fit point next to. |
| InsertBefore | Boolean | Input Boolean indicating if the fit point should be inserted before or after the target index.   This is an optional argument whose default value is True. |

## Version

Introduced in version 6
