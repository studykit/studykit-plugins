# BSplineCurve2d.Evaluator Property

Parent Object: [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md)

## Description

Gets the Curve2dEvaluator for this curve.

## Syntax

BSplineCurve2d.**Evaluator**() As [Curve2dEvaluator](../Curve2dEvaluator/Curve2dEvaluator.md)

## Property Value

This is a read only property whose value is a [Curve2dEvaluator](../Curve2dEvaluator/Curve2dEvaluator.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Approximate Polyline to 3D Curve](../../sample-programs/Approximate3DSketchGeometry_Sample.md) | Draws a polyline that is an approximation of the selected curve. To use this have a part open that contains a 3D skech that contains curves. |
| [Extract a Partial Curve from a Curve](../../sample-programs/ExtractPartial2DCurves_Sample.md) | Demonstrates the ability to extract partial curves from a transient geometry curve. This sample has you select an existing sketch spline and extracts three curves from the curve. It then creates real curves using the extracted curves and deletes the original sketch curve. |
| [Split a 2D Curve](../../sample-programs/Split2DCurve_Sample.md) | Demonstrates the ability to extract split curves from a transient geometry curve. This sample has you select an existing sketch spline and splits it at the midpoint of parametric space. It then creates real curves using the split curve results and deletes the original sketch curve. |

## Version

Introduced in version 4
