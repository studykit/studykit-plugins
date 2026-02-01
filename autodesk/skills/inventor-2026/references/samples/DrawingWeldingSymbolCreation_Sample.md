# Drawing Welding Symbol Creation

## Description

This sample is to demonstrate how to create a drawing welding symbol.

## Code Samples

* [VBA](#VBA)

This sample is to demonstrate how to create a drawing welding symbol.

```
Public Sub AddDrawingWeldingSymbolSample()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet.
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Set a reference to the drawing curve segment.
    ' Please select a linear drwaing curve.
    Dim oDrawingCurveSegment As DrawingCurveSegment
    Set oDrawingCurveSegment = ThisApplication.CommandManager.Pick(kDrawingCurveSegmentFilter, "Select a linear curve")

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

    Dim oWeldingSymDefs As DrawingWeldingSymbolDefinitions
    Set oWeldingSymDefs = oActiveSheet.WeldingSymbols.CreateDefinitions()

    Dim oWeldingSymDef As DrawingWeldingSymbolDefinition
    Set oWeldingSymDef = oWeldingSymDefs.Add(1)

    ' Specify the weld symbol type(WeldSymbolTypeEnum/BackingSymbolTypeEnum)
    oWeldingSymDef.WeldSymbolOne.WeldSymbolType = BackingSymbolTypeEnum.kConsumableInsertANSI
    oWeldingSymDef.WeldSymbolTwo.WeldSymbolType = WeldSymbolTypeEnum.kNoneWeldSymbolType
    oWeldingSymDef.ClosedNoteTail = True
    oWeldingSymDef.FieldWeldingSymbol = True

    ' Create the symbol with a leader
    Dim oSymbol As DrawingWeldingSymbol
    Set oSymbol = oActiveSheet.WeldingSymbols.Add(oLeaderPoints, oWeldingSymDefs)
End Sub
```
