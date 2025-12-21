# SketchEquationCurve3D.SetEquation Method

Parent Object: [SketchEquationCurve3D](../SketchEquationCurve3D/SketchEquationCurve3D.md)

## Description

Method that returns all of the information that defines the equatino for this curve. To edit use the SetEquation method.

## Syntax

SketchEquationCurve3D.**SetEquation**( ***CoordinateSystemType*** As [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md), ***XValueOrRadius*** As String, ***YValueOrTheta*** As String, ***ZValueOrPhi*** As String, ***MinValue*** As Variant, ***MaxValue*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CoordinateSystemType | [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md) | Enum value indicating if the coordinate system being used is Cartesian or Polar. |
| XValueOrRadius | String | Expression that defines the equation for the X value when using a Cartesian coordinate system and the radius when using a Cylindrical or Spherical coordinate system. |
| YValueOrTheta | String | Expression that defines the equation for the Y value when using a Cartesian coordinate system and the theta value (or angle from the X axis) when using a Cylindrical coordinate system, and the theta value (or azimuth) for a spherical coordinate system. |
| ZValueOrPhi | String | Expression that defines the equation for the Z value when using a Cartesian or Cylindrical coordinate system, and the phi value (or inclination) for a spherical coordinate system. |
| MinValue | Variant | Input Variant that defines the the minimum value of “t”. This can be either a numeric value or a string and is assigned to the associated parameter. If a string is input, the resulting equation must be unitless. |
| MaxValue | Variant | Input Variant that defines the the maximum value of “t”. This can be either a numeric value or a string and is assigned to the associated parameter. If a string is input, the resulting equation must be unitless. |

## Version

Introduced in version 2014
