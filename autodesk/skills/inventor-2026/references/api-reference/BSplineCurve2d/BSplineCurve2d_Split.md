# BSplineCurve2d.Split Method

Parent Object: [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md)

## Description

Creates two new curves that are the result of splitting this curve at the specified point. The original curve is left unchanged.

## Syntax

BSplineCurve2d.**Split**( ***SplitParam*** As Double, ***CurveOne*** As [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md), ***CurveTwo*** As [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SplitParam | Double | Input Double that specifies the parameter where the curve is to be split. |
| CurveOne | [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md) | Output BSplineCurve2d that is the portion of the curve from the start of the curve to the split parameter location. |
| CurveTwo | [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md) | Output BSplineCurve2d that is the portion of the curve from the split parameter location to the end of the curve. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Split a 2D Curve](../../sample-programs/Split2DCurve_Sample.md) | Demonstrates the ability to extract split curves from a transient geometry curve. This sample has you select an existing sketch spline and splits it at the midpoint of parametric space. It then creates real curves using the split curve results and deletes the original sketch curve. |

## Version

Introduced in version 2013
