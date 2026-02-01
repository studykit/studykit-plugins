# Curve2dEvaluator.GetParamExtents Method

Parent Object: [Curve2dEvaluator](../Curve2dEvaluator/Curve2dEvaluator.md)

## Description

Gets the valid parameter range of the curve if the curve is bounded.

## Syntax

Curve2dEvaluator.**GetParamExtents**( ***MinParam*** As Double, ***MaxParam*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MinParam | Double | Output Double that returns the minimum valid parameter value. |
| MaxParam | Double | Output Double that returns the maximum valid parameter value. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extract a Partial Curve from a Curve](../../sample-programs/ExtractPartial2DCurves_Sample.md) | Demonstrates the ability to extract partial curves from a transient geometry curve. This sample has you select an existing sketch spline and extracts three curves from the curve. It then creates real curves using the extracted curves and deletes the original sketch curve. |
| [Split a 2D Curve](../../sample-programs/Split2DCurve_Sample.md) | Demonstrates the ability to extract split curves from a transient geometry curve. This sample has you select an existing sketch spline and splits it at the midpoint of parametric space. It then creates real curves using the split curve results and deletes the original sketch curve. |

## Version

Introduced in version 4
