# Control point, equation, and intersection curve creation.

## Description

This sample demonstrates several new curve creation techniques introduced in Inventor 2014. It creates a new part and then create a 2d control point spline and a 2d equation curve. Surfaces are created from these two curves by extruding them. A 3d intersection curve is created between the extrusions. A 3d control point spline and 3d equation curve are also created.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub SketchCurves()
    ' Create a new part.
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                  ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))
    Dim partDef As PartComponentDefinition
    Set partDef = partDoc.ComponentDefinition

    ' Create a 2D sketch on the X-Y plane.
    Dim sketch1 As PlanarSketch
    Set sketch1 = partDef.Sketches.Add(partDef.WorkPlanes.Item(3))

    Dim tg As TransientGeometry
    Set tg = ThisApplication.TransientGeometry

    ' Create a spline based on control points.
    Dim pnts As ObjectCollection
    Set pnts = ThisApplication.TransientObjects.CreateObjectCollection
    Call pnts.Add(tg.CreatePoint2d(2, 0))
    Call pnts.Add(tg.CreatePoint2d(4, 1))
    Call pnts.Add(tg.CreatePoint2d(4, 2))
    Call pnts.Add(tg.CreatePoint2d(6, 3))
    Call pnts.Add(tg.CreatePoint2d(8, 1))
    Dim controlPointSpline As SketchControlPointSpline
    Set controlPointSpline = sketch1.SketchControlPointSplines.Add(pnts)

    ' Create a 2D sketch on the Y-Z plane.
    Dim sketch2 As PlanarSketch
    Set sketch2 = partDef.Sketches.Add(partDef.WorkPlanes.Item(1))

    ' Create a spline based on an equation.
    Dim equationCurve As SketchEquationCurve
    Set equationCurve = sketch2.SketchEquationCurves.Add(kParametric, kCartesian, _
                                ".001*t * cos(t)", ".001*t * sin(t)", 0, 360 * 3)

    ' Create a 3D sketch.
    Dim sketch3 As sketch3D
    Set sketch3 = partDef.Sketches3D.Add

    ' Create a 3D spline based on control points.
    Set pnts = ThisApplication.TransientObjects.CreateObjectCollection
    Call pnts.Add(tg.CreatePoint(10, 0, 0))
    Call pnts.Add(tg.CreatePoint(12, 1, 3))
    Call pnts.Add(tg.CreatePoint(12, 2, -5))
    Call pnts.Add(tg.CreatePoint(14, 3, 2))
    Call pnts.Add(tg.CreatePoint(16, 1, -3))
    Dim controlPointSpline2 As SketchControlPointSpline3D
    Set controlPointSpline2 = sketch3.SketchControlPointSplines3D.Add(pnts)

    ' Create a 3D spline based on an equation.
    Dim equationCurve2 As SketchEquationCurve3D
    Set equationCurve2 = sketch3.SketchEquationCurves3D.Add(kCartesian, _
                            ".001*t * cos(t) + 8", ".001*t * sin(t)", "0.002*t", 0, 360 * 3)

    ThisApplication.ActiveView.Fit

    ' Extrude the 2d curves.
    Dim prof As Profile
    Set prof = sketch1.Profiles.AddForSurface(controlPointSpline)
    Dim extrudeDef As ExtrudeDefinition
    Set extrudeDef = partDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(prof, kSurfaceOperation)
    Call extrudeDef.SetDistanceExtent(6, kSymmetricExtentDirection)
    Dim extrude1 As ExtrudeFeature
    Set extrude1 = partDef.Features.ExtrudeFeatures.Add(extrudeDef)

    ' Change the work surface to not be transparent.
    Dim surf As WorkSurface
    Set surf = extrude1.SurfaceBodies.Item(1).Parent
    surf.Translucent = False

    Set prof = sketch2.Profiles.AddForSurface(equationCurve)
    Set extrudeDef = partDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(prof, kSurfaceOperation)
    Call extrudeDef.SetDistanceExtent(9, kPositiveExtentDirection)
    Dim extrude2 As ExtrudeFeature
    Set extrude2 = partDef.Features.ExtrudeFeatures.Add(extrudeDef)

    ' Create a new sketch and an intersection curve.
    Dim interSketch As sketch3D
    Set interSketch = partDef.Sketches3D.Add

    Call interSketch.IntersectionCurves.Add(extrude1.SurfaceBodies.Item(1), extrude2.SurfaceBodies.Item(1))
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |