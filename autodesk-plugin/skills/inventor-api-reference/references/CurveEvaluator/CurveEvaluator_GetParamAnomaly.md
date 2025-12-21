# CurveEvaluator.GetParamAnomaly Method

Parent Object: [CurveEvaluator](../CurveEvaluator/CurveEvaluator.md)

## Description

Gets general information about the parameterization of the curve, such as whether or not it is periodic, singular, or unbounded in the parameter domain.

## Syntax

CurveEvaluator.**GetParamAnomaly**( ***Periodicity***() As Double, ***IsSingular*** As Boolean, ***UnboundedParam*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Periodicity | Double | Output two element Double array that returns whether the curve is periodic. If the curve is periodic, the first array element is the period of the curve and the second element is the starting parameter of the principle period. If the curve is not periodic, the first element is zero, and the second element is unused. |
| IsSingular | Boolean | Output Boolean that returns whether the curve is degenerate to a singularity. |
| UnboundedParam | Boolean | Output Boolean that returns whether the curve has an unbounded parameter range. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |