# Browser Search Box Sample

## Description

This sample demonstrates how to use the search box in a document's browser pane.

## Code Samples

* [VBA](#VBA)

Open a document in Inventor first before running below sample.

|  |
| --- |
| Copy Code |

```
Sub SearchBoxSample()
    Dim oDoc As Document
    Set oDoc = ThisApplication.ActiveDocument

    Dim oPane As BrowserPane
    ' Get the BrowserPane that support the search box.
    If oDoc.DocumentType = kPartDocumentObject Then
        Set oPane = oDoc.BrowserPanes("PmDefault")
    ElseIf oDoc.DocumentType = kAssemblyDocumentObject Then
        Set oPane = oDoc.BrowserPanes("AmBrowserArrangement")
    ElseIf oDoc.DocumentType = kDrawingDocumentObject Then
        Set oPane = oDoc.BrowserPanes("DlHierarchy")
    ElseIf oDoc.DocumentType = kPresentationDocumentObject Then
        Set oPane = oDoc.BrowserPanes("DxHierarchy")
    End If

    Dim oSearchBox As SearchBox
    Set oSearchBox = oPane.SearchBox

    ' Enable the search box and display it in the broser pane for search text.
    oSearchBox.Enabled = True
    oSearchBox.Visible = True
    Call oSearchBox.Search("Part")
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |