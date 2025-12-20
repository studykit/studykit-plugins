# Border Insert Default

## Description

This sample illustrates inserting a default border using the default values.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub InsertDefaultBorderUsingDefaults()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    ' Check to see if the sheet already has a border and delete it if it does.
    If Not oSheet.Border Is Nothing Then
        oSheet.Border.Delete
    End If

    ' Add the border to the sheet.
    Dim oBorder As DefaultBorder
    Set oBorder = oSheet.AddDefaultBorder()
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |