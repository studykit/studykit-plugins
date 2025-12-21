# create punch note

## Description

This sample demonstrates the creation of a punch note on the drawing view of a flat pattern.

## Code Samples

* [VBA](#VBA)

Select a punch edge on a flat pattern drawing view and run the sample.

```
Sub AddPunchNote()
    ' Assumes that a drawing document is active
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Check to make sure a punch edge is selected.
    If oDoc.SelectSet.Count <> 1 Then
        MsgBox "A single punch edge must be selected."
        Exit Sub
    End If

    If Not TypeOf oDoc.SelectSet(1) Is DrawingCurveSegment Then
        MsgBox "A punch edge must be selected."
        Exit Sub
    End If

    Dim oPunchEdge As DrawingCurve
    Set oPunchEdge = oDoc.SelectSet(1).Parent

    If Not (oPunchEdge.EdgeType = kPunchUpEdge Or oPunchEdge.EdgeType = kPunchDownEdge) Then
        MsgBox "A punch edge must be selected."
        Exit Sub
    End If

    Dim oPunchEdgeIntent As GeometryIntent
    Set oPunchEdgeIntent = oDoc.ActiveSheet.CreateGeometryIntent(oPunchEdge)

    Dim oPosition As Point2d
    Set oPosition = ThisApplication.TransientGeometry.CreatePoint2d(5, 25)

    ' Create the punch note
    Dim oPunchNote As PunchNote
    Set oPunchNote = oDoc.ActiveSheet.DrawingNotes.PunchNotes.Add(oPosition, oPunchEdgeIntent)
End Sub
```
