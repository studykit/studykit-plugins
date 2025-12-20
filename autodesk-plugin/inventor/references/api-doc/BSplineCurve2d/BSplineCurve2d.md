# BSplineCurve2d Object

## Description

The BSplineCurve2d object. For more information, see the Transient Geometry overview.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../BSplineCurve2d/BSplineCurve2d_Copy.md) | Creates a copy of this BSplineCurve2d object. The result is entirely independent and can be edited without affecting the original BSplineCurve2d object. |
| [ExtractPartial](../BSplineCurve2d/BSplineCurve2d_ExtractPartial.md) | Creates a new curve by extracting a portion of an existing curve. |
| [GetBSplineData](../BSplineCurve2d/BSplineCurve2d_GetBSplineData.md) | Get the data defining this B-spline. |
| [GetBSplineInfo](../BSplineCurve2d/BSplineCurve2d_GetBSplineInfo.md) | Gets general information about the definition of the spline, including its order, number of poles and knots, and its rational, periodic, closed, and planar states. |
| [PutBSplineInfoAndData](../BSplineCurve2d/BSplineCurve2d_PutBSplineInfoAndData.md) | Sets the definition data of the spline. |
| [Split](../BSplineCurve2d/BSplineCurve2d_Split.md) | Creates two new curves that are the result of splitting this curve at the specified point. The original curve is left unchanged. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Evaluator](../BSplineCurve2d/BSplineCurve2d_Evaluator.md) | Gets the Curve2dEvaluator for this curve. |
| [PoleAtIndex](../BSplineCurve2d/BSplineCurve2d_PoleAtIndex.md) | Indicates the pole coordinate point at the specified index into the spline's pole vector. |

## Accessed From

[BSplineCurve2d.Copy](../BSplineCurve2d/BSplineCurve2d_Copy.md), [BSplineCurve2d.ExtractPartial](../BSplineCurve2d/BSplineCurve2d_ExtractPartial.md), [BSplineCurve2d.Split](../BSplineCurve2d/BSplineCurve2d_Split.md), [SketchControlPointSpline.Geometry](../SketchControlPointSpline/SketchControlPointSpline_Geometry.md), [SketchControlPointSplineProxy.Geometry](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Geometry.md), [SketchEquationCurve.Geometry](../SketchEquationCurve/SketchEquationCurve_Geometry.md), [SketchEquationCurveProxy.Geometry](../SketchEquationCurveProxy/SketchEquationCurveProxy_Geometry.md), [SketchFixedSpline.Geometry](../SketchFixedSpline/SketchFixedSpline_Geometry.md), [SketchFixedSplineProxy.Geometry](../SketchFixedSplineProxy/SketchFixedSplineProxy_Geometry.md), [SketchOffsetSpline.Geometry](../SketchOffsetSpline/SketchOffsetSpline_Geometry.md), [SketchOffsetSplineProxy.Geometry](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Geometry.md), [SketchSpline.Geometry](../SketchSpline/SketchSpline_Geometry.md), [SketchSplineProxy.Geometry](../SketchSplineProxy/SketchSplineProxy_Geometry.md), [TransientGeometry.CreateBSplineCurve2d](../TransientGeometry/TransientGeometry_CreateBSplineCurve2d.md), [TransientGeometry.CreateFittedBSplineCurve2d](../TransientGeometry/TransientGeometry_CreateFittedBSplineCurve2d.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Approximate Polyline to 3D Curve](../../sample-programs/Approximate3DSketchGeometry_Sample.md) | Draws a polyline that is an approximation of the selected curve. To use this have a part open that contains a 3D skech that contains curves. |
| [Extract a Partial Curve from a Curve](../../sample-programs/ExtractPartial2DCurves_Sample.md) | Demonstrates the ability to extract partial curves from a transient geometry curve. This sample has you select an existing sketch spline and extracts three curves from the curve. It then creates real curves using the extracted curves and deletes the original sketch curve. |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |
| [Split a 2D Curve](../../sample-programs/Split2DCurve_Sample.md) | Demonstrates the ability to extract split curves from a transient geometry curve. This sample has you select an existing sketch spline and splits it at the midpoint of parametric space. It then creates real curves using the split curve results and deletes the original sketch curve. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |