# Sketch Edit Orientation

## Description

This sample demonstrates modifying the orientation of a sketch.

## Code Samples

* [VBA](#VBA)

To use this sample, have a part document open that contains a box and run the program.

|  |
| --- |
| Copy Code |

```
Public Sub ChangeSketchPlane()
   ' Set a reference to the part component definition.
   ' This assumes that a part document is active.
   Dim oCompDef As PartComponentDefinition
   Set oCompDef = ThisApplication.ActiveDocument.ComponentDefinition

   ' Get the first face of the model. This sample assumes a simple
   ' model where at least the first face is a plane. (A box is a good
   ' test case.)
   Dim oFace As Face
   Set oFace = oCompDef.SurfaceBodies.Item(1).Faces.Item(1)

   ' Create a new sketch
   Dim oSketch As PlanarSketch
   Set oSketch = oCompDef.Sketches.Add(oFace, True)

   ' Draw a circle at the origin of the sketch plane.
   Dim oCircle As SketchCircle
   Set oCircle = oSketch.SketchCircles.AddByCenterRadius( _
   ThisApplication.TransientGeometry.CreatePoint2d(0, 0), 1)

   ' Draw a line along the X axis.
   Call oSketch.SketchLines.AddByTwoPoints(oCircle.CenterSketchPoint, _
   ThisApplication.TransientGeometry.CreatePoint2d(1, 0))

   MsgBox "The sketch will be moved to another face."

   ' Move the sketch to the second face of the model.
   Set oFace = oCompDef.SurfaceBodies.Item(1).Faces.Item(2)
   oSketch.PlanarEntity = oFace

   MsgBox "Current Origin Point: " & oSketch.OriginPointGeometry.X & ", " & _
   oSketch.OriginPointGeometry.Y & ", " & oSketch.OriginPointGeometry.Z & _
   Chr(13) & Chr(13) & _
   "The origin of the sketch will now be set to the center point."

   ' Set the origin point to use the center point work point.
   oSketch.OriginPoint = oCompDef.WorkPoints.Item(1)

   MsgBox "New Origin Point: " & oSketch.OriginPointGeometry.X & ", " & _
   oSketch.OriginPointGeometry.Y & ", " & oSketch.OriginPointGeometry.Z & _
   Chr(13) & Chr(13) & _
   "The origin of the sketch will now be set to the center point."

   MsgBox "Current X axis: " & oSketch.AxisEntityGeometry.Direction.X & ", " & _
   oSketch.AxisEntityGeometry.Direction.Y & ", " & _
   oSketch.AxisEntityGeometry.Direction.Z

   MsgBox "The X axis of the sketch will now be redefined."

   ' Set the axis to be one of the edges of the face.
   oSketch.AxisEntity = oFace.Edges.Item(2)

   MsgBox "New X axis: " & oSketch.AxisEntityGeometry.Direction.X & ", " & _
   oSketch.AxisEntityGeometry.Direction.Y & ", " & _
   oSketch.AxisEntityGeometry.Direction.Z

   MsgBox "The direction of the axis will now be reversed."

   ' Reverse the axis direction.
   oSketch.NaturalAxisDirection = False

   MsgBox "New X axis: " & oSketch.AxisEntityGeometry.Direction.X & ", " & _
   oSketch.AxisEntityGeometry.Direction.Y & ", " & _
   oSketch.AxisEntityGeometry.Direction.Z

   MsgBox "The axis will be changed to define the Y instead of the X axis."

   ' Change the axis definition.
   oSketch.AxisIsX = False
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |