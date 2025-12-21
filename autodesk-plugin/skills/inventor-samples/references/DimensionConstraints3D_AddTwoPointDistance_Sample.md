# Create a 3D sketch dimension

## Description

This sample demonstrates the creation of a 3d sketch line and a dimension between the start and the end points of the line.

## Code Samples

* [VBA](#VBA)

To run this sample you must have a 3D sketch active.

|  |
| --- |
| Copy Code |

```
Public Sub Create3DSketchDimension()
    ' Check to make sure a 3d sketch is open.
    If Not Typeof ThisApplication.ActiveEditObject Is Sketch3D Then
        MsgBox "A 3d sketch must be active."
        Exit Sub
    End If

    ' Set a reference to the active sketch.
    Dim oSketch As Sketch3D
    Set oSketch = ThisApplication.ActiveEditObject

    ' Set a reference to the transient geometry collection.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Create a sketch line
    Dim oSketchLine As SketchLine3D
    Set oSketchLine = oSketch.SketchLines3D.AddByTwoPoints(oTransGeom.CreatePoint(5, 5, 0), oTransGeom.CreatePoint(10, 10, 20))

    ' Create an object collection and add the end points.
    Dim oColl As ObjectCollection
    Set oColl = ThisApplication.TransientObjects.CreateObjectCollection

    oColl.Add oSketchLine.StartSketchPoint
    oColl.Add oSketchLine.EndSketchPoint

    ' The text point for the dimension needs to be on a plane
    ' that Inventor internally computes based on the sketch
    ' entities being dimensioned. Get this plane.
    Dim oDimPlane As Plane
    Set oDimPlane = oSketch.DimensionConstraints3D.GetDimensionPlane(oColl)

    ' Get the normal of the plane
    Dim oPlaneNormal As UnitVector
    Set oPlaneNormal = oDimPlane.Normal

    ' Get the sketch line direction
    Dim oLineDir As UnitVector
    Set oLineDir = oSketchLine.Geometry.Direction

    ' Get the direction in which to offset the text point.
    ' (This should be perpendicular to the plane normal
    ' and the line direction).
    Dim oOffsetDir As UnitVector
    Set oOffsetDir = oPlaneNormal.CrossProduct(oLineDir)

    ' Get the midpoint of the sketch line
    Dim oMidPoint As Point
    Set oMidPoint = oSketchLine.Geometry.MidPoint

    ' Offset the midpoint from the line by a distance.
    Dim oOffsetPoint As Point
    Set oOffsetPoint = oMidPoint
    Call oOffsetPoint.TranslateBy(oOffsetDir.AsVector)

    ' Create the dimension.
    Dim oTwoPointDim As TwoPointDistanceDimConstraint3D
    Set oTwoPointDim = oSketch.DimensionConstraints3D.AddTwoPointDistance(oSketchLine.StartSketchPoint, oSketchLine.EndSketchPoint, oOffsetPoint)

    ' Make sure that the dimension text was placed at the specified point.
    If oOffsetPoint.IsEqualTo(oTwoPointDim.TextPoint) Then
        MsgBox "Dimension text placed at specified point."
    End If
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |