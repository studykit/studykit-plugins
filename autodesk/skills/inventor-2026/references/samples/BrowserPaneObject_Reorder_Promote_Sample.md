# Promote occurence

## Description

This sample demonstrates how to promote an occurrence.

## Code Samples

* [VBA](#VBA)

```
Public Sub Promote()
    ' Get the active assembly document
    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oDef As AssemblyComponentDefinition
    Set oDef = oDoc.ComponentDefinition

    ' Get the top level occurrence of an assembly
    Dim oSubAssyOcc As ComponentOccurrence
    Set oSubAssyOcc = oDef.Occurrences.Item(1)

    ' Get the 2nd level occurrence under the assembly occurrence
    Dim oSubOcc As ComponentOccurrenceProxy
    Set oSubOcc = oDef.Occurrences.Item(1).SubOccurrences.Item(1)

    Dim oPane As BrowserPane
    Set oPane = oDoc.BrowserPanes.Item("Model")

    ' Get the browser nodes corresponding to the two occurrences
    Dim oTargetNode As BrowserNode
    Set oTargetNode = oPane.GetBrowserNodeFromObject(oSubAssyOcc)

    Dim oSourceNode As BrowserNode
    Set oSourceNode = oPane.GetBrowserNodeFromObject(oSubOcc)

    ' Reorder the nodes to promote the sub-occurrence to the top level
    Call oPane.Reorder(oTargetNode, True, oSourceNode)
End Sub
```
