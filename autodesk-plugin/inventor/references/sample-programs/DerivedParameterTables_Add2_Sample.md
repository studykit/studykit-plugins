# Selectively link paramaters

## Description

This sample demonstrates the selective linking of parameters from another Inventor file.

## Code Samples

* [VBA](#VBA)

Before running this sample, make sure that the file C:\temp\block.ipt exists (or change the path in the sample). The sample assumes that the file contains parameters named d0, d1 and d2.

|  |
| --- |
| Copy Code |

```
Sub SelectivelyLinkParams()
    ' Open the source document invisible.
    Dim oSourceDoc As PartDocument
    Set oSourceDoc = ThisApplication.Documents.Open("C:\temp\block.ipt", False)

    ' Set a reference to the component definition.
    Dim oSourceCompDef As PartComponentDefinition
    Set oSourceCompDef = oSourceDoc.ComponentDefinition

    Dim oParamsToLink As ObjectCollection
    Set oParamsToLink = ThisApplication.TransientObjects.CreateObjectCollection

    ' Add parameters named "d0" and "d1".
    ' This assumes that the source document contains
    ' parameters with these names.
    oParamsToLink.Add oSourceCompDef.Parameters.Item("d0")
    oParamsToLink.Add oSourceCompDef.Parameters.Item("d1")

    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    ' Create a derived parameter table that links only to "d0"
    ' and "d1" in the source part.
    ' Note: If parameters "d0" and "d1" in the source part
    ' are not already exported, they will be automatically
    ' exported and hence will result in changing the source part.
    Dim oDerivedParamTable As DerivedParameterTable
    Set oDerivedParamTable = oPartDoc.ComponentDefinition.Parameters. _
        DerivedParameterTables.Add2("C:\temp\block.ipt", oParamsToLink)

    ' Add parameter named "d2"
    ' This assumes that the source document
    ' contains a parameters named "d2".
    oParamsToLink.Add oSourceCompDef.Parameters.Item("d2")

    ' Change derived parameter table so it also links to "d2".
    oDerivedParamTable.LinkedParameters = oParamsToLink
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |