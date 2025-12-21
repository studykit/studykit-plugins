# RemoveAssemblyOverrides

## Description

Removes all appearance overrides that have been assigned in the active assembly.

## Code Samples

* [VBA](#VBA)

```
Public Sub RemoveAssemblyOverrides()
    ' Get the active assembly document.
    Dim asmDoc As AssemblyDocument
    Set asmDoc = ThisApplication.ActiveDocument

    ' Iterate through the objects that have an override.
    Dim obj As ComponentOccurrence
    For Each obj In asmDoc.ComponentDefinition.AppearanceOverridesObjects
        ' Set it so the occurrence uses the original color of the part.
        obj.AppearanceSourceType = kPartAppearance
    Next
End Sub
```
