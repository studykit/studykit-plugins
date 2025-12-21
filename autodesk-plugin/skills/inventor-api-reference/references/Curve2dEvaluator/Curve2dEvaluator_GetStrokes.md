# Curve2dEvaluator.GetStrokes Method

Parent Object: [Curve2dEvaluator](../Curve2dEvaluator/Curve2dEvaluator.md)

## Description

Calculates a set of connected line segments that approximate the curve within the specified tolerance.

## Syntax

Curve2dEvaluator.**GetStrokes**( ***FromParam*** As Double, ***ToParam*** As Double, ***Tolerance*** As Double, ***VertexCount*** As Long, ***VertexCoordinates***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FromParam | Double | Input Double that specifies the starting parameter value to begin calculating the strokes. By specifying the from and to parameter values you can calculate strokes over a portion of a curve.  If you want to calculate strokes over the entire curve you can call GetParamExtents to get the min and max param values for the entire curve. Remember that some curves are infinite and cannot return min and max param values. |
| ToParam | Double | Input Double that specifies the ending parameter value to end calculating the strokes. By specifying the from and to parameter values you can calculate strokes over a portion of a curve.  If you want to calculate strokes over the entire curve you can call GetParamExtents to get the min and max param values for the entire curve. Remember that some curves are infinite and cannot return min and max param values. |
| Tolerance | Double | Input Double that specifies the tolerance of the resulting strokes. This is the maximum distance that the stroked lines can be from the actual curve (chord height tolerance). The distance is specified in centimeters. |
| VertexCount | Long | Output Long indicating the number of points in the output connected line segments. |
| VertexCoordinates | Double | Output array of Double values that are the coordinates of the connected line segments. The coordinate values are in 2d space (either the parametric space of the EdgeUse object or sketch space) and are in centimeters. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |