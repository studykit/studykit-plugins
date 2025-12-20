# SketchEquationCurves3D.Add Method

Parent Object: [SketchEquationCurves3D](../SketchEquationCurves3D/SketchEquationCurves3D.md)

## Description

Creates a new sketch equation curve in a 3D sketch.

## Syntax

SketchEquationCurves3D.**Add**( ***CoordinateSystemType*** As [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md), ***XValueOrRadius*** As String, ***YValueOrTheta*** As String, ***ZValueOrPhi*** As String, ***MinValue*** As Variant, ***MaxValue*** As Variant ) As [SketchEquationCurve3D](../SketchEquationCurve3D/SketchEquationCurve3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CoordinateSystemType | [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md) | Enum value indicating if the coordinate system being used is Cartesian, Cylindrical, or Spherical. |
| XValueOrRadius | String | Expression that defines the equation for the X value when using a Cartesian coordinate system and the radius when using a Cylindrical or Spherical coordinate system. |
| YValueOrTheta | String | Expression that defines the equation for the Y value when using a Cartesian coordinate system and the theta value (or angle from the X axis) when using a Cylindrical coordinate system, and the theta value (or azimuth) for a spherical coordinate system. |
| ZValueOrPhi | String | Expression that defines the equation for the Z value when using a Cartesian or Cylindrical coordinate system, and the phi value (or inclination) for a spherical coordinate system. |
| MinValue | Variant | Expression defining the minimum value of “t”. |
| MaxValue | Variant | Expression defining the maximum value of “t”. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Control point, equation, and intersection curve creation.](../../sample-programs/AdvancedCurveCreation_Sample.md) | This sample demonstrates several new curve creation techniques introduced in Inventor 2014. It creates a new part and then create a 2d control point spline and a 2d equation curve. Surfaces are created from these two curves by extruding them. A 3d intersection curve is created between the extrusions. A 3d control point spline and 3d equation curve are also created. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |