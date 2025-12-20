# Sketch Lines

## Description

This sample demonstrates creating lines. It uses all of the various methods to create lines, both singly and as rectangles.

## Code Samples

* [VBA](#VBA)

To run this sample you must have a sketch active.

|  |
| --- |
| Copy Code |

```
Public Sub DrawSketchLine()
    ' Check to make sure a sketch is open.
    If Not TypeOf ThisApplication.ActiveEditObject Is PlanarSketch Then
      MsgBox "A sketch must be active."
      Exit Sub
    End If

    ' Set a reference to the active sketch.
    Dim oSketch As PlanarSketch
    Set oSketch = ThisApplication.ActiveEditObject

    ' Set a reference to the transient geometry collection.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Create a new transaction to wrap the construction of the three lines
    ' into a single undo.
    Dim oTrans As Transaction
    Set oTrans = ThisApplication.TransactionManager.StartTransaction( _
    ThisApplication.ActiveDocument, _
    "Create Triangle Sample")

    ' Create the first line of the triangle. This uses two transient points as
    ' input to definethe coordinates of the ends of the line. Since a transient
    ' point is input a sketch point is automatically created at that location and
    ' the line is attached to it.
    Dim oLines(1 To 3) As SketchLine
    Set oLines(1) = oSketch.SketchLines.AddByTwoPoints(oTransGeom.CreatePoint2d(0, 0), _
    oTransGeom.CreatePoint2d(4, 0))

    ' Create a sketch line that is connected to the sketch point the previous lines
    ' end point is connected to. This will automatically create the constraint to
    ' tie the new line to the sketch point the previous line is also connected to.
    ' This will result in the the two lines being connected since they're both tied
    ' to the same sketch point.
    Set oLines(2) = oSketch.SketchLines.AddByTwoPoints(oLines(1).EndSketchPoint, _
    oTransGeom.CreatePoint2d(2, 3))

    ' Create a third line and connect it to the start point of the first line and the
    ' end point of the second line. This will result in a connected triangle.
    Set oLines(3) = oSketch.SketchLines.AddByTwoPoints(oLines(2).EndSketchPoint, _
    oLines(1).StartSketchPoint)

    ' End the transaction for the triangle.
    oTrans.End

    ' Create a rectangle whose lines are parallel to the sketch planes x and y axes
    ' by using the SketchLines.AddAsTwoPointRectangle method. The top point of the
    ' triangle will be used as input for one of the points so the rectangle will be
    ' tied to that point.
    Dim oRectangleLines As SketchEntitiesEnumerator
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
    oLines(3).StartSketchPoint, _
    oTransGeom.CreatePoint2d(5, 5))

    ' Create a rotated rectangle by using the SketchLines.AddAsTwoRectangle method.
    ' One of the corners of this rectangle will be tied to the corner of the previous
    ' rectangle.
    Set oRectangleLines = oSketch.SketchLines.AddAsThreePointRectangle( _
    oRectangleLines(2).EndSketchPoint, _
    oTransGeom.CreatePoint2d(7, 3), _
    oTransGeom.CreatePoint2d(8, 8))
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |