# Post Private Event Sample

## Description

This sample demonstrates how to use the PostPrivateEvent to configure the options for placing a part component.

## Code Samples

* [VBA](#VBA)

This sample demonstrates how to use the PostPrivateEvent to configure the options for placing a part component.

|  |
| --- |
| Copy Code |

```
Sub AssemblyPlaceComponentCmdWithPPE()
    ' In UI create a part and create an iMate definition to its face, save it and set its full filename below.

    Dim strFullFileName As String
    strFullFileName = "C:\Temp\iMate.ipt"

    Dim oAssyDoc As AssemblyDocument
    Set oAssyDoc = ThisApplication.Documents.Add(kAssemblyDocumentObject)

    Dim oOccu As ComponentOccurrence
    Set oOccu = oAssyDoc.ComponentDefinition.Occurrences.Add(strFullFileName, ThisApplication.TransientGeometry.CreateMatrix)

    Dim oCM As CommandManager
    Set oCM = ThisApplication.CommandManager

    ' clear existing clipboard
    oCM.ClearPrivateEvents

    Call oCM.PostPrivateEvent(kFileNameEvent, strFullFileName)

    Dim oNV As NameValueMap
    Set oNV = ThisApplication.TransientObjects.CreateNameValueMap

    Call oNV.Add("Use iMate", True)
    Call oCM.PostPrivateEvent(kBooleanEvent, oNV)

    oNV.Clear
    Call oNV.Add("Generate iMate Results", True)
    Call oCM.PostPrivateEvent(kBooleanEvent, oNV)

    Call oCM.PostPrivateEvent(kStringEvent, "Design View Representation|Front")

    oNV.Clear
    Call oNV.Add("Associative Design View", True)
    Call oCM.PostPrivateEvent(kBooleanEvent, oNV)

    Call oCM.PostPrivateEvent(kStringEvent, "Model State|[Primary]")

    ' Call below command will cause to placing the component using above settings.
    Dim oCat As ControlDefinition
    Set oCat = oCM.ControlDefinitions.Item("AssemblyPlaceComponentCmd")
    Call oCat.Execute2(True)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |