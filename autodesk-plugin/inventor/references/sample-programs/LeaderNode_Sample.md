# Add new leader note

## Description

This sample illustrates creating leader text on a sheet.

## Code Samples

* [VBA](#VBA)

Before running this sample, open a drawing document and select a linear drawing edge.

|  |
| --- |
| Copy Code |

```
Public Sub AddLeaderNote()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet.
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Set a reference to the drawing curve segment.
    ' This assumes that a drawing curve is selected.
    Dim oDrawingCurveSegment As DrawingCurveSegment
    Set oDrawingCurveSegment = oDrawDoc.SelectSet.Item(1)

    ' Set a reference to the drawing curve.
    Dim oDrawingCurve As DrawingCurve
    Set oDrawingCurve = oDrawingCurveSegment.Parent

    ' Get the mid point of the selected curve
    ' assuming that the selected curve is linear
    Dim oMidPoint As Point2d
    Set oMidPoint = oDrawingCurve.MidPoint

    ' Set a reference to the TransientGeometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    Dim oLeaderPoints As ObjectCollection
    Set oLeaderPoints = ThisApplication.TransientObjects.CreateObjectCollection

    ' Create a few leader points.
    Call oLeaderPoints.Add(oTG.CreatePoint2d(oMidPoint.X + 10, oMidPoint.Y + 10))
    Call oLeaderPoints.Add(oTG.CreatePoint2d(oMidPoint.X + 10, oMidPoint.Y + 5))

    ' Create an intent and add to the leader points collection.
    ' This is the geometry that the leader text will attach to.
    Dim oGeometryIntent As GeometryIntent
    Set oGeometryIntent = oActiveSheet.CreateGeometryIntent(oDrawingCurve)

    Call oLeaderPoints.Add(oGeometryIntent)

    ' Create text with simple string as input. Since this doesn't use
    ' any text overrides, it will default to the active text style.
    Dim sText As String
    sText = "API Leader Note"

    Dim oLeaderNote As LeaderNote
    Set oLeaderNote = oActiveSheet.DrawingNotes.LeaderNotes.Add(oLeaderPoints, sText)

    ' Insert a node.
    Dim oFirstNode As LeaderNode
    Set oFirstNode = oLeaderNote.Leader.RootNode.ChildNodes.Item(1)

    Dim oSecondNode As LeaderNode
    Set oSecondNode = oFirstNode.ChildNodes.Item(1)

    Call oFirstNode.InsertNode(oSecondNode, oTG.CreatePoint2d(oMidPoint.X + 5, oMidPoint.Y + 5))
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |