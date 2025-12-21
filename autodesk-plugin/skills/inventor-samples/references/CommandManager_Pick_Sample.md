# Single selection - simple

## Description

The following sample demonstrates getting a single selection from the user.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub GetSingleSelection()
    ' Get a feature selection from the user
    Dim oObject As Object
    Set oObject = ThisApplication.CommandManager.Pick(kPartFeatureFilter, "Pick a feature")

    MsgBox "Picked: " & oObject.Name
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |