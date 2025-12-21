# Add assembly occurrences to a new folder

## Description

Demonstrates assembly occurrences to a new folder

## Code Samples

* [VBA](#VBA)

Have an assembly with at least one occurrence in it and run the sample.

|  |
| --- |
| Copy Code |

```
Public Sub AddOccurrencesToFolder()
    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oDef As AssemblyComponentDefinition
    Set oDef = oDoc.ComponentDefinition

    Dim oPane As BrowserPane
    Set oPane = oDoc.BrowserPanes.ActivePane

    Dim oOccurrenceNodes As ObjectCollection
    Set oOccurrenceNodes = ThisApplication.TransientObjects.CreateObjectCollection

    Dim oOcc As ComponentOccurrence
    For Each oOcc In oDef.Occurrences

        Dim oNode As BrowserNode
        Set oNode = oPane.GetBrowserNodeFromObject(oOcc)

        oOccurrenceNodes.Add oNode
    Next

    Dim oFolder As BrowserFolder
    Set oFolder = oPane.AddBrowserFolder("My Occurrence Folder", oOccurrenceNodes)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |