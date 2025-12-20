# SketchEquationCurves.Add Method

Parent Object: [SketchEquationCurves](../SketchEquationCurves/SketchEquationCurves.md)

## Description

Creates a new sketch equation curve.

## Syntax

SketchEquationCurves.**Add**( ***EquationType*** As [CurveEquationTypeEnum](../CurveEquationTypeEnum.md), ***CoordinateSystemType*** As [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md), ***XValueOrRadius*** As String, ***YValueOrTheta*** As String, ***MinValue*** As Variant, ***MaxValue*** As Variant ) As [SketchEquationCurve](../SketchEquationCurve/SketchEquationCurve.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EquationType | [CurveEquationTypeEnum](../CurveEquationTypeEnum.md) | Enum value indicating if the equation is parametric or explicit. |
| CoordinateSystemType | [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md) | Enum value indicating if the coordinate system being used is Cartesian or Polar. |
| XValueOrRadius | String | Expression that defines the equation for the X value when using a Cartesian coordinate system and the radius when using a Polar coordinate system. |
| YValueOrTheta | String | Expression that defines the equation for the Y value when using a Cartesian coordinate system and the theta value (or angle from the X axis) when using a Polar coordinate system. |
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