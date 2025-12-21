# Create sheet with multiple views

## Description

This sample demonstrates the creation of a drawing sheet based on a particular sheet format containing the definition for multiple views.

## Code Samples

* [VBA](#VBA)

Have a drawing document open and run the following macro.

|  |
| --- |
| Copy Code |

```
Public Sub AddUsingSheetFormat()
    'Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    'Set a reference to the sheet format named "C size, 4 view"
    Dim oFormat As SheetFormat
    Set oFormat = oDrawDoc.SheetFormats.Item("C size, 4 view")

    'Open the model document invisible
    Dim oModel As Document
    Set oModel = ThisApplication.Documents.Open("C:\temp\block.ipt", False)

    'Create a new sheet based on the sheet format
    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.Sheets.AddUsingSheetFormat(oFormat, oModel)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |