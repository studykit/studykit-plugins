# Extract a Partial Curve from a Curve

## Description

Demonstrates the ability to extract partial curves from a transient geometry curve. This sample has you select an existing sketch spline and extracts three curves from the curve. It then creates real curves using the extracted curves and deletes the original sketch curve.

## Code Samples

* [VBA](#VBA)

To use this sample a part must be active.

|  |
| --- |
| Copy Code |

```
Public Sub ExtractPartialCurves2D()
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.ActiveDocument

    Dim spline As Object
    Set spline = ThisApplication.CommandManager.Pick(kSketchCurveSplineFilter, "Select 2d spline")

    ' Get the spline geometry from the entity.
    Dim splineCurve As BSplineCurve2d
    Set splineCurve = spline.Geometry

    ' Get the parameter bounds of the curve.
    Dim startParam As Double
    Dim endParam As Double
    Call splineCurve.Evaluator.GetParamExtents(startParam, endParam)

    ' Extract three curves where they are in thirds of the original
    ' relative to the curves parameter space.
    Dim curves(2) As BSplineCurve2d
    Set curves(0) = splineCurve.ExtractPartial(startParam, (startParam + endParam) / 3)
    Set curves(1) = splineCurve.ExtractPartial((startParam + endParam) / 3, ((startParam + endParam) / 3) * 2)
    Set curves(2) = splineCurve.ExtractPartial(((startParam + endParam) / 3) * 2, endParam)

    ' Create new sketch curves using the extracted splines.
    Dim splineSketch As sketch
    Set splineSketch = spline.Parent
    Call splineSketch.SketchFixedSplines.Add(curves(0))
    Call splineSketch.SketchFixedSplines.Add(curves(1))
    Call splineSketch.SketchFixedSplines.Add(curves(2))

    ' Delete the original curve.
    spline.Delete
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |