# Import Revit data into Inventor

## Description

The samples demonstrate how to import Revit data(.rvt) into Inventor part and assembly documents.

## Code Samples

* [VBA](#VBA)

The VBA samples demonstrate how to import Revit data(.rvt) into Inventor part and assembly documents. You should prepare a Revit data before running the samples.

|  |
| --- |
| Copy Code |

```
Sub ImportRVTToAssembly()
    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.Documents.Add(kAssemblyDocumentObject)

    Dim sFile As String
    sFile = "C:\RevitFile.rvt"

    Dim oImportedRVTDef As ImportedRVTComponentDefinition
    Set oImportedRVTDef = oDoc.ComponentDefinition.ImportedComponents.CreateDefinition(sFile)
    oImportedRVTDef.Imported3DView = "{3D}"
    oImportedRVTDef.ImportedAssemblyOrganizationType = kImportedAsAssembly

    Dim oComp As ImportedRVTComponent
    Set oComp = oDoc.ComponentDefinition.ImportedComponents.Add(oImportedRVTDef)
End Sub

Sub ImportRVTToPart()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim sFile As String
    sFile = "C:\RevitFile.rvt"

    Dim oImportedRVTDef As ImportedRVTComponentDefinition
    Set oImportedRVTDef = oDoc.ComponentDefinition.ReferenceComponents.ImportedComponents.CreateDefinition(sFile)

    oImportedRVTDef.Imported3DView = "{3D}"
    oImportedRVTDef.ImportedAssemblyOrganizationType = kImportedAsMultibodyPart

    Dim oComp As ImportedRVTComponent
    Set oComp = oDoc.ComponentDefinition.ReferenceComponents.ImportedComponents.Add(oImportedRVTDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |