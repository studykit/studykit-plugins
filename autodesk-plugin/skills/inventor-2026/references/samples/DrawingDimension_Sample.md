# Dimensions - edit

## Description

This sample demonstrates the editing of sheet dimensions and the associated dimension style.

## Code Samples

* [VBA](#VBA)

To run this sample, open a drawing document that has one or more drawing views on the active sheet and add various sheet dimensions to it.

```
Public Sub EditDrawingDimensions()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    'Set a reference to the active sheet.
    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    Dim counter As Long
    counter = 1

    Dim oDrawingDim As DrawingDimension
    For Each oDrawingDim In oSheet.DrawingDimensions

        ' Add some formatted text to all dimensions on the sheet.
        oDrawingDim.Text.FormattedText = " (Metric)"
        counter = counter + 1

    Next

    ' Set a reference to the first general dimension in the collection.
    Dim oGeneralDim As GeneralDimension
    Set oGeneralDim = oSheet.DrawingDimensions.GeneralDimensions.Item(1)

    ' Set a reference to the dimension style of that dimension.
    Dim oDimStyle As DimensionStyle
    Set oDimStyle = oGeneralDim.Style

    ' Modify some properties of the dimension style.
    ' This will modify all dimensions that use this style.
    oDimStyle.LinearPrecision = kFourDecimalPlacesLinearPrecision
    oDimStyle.AngularPrecision = kFourDecimalPlacesAngularPrecision
    oDimStyle.LeadingZeroDisplay = False
    oDimStyle.Tolerance.SetToSymmetric (0.02)
End Sub
```
