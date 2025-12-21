# BSplineCurve2d.ExtractPartial Method

Parent Object: [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md)

## Description

Creates a new curve by extracting a portion of an existing curve.

## Syntax

BSplineCurve2d.**ExtractPartial**( ***StartParam*** As Double, ***EndParam*** As Double ) As [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartParam | Double | Input Double that specifies the starting parameter of where the new curve is extracted. |
| EndParam | Double | Input Double that specifies the ending parameter of where the new curve is extracted. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extract a Partial Curve from a Curve](../../sample-programs/ExtractPartial2DCurves_Sample.md) | Demonstrates the ability to extract partial curves from a transient geometry curve. This sample has you select an existing sketch spline and extracts three curves from the curve. It then creates real curves using the extracted curves and deletes the original sketch curve. |

## Version

Introduced in version 2013
