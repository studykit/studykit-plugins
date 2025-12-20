# Show online help sample for file dialog

## Description

The sample demonstrate how to set the online help for a file dialog.

## Code Samples

* [VBA](#VBA)

The VBA sample demonstrates how to set the online help page for a file dialog.

|  |
| --- |
| Copy Code |

```
Public Sub ShowOnlineHelpForFileDialog()
    Dim helpWebsite As String
    helpWebsite = "www.google.com"

    Dim oFileDialog As FileDialog
    ThisApplication.CreateFileDialog oFileDialog

    ' when set the help context to an online website, the context should be specified as -1
    oFileDialog.SetHelpContext helpWebsite, -1

    oFileDialog.ShowOpen
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |