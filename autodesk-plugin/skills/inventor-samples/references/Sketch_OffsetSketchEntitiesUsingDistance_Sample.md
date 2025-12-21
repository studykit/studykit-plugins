# Offset a 2D sketch

## Description

This sample demonstrates the creation of offsets in 2d sketches. Two ways of creating the offset are shown - one uses a distance and the other uses the input point.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub Offset()
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

    ' Create a rectangle
    Dim oRectangleLines As SketchEntitiesEnumerator
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
                                                oTransGeom.CreatePoint2d(0, 0), _
                                                oTransGeom.CreatePoint2d(10, -10))

    ' Create a new object collection
    Dim oCollection As ObjectCollection
    Set oCollection = ThisApplication.TransientObjects.CreateObjectCollection

    ' Add the first sketch line of the rectangle to the collection
    oCollection.Add oRectangleLines.Item(1)

    ' Create a point at (0,3). The entity resulting
    ' from the offset of the first sketch line must
    ' pass thru this point.
    Dim oOffsetPoint As Point2d
    Set oOffsetPoint = oTransGeom.CreatePoint2d(0, 3)

    ' Create an offset rectangle using the offset point.
    Call oSketch.OffsetSketchEntitiesUsingPoint(oCollection, oOffsetPoint, True)

    ' Get the sketch normal
    Dim oNormalVector As UnitVector
    Set oNormalVector = oSketch.PlanarEntityGeometry.Normal

    ' Get the direction of the sketch line being offset
    Dim oLineDir As UnitVector2d
    Set oLineDir = oRectangleLines.Item(1).Geometry.Direction

    Dim oLineVector As UnitVector
    Set oLineVector = oTransGeom.CreateUnitVector(oLineDir.X, oLineDir.Y, 0)

    ' The cross product of these vectors is the
    ' natural offset direction for the sketch line.
    Dim oOffsetVector As UnitVector
    Set oOffsetVector = oLineVector.CrossProduct(oNormalVector)

    ' Get the desired offset vector (the +ve y-axis)
    Dim oDesiredVector As UnitVector
    Set oDesiredVector = oTransGeom.CreateUnitVector(0, 1, 0)

    Dim bNaturalOffsetDir As Boolean

    If oOffsetVector.IsEqualTo(oDesiredVector) Then
        bNaturalOffsetDir = True
    Else
        bNaturalOffsetDir = False
    End If

    ' Create an offset at a distance of 6 cms.
    Call oSketch.OffsetSketchEntitiesUsingDistance(oCollection, 6, bNaturalOffsetDir, True)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |