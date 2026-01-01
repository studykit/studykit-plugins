# SketchSpline3D.InsertFitPoint Method

Parent Object: [SketchSpline3D](../SketchSpline3D/SketchSpline3D.md)

## Description

Method that inserts a new fit point into the spline and returns the inserted fit point.

## Syntax

SketchSpline3D.**InsertFitPoint**( ***FitPoint*** As Object, [***TargetIndex***] As Long, [***InsertBefore***] As Boolean ) As [SketchPoint3D](../SketchPoint3D/SketchPoint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FitPoint | Object | Input object that specifies the position of the new fit point. This can be a , a SketchPoint, a workpoint or a vertex. If the input is not a SketchPoint3D object, a SketchPoint3D object is automatically created at the position of the input point. |
| TargetIndex | Long | Optional input Long that specifies the existing fit point to insert the new fit point next to. If not supplied, this value defaults to 0. If the value is 0, then the new fit point is inserted between the two existing fit points that are closest to the new fit point. |
| InsertBefore | Boolean | Optional input Boolean indicating if the fit point should be inserted before or after the target index. The default is true, meaning that the new fit point will be inserted before the target index. This Boolean is ignored if the TargetIndex specified is 0.   This is an optional argument whose default value is True. |

## Version

Introduced in version 8
