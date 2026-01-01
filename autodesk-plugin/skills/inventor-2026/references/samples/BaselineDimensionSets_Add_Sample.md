# Baseline dimension sets

## Description

This sample demonstrates the creation of a baseline set dimension in a drawing.

## Code Samples

* [VBA](#VBA)

Create a drawing view and select multiple edges in the view before running the sample.

```
Public Sub CreateBaselineDimensionSet()
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

    ' Set a reference to the baseline dimension sets collection.
    Dim oBaselineSets As BaselineDimensionSets
    Set oBaselineSets = oActiveSheet.DrawingDimensions.BaselineDimensionSets

    ' Determine the placement point
    Dim oPlacementPoint As Point2d
    Set oPlacementPoint = ThisApplication.TransientGeometry.CreatePoint2d(oDrawingView.Left - 5, oDrawingView.Center.Y)

    ' Create a vertical baseline set dimension.
    Dim oBaselineSet As BaselineDimensionSet
    Set oBaselineSet = oBaselineSets.Add(oIntentCollection, oPlacementPoint, kVerticalDimensionType)
End Sub
```
