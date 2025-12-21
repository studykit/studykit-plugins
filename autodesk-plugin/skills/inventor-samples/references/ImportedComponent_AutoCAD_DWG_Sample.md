# Associatively import AutoCAD

## Description

This sample demonstrates how to import AutoCAD associatively.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Sub AssociativelyImportAutoCADDWGSample()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oPartCompDef As PartComponentDefinition
    Set oPartCompDef = oDoc.ComponentDefinition

    ' Create the ImportedDWGComponentDefinition bases on an AutoCAD file
    Dim oImportedDWGCompDef As ImportedDWGComponentDefinition
    Set oImportedDWGCompDef = oPartCompDef.ReferenceComponents.ImportedComponents.CreateDefinition("C:\Temp\MyDesign.dwg")

    ' Import the AutoCAD DWG
    Dim oImportedComp As ImportedComponent
    Set oImportedComp = oPartCompDef.ReferenceComponents.ImportedComponents.Add(oImportedDWGCompDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |