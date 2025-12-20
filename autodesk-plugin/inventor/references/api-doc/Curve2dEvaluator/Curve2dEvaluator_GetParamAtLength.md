# Curve2dEvaluator.GetParamAtLength Method

Parent Object: [Curve2dEvaluator](../Curve2dEvaluator/Curve2dEvaluator.md)

## Description

Calculates the parameter value at the point measured from the specified starting parameter along the curve.

## Syntax

Curve2dEvaluator.**GetParamAtLength**( ***FromParam*** As Double, ***Length*** As Double, ***Param*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FromParam | Double | Input Double that specifies the parameter value to measure the length from. |
| Length | Double | Input Double that specifies the distance measured along the curve. |
| Param | Double | Output Double that returns the parameter value at the specified Length from FromParam. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Split a 2D Curve](../../sample-programs/Split2DCurve_Sample.md) | Demonstrates the ability to extract split curves from a transient geometry curve. This sample has you select an existing sketch spline and splits it at the midpoint of parametric space. It then creates real curves using the split curve results and deletes the original sketch curve. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |