# Removes all appearance overrides in a part.

## Description

This sample removes all appearance overrides that have been placed on a part.

## Code Samples

* [VBA](#VBA)

```
Public Sub RemovePartOverrides()
    ' Get the active part document.
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.ActiveDocument

    ' Iterate through the objects that have an override.
    Dim obj As Object
    For Each obj In partDoc.ComponentDefinition.AppearanceOverridesObjects
        ' Set the source of the appearance based on the type of object.
        ' It's possible to use kPartAppearance in all cases, but this sets
        ' it to the default source used by Inventor when no overrides exist.
        If TypeOf obj Is SurfaceBody Then
            obj.AppearanceSourceType = kPartAppearance
        ElseIf TypeOf obj Is PartFeature Then
            obj.AppearanceSourceType = kBodyAppearance
        ElseIf TypeOf obj Is Face Then
            obj.AppearanceSourceType = kFeatureAppearance
        Else
            MsgBox "Unexpected type with appearance override: " & TypeName(obj)
        End If
    Next
End Sub
```
