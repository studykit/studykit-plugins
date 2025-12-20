# Create Revit Export sample

## Description

This sample demonstrates how to create a RevitExport object.

## Code Samples

* [VBA](#VBA)

This sample demonstrates how to create a RevitExport object. Open an assembly firstly before running this sample.

|  |
| --- |
| Copy Code |

```
Sub CreateRevitExportSample()
    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Actiate the Master model state if the active model state is substitute.
    If oDoc.ComponentDefinition.ModelStates.ActiveModelState.ModelStateType = ModelStateTypeEnum.kSubstituteModelStateType Then
        oDoc.ComponentDefinition.ModelStates.Item(1).Activate
        Set oDoc = ThisApplication.ActiveDocument
    End If

    Dim oRevitExportDef As RevitExportDefinition
    Set oRevitExportDef = oDoc.ComponentDefinition.RevitExports.CreateDefinition

    oRevitExportDef.Location = "C:\Temp"
    oRevitExportDef.FileName = "MyRevitExport.rvt"
    oRevitExportDef.Structure = kEachTopLevelComponentStructure
    oRevitExportDef.EnableUpdating = True

    ' Create RevitExport.
    Dim oRevitExport As RevitExport
    Set oRevitExport = oDoc.ComponentDefinition.RevitExports.Add(oRevitExportDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |