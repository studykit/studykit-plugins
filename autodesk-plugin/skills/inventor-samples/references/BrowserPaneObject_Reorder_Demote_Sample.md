# Demote occurence

## Description

This sample demonstrates how to demote a top level occurrence in an assembly into a new sub-assembly occurrence.

## Code Samples

* [VBA](#VBA)

```
Public Sub Demote()
    ' Get the active assembly document
    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oDef As AssemblyComponentDefinition
    Set oDef = oDoc.ComponentDefinition

    ' Get the occurrence to be demoted
    Dim oOcc As ComponentOccurrence
    Set oOcc = oDef.Occurrences.Item(1)

    ' Create a new sub-assembly to demote the occurrence into
    Dim oNewSubAssy As AssemblyDocument
    Set oNewSubAssy = ThisApplication.Documents.Add(kAssemblyDocumentObject, , False)

    Dim oMat As Matrix
    Set oMat = ThisApplication.TransientGeometry.CreateMatrix

    ' Create an instance of the new sub-assembly
    Dim oSubAssyOcc As ComponentOccurrence
    Set oSubAssyOcc = oDef.Occurrences.AddByComponentDefinition(oNewSubAssy.ComponentDefinition, oMat)

    ' Get the model browser
    Dim oPane As BrowserPane
    Set oPane = oDoc.BrowserPanes.Item("Model")

    ' Get the browser node that corresponds to the new sub-assembly occurrence
    Dim oSubAssyNode As BrowserNode
    Set oSubAssyNode = oPane.GetBrowserNodeFromObject(oSubAssyOcc)

    ' Get the last visible child node under the sub-assembly occurrence
    Dim oTargetNode As BrowserNode
    Dim i As Long
    For i = oSubAssyNode.BrowserNodes.Count To 1 Step -1
        If oSubAssyNode.BrowserNodes.Item(i).Visible Then
            Set oTargetNode = oSubAssyNode.BrowserNodes.Item(i)
            Exit For
        End If
    Next

    ' Get the browser node that corresponds to the occurrence to be demoted
    Dim oSourceNode As BrowserNode
    Set oSourceNode = oPane.GetBrowserNodeFromObject(oOcc)

    ' Demote the occurrence
    Call oPane.Reorder(oTargetNode, False, oSourceNode)
End Sub
```
