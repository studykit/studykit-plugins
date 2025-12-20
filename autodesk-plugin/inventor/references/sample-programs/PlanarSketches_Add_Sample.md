# Sketch Add

## Description

This sample demonstrates the creation of a sketch using the Sketches.Add method.

## Code Samples

* [VBA](#VBA)

Before using this sample, open a part document that contains a box.

|  |
| --- |
| Copy Code |

```
Public Sub AddSketch()
    ' Set a reference to the part component definition.
    ' This assumes that a part document is active.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Get the first face of the model.  This sample assumes a simple
    ' model where at least the first face is a plane.  (A box is a good
    ' test case.)
    Dim oFace As Face
    Set oFace = oCompDef.SurfaceBodies.Item(1).Faces.Item(1)

    ' Create a new sketch.  The second argument specifies to include
    ' the edges of the face in the sketch.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oFace, True)

    ' Change the name.
    oSketch.Name = "My New Sketch"
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |