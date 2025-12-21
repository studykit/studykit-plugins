# SurfaceEvaluator.GetSecondDerivatives Method

Parent Object: [SurfaceEvaluator](../SurfaceEvaluator/SurfaceEvaluator.md)

## Description

Calculates the second order derivatives at the given parameter values on the surface.

## Syntax

SurfaceEvaluator.**GetSecondDerivatives**( ***Params***() As Double, ***UUPartials***() As Double, ***UVPartials***() As Double, ***VVPartials***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Params | Double | Input/output array of Doubles that specifies the parameters. |
| UUPartials | Double | Output Double array that returns the second U partial derivatives. |
| UVPartials | Double | Output Double array that returns the second mixed UV partial derivatives. |
| VVPartials | Double | Output Double array that returns the second V partial derivatives. |

## Version

Introduced in version 4
