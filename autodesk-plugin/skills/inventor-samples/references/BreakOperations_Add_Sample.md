# Creation of a break operation in a drawing view

## Description

Demonstrates the creation of a break operation.

## Code Samples

* [VBA](#VBA)

Before running this sample, select a drawing view in the active drawing.

|  |
| --- |
| Copy Code |

```
Public Sub CreateBreakoperationInDrawingView()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    'Set a reference to the active sheet.
    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    ' Check to make sure a drawing view is selected.
    If Not TypeOf oDrawDoc.SelectSet.Item(1) Is DrawingView Then
        MsgBox "A drawing view must be selected."
        Exit Sub
    End If

    ' Set a reference to the selected drawing. This assumes
    ' that the selected view is not a draft view.
    Dim oDrawingView As DrawingView
    Set oDrawingView = oDrawDoc.SelectSet.Item(1)

    ' Set a reference to the center of the base view.
    Dim oCenter As Point2d
    Set oCenter = oDrawingView.Center

    ' Define the start point of the break
    Dim oStartPoint As Point2d
    Set oStartPoint = ThisApplication.TransientGeometry.CreatePoint2d(oCenter.X - 1, oCenter.Y)

    ' Define the end point of the break
    Dim oEndPoint As Point2d
    Set oEndPoint = ThisApplication.TransientGeometry.CreatePoint2d(oCenter.X + 1, oCenter.Y)

    Dim oBreakOperation As BreakOperation
    Set oBreakOperation = oDrawingView.BreakOperations.Add(kHorizontalBreakOrientation, oStartPoint, oEndPoint, kRectangularBreakStyle, 5)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |