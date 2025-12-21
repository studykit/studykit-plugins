# Create bend note

## Description

This sample demonstrates the creation of a bend note on the drawing view of a flat pattern.

## Code Samples

* [VBA](#VBA)

Select a bend edge on a flat pattern drawing view and run the sample.

```
Sub AddBendNote()
    ' Assumes that a drawing document is active
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Check to make sure a bend edge is selected.
    If oDoc.SelectSet.Count <> 1 Then
        MsgBox "A single bend edge must be selected."
        Exit Sub
    End If

    If Not TypeOf oDoc.SelectSet(1) Is DrawingCurveSegment Then
        MsgBox "A bend edge must be selected."
        Exit Sub
    End If

    Dim oBendEdge As DrawingCurve
    Set oBendEdge = oDoc.SelectSet(1).Parent

    If Not (oBendEdge.EdgeType = kBendUpEdge Or oBendEdge.EdgeType = kBendDownEdge) Then
        MsgBox "A bend edge must be selected."
        Exit Sub
    End If

    ' Create the bend note
    Dim oBendNote As BendNote
    Set oBendNote = oDoc.ActiveSheet.DrawingNotes.BendNotes.Add(oBendEdge)
End Sub
```
