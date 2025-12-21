# Create thread note

## Description

This sample demonstrates the creation of a thread note on a drawing view.

## Code Samples

* [VBA](#VBA)

Select a thread edge on a drawing view and run the sample.

|  |
| --- |
| Copy Code |

```
Sub AddThreadNote()
    ' Assumes that a drawing document is active
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Check to make sure a thread edge is selected.
    If oDoc.SelectSet.Count <> 1 Then
        MsgBox "A single thread edge must be selected."
        Exit Sub
    End If

    If Not TypeOf oDoc.SelectSet(1) Is DrawingCurveSegment Then
        MsgBox "A thread edge must be selected."
        Exit Sub
    End If

    Dim oThreadEdge As DrawingCurve
    Set oThreadEdge = oDoc.SelectSet(1).Parent

    If Not (oThreadEdge.EdgeType = kThreadEdge) Then
        MsgBox "A thread edge must be selected."
        Exit Sub
    End If

    Dim oPosition As Point2d
    Set oPosition = ThisApplication.TransientGeometry.CreatePoint2d(5, 25)

    ' Create the thread note
    Dim oThreadNote As HoleThreadNote
    Set oThreadNote = oDoc.ActiveSheet.DrawingNotes.HoleThreadNotes.Add(oPosition, oThreadEdge)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |