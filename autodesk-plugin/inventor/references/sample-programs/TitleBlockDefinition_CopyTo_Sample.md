# Copying a title block definition

## Description

This sample demonstrates copying a title block definition from one drawing to another and replacing the existing title blocks in the drawing with the new title block.

## Code Samples

* [VBA](#VBA)

Before running this sample, have the drawing document open with a sheet active that contains the title block you want to copy. Also, change the path of the new document (oNewDocument) to point to a drawing document in which you want the titleblocks changed.

|  |
| --- |
| Copy Code |

```
Public Sub TitleBlockCopy()
    Dim oSourceDocument As DrawingDocument
    Set oSourceDocument = ThisApplication.ActiveDocument

    ' Open the new drawing to copy the title block into.
    Dim oNewDocument As DrawingDocument
    Set oNewDocument = ThisApplication.Documents.Open("C:\temp\TitleBlockChange.idw")

    ' Get the new source title block definition.
    Dim oSourceTitleBlockDef As TitleBlockDefinition
    Set oSourceTitleBlockDef = oSourceDocument.ActiveSheet.TitleBlock.Definition

    ' Get the new title block definition.
    Dim oNewTitleBlockDef As TitleBlockDefinition
    Set oNewTitleBlockDef = oSourceTitleBlockDef.CopyTo(oNewDocument)

    ' Iterate through the sheets.
    Dim oSheet As Sheet
    For Each oSheet In oNewDocument.Sheets
        oSheet.Activate

        oSheet.TitleBlock.Delete
        Call oSheet.AddTitleBlock(oNewTitleBlockDef)
    Next
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |