# Create sketch elliptical arc

## Description

This sample demonstrates creating an elliptical arc in a sketch and dimensioning its minor radius.

## Code Samples

* [VBA](#VBA)

To run this sample you must have a sketch active.

|  |
| --- |
| Copy Code |

```
Sub DrawSketchEllipticalArc()
    ' Check to make sure a sketch is open.
    If Not Typeof ThisApplication.ActiveEditObject Is PlanarSketch Then
        MsgBox "A sketch must be active."
        Exit Sub
    End If

    ' Set a reference to the active sketch.
    Dim oSketch As PlanarSketch
    Set oSketch = ThisApplication.ActiveEditObject

    ' Set a reference to the transient geometry collection.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Arc center point at 0,0
    Dim oCenter As Point2d
    Set oCenter = oTransGeom.CreatePoint2d(0, 0)

    ' Arc major axis as the y-axis
    Dim oMajorAxis As UnitVector2d
    Set oMajorAxis = oTransGeom.CreateUnitVector2d(0, 1)

    Dim PI As Double
    PI = 4# * Atn(1#)

    ' Create the elliptical arc
    Dim oEllipticalArc As SketchEllipticalArc
    Set oEllipticalArc = oSketch.SketchEllipticalArcs.Add(oCenter, oMajorAxis, 5, 2, 0, PI / 2)

    Dim oTextPt As Point2d
    Set oTextPt = oTransGeom.CreatePoint2d(-1, -0.5)

    ' Create a radius dimension
    Dim oEllipseRadiusDim As EllipseRadiusDimConstraint
    Set oEllipseRadiusDim = oSketch.DimensionConstraints.AddEllipseRadius(oEllipticalArc, False, oTextPt)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |