# Polyline2d Object

## Description

The Polyline2d object is a mathematical utility object that represents a set of connected line segments in a two dimension space. It is a transient object that is never shown graphically or saved in the Inventor document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../Polyline2d/Polyline2d_Copy.md) | Creates a copy of this Polyline2d object. The result is entirely independent and can be edited without affecting the original Polyline2d object. |
| [GetPoints](../Polyline2d/Polyline2d_GetPoints.md) | Method that returns the points defining the shape of the polyline. |
| [PutPoints](../Polyline2d/Polyline2d_PutPoints.md) | Method that sets all of the coordinates of the polyline. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Evaluator](../Polyline2d/Polyline2d_Evaluator.md) | Property that returns an evaluator object for the curve. The evaluator supports general curve evaluation functions. |
| [PointAtIndex](../Polyline2d/Polyline2d_PointAtIndex.md) | Gets or sets the x, y position of a specified point. |
| [PointCount](../Polyline2d/Polyline2d_PointCount.md) | Property that returns the number of points defining the polyline. |

## Accessed From

[Polyline2d.Copy](../Polyline2d/Polyline2d_Copy.md), [TransientGeometry.CreatePolyline2d](../TransientGeometry/TransientGeometry_CreatePolyline2d.md), [TransientGeometry.CreatePolyline2dFromCurve](../TransientGeometry/TransientGeometry_CreatePolyline2dFromCurve.md)

## Version

Introduced in version 2009
