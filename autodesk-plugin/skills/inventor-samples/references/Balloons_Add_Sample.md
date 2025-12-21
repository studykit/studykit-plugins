# Creation a balloon

## Description

This sample demonstrates the creation of a balloon.

## Code Samples

* [VBA](#VBA)

Select a linear drawing curve and run the sample.

```
Public Sub CreateBalloon()
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
    ' assuming that the selection curve is linear. This is used to calculate the position of balloon and leader line.
    Dim oMidPoint As Point2d
    Set oMidPoint = oDrawingCurve.MidPoint

    ' Set a reference to the TransientGeometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    Dim oLeaderPoints As ObjectCollection
    Set oLeaderPoints = ThisApplication.TransientObjects.CreateObjectCollection

    ' Create a couple of leader points.
    Call oLeaderPoints.Add(oTG.CreatePoint2d(oMidPoint.X + 10, oMidPoint.Y + 10))
    Call oLeaderPoints.Add(oTG.CreatePoint2d(oMidPoint.X + 10, oMidPoint.Y + 5))

    ' Add the GeometryIntent to the leader points collection.
    ' This is the geometry that the balloon will attach to. The mid-point of the geometry will be attached to.
    Dim oGeometryIntent As GeometryIntent
    Set oGeometryIntent = oActiveSheet.CreateGeometryIntent(oDrawingCurve,oMidPoint)
    Call oLeaderPoints.Add(oGeometryIntent)

    ' Set a reference to the parent drawing view of the selected curve
    Dim oDrawingView As DrawingView
    Set oDrawingView = oDrawingCurve.Parent

    ' Set a reference to the referenced model document
    Dim oModelDoc As Document
    Set oModelDoc = oDrawingView.ReferencedDocumentDescriptor.ReferencedDocument

    ' Check if a partslist or a balloon has already been created for this model
    Dim IsDrawingBOMDefined As Boolean
    IsDrawingBOMDefined = oDrawDoc.DrawingBOMs.IsDrawingBOMDefined(oModelDoc.FullFileName)

    Dim oBalloon As Balloon

    If IsDrawingBOMDefined Then

        ' Just create the balloon with the leader points
        ' All other arguments can be ignored
        Set oBalloon = oDrawDoc.ActiveSheet.Balloons.Add(oLeaderPoints)
    Else

        ' First check if the 'structured' BOM view has been enabled in the model

        ' Set a reference to the model's BOM object
        Dim oBOM As BOM
        Set oBOM = oModelDoc.ComponentDefinition.BOM

        If oBOM.StructuredViewEnabled Then

            ' Level needs to be specified
            ' Numbering options have already been defined
            ' Get the Level ('All levels' or 'First level only')
            ' from the model BOM view - must use the same here
            Dim Level As PartsListLevelEnum
            If oBOM.StructuredViewFirstLevelOnly Then
                Level = kStructured
            Else
                Level = kStructuredAllLevels
            End If

            ' Create the balloon by specifying just the level
            Set oBalloon = oActiveSheet.Balloons.Add(oLeaderPoints, , Level)
        Else

            ' Level and numbering options must be specified
            ' The corresponding model BOM view will automatically be enabled
            Dim oNumberingScheme As NameValueMap
            Set oNumberingScheme = ThisApplication.TransientObjects.CreateNameValueMap

            ' Add the option for a comma delimiter
            oNumberingScheme.Add "Delimiter", ","

            ' Create the balloon by specifying the level and numbering scheme
            Set oBalloon = oActiveSheet.Balloons.Add(oLeaderPoints, , kStructuredAllLevels, oNumberingScheme)
        End If
    End If
End Sub
```
