# Chain dimensions sets

## Description

This sample demonstrates the creation of a chain dimension set in a drawing.

## Code Samples

* [VBA](#VBA)

Create a drawing view and select multiple edges in the view before running the sample.

```
Public Sub CreateChainDimensionSet()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet.
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    Dim oIntentCollection As ObjectCollection
    Set oIntentCollection = ThisApplication.TransientObjects.CreateObjectCollection

    ' Get all the selected drawing curve segments.
    Dim oDrawingCurveSegment As DrawingCurveSegment
    Dim oDrawingCurve As DrawingCurve
    For Each oDrawingCurveSegment In oDrawDoc.SelectSet

        ' Set a reference to the drawing curve.
        Set oDrawingCurve = oDrawingCurveSegment.Parent

        Dim oDimIntent As GeometryIntent
        Set oDimIntent = oActiveSheet.CreateGeometryIntent(oDrawingCurve)

        Call oIntentCollection.Add(oDimIntent)
    Next

   ' Set a reference to the view to which the curve belongs.
    Dim oDrawingView As DrawingView
    Set oDrawingView = oDrawingCurve.Parent

    ' Set a reference to the chain dimension sets collection.
    Dim oChainDimSets As ChainDimensionSets
    Set oChainDimSets = oActiveSheet.DrawingDimensions.ChainDimensionSets

    ' Determine the placement point
    Dim oPlacementPoint As Point2d
    Set oPlacementPoint = ThisApplication.TransientGeometry.CreatePoint2d(oDrawingView.Center.X, oDrawingView.Top + 5)

    ' Create a horizontal chain dimension set.
    Dim oChainDimSet As ChainDimensionSet
    Set oChainDimSet = oChainDimSets.Add(oIntentCollection, oPlacementPoint, kHorizontalDimensionType)
End Sub
```
