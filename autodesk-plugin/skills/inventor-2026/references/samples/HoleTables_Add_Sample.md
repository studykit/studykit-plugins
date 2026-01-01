# Creating hole tables

## Description

This sample demonstrates the creation of hole tables in a drawing.

## Code Samples

* [VBA](#VBA)

Select a drawing view that contains holes and run the following sample.

```
Sub CreateHoleTables()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet.
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Set a reference to the drawing view.
    ' This assumes that a drawing view is selected.
    Dim oDrawingView As DrawingView
    Set oDrawingView = oDrawDoc.SelectSet.Item(1)

    ' Create origin indicator if it has not been already created.
    If Not oDrawingView.HasOriginIndicator Then
        ' Create point intent to anchor the origin to.
        Dim oDimIntent As GeometryIntent
        Dim oPointIntent As Point2d

        ' Get the first curve on the view
        Dim oCurve As DrawingCurve
        Set oCurve = oDrawingView.DrawingCurves.Item(1)

        ' Check if it has a strt point
        Set oPointIntent = oCurve.StartPoint

        If oPointIntent Is Nothing Then
            ' Else use the center point
            Set oPointIntent = oCurve.CenterPoint
        End If

        Set oDimIntent = oActiveSheet.CreateGeometryIntent(oCurve, oPointIntent)

        oDrawingView.CreateOriginIndicator oDimIntent
    End If

    Dim oPlacementPoint As Point2d

    ' Set a reference to th sheet's border
    Dim oBorder As Border
    Set oBorder = oActiveSheet.Border

    If Not oBorder Is Nothing Then
        ' A border exists. The placement point
        ' is the top-left corner of the border.
        Set oPlacementPoint = ThisApplication.TransientGeometry.CreatePoint2d(oBorder.RangeBox.MinPoint.X, oBorder.RangeBox.MaxPoint.Y)
    Else
        ' There is no border. The placement point
        ' is the top-left corner of the sheet.
        Set oPlacementPoint = ThisApplication.TransientGeometry.CreatePoint2d(0, oActiveSheet.height)
    End If

    ' Create a 'view' hole table
    ' This hole table includes all holes as specified by the active hole table style
    Dim oViewHoleTable As HoleTable
    Set oViewHoleTable = oActiveSheet.HoleTables.Add(oDrawingView, oPlacementPoint)

    oPlacementPoint.X = oActiveSheet.width / 2

    ' Create a 'feature type' hole table
    ' This hole table includes specified hole types only
    Dim oFeatureHoleTable As HoleTable
    Set oFeatureHoleTable = oActiveSheet.HoleTables.AddByFeatureType(oDrawingView, oPlacementPoint, _
            True, True, True, True, False, False, False)
End Sub
```
