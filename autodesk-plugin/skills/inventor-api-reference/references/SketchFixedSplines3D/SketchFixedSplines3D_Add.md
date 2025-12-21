# SketchFixedSplines3D.Add Method

Parent Object: [SketchFixedSplines3D](../SketchFixedSplines3D/SketchFixedSplines3D.md)

## Description

Method that creates a fixed spline based on an input NURBS definition.

## Syntax

SketchFixedSplines3D.**Add**( ***SplineCurve*** As [BSplineCurve](../BSplineCurve/BSplineCurve.md), [***StartPoint***] As Variant, [***EndPoint***] As Variant ) As [SketchFixedSpline3D](../SketchFixedSpline3D/SketchFixedSpline3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SplineCurve | [BSplineCurve](../BSplineCurve/BSplineCurve.md) | Input BSplineCurve geometry object that contains the definition of a curve from which to create a SketchFixedSpline3D. |
| StartPoint | Variant | Optional input Object that contains the start point to fit the curve through. The point can be either an existing SketchPoint3D object, a SketchPoint object, a workpoint or vertex. If the input is not a SketchPoint3D object, a SketchPoint3D object is automatically created at the position of the input point. If the argument is not supplied, a SketchPoint3D object is automatically created at the position of the start point of the input BSplineCurve. |
| EndPoint | Variant | Optional input Object that contains the end point to fit the curve through. The point can be either an existing SketchPoint3D object, a SketchPoint object, a workpoint or vertex . If the input is not a SketchPoint3D object, a SketchPoint3D object is automatically created at the position of the input point. If the argument is not supplied, a SketchPoint3D object is automatically created at the position of the end point of the input BSplineCurve.   This is an optional argument whose default value is null. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |