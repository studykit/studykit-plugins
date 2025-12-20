# Modify Multiple Model States Sample

## Description

This sample demonstrates how to set multiple but not all model states into edit mode.

## Code Samples

* [VBA](#VBA)
* [VBA](#VBA)

This sample demonstrates how to set multiple but not all model states into edit mode.

|  |
| --- |
| Copy Code |

```
Sub ModifyMultipleModelStatesSample()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    Dim oModelStates As ModelStates
    Set oModelStates = oCompDef.ModelStates

    ' New several model state objects
    Dim i As Long
    For i = 1 To 4
        oModelStates.Add
    Next

    Dim oCol As ObjectCollection
    Set oCol = ThisApplication.TransientObjects.CreateObjectCollection

    ' Say we would like to edit the model state from the second one to the fourth one.
    ' we should make sure the active model state is added to the edit mode
    Dim oMS As ModelState
    Set oMS = oModelStates.Item(2)
    oMS.Activate

    For i = 2 To 4
        oCol.Add oModelStates.Item(i)
    Next

    oModelStates.ModelStatesInEdit = oCol

    ' When multiple model states but not all in edit mode
    ' the MemberEditScope will be set to kEditMultipleMembers.
    Debug.Print oModelStates.MemberEditScope = kEditMultipleMembers
End Sub
```

This sample demonstrates how to set multiple but not all model states into edit mode.

|  |
| --- |
| Copy Code |

```
Sub ModifyMultipleModelStatesSample()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    Dim oModelStates As ModelStates
    Set oModelStates = oCompDef.ModelStates

    ' New several model state objects
    Dim i As Long
    For i = 1 To 4
        oModelStates.Add
    Next

    Dim oCol As ObjectCollection
    Set oCol = ThisApplication.TransientObjects.CreateObjectCollection

    ' Say we would like to edit the model state from the second one to the fourth one.
    ' we should make sure the active model state is added to the edit mode
    Dim oMS As ModelState
    Set oMS = oModelStates.Item(2)
    oMS.Activate

    For i = 2 To 4
        oCol.Add oModelStates.Item(i)
    Next

    oModelStates.ModelStatesInEdit = oCol

    ' When multiple model states but not all in edit mode
    ' the MemberEditScope will be set to kEditMultipleMembers.
    Debug.Print oModelStates.MemberEditScope = kEditMultipleMembers
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |