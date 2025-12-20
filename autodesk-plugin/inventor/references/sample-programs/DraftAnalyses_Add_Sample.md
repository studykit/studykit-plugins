# Create a Draft Analysis

## Description

This sample demonstrates the creation of a draft analysis in a part.

## Code Samples

* [VBA](#VBA)

Open a part document and run the following sample.

|  |
| --- |
| Copy Code |

```
Public Sub CreateDraftAnalysis()
    ' Set a reference to the active part document
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Set a reference to the component definition
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    ' Set a reference to the analysis manager
    Dim oAnalysisMgr As AnalysisManager
    Set oAnalysisMgr = oCompDef.AnalysisManager

    ' Get the y-axis, to be used as the pull direction for the draft analysis
    Dim oYAxis As WorkAxis
    Set oYAxis = oCompDef.WorkAxes.Item(2)

    ' Create the draft analysis with the following input values
    '   Start Angle = -3 degrees
    '   End Angle =   3 degrees
    '   Pull direction = Negative Y Axis
    '   Display Quality = 50%

    Dim oDraftAnalysis As DraftAnalysis
    Set oDraftAnalysis = oAnalysisMgr.DraftAnalyses.Add(-0.05236, 0.05236, oYAxis, True, , , 5)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |