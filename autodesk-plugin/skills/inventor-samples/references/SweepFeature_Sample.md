# Sweep Feature Add

## Description

This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch.

## Code Samples

* [VBA](#VBA)

To run the sample have a part document open.

|  |
| --- |
| Copy Code |

```
Public Sub SweepFeature()
    ' Set a reference to the currently active document.
    ' This assumes that it is a part document.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Set a reference to the transient geometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Create some workpoints that will be used for the 3D sketch.
    Dim oWPs(1 To 5) As WorkPoint
    Set oWPs(1) = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(0, 0, 0))
    Set oWPs(2) = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(3, 0, 0))
    Set oWPs(3) = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(3, 4, 0))
    Set oWPs(4) = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(3, 4, 2))
    Set oWPs(5) = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(6, 4, 2))

    ' Create a new 3D Sketch.
    Dim oSketch3D As Sketch3D
    Set oSketch3D = oPartDoc.ComponentDefinition.Sketches3D.Add

    ' Draw 3D lines. The first line is drawn between two of the work points.
    Dim oLine As SketchLine3D
    Set oLine = oSketch3D.SketchLines3D.AddByTwoPoints(oWPs(1), oWPs(2), True, 1)

    ' This second and subsequent lines are drawn between a 3D sketch point and a work point.
    ' The work point is obtained from the previous line. Because the two lines will share
    ' this 3D sketch point, Inventor will treat them as connected lines when creating any
    ' paths.
    Set oLine = oSketch3D.SketchLines3D.AddByTwoPoints(oLine.EndPoint, oWPs(3), True, 1)
    Set oLine = oSketch3D.SketchLines3D.AddByTwoPoints(oLine.EndPoint, oWPs(4), True, 0.75)
    Set oLine = oSketch3D.SketchLines3D.AddByTwoPoints(oLine.EndPoint, oWPs(5), True, 1)

    ' Create a 2D sketch.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(2))

    ' Determine the model origin relative to the sketch space.
    Dim oOrigin As Point2d
    Set oOrigin = oSketch.ModelToSketchSpace(oTG.CreatePoint(0, 0, 0))

    ' Create two lines.
    Dim oNewPoint As Point2d
    Set oNewPoint = oTG.CreatePoint2d(oOrigin.X, oOrigin.Y - 4)
    Dim oSketchLine1 As SketchLine
    Set oSketchLine1 = oSketch.SketchLines.AddByTwoPoints(oOrigin, oNewPoint)
    oNewPoint.X = oNewPoint.X + 3
    Dim oSketchLine2 As SketchLine
    Set oSketchLine2 = oSketch.SketchLines.AddByTwoPoints(oSketchLine1.EndSketchPoint, oNewPoint)

    ' Create a fillet between the two lines.
    Call oSketch.SketchArcs.AddByFillet(oSketchLine1, oSketchLine2, 1, oSketchLine1.StartSketchPoint.Geometry, oSketchLine2.EndSketchPoint.Geometry)

    ' Get the end of the 2d sketch in model space.
    Dim oModelPoint As Point
    Set oModelPoint = oSketch.SketchToModelSpace(oSketchLine2.EndSketchPoint.Geometry)

    ' Create a work plane at the end of the 2D sketch.
    Dim oWP As WorkPlane
    Set oWP = oCompDef.WorkPlanes.AddByNormalToCurve(oSketchLine2, oSketchLine2.EndSketchPoint)

    ' Create a path. Because the 3D and 2D sketches physically connect the path will include
    ' both of them.
    Dim oPath As Path
    Set oPath = oCompDef.Features.CreatePath(oSketchLine2)

    ' Create a sketch containing a circle.
    Set oSketch = oCompDef.Sketches.Add(oWP)
    Set oOrigin = oSketch.ModelToSketchSpace(oTG.CreatePoint(0, 0, 0))
    Call oSketch.SketchCircles.AddByCenterRadius(oSketch.ModelToSketchSpace(oModelPoint), 0.375)

    ' Create a profile.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create the sweep feature.
    Dim oSweep As SweepFeature
    Set oSweep = oCompDef.Features.SweepFeatures.AddUsingPath(oProfile, oPath, kJoinOperation)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |