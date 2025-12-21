# Edit width extent of an existing flange feature

## Description

This sample demonstrates editing the width extent of an existing flange feature. This expects an existing sheet metal document that contains a flange feature that contains for physical flanges. It changes the type of width extent for each of the physical flanges. The result from the FlangeWidthsCreation sample can be used as the document to run this macro in.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub EditFlangeWidths()
    ' Create the active sheet metal document.
    Dim sheetMetalDoc As PartDocument
    Set sheetMetalDoc = ThisApplication.ActiveDocument

    ' Get the sheet metal component definition.
    Dim smCompDef As SheetMetalComponentDefinition
    Set smCompDef = sheetMetalDoc.ComponentDefinition

    Dim smFeatures As SheetMetalFeatures
    Set smFeatures = smCompDef.Features

    ' Get the flange feature.
    Dim flange As FlangeFeature
    Set flange = smFeatures.FlangeFeatures.Item(1)

    ' Position the end of part marker to just before this feature so the
    ' edges are in their original state.
    Call flange.SetEndOfPart(True)

    Dim flangeDef As FlangeDefinition
    Set flangeDef = flange.Definition

    ' Iterate over the four edges and edit the width extent for each one.
    Dim i As Integer
    For i = 1 To 4
        Dim currentEdge As Edge
        Set currentEdge = flangeDef.Edges.Item(i)
        Select Case i
            Case 1
                ' Edit the width extent to be offset as measured from the vertices of the edge.
                Call flangeDef.SetOffsetWidthExtent(currentEdge, currentEdge.StartVertex, 2, currentEdge.StopVertex, 5)
            Case 2
                Call flangeDef.SetEdgeWidthExtent(currentEdge)
            Case 3
                ' Edit the width extent to be an offset width extent.
                Call flangeDef.SetWidthOffsetWidthExtent(currentEdge, 6, 2, currentEdge.StartVertex, True)
            Case 4
                ' Edit the width extent to be centered.
                Call flangeDef.SetCenteredWidthExtent(currentEdge, 10)
        End Select
    Next

    ' Set the stop node back to the bottom of the browser.
    Call smCompDef.SetEndOfPartToTopOrBottom(False)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |