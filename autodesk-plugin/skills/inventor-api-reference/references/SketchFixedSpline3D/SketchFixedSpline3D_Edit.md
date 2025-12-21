# SketchFixedSpline3D.Edit Method

Parent Object: [SketchFixedSpline3D](../SketchFixedSpline3D/SketchFixedSpline3D.md)

## Description

Method that edits a fixed sketch spline based on an input NURBS definition. This method is only valid for SketchFixedSpline3D objects that were created using a BSplineCurve as input. This method will fail if the curve was created with an Edge.

## Syntax

SketchFixedSpline3D.**Edit**( ***SplineCurve*** As [BSplineCurve](../BSplineCurve/BSplineCurve.md), [***StartPoint***] As Variant, [***EndPoint***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SplineCurve | [BSplineCurve](../BSplineCurve/BSplineCurve.md) | Input BSplineCurve geometry object that contains the definition of a curve that will be used to redefine the spline. |
| StartPoint | Variant | Optional input Object that contains the start point to fit the curve through. The point can be either an existing SketchPoint3D object, a SketchPoint object, a workpoint or vertex. If the input is not a SketchPoint3D object, a SketchPoint3D object is automatically created at the position of the input point. If the argument is not supplied, a SketchPoint3D object is automatically created at the position of the start point of the input BSplineCurve. |
| EndPoint | Variant | Optional input Object that contains the end point to fit the curve through. The point can be either an existing SketchPoint3D object, a SketchPoint object, a workpoint or vertex. If the input is not a SketchPoint3D object, a SketchPoint3D object is automatically created at the position of the input point. If the argument is not supplied, a SketchPoint3D object is automatically created at the position of the end point of the input BSplineCurve.   This is an optional argument whose default value is null. |

## Version

Introduced in version 9
