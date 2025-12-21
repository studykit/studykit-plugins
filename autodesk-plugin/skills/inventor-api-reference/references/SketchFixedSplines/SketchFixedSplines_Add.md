# SketchFixedSplines.Add Method

Parent Object: [SketchFixedSplines](../SketchFixedSplines/SketchFixedSplines.md)

## Description

Method that creates a fixed spline based on an input NURBS definition.

## Syntax

SketchFixedSplines.**Add**( ***SplineCurve*** As [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md), [***StartPoint***] As Variant, [***EndPoint***] As Variant ) As [SketchFixedSpline](../SketchFixedSpline/SketchFixedSpline.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SplineCurve | [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md) | Input BSplineCurve2d geometry object that contains the definition of a curve from which to create a SketchFixedSpline. |
| StartPoint | Variant | Optional input SketchPoint object that contains the start point to fit the curve through. If this argument is not specified, a sketch point is created at the point defined by the start point of the input BSplineCurve2d and the resulting spline is constrained to it. |
| EndPoint | Variant | Optional input SketchPoint that contains the end point to fit the curve through. If this argument is not specified, a sketch point is created at the point defined by the end point of the input BSplineCurve2d and the resulting spline is constrained to it.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extract a Partial Curve from a Curve](../../sample-programs/ExtractPartial2DCurves_Sample.md) | Demonstrates the ability to extract partial curves from a transient geometry curve. This sample has you select an existing sketch spline and extracts three curves from the curve. It then creates real curves using the extracted curves and deletes the original sketch curve. |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |
| [Split a 2D Curve](../../sample-programs/Split2DCurve_Sample.md) | Demonstrates the ability to extract split curves from a transient geometry curve. This sample has you select an existing sketch spline and splits it at the midpoint of parametric space. It then creates real curves using the split curve results and deletes the original sketch curve. |

## Version

Introduced in version 9
