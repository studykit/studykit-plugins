# Adding and editing a feature control frame

## Description

These samples demonstrate editing an existing feature control frame symbol. The first sample adds a row to an existing symbol. The second sample replaces all rows of an existing symbol.

## Code Samples

* [VBA](#VBA)

```
Public Sub EditFeatureControlFrame()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Get the feature control frame selection
    Dim oFCF As FeatureControlFrame
    Set oFCF = oDrawDoc.SelectSet.Item(1)

    ' Add a new row to the FCF symbol
    Dim oNewRow As FeatureControlFrameRow
    Set oNewRow = oFCF.FeatureControlFrameRows.Add(kParallelism, "0.40", , "C")
End Sub

Public Sub BatchUpdateFeatureControlFrameRows()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet.
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Get the feature control frame selection
    Dim oFCF As FeatureControlFrame
    Set oFCF = oDrawDoc.SelectSet.Item(1)

    ' Create a FeatureControlFrameRows object to define the symbol's rows
    Dim oRows As FeatureControlFrameRows
    Set oRows = oActiveSheet.FeatureControlFrames.CreateFeatureControlFrameRows

    ' Add two rows
    Call oRows.Add(kProfileOfAnySurface, "0.20", , "A", "B")
    Call oRows.Add(kParallelism, "0.40", , "C")

    oFCF.FeatureControlFrameRows = oRows
End Sub
```
