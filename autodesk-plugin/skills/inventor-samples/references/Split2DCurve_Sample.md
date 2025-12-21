# Split a 2D Curve

## Description

Demonstrates the ability to extract split curves from a transient geometry curve. This sample has you select an existing sketch spline and splits it at the midpoint of parametric space. It then creates real curves using the split curve results and deletes the original sketch curve.

## Code Samples

* [VBA](#VBA)

To use this sample a part must be active.

```
Public Sub SplitCurve2D()
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.ActiveDocument

    Dim spline As Object
    Set spline = ThisApplication.CommandManager.Pick(kSketchCurveSplineFilter, "Select 2d spline")

    ' Get the spline geometry from the entity.
    Dim splineCurve As BSplineCurve2d
    Set splineCurve = spline.Geometry

    ' Determine the parameter value for geometric midpoint of the curve.
    Dim curveEval As Curve2dEvaluator
    Set curveEval = splineCurve.Evaluator
    Dim startParam As Double
    Dim endParam As Double
    Call curveEval.GetParamExtents(startParam, endParam)
    Dim midParam As Double
    Call curveEval.GetParamAtLength(startParam, spline.Length / 2, midParam)

    ' Split the curve.
    Dim curve1 As BSplineCurve2d
    Dim curve2 As BSplineCurve2d
    Call splineCurve.Split(midParam, curve1, curve2)

    ' Create new sketch curves using the extracted splines.
    Dim splineSketch As sketch
    Set splineSketch = spline.Parent
    Call splineSketch.SketchFixedSplines.Add(curve1)
    Call splineSketch.SketchFixedSplines.Add(curve2)

    ' Delete the original curve.
    spline.Delete
End Sub
```
