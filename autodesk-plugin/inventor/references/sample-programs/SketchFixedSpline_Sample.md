# Spline - create NURBS

## Description

This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way.

## Code Samples

* [VBA](#VBA)

Have a part document open and run the following sample.

|  |
| --- |
| Copy Code |

```
Public Sub SplineByDefinition()
    ' Set a reference to the part component definition.
    ' This assumes that a part document is active.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Set a reference to the transient geometry collection.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Create the collection that will contain the fit points for the regular spline.
    Dim oFitPoints As ObjectCollection
    Set oFitPoints = ThisApplication.TransientObjects.CreateObjectCollection

    ' Define the points to fit the spline through. The
    ' points are at (0,0), (2,2), (4,0), (6,4).
    Dim oPoints(1 To 4) As Point2d
    Set oPoints(1) = oTransGeom.CreatePoint2d(0, 0)
    oFitPoints.Add oPoints(1)

    Set oPoints(2) = oTransGeom.CreatePoint2d(2, 2)
    oFitPoints.Add oPoints(2)

    Set oPoints(3) = oTransGeom.CreatePoint2d(4, 0)
    oFitPoints.Add oPoints(3)

    Set oPoints(4) = oTransGeom.CreatePoint2d(6, 4)
    oFitPoints.Add oPoints(4)

    'Create the first sketch on the X-Y plane
    Dim oSketch1 As PlanarSketch
    Set oSketch1 = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

    ' Create the spline.
    Dim oSpline As SketchSpline
    Set oSpline = oSketch1.SketchSplines.Add(oFitPoints)

    ' Create a work plane parallel to X-Y plane.
    Dim oWorkPlane As WorkPlane
    Set oWorkPlane = oCompDef.WorkPlanes.AddByPlaneAndOffset(oCompDef.WorkPlanes(3), 2)

    'Create the second sketch.
    Dim oSketch2 As PlanarSketch
    Set oSketch2 = oCompDef.Sketches.Add(oWorkPlane)

    ' Set a reference to the geometry of the spline on the first sketch
    Dim oBSplineCurve2d As BSplineCurve2d
    Set oBSplineCurve2d = oSpline.Geometry

    ' Create a fixed spline on the second sketch based
    ' on the geometry of the spline on the first sketch.
    Dim oFixedSpline As SketchFixedSpline
    Set oFixedSpline = oSketch2.SketchFixedSplines.Add(oBSplineCurve2d)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |