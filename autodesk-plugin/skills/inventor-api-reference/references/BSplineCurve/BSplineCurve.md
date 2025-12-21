# BSplineCurve Object

## Description

The BSplineCurve object is a mathematical utility object that represents a NURBS curve. It is a transient object that is never shown graphically or saved in the Inventor document

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../BSplineCurve/BSplineCurve_Copy.md) | Creates a copy of this BSplineCurve object. The result is entirely independent and can be edited without affecting the original BSplineCurve object. |
| [ExtractPartial](../BSplineCurve/BSplineCurve_ExtractPartial.md) | Creates a new curve by extracting a portion of an existing curve. |
| [GetBSplineData](../BSplineCurve/BSplineCurve_GetBSplineData.md) | Get the data defining this B-spline. |
| [GetBSplineInfo](../BSplineCurve/BSplineCurve_GetBSplineInfo.md) | Gets general information about the definition of the spline, including its order, number of poles and knots, and its rational, periodic, closed, and planar states. |
| [PutBSplineInfoAndData](../BSplineCurve/BSplineCurve_PutBSplineInfoAndData.md) | Sets the definition data of the spline. |
| [Split](../BSplineCurve/BSplineCurve_Split.md) | Creates two new curves that are the result of splitting this curve at the specified point. The original curve is left unchanged. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Evaluator](../BSplineCurve/BSplineCurve_Evaluator.md) | Property that returns an evaluator object for the curve. The evaluator supports general curve evaluation functions. |
| [PoleAtIndex](../BSplineCurve/BSplineCurve_PoleAtIndex.md) | Property that returns the x, y, z position of a specified pole. |

## Accessed From

[BSplineCurve.Copy](../BSplineCurve/BSplineCurve_Copy.md), [BSplineCurve.ExtractPartial](../BSplineCurve/BSplineCurve_ExtractPartial.md), [BSplineCurve.Split](../BSplineCurve/BSplineCurve_Split.md), [SketchControlPointSpline.Geometry3d](../SketchControlPointSpline/SketchControlPointSpline_Geometry3d.md), [SketchControlPointSpline3D.Geometry](../SketchControlPointSpline3D/SketchControlPointSpline3D_Geometry.md), [SketchControlPointSpline3DProxy.Geometry](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_Geometry.md), [SketchControlPointSplineProxy.Geometry3d](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Geometry3d.md), [SketchEquationCurve.Geometry3d](../SketchEquationCurve/SketchEquationCurve_Geometry3d.md), [SketchEquationCurve3D.Geometry](../SketchEquationCurve3D/SketchEquationCurve3D_Geometry.md), [SketchEquationCurve3DProxy.Geometry](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_Geometry.md), [SketchEquationCurveProxy.Geometry3d](../SketchEquationCurveProxy/SketchEquationCurveProxy_Geometry3d.md), [SketchFixedSpline.Geometry3d](../SketchFixedSpline/SketchFixedSpline_Geometry3d.md), [SketchFixedSpline3D.Geometry](../SketchFixedSpline3D/SketchFixedSpline3D_Geometry.md), [SketchFixedSpline3DProxy.Geometry](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Geometry.md), [SketchFixedSplineProxy.Geometry3d](../SketchFixedSplineProxy/SketchFixedSplineProxy_Geometry3d.md), [SketchOffsetSpline.Geometry3d](../SketchOffsetSpline/SketchOffsetSpline_Geometry3d.md), [SketchOffsetSplineProxy.Geometry3d](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Geometry3d.md), [SketchSpline.Geometry3d](../SketchSpline/SketchSpline_Geometry3d.md), [SketchSpline3D.Geometry](../SketchSpline3D/SketchSpline3D_Geometry.md), [SketchSpline3DProxy.Geometry](../SketchSpline3DProxy/SketchSpline3DProxy_Geometry.md), [SketchSplineProxy.Geometry3d](../SketchSplineProxy/SketchSplineProxy_Geometry3d.md), [TransientGeometry.CreateBSplineCurve](../TransientGeometry/TransientGeometry_CreateBSplineCurve.md), [TransientGeometry.CreateFittedBSplineCurve](../TransientGeometry/TransientGeometry_CreateFittedBSplineCurve.md)

## Version

Introduced in version 4
