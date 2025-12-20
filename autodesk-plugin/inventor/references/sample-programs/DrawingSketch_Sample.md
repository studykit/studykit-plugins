# Drawing Sketches - editing line type and color

## Description

This sample demonstrates the modification of sketch entity line type and color in drawings.

## Code Samples

* [VBA](#VBA)

Open a drawing document and run the following sample.

|  |
| --- |
| Copy Code |

```
Public Sub ModifyDrawingSketchEntityProperties()
    ' Set a reference to the active document.  This assumes it
    ' is a drawing document.
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Set a reference to the drawing view on the active sheet.
    Dim oDrawView As DrawingView
    Set oDrawView = oDoc.ActiveSheet.DrawingViews.AddDraftView

    ' Set a reference to the sketch of the draft view.
    Dim oSketch As DrawingSketch
    Set oSketch = oDrawView.Sketches.Item(1)

    ' Set a reference to the transient geometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Draw two lines in the sketch.
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(10, 10), oTG.CreatePoint2d(30, 30))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(10, 30), oTG.CreatePoint2d(30, 10))

    ' Create a transient color object.
    Dim oColor As Color
    Set oColor = ThisApplication.TransientObjects.CreateColor(255, 0, 0) 'Red

    ' Override the color of the first line.
    oSketch.SketchLines(1).OverrideColor = oColor

    ' Override the line type of the second line.
    oSketch.SketchLines(2).LineType = kDashedLineType

    ' Override the line weight of the second line.
    oSketch.SketchLines(2).LineWeight = 0.11

    ' Override the line scale of the second line.
    oSketch.SketchLines(2).LineScale = 0.5

    ' Exit from editing the sketch.
    oSketch.ExitEdit
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |