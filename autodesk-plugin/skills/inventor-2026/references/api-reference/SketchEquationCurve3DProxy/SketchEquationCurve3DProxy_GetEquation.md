# SketchEquationCurve3DProxy.GetEquation Method

Parent Object: [SketchEquationCurve3DProxy](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy.md)

## Description

Method that returns all of the information that defines the equatino for this curve. To edit use the SetEquation method.

## Syntax

SketchEquationCurve3DProxy.**GetEquation**( ***CoordinateSystemType*** As [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md), ***XValueOrRadius*** As String, ***YValueOrTheta*** As String, ***ZValueOrPhi*** As String, ***MinValue*** As [Parameter](../Parameter/Parameter.md), ***MaxValue*** As [Parameter](../Parameter/Parameter.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CoordinateSystemType | [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md) | Enum value indicating if the coordinate system being used is Cartesian, Cylindrical, or Spherical. |
| XValueOrRadius | String | Expression that defines the equation for the X value when using a Cartesian coordinate system and the radius when using a Cylindrical or Spherical coordinate system. |
| YValueOrTheta | String | Expression that defines the equation for the Y value when using a Cartesian coordinate system and the theta value (or angle from the X axis) when using a Cylindrical coordinate system, and the theta value (or azimuth) for a spherical coordinate system. |
| ZValueOrPhi | String | Expression that defines the equation for the Z value when using a Cartesian or Cylindrical coordinate system, and the phi value (or inclination) for a spherical coordinate system. |
| MinValue | [Parameter](../Parameter/Parameter.md) | Parameter that defines the minimum value of “t”. The value can be queried and edited by using the returned Parameter object. |
| MaxValue | [Parameter](../Parameter/Parameter.md) | Parameter that defines the maximum value of “t”. The value can be queried and edited by using the returned Parameter object. |

## Version

Introduced in version 2014
