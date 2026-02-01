# Move sketch entities

## Description

This sample demonstrates the translation of all the objects on the active sketch by a certain distance.

## Code Samples

* [VBA](#VBA)

Have a sketch active that contains several entities (this could include text boxes and images) and run the sample.

```
Public Sub MoveSketchObjects()
    ' Check to make sure a sketch is open.
    If Not Typeof ThisApplication.ActiveEditObject Is Sketch Then
        MsgBox "A sketch must be active."
        Exit Sub
    End If

    ' Set a reference to the active sketch.
    Dim oSketch As Sketch
    Set oSketch = ThisApplication.ActiveEditObject

    ' Create a vector along the x-axis.
    Dim oVec As Vector2d
    Set oVec = ThisApplication.TransientGeometry.CreateVector2d(5, 0)

    Dim oSketchObjects As ObjectCollection
    Set oSketchObjects = ThisApplication.TransientObjects.CreateObjectCollection

    ' Get all entities in the sketch
    Dim oSketchEntity As SketchEntity
    For Each oSketchEntity In oSketch.SketchEntities
        oSketchObjects.Add oSketchEntity
    Next

    ' Move all sketch objects along x-axis by 5 units.
    ' This will move all the text boxes and images in
    ' the sketch as well since these have sketch lines
    ' as boundary geometry or a sketch point as an
    ' origin point.
    Call oSketch.MoveSketchObjects(oSketchObjects, oVec)
End Sub
```
