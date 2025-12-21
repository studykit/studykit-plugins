# Draft Views - create

## Description

This sample demonstrates the creation of a draft view in a drawing.

## Code Samples

* [VBA](#VBA)

Open a drawing document and run the following sample.

```
Public Sub CreateDraftView()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    'Set a reference to the active sheet.
    'A draft view can only be created on an active sheet.
    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    'Set a reference to the drawing view.
    Dim oDraftView As DrawingView
    Set oDraftView = oSheet.DrawingViews.AddDraftView(1#, "My Draft View")

    ' Set a reference to the sketch of the created draft view.
    Dim oSketch As DrawingSketch
    Set oSketch = oDraftView.Sketches.Item(1)

    ' Set a reference to the transient geometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Draw two lines in the sketch.
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(10, 10), oTG.CreatePoint2d(30, 30))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(10, 30), oTG.CreatePoint2d(30, 10))

    ' Exit from editing the sketch.
    oSketch.ExitEdit

End Sub
```
