# CropOperation creation sample

## Description

This sample demonstrates how to create a crop operation for a drawing view bases on a sketch under the drawing view.

## Code Samples

* [VBA](#VBA)

This sample demonstrates how to create a crop operation for a drawing view bases on a sketch under the drawing view. You need to open a drawing document with a drawing view in the active sheet before running this sample.

|  |
| --- |
| Copy Code |

```
Sub CropOperationSample()
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oSheet As Sheet
    Set oSheet = oDoc.ActiveSheet

    Dim oView As DrawingView
    Set oView = oSheet.DrawingViews(1)

    Dim oSk As DrawingSketch
    Set oSk = oView.Sketches.Add

    oSk.Edit

    Dim oPtOne As Point2d
    Dim oPtTwo As Point2d
    Set oPtOne = ThisApplication.TransientGeometry.CreatePoint2d(0, 0)
    Set oPtTwo = ThisApplication.TransientGeometry.CreatePoint2d(oView.Width / 2, oView.Height / 2)

    ' Create a rectangler used for crop operation.
    oSk.SketchLines.AddAsTwoPointRectangle oPtOne, oPtTwo

    oSk.ExitEdit

    ' Create a CropOperation.
    Dim oCrop As CropOperation
    Set oCrop = oView.CropOperations.AddBySketch(oSk, True)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |