# SketchSplines.Add Method

Parent Object: [SketchSplines](../SketchSplines/SketchSplines.md)

## Description

Method that creates a sketch spline through the set of input points.

## Syntax

SketchSplines.**Add**( ***FitPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***FitMethod***] As [SplineFitMethodEnum](../SplineFitMethodEnum.md) ) As [SketchSpline](../SketchSpline/SketchSpline.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FitPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the set of points to fit the curve through. The points can be either existing SketchPoint objects or Point2d objects. If a Point2d object is input a SketchPoint is automatically created at that position. The curve passes through all of the fit points and is related to them by SplineFitPointConstraints, which are also automatically created. |
| FitMethod | [SplineFitMethodEnum](../SplineFitMethodEnum.md) | Property that indicates the fit method (SplineFitMethodEnum) used for the spline. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |
| [Sketch Spline](../../sample-programs/SketchSpline_Sample.md) | This sample demonstrates creating and manipulating a sketch spline. |

## Version

Introduced in version 5
