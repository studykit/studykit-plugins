# Sketch within a drawing view

## Description

This sample demonstrates creating a sketch within an existing drawing view.

## Code Samples

* [VBA](#VBA)

To run this sample have a drawing open where the active sheet contains at least one drawing view.

|  |
| --- |
| Copy Code |

```
Private Sub CreateDrawingSketchInView()
    ' Set a reference to the active document.  This assumes it
    ' is a drawing document.
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Set a reference to the first drawing view on the active sheet.  This
    ' assumes the active sheet contains at least one drawing view.
    Dim oDrawView As DrawingView
    Set oDrawView = oDoc.ActiveSheet.DrawingViews.Item(1)

    ' Create the new drawing sketch.
    Dim oSketch As DrawingSketch
    Set oSketch = oDrawView.Sketches.Add

    ' Set a reference to the transient geometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Open the sketch for edit.
    oSketch.Edit

    ' Draw two lines in the sketch.
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(0, 0), oTG.CreatePoint2d(3, 3))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(0, 3), oTG.CreatePoint2d(3, 0))

    ' Exit from editing the sketch.
    oSketch.ExitEdit
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |