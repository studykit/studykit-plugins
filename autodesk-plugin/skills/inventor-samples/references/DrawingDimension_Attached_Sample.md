# Find and remove unattached dimensions

## Description

This sample finds and deletes all unattached drawing dimensions on the active sheet in a drawing.

## Code Samples

* [VBA](#VBA)

Before you run the sample, have a drawing document open that contains several drawing dimensions including unattached (sick) ones.

```
Public Sub DeleteUnattachedDimensions()
    ' Set a reference to the active drawing document
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet
    Dim oSheet As Sheet
    Set oSheet = oDoc.ActiveSheet

    Dim oDrawingDim As DrawingDimension

    ' Iterate over all dimensions in the drawing
    ' and delete unattached (sick) dimensions.

    For Each oDrawingDim In oSheet.DrawingDimensions
        If oDrawingDim.Attached = False Then
            Call oDrawingDim.Delete
        End If
    Next
End Sub
```
