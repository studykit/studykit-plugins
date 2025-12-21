# Curve2dEvaluator.GetParamAtPoint Method

Parent Object: [Curve2dEvaluator](../Curve2dEvaluator/Curve2dEvaluator.md)

## Description

Calculates the parameter value on the curve that is equal to the specified point. The point must lie on the curve.

## Syntax

Curve2dEvaluator.**GetParamAtPoint**( ***Points***() As Double, ***GuessParams***() As Double, ***MaxDeviations***() As Double, ***Params***() As Double, ***SolTypes***() As [SolutionNatureEnum](../SolutionNatureEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Points | Double | Input/output double that specifies the points. |
| GuessParams | Double | Input array of parameter values that are an initial guess to optimize the calculation. |
| MaxDeviations | Double | Output array of Doubles that returns the maximum deviation achieved from the input points. |
| Params | Double | Input/output array of Doubles that specifies the parameters. |
| SolTypes | [SolutionNatureEnum](../SolutionNatureEnum.md) | Output that returns the nature of the solution found. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |