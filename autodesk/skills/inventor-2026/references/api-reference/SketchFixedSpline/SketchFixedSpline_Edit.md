# SketchFixedSpline.Edit Method

Parent Object: [SketchFixedSpline](../SketchFixedSpline/SketchFixedSpline.md)

## Description

Method that edits a fixed sketch spline based on an input NURBS definition.

## Syntax

SketchFixedSpline.**Edit**( ***SplineCurve*** As [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md), [***StartPoint***] As Variant, [***EndPoint***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SplineCurve | [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md) | Input BSplineCurve2d geometry object that contains the definition of a curve that will be used to redefine the spline. |
| StartPoint | Variant | Optional input SketchPoint object that contains the start point to fit the curve through. If this argument is not specified, a sketch point is created at the point defined by the start point of the input BSplineCurve2d and the resulting spline is constrained to it. |
| EndPoint | Variant | Optional input SketchPoint that contains the end point to fit the curve through. If this argument is not specified, a sketch point is created at the point defined by the end point of the input BSplineCurve2d and the resulting spline is constrained to it.   This is an optional argument whose default value is null. |

## Version

Introduced in version 9
