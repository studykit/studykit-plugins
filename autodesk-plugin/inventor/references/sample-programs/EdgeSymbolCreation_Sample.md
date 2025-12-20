# EdgeSymbol Creation Sample

## Description

This sample is to demonstrate how to create a EdgeSymbol in drawing document.

## Code Samples

* [VBA](#VBA)

This sample is to demonstrate how to create a EdgeSymbol in drawing document.

|  |
| --- |
| Copy Code |

```
Public Sub CreateEdgeSymbol()

    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet.
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Set a reference to the TransientGeometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Specify the leader points
    Dim oPoints(1 To 2) As Point2d
    Set oPoints(1) = oTG.CreatePoint2d(10, 10)
    Set oPoints(2) = oTG.CreatePoint2d(13, 15)

    Dim oLeaderPoints As ObjectCollection
    Set oLeaderPoints = ThisApplication.TransientObjects.CreateObjectCollection

    Dim i As Long
    For i = 1 To 2
        Call oLeaderPoints.Add(oPoints(i))
    Next

    Dim oEdgeSymbolDef As EdgeSymbolDefinition
    Set oEdgeSymbolDef = oActiveSheet.EdgeSymbols.CreateDefinition(kEdgeSymbolValueNoValues, kAllEdgesIndicationType)

    ' Create teh edge symbol.
    Dim oEdgeSymbol As EdgeSymbol
    Set oEdgeSymbol = oActiveSheet.EdgeSymbols.Add(oLeaderPoints, oEdgeSymbolDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |