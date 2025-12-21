# Create and insert a sketch block definition into a part sketch

## Description

This sample demonstrates inserting a sketch block into a part sketch.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateSketchBlockDefinition()
    ' Set a reference to the part document.
    ' This assumes a part document is active.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    ' Create the new sketch block definition.
    Dim oSketchBlockDef As SketchBlockDefinition
    Set oSketchBlockDef = oPartDoc.ComponentDefinition.SketchBlockDefinitions.Add("My Block Def")

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw a 4cm x 3cm rectangle with the corner at (0,0)
    Dim oRectangleLines As SketchEntitiesEnumerator
    Set oRectangleLines = oSketchBlockDef.SketchLines.AddAsTwoPointRectangle( _
                                oTransGeom.CreatePoint2d(0, 0), _
                                oTransGeom.CreatePoint2d(4, 3))

End Sub

Public Sub InsertSketchBlockDefinition()

    ' Set a reference to the part document.
    ' This assumes a part document is active.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

    ' Set a reference to the definition named "My Block Def"
    Dim oSketchBlockDef As SketchBlockDefinition
    Set oSketchBlockDef = oCompDef.SketchBlockDefinitions.Item("My Block Def")

    Dim oPosition As Point2d
    Set oPosition = ThisApplication.TransientGeometry.CreatePoint2d(10, 10)

    ' Insert the sketch block definition
    Call oSketch.SketchBlocks.AddByDefinition(oSketchBlockDef, oPosition)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |