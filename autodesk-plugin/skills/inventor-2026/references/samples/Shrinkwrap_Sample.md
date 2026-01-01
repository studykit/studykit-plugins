# Shrink wrap substitute in assembly

## Description

The following sample demonstrates the creation of a shrinkwrap substitute within an assembly.

## Code Samples

* [VBA](#VBA)

Open any assembly document and run the sample. A shrinkwrap part is created at the same location as the assembly.

```
Sub CreateShrinkwrapSubstitute()
    ' Set a reference to the active assembly document
    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oDef As AssemblyComponentDefinition
    Set oDef = oDoc.ComponentDefinition

    ' Create a new part document that will be the shrinkwrap substitute
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, , False)

    Dim oPartDef As PartComponentDefinition
    Set oPartDef = oPartDoc.ComponentDefinition

    Dim oDerivedAssemblyDef As DerivedAssemblyDefinition
    Set oDerivedAssemblyDef = oPartDef.ReferenceComponents.DerivedAssemblyComponents.CreateDefinition(oDoc.FullDocumentName)

    ' Set various shrinkwrap related options
    oDerivedAssemblyDef.DeriveStyle = kDeriveAsSingleBodyNoSeams
    oDerivedAssemblyDef.IncludeAllTopLevelWorkFeatures = kDerivedIncludeAll
    oDerivedAssemblyDef.IncludeAllTopLevelSketches = kDerivedIncludeAll
    oDerivedAssemblyDef.IncludeAllTopLeveliMateDefinitions = kDerivedExcludeAll
    oDerivedAssemblyDef.IncludeAllTopLevelParameters = kDerivedExcludeAll
    oDerivedAssemblyDef.ReducedMemoryMode = True

    Call oDerivedAssemblyDef.SetHolePatchingOptions(kDerivedPatchAll)
    Call oDerivedAssemblyDef.SetRemoveByVisibilityOptions(kDerivedRemovePartsAndFaces, 25)

    ' Create the shrinkwrap component
    Dim oDerivedAssembly As DerivedAssemblyComponent
    Set oDerivedAssembly = oPartDef.ReferenceComponents.DerivedAssemblyComponents.Add(oDerivedAssemblyDef)

    ' Save the part
    Dim strSubstituteFileName As String
    strSubstituteFileName = Left$(oDoc.FullFileName, Len(oDoc.FullFileName) - 4)
    strSubstituteFileName = strSubstituteFileName & "_ShrinkwrapSubstitute.ipt"

    ThisApplication.SilentOperation = True
    Call oPartDoc.SaveAs(strSubstituteFileName, False)
    ThisApplication.SilentOperation = False

    ' Create a substitute level of detail using the shrinkwrap part.
    Dim oSubstituteMS As ModelState
    Set oSubstituteMS = oDef.ModelStates.AddSubstitute(strSubstituteFileName)

    ' Release reference of the invisibly opened part document.
    oPartDoc.ReleaseReference
End Sub
```
