# Create BreakOpertion by Sketch Sample

## Description

This sample demonstrates how to create a break operation using a sketch.

## Code Samples

* [VBA](#VBA)
* [VBA](#VBA)

This sample demonstrates how to create a break operation using a sketch. You need to open a drawing document with a drawing view on the active sheet before running this sample.

```
Sub CreateBreakOpertionBySketchSample()
    ' Open a drawing document and place a drawing view on the active sheet before running this sample.
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oView As DrawingView
    Set oView = oDoc.ActiveSheet.DrawingViews(1)

    Dim oSk As DrawingSketch
    Set oSk = oView.Sketches.Add
    oSk.Edit

    Dim oLine As SketchLine
    Dim oPt1 As Point2d, oPt2 As Point2d
    Set oPt1 = ThisApplication.TransientGeometry.CreatePoint2d(-oView.Width / 6, oView.Height / 2)
    Set oPt2 = ThisApplication.TransientGeometry.CreatePoint2d(-oView.Width / 6, -oView.Height / 2)

    Set oLine = oSk.SketchLines.AddByTwoPoints(oPt1, oPt2)

    Set oPt1 = ThisApplication.TransientGeometry.CreatePoint2d(oView.Width / 6, oView.Height / 2)
    Set oPt2 = ThisApplication.TransientGeometry.CreatePoint2d(oView.Width / 6, -oView.Height / 2)
    Set oLine = oSk.SketchLines.AddByTwoPoints(oPt1, oPt2)
    oSk.ExitEdit

    ' Create break operation bases on sketch
    Dim oBreak As BreakOperation
    Set oBreak = oView.BreakOperations.AddBySketch(oSk, kRectangularBreakStyle)
End Sub
```

This sample demonstrates how to create a break operation using a sketch. You need to open a drawing document with a drawing view on the active sheet before running this sample.

```
Sub CreateBreakOpertionBySketchSample()
    ' Open a drawing document and place a drawing view on the active sheet before running this sample.
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oView As DrawingView
    Set oView = oDoc.ActiveSheet.DrawingViews(1)

    Dim oSk As DrawingSketch
    Set oSk = oView.Sketches.Add
    oSk.Edit

    Dim oLine As SketchLine
    Dim oPt1 As Point2d, oPt2 As Point2d
    Set oPt1 = ThisApplication.TransientGeometry.CreatePoint2d(-oView.Width / 6, oView.Height / 2)
    Set oPt2 = ThisApplication.TransientGeometry.CreatePoint2d(-oView.Width / 6, -oView.Height / 2)

    Set oLine = oSk.SketchLines.AddByTwoPoints(oPt1, oPt2)

    Set oPt1 = ThisApplication.TransientGeometry.CreatePoint2d(oView.Width / 6, oView.Height / 2)
    Set oPt2 = ThisApplication.TransientGeometry.CreatePoint2d(oView.Width / 6, -oView.Height / 2)
    Set oLine = oSk.SketchLines.AddByTwoPoints(oPt1, oPt2)
    oSk.ExitEdit

    ' Create break operation bases on sketch
    Dim oBreak As BreakOperation
    Set oBreak = oView.BreakOperations.AddBySketch(oSk, kRectangularBreakStyle)
End Sub
```
