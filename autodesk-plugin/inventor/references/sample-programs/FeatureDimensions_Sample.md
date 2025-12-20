# Query feature dimensions

## Description

This sample demonstrates querying the dimensions of a feature in a part or an assembly document. The sample also demonstrates how to show the dimensions of a feature.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Sub QueryAndShowFeatureDimensions()
    Dim oDoc As Document
    Set oDoc = ThisApplication.ActiveDocument

    ' Check to make sure a feature is selected.
    If Not Typeof oDoc.SelectSet.Item(1) Is PartFeature Then
        MsgBox "A feature must be selected."
        Exit Sub
    End If

    ' Set a reference to the selected feature.
    Dim oFeature As PartFeature
    Set oFeature = oDoc.SelectSet.Item(1)

    Dim oFeatureDim As FeatureDimension
    Dim i As Long
    i = 0
    ' Iterate over all dimensions of the feature.
    For Each oFeatureDim In oFeature.FeatureDimensions
        i = i + 1
        ' Format and print the name and position.
        Debug.Print i & ". Name: " & oFeatureDim.Parameter.Name _
                 & "  Position: (" & oFeatureDim.TextPoint.X & _
                              ", " & oFeatureDim.TextPoint.Y & _
                              ", " & oFeatureDim.TextPoint.Z & ")"
    Next

    ' Show all the feature dimensions
    oFeature.FeatureDimensions.Show
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |