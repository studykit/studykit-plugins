# SurfaceEvaluator.GetParamAtPoint Method

Parent Object: [SurfaceEvaluator](../SurfaceEvaluator/SurfaceEvaluator.md)

## Description

Calculates the parameter value on the surface that is equal to the specified point. The point must lie on the surface.

## Syntax

SurfaceEvaluator.**GetParamAtPoint**( ***Points***() As Double, ***GuessParams***() As Double, ***MaxDeviations***() As Double, ***Params***() As Double, ***SolutionNatures***() As [SolutionNatureEnum](../SolutionNatureEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Points | Double | Input/output double that specifies the points. |
| GuessParams | Double | Input array of parameter points that are an initial guess to optimize the calculation. |
| MaxDeviations | Double | Output array of Doubles that returns the maximum deviation achieved from the input points. |
| Params | Double | Input/output array of Doubles that specifies the parameters. |
| SolutionNatures | [SolutionNatureEnum](../SolutionNatureEnum.md) | Output SolutionNatureEnum that returns the nature of the solution found. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |