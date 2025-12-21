# Sketch Add Oriented

## Description

This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method.

## Code Samples

* [VBA](#VBA)

To use this sample, open a part document that contains a box before running the sample code.

|  |
| --- |
| Copy Code |

```
Public Sub AddOrientedSketch()
    ' Set a reference to the part component definition.
    ' This assumes that a part document is active.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Get the first face of the model.  This sample assumes a simple
    ' model where at least the first face is a plane.  (A box is a good
    ' test case.)
    Dim oFace As Face
    Set oFace = oCompDef.SurfaceBodies.Item(1).Faces.Item(1)

    ' Get one of the edges of the face to use as the sketch x-axis.
    Dim oEdge As Edge
    Set oEdge = oFace.Edges.Item(2)

    ' Get the start vertex of the edge to use as the origin of the sketch.
    Dim oVertex As Vertex
    Set oVertex = oEdge.StartVertex

    ' Create a new sketch.  This last argument is set to true to cause the
    ' creation of sketch geometry from the edges of the face.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.AddWithOrientation(oFace, oEdge, True, _
                                                        True, oVertex, True)

    ' Change the name.
    oSketch.Name = "My Oriented Sketch"

    ' Draw a circle at the origin of the sketch plane.
    Dim oCircle As SketchCircle
    Set oCircle = oSketch.SketchCircles.AddByCenterRadius( _
                ThisApplication.TransientGeometry.CreatePoint2d(0, 0), 1)

    ' Draw a line along the X axis.
    Call oSketch.SketchLines.AddByTwoPoints(oCircle.CenterSketchPoint, _
                ThisApplication.TransientGeometry.CreatePoint2d(1, 0))

    ' Create one more sketch on another face with the origin defined by
    ' the center point.  (The first workpoint in the collection is the center
    ' point work point.)  In this case, no sketch geometry will be created
    ' since the final argument has been left out and it defaults to false.
    Set oFace = oCompDef.SurfaceBodies.Item(1).Faces.Item(5)
    Set oEdge = oFace.Edges.Item(1)
    Set oSketch = oCompDef.Sketches.AddWithOrientation(oFace, oEdge, True, _
                                                True, oCompDef.WorkPoints.Item(1))

    ' Change the name.
    oSketch.Name = "My Origin Sketch"

    ' Draw a circle at the origin of the sketch plane.
    Set oCircle = oSketch.SketchCircles.AddByCenterRadius( _
                ThisApplication.TransientGeometry.CreatePoint2d(0, 0), 1)

    ' Draw a line along the X axis.
    Call oSketch.SketchLines.AddByTwoPoints(oCircle.CenterSketchPoint, _
                ThisApplication.TransientGeometry.CreatePoint2d(1, 0))
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |