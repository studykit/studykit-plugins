# Find component referenced by balloon

## Description

This sample demonstrates how to find the component that a balloon references.

## Code Samples

* [VBA](#VBA)

Select a balloon in a drawing and run the following sample.

|  |
| --- |
| Copy Code |

```
Public Sub GetComponentReferencedByBalloon()
    ' Set a reference to the active drawing document
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Get the selected balloon
    Dim oBalloon As Balloon
    Set oBalloon = oDoc.SelectSet(1)

    Dim oBalloonValueSet As BalloonValueSet
    For Each oBalloonValueSet In oBalloon.BalloonValueSets
        Dim strDisplay As String
        strDisplay = "Balloon Item Number: "

        ' Add the balloon item number (the overridden value if there is one)
        If oBalloonValueSet.OverrideValue = "" Then
            strDisplay = strDisplay & oBalloonValueSet.Value
        Else
            strDisplay = strDisplay & oBalloonValueSet.OverrideValue
        End If

        Dim oDrawingBOMRow As DrawingBOMRow
        Set oDrawingBOMRow = oBalloonValueSet.ReferencedRow

        If oDrawingBOMRow.Custom Then
            ' The referenced item is a custom parts list row.
            strDisplay = strDisplay & vbNewLine & "Referenced Component(s):"
            strDisplay = strDisplay & vbNewLine & "     Custom PartsList Row"
        Else
            Dim oBOMRow As BOMRow
            Set oBOMRow = oDrawingBOMRow.BOMRow

            ' Add the Item Number from the model BOM.
            strDisplay = strDisplay & vbNewLine & "BOM Item Number: " & oBOMRow.ItemNumber

            strDisplay = strDisplay & vbNewLine & "Referenced Component(s):"

            Dim oCompDefs As ComponentDefinitionsEnumerator
            Set oCompDefs = oBOMRow.ComponentDefinitions

            If oDrawingBOMRow.Virtual Then
                ' The referenced item is a virtual component.
                strDisplay = strDisplay & vbNewLine & "     Virtual: " & oCompDefs.Item(1).DisplayName
            Else

                ' Add the document name of the referenced component.
                ' There could be multiple if the balloon references
                ' a merged BOM row in the model.
                Dim oCompDef As ComponentDefinition
                For Each oCompDef In oCompDefs
                    strDisplay = strDisplay & vbNewLine & "     " & oCompDef.Document.FullDocumentName
                Next

            End If
        End If
        MsgBox strDisplay
    Next
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |