# BSplineSurface Object

## Description

The BSplineSurface object represent a surface curved according to BSpline poles, order, weights, and knots.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../BSplineSurface/BSplineSurface_Copy.md) | Creates a copy of this BSplineSurface object. The result is entirely independent and can be edited without affecting the original BSplineSurface object. |
| [GetBSplineData](../BSplineSurface/BSplineSurface_GetBSplineData.md) | Get the data defining this B-spline. |
| [GetBSplineInfo](../BSplineSurface/BSplineSurface_GetBSplineInfo.md) | Gets general information about the definition of the spline, including its order, number of poles and knots, and its rational, periodic, closed, and planar states. |
| [PutBSplineInfoAndData](../BSplineSurface/BSplineSurface_PutBSplineInfoAndData.md) | Sets the definition data of the spline surface. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Evaluator](../BSplineSurface/BSplineSurface_Evaluator.md) | Gets the surface evaluator for this surface. |
| [PoleAtIndex](../BSplineSurface/BSplineSurface_PoleAtIndex.md) | Indicates the pole coordinate point at the specified UV indices into the spline's pole array. |

## Accessed From

[BSplineSurface.Copy](../BSplineSurface/BSplineSurface_Copy.md), [TransientGeometry.CreateBSplineSurface](../TransientGeometry/TransientGeometry_CreateBSplineSurface.md)

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |