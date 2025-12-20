# Create sketch block from an existing sketch

## Description

This sample demonstrates creating a sketch block from an existing sketch.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateSketchBlock()
    ' Set a reference to the part document.
    ' This assumes a part document is active.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw a 4cm x 3cm rectangle with the corner at (0,0)
    Dim oRectangleLines As SketchEntitiesEnumerator
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
                                oTransGeom.CreatePoint2d(0, 0), _
                                oTransGeom.CreatePoint2d(4, 3))

    Dim oSketchObjects As ObjectCollection
    Set oSketchObjects = ThisApplication.TransientObjects.CreateObjectCollection

    Dim oLine As SketchEntity
    For Each oLine In oRectangleLines
       Call oSketchObjects.Add(oLine)
    Next

    ' Insert the sketch block definition
    Call oSketch.SketchBlocks.Add(oSketchObjects)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |