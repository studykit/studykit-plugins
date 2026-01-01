# SketchEquationCurve.SetEquation Method

Parent Object: [SketchEquationCurve](../SketchEquationCurve/SketchEquationCurve.md)

## Description

Method that returns edits the information of the curve. You can use the GetEquation method to get the current equation values.

## Syntax

SketchEquationCurve.**SetEquation**( ***EquationType*** As [CurveEquationTypeEnum](../CurveEquationTypeEnum.md), ***CoordinateSystemType*** As [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md), ***XValueOrRadius*** As String, ***YValueOrTheta*** As String, ***MinValue*** As Variant, ***MaxValue*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EquationType | [CurveEquationTypeEnum](../CurveEquationTypeEnum.md) | Enum value indicating if the equation is parametric or explicit. |
| CoordinateSystemType | [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md) | Enum value indicating if the coordinate system being used is Cartesian or Polar. |
| XValueOrRadius | String | Expression that defines the equation for the X value when using a Cartesian coordinate system and the radius when using a Polar coordinate system. |
| YValueOrTheta | String | Expression that defines the equation for the Y value when using a Cartesian coordinate system and the theta value (or angle from the X axis) when using a Polar coordinate system. |
| MinValue | Variant | Input Variant that defines the the minimum value of “t”. This can be either a numeric value or a string and is assigned to the associated parameter. If a string is input, the resulting equation must be unitless. |
| MaxValue | Variant | Input Variant that defines the the maximum value of “t”. This can be either a numeric value or a string and is assigned to the associated parameter. If a string is input, the resulting equation must be unitless. |

## Version

Introduced in version 2014
