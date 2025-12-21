# Add surface texture symbol to dimension

## Description

This sample demonstrates the creation of a surface texture symbol attached to the extension line of a drawing dimension.

## Code Samples

* [VBA](#VBA)

Select a linear general dimension in a drawing and run the sample.

|  |
| --- |
| Copy Code |

```
Public Sub AddSurfaceTextureSymbol()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Check to make sure a linear dimension is selected.
    If Not TypeOf oDrawDoc.SelectSet.Item(1) Is LinearGeneralDimension Then
        MsgBox "A linear general dimension must be selected."
        Exit Sub
    End If

    ' Set a reference to the active sheet.
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Set a reference to the drawing dimension.
    ' This assumes that a linear general dimension is selected.
    Dim oLinearDim As LinearGeneralDimension
    Set oLinearDim = oDrawDoc.SelectSet.Item(1)

    ' Get the mid point of the first extension line of the dimension
    Dim oMidPoint As Object
    Set oMidPoint = oLinearDim.ExtensionLineOne.MidPoint

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
    Set oGeometryIntent = oActiveSheet.CreateGeometryIntent(oLinearDim, oMidPoint)

    Call oLeaderPoints.Add(oGeometryIntent)

    ' Create the symbol with a leader
    Dim oSymbol As SurfaceTextureSymbol
    Set oSymbol = oActiveSheet.SurfaceTextureSymbols.Add(oLeaderPoints, _
            kMaterialRemovalRequiredSurfaceType, _
            True, _
            True, _
            True, _
            0.1, _
            , , , , , _
            kParticulateNondirectional)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |