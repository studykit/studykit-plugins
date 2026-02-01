# Create ordinate dimension

## Description

This sample demonstrates the creation of ordinate dimensions in a drawing document.

## Code Samples

* [VBA](#VBA)

Before running this sample, select a linear drawing curve on the active drawing document.

```
Public Sub CreateOrdinateDimensions()
  ' Set a reference to the drawing document.
  ' This assumes a drawing document is active.
  Dim oDrawDoc As DrawingDocument
  Set oDrawDoc = ThisApplication.ActiveDocument

  ' Set a reference to the active sheet.
  Dim oActiveSheet As Sheet
  Set oActiveSheet = oDrawDoc.ActiveSheet

  ' Set a reference to the drawing curve segment.
  ' This assumes that a linear drawing curve is selected.
  Dim oDrawingCurveSegment As DrawingCurveSegment
  Set oDrawingCurveSegment = oDrawDoc.SelectSet.Item(1)

  ' Set a reference to the drawing curve.
  Dim oDrawingCurve As DrawingCurve
  Set oDrawingCurve = oDrawingCurveSegment.Parent

  If Not oDrawingCurve.CurveType = kLineSegmentCurve Then
    MsgBox "A linear curve should be selected for this sample."
    Exit Sub
  End If

  ' Create point intents to anchor the dimension to.
  Dim oDimIntent1 As GeometryIntent
  Set oDimIntent1 = oActiveSheet.CreateGeometryIntent(oDrawingCurve, kStartPointIntent)

  Dim oDimIntent2 As GeometryIntent
  Set oDimIntent2 = oActiveSheet.CreateGeometryIntent(oDrawingCurve, kEndPointIntent)

  ' Set a reference to the view to which the curve belongs.
  Dim oDrawingView As DrawingView
  Set oDrawingView = oDrawingCurve.Parent

  ' If origin indicator has not been already created, create it first.
  If Not oDrawingView.HasOriginIndicator Then
    ' The indicator will be located at the start point of the selected curve.
    oDrawingView.CreateOriginIndicator oDimIntent1
  End If

  ' Set a reference to the ordinate dimensions collection.
  Dim oOrdinateDimensions As OrdinateDimensions
  Set oOrdinateDimensions = oActiveSheet.DrawingDimensions.OrdinateDimensions

  ' Create the x-axis vector
  Dim oXAxis As Vector2d
  Set oXAxis = ThisApplication.TransientGeometry.CreateVector2d(1, 0)

  Dim oCurveVector As Vector2d
  Set oCurveVector = oDrawingCurve.StartPoint.VectorTo(oDrawingCurve.EndPoint)

  Dim oTextOrigin1 As Point2d
  Dim oTextOrigin2 As Point2d
  Dim DimType As DimensionTypeEnum

  If oCurveVector.IsParallelTo(oXAxis) Then
    ' Selected curve is horizontal
    DimType = kVerticalDimensionType

    ' Set the text points for the 2 dimensions.
    Set oTextOrigin1 = ThisApplication.TransientGeometry.CreatePoint2d(oDrawingCurve.StartPoint.X, oDrawingView.Top + 5)
    Set oTextOrigin2 = ThisApplication.TransientGeometry.CreatePoint2d(oDrawingCurve.EndPoint.X, oDrawingView.Top + 5)

  Else
    ' Selected curve is vertical or at an angle.
    DimType = kHorizontalDimensionType

    ' Set the text points for the 2 dimensions.
    Set oTextOrigin1 = ThisApplication.TransientGeometry.CreatePoint2d(oDrawingView.Left - 5, oDrawingCurve.StartPoint.Y)
    Set oTextOrigin2 = ThisApplication.TransientGeometry.CreatePoint2d(oDrawingView.Left - 5, oDrawingCurve.EndPoint.Y)

  End If

  ' Create the first ordinate dimension.
  Dim oOrdinateDimension1 As OrdinateDimension
  Set oOrdinateDimension1 = oOrdinateDimensions.Add(oDimIntent1, oTextOrigin1, DimType)

  ' Create the second ordinate dimension.
  Dim oOrdinateDimension2 As OrdinateDimension
  Set oOrdinateDimension2 = oOrdinateDimensions.Add(oDimIntent2, oTextOrigin2, DimType)
End Sub
```
