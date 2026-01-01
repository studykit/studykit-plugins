# SketchEquationCurve.GetEquation Method

Parent Object: [SketchEquationCurve](../SketchEquationCurve/SketchEquationCurve.md)

## Description

Method that returns all of the information that defines the equation for this curve. To edit the equation use the SetEquation method.

## Syntax

SketchEquationCurve.**GetEquation**( ***EquationType*** As [CurveEquationTypeEnum](../CurveEquationTypeEnum.md), ***CoordinateSystemType*** As [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md), ***XValueOrRadius*** As String, ***YValueOrTheta*** As String, ***MinValue*** As [Parameter](../Parameter/Parameter.md), ***MaxValue*** As [Parameter](../Parameter/Parameter.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EquationType | [CurveEquationTypeEnum](../CurveEquationTypeEnum.md) | Enum value indicating if the equation is parametric or explicit. |
| CoordinateSystemType | [CoordinateSystemTypeEnum](../CoordinateSystemTypeEnum.md) | Enum value indicating if the coordinate system being used is Cartesian or Polar. |
| XValueOrRadius | String | Expression that defines the equation for the X value when using a Cartesian coordinate system and the radius when using a Polar coordinate system. |
| YValueOrTheta | String | Expression that defines the equation for the Y value when using a Cartesian coordinate system and the theta value (or angle from the X axis) when using a Polar coordinate system. |
| MinValue | [Parameter](../Parameter/Parameter.md) | Parameter that defines the minimum value of “t”. The value can be queried and edited by using the returned Parameter object. |
| MaxValue | [Parameter](../Parameter/Parameter.md) | Parameter that defines the maximum value of “t”. The value can be queried and edited by using the returned Parameter object. |

## Version

Introduced in version 2014
