# Create linear foreshortened dimension sample

## Description

This sample demonstrates the creation of a linear foreshortened dimension.

## Code Samples

* [VBA](#VBA)

Have a drawing document open and select two paralell linear drawing curve segments in the same drawing view and run the following macro.

|  |
| --- |
| Copy Code |

```
Sub CreateLinearForeshortenedDimSample()
    ' Open a drawing document and select two parallel linear curves in same drawing view first.
    Dim oApp As Inventor.Application
    Set oApp = ThisApplication

    Dim oDoc As Document
    Set oDoc = oApp.ActiveDocument
    If Not (oDoc Is Nothing) Then
        If Not (oDoc.DocumentType = kDrawingDocumentObject) Then
            MsgBox "Please activate a drawing document for this sample.", vbCritical, "Inventor"
            Exit Sub
        End If
    Else
        MsgBox "Please open a drawing document for this sample.", vbCritical, "Inventor"
        Exit Sub
    End If

    If Not (oDoc.SelectSet.Count = 2) Then
        MsgBox "Please select two parallel linear drawing curves from same drawing view for this sample.", vbCritical, "Inventor"
        Exit Sub
    ElseIf (oDoc.SelectSet(1).Type <> kDrawingCurveSegmentObject Or oDoc.SelectSet(1).Type <> kDrawingCurveSegmentObject) Then
        MsgBox "Please select two parallel linear drawing curves from same drawing view for this sample.", vbCritical, "Inventor"
        Exit Sub
    End If

    Dim oCurve1 As DrawingCurve, oCurve2 As DrawingCurve
    Set oCurve1 = oDoc.SelectSet(1).Parent
    Set oCurve2 = oDoc.SelectSet(2).Parent

    Dim oSheet As Sheet
    Set oSheet = oCurve1.Parent.Parent

    ' Create two GeometryIntent based on the selected drawing curve segments.
    Dim oIntent1 As GeometryIntent, oIntent2 As GeometryIntent
    Set oIntent1 = oSheet.CreateGeometryIntent(oCurve1)
    Set oIntent2 = oSheet.CreateGeometryIntent(oCurve2)

    Dim oTextPos As Point2d
    Set oTextPos = oApp.TransientGeometry.CreatePoint2d(12, 12)

    ' Create the linear foreshortened dimension
    Dim oLinearForeshortenedDim As LinearGeneralDimension
    Set oLinearForeshortenedDim = oSheet.DrawingDimensions.GeneralDimensions.AddLinearForeshortened(oTextPos, oIntent1, oIntent2, True)

End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |