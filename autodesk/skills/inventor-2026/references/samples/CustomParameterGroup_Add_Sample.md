# Creating a new parameter group

## Description

This sample demonstrates the creation of model, reference and user parameters and copying these parameters to a newly created group.

## Code Samples

* [VBA](#VBA)

```
Public Sub CreateParametersAndGroup()
    ' Create a new Part document.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                 ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Set a reference to the compdef.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a model parameter
    Dim oModelParam As ModelParameter
    Set oModelParam = oCompDef.Parameters.ModelParameters.AddByValue(2, kCentimeterLengthUnits)

    ' Create a reference parameter
    Dim oReferenceParam As ReferenceParameter
    Set oReferenceParam = oCompDef.Parameters.ReferenceParameters.AddByValue(4, kCentimeterLengthUnits)

    ' Create a user parameter
    Dim oUserParam As UserParameter
    Set oUserParam = oCompDef.Parameters.UserParameters.AddByValue("length", 6, kCentimeterLengthUnits)

    ' Create a new custom parameter group
    Dim oCustomParamGroup As CustomParameterGroup
    Set oCustomParamGroup = oCompDef.Parameters.CustomParameterGroups.Add("Custom Group", "CustomGroup1")

    ' Add the created parameters to this group
    ' Note that adding the parameters to the custom group
    ' does not remove it from the original group.
    Call oCustomParamGroup.Add(oModelParam)
    Call oCustomParamGroup.Add(oReferenceParam)
    Call oCustomParamGroup.Add(oUserParam)
End Sub
```
