# Center Dimension Text

## Description

This sample demonstrates how to center the text of all dimensions on the active sheet in a drawing.

## Code Samples

* [VBA](#VBA)

Only linear and angular general dimensions are supported. Open a drawing document that contains several dimensions and run the sample.

```
Public Sub CenterAllDimensions()
    ' Set a reference to the active drawing document
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet
    Dim oSheet As Sheet
    Set oSheet = oDoc.ActiveSheet

    Dim oDrawingDim As DrawingDimension

    ' Iterate over all dimensions in the drawing and
    ' center them if they are linear or angular.

    For Each oDrawingDim In oSheet.DrawingDimensions
        If TypeOf oDrawingDim Is LinearGeneralDimension Or _
           TypeOf oDrawingDim Is AngularGeneralDimension Then
            Call oDrawingDim.CenterText
        End If
    Next
End Sub
```
