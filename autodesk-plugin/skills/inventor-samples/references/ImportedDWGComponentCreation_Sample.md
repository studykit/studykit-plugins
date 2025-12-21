# ImportedDWGComponent Creation

## Description

This sample demonstrates how to create an imported DWG component into Inventor part document, and project the DWG entities onto Inventor planar sketch.

## Code Samples

* [VBA](#VBA)

```
Sub CreateImportedDWGComponentSample()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    Dim oRefComponents As ReferenceComponents
    Set oRefComponents = oCompDef.ReferenceComponents

    ' Create a ImportedComponentDefinition based on an AutoCAD file.
    Dim oImportedCompDef As ImportedComponentDefinition
    Set oImportedCompDef = oRefComponents.ImportedComponents.CreateDefinition("C:\Temp\ACADDWG.dwg")

    Dim oImportedDWGDef As ImportedDWGComponentDefinition

    If oImportedCompDef.Type = kImportedDWGComponentDefinitionObject Then
        Set oImportedDWGDef = oImportedCompDef
    Else
        End
    End If

    Dim oMatrix As Matrix
    Set oMatrix = ThisApplication.TransientGeometry.CreateMatrix
    oMatrix.SetTranslation ThisApplication.TransientGeometry.CreateVector(0, 0, 10)

    oImportedDWGDef.Transformation = oMatrix

    ' Create the ImportedComponent
    Dim oImportedComponent As ImportedComponent
    Set oImportedComponent = oRefComponents.ImportedComponents.Add(oImportedDWGDef)

    Dim oImportedDWGComponent As ImportedDWGComponent

    If oImportedComponent.Type = kImportedDWGComponentObject Then
        Set oImportedDWGComponent = oImportedComponent

        Dim oSk As PlanarSketch
        Set oSk = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

        ' Get the DWGBlockDefinition for model space.
        Dim oDWGModelSpaceDef As DWGBlockDefinition
        Set oDWGModelSpaceDef = oImportedDWGComponent.ModelSpaceDefinition

        ' Project DWG entities to planar sketch.
        Dim oDWGEntity As DWGEntity
        For Each oDWGEntity In oDWGModelSpaceDef.Entities

            Call oSk.AddByProjectingEntity(oDWGEntity)
        Next
    End If
End Sub
```
