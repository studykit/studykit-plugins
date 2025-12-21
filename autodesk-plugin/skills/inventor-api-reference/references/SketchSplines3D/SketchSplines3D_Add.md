# SketchSplines3D.Add Method

Parent Object: [SketchSplines3D](../SketchSplines3D/SketchSplines3D.md)

## Description

Method that creates a sketch spline through the set of input points.

## Syntax

SketchSplines3D.**Add**( ***FitPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***FitMethod***] As [SplineFitMethodEnum](../SplineFitMethodEnum.md) ) As [SketchSpline3D](../SketchSpline3D/SketchSpline3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FitPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input that contains the set of points to fit the curve through. The points can be either existing SketchPoint3D objects, SketchPointobjects, workpoints or vertices. If the input is not a SketchPoint3D object, a SketchPoint3D object is automatically created at the position of the input point. The curve passes through all of the fit points and is related to them by the SplineFitPointsConstraint3D object, which is also automatically created. |
| FitMethod | [SplineFitMethodEnum](../SplineFitMethodEnum.md) | Property that indicates the fit method (SplineFitMethodEnum) used for the spline. |

## Version

Introduced in version 8
