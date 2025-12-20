# Create a feature control frame symbol

## Description

This sample demonstrates the creation of a feature control frame symbol.

## Code Samples

* [VBA](#VBA)

Select a linear drawing curve and run the sample.

|  |
| --- |
| Copy Code |

```
Public Sub AddFeatureControlFrame()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet.
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Set a reference to the drawing curve segment.
    ' This assumes that a drwaing curve is selected.
    Dim oDrawingCurveSegment As DrawingCurveSegment
    Set oDrawingCurveSegment = oDrawDoc.SelectSet.Item(1)

    ' Set a reference to the drawing curve.
    Dim oDrawingCurve As DrawingCurve
    Set oDrawingCurve = oDrawingCurveSegment.Parent

    ' Get the mid point of the selected curve
    ' assuming that the selection curve is linear
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
    ' This is the geometry that the symbol will attach to.
    Dim oGeometryIntent As GeometryIntent
    Set oGeometryIntent = oActiveSheet.CreateGeometryIntent(oDrawingCurve)
    Call oLeaderPoints.Add(oGeometryIntent)

    ' Create a FeatureControlFrameRows object to define the symbol's rows
    Dim oRows As FeatureControlFrameRows
    Set oRows = oActiveSheet.FeatureControlFrames.CreateFeatureControlFrameRows

    ' Add a row
    Dim oRow As FeatureControlFrameRow
    Set oRow = oRows.Add(kProfileOfAnySurface, "0.20", , "A", "B")

    ' Create the feature control frame symbol with a leader
    Dim oSymbol As FeatureControlFrame
    Set oSymbol = oActiveSheet.FeatureControlFrames.Add(oLeaderPoints, oRows)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |