# Polyline3d Object

## Description

The Polyline3d object is a mathematical utility object that represents a set of connected line segments. It is a transient object that is never shown graphically or saved in the Inventor document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../Polyline3d/Polyline3d_Copy.md) | Creates a copy of this Polyline3d object. The result is entirely independent and can be edited without affecting the original Polyline3d object. |
| [GetPoints](../Polyline3d/Polyline3d_GetPoints.md) | Method that returns the points defining the shape of the polyline. |
| [PutPoints](../Polyline3d/Polyline3d_PutPoints.md) | Method that sets all of the coordinates of the polyline. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Evaluator](../Polyline3d/Polyline3d_Evaluator.md) | Property that returns an evaluator object for the curve. The evaluator supports general curve evaluation functions. |
| [PointAtIndex](../Polyline3d/Polyline3d_PointAtIndex.md) | Gets or sets the x, y, z position of a specified point. |
| [PointCount](../Polyline3d/Polyline3d_PointCount.md) | Property that returns the number of points defining the polyline. |

## Accessed From

[Polyline3d.Copy](../Polyline3d/Polyline3d_Copy.md), [TransientGeometry.CreatePolyline3d](../TransientGeometry/TransientGeometry_CreatePolyline3d.md), [TransientGeometry.CreatePolyline3dFromCurve](../TransientGeometry/TransientGeometry_CreatePolyline3dFromCurve.md)

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |