# DrawingCurveSegment.Geometry Property

Parent Object: [DrawingCurveSegment](../DrawingCurveSegment/DrawingCurveSegment.md)

## Description

Read-only property that returns a 2d geometry object that represents this drawing curve segment in sheet space. The true drawing curve is 3d geometry and this is a flattened 2d version. As a result the geometry type can be different. For example a 3d circle can flatten to a 2d ellipse or a line if the circle is viewed completely on edge. There isn’t any expected correlation between the parameterization of this curve and the original 3d curve.

## Syntax

DrawingCurveSegment.**Geometry**() As Object

## Property Value

This is a read only property whose value is an Object.

## Version

Introduced in version 2013
