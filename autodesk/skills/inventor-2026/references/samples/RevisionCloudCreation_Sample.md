# RevisionCloud Creation Sample

## Description

This sample is to demonstrate how to create a revision cloud in drawing document.

## Code Samples

* [VBA](#VBA)

This sample is to demonstrate how to create a revision cloud in drawing document.

```
Public Sub CreateRevisionCloud()

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

    ' Specify the control points position
    Dim oPosition(1 To 4) As Point2d
    Set oPosition(1) = oTG.CreatePoint2d(10, 10)
    Set oPosition(2) = oTG.CreatePoint2d(13, 15)
    Set oPosition(3) = oTG.CreatePoint2d(18, 10)
    Set oPosition(4) = oTG.CreatePoint2d(13, 6)

    Dim oControlPoints As ObjectCollection
    Set oControlPoints = ThisApplication.TransientObjects.CreateObjectCollection

    Dim i As Long
    For i = 1 To 4
        Call oControlPoints.Add(oPosition(i))
    Next

    ' Create teh revision cloud definition object.
    Dim oRCDef As RevisionCloudDefinition
    Set oRCDef = oActiveSheet.RevisionClouds.CreateRevisionCloudDefinition(oControlPoints, "View Rev 1")

    ' Create the revision cloud.
    Dim oRevisionCloud As RevisionCloud
    Set oRevisionCloud = oActiveSheet.RevisionClouds.Add(oRCDef)

End Sub
```
