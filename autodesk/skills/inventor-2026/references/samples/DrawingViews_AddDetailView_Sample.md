# Add detail drawing view

## Description

This sample demonstrates the creation of a detail drawing view with an attach point.

## Code Samples

* [VBA](#VBA)

Before running this sample, select a drawing view in the active drawing.

```
Public Sub CreateDetailView()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Select a drawing view.
    Dim oDrawingView As DrawingView
    Set oDrawingView = ThisApplication.CommandManager.Pick(kDrawingViewFilter, "Select a drawing view.")

    'Set a reference to the active sheet.
    Dim oSheet As Sheet
    Set oSheet = oDrawingView.Parent

    ' Set a reference to the center of the base view.
    Dim oPoint As Point2d
    Set oPoint = oDrawingView.Center

    ' Translate point by a distance equal to the width of the view
    ' This will be the placement point of the detail view.
    oPoint.X = oPoint.X + oDrawingView.Width

    ' Arbitrarily find an arc within the selected drawing view.
    ' The detail view will include this arc.
    Dim oCurve As DrawingCurve
    Dim oArcCurve As DrawingCurve
    For Each oCurve In oDrawingView.DrawingCurves
        If oCurve.CurveType = kCircularArcCurve Then
            Set oArcCurve = oCurve
            Exit For
        End If
    Next

    If Not oArcCurve Is Nothing Then
        ' Use the range of the arc in sheet space to calculate the detail view box.
        Dim oCornerOne As Point2d
        Set oCornerOne = oArcCurve.Evaluator2D.RangeBox.MinPoint
        oCornerOne.X = oCornerOne.X - 1
        oCornerOne.Y = oCornerOne.Y - 1

        Dim oCornerTwo As Point2d
        Set oCornerTwo = oArcCurve.Evaluator2D.RangeBox.MaxPoint
        oCornerTwo.X = oCornerTwo.X + 1
        oCornerTwo.Y = oCornerTwo.Y + 1

        ' Create the detail view with a rectangular box.
        Dim oDetailView As DetailDrawingView
        Set oDetailView = oSheet.DrawingViews.AddDetailView(oDrawingView, oPoint, _
        kFromBaseDrawingViewStyle, False, oCornerOne, oCornerTwo, , oDrawingView.Scale * 2)
    Else
        MsgBox "No arc was found in the selected drawing view."
    End If
End Sub
```
