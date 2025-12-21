# Single selection - simple

## Description

The following sample demonstrates getting a single selection from the user.

## Code Samples

* [VBA](#VBA)

```
Public Sub GetSingleSelection()
    ' Get a feature selection from the user
    Dim oObject As Object
    Set oObject = ThisApplication.CommandManager.Pick(kPartFeatureFilter, "Pick a feature")

    MsgBox "Picked: " & oObject.Name
End Sub
```
