# Creating a parts list

## Description

This sample demonstrates the creation of a parts list. The parts list is placed at the top right corner of the border if one exists, else it is placed at the top right corner of the sheet.

## Code Samples

* [VBA](#VBA)

To run this sample, have a drawing document open. The active sheet in the drawing should have at least one drawing view and the first drawing view on the sheet should not be a draft view.

|  |
| --- |
| Copy Code |

```
Public Sub CreatePartsList()
    On Error Resume Next

    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    'Set a reference to the active sheet.
    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    ' Set a reference to the first drawing view on
    ' the sheet. This assumes the first drawing
    ' view on the sheet is not a draft view.
    Dim oDrawingView As DrawingView
    Set oDrawingView = oSheet.DrawingViews(1)

    ' Set a reference to th sheet's border
    Dim oBorder As Border
    Set oBorder = oSheet.Border

    Dim oPlacementPoint As Point2d

    If Not oBorder Is Nothing Then
        ' A border exists. The placement point
        ' is the top-right corner of the border.
        Set oPlacementPoint = oBorder.RangeBox.MaxPoint
    Else
        ' There is no border. The placement point
        ' is the top-right corner of the sheet.
        Set oPlacementPoint = ThisApplication.TransientGeometry.CreatePoint2d(oSheet.Width, oSheet.height)
    End If

    ' Create the parts list.
    Dim oPartsList As PartsList
    Set oPartsList = oSheet.PartsLists.Add(oDrawingView, oPlacementPoint)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |