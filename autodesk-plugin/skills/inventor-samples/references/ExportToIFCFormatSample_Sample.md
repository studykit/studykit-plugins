# Export to IFC Format Sample

## Description

This sample demonstrates how to export an assembly to IFC format.

## Code Samples

* [VBA](#VBA)

This sample demonstrates how to export an assembly to IFC format. You should open an assembly before running below code sample.

|  |
| --- |
| Copy Code |

```
Sub ExportToIFCFormatSample()
    ' Make sure the BIM Content addin is loaded.
    Dim oBIMContent As ApplicationAddIn
    Set oBIMContent = ThisApplication.ApplicationAddIns.ItemById("{842004D5-C360-43A8-A00D-D7EB72DAAB69}")
    If Not oBIMContent.Activated Then
        oBIMContent.Activate
    End If

    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oCompDef As AssemblyComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    Dim oBIMComp As BIMComponent
    Set oBIMComp = oCompDef.BIMComponent

    Dim oOptions As NameValueMap
    Set oOptions = ThisApplication.TransientObjects.CreateNameValueMap
    ' specify the IFC file version to export: IFC2x3 or IFC4x3.
    oOptions.Value("IFCFileVersion") = "IFC4x3"

    ' export to IFC format with specified file version. Make sure the RCE(Revit Core Engine) is installed.
    oBIMComp.ExportBuildingComponentWithOptions "C:\Temp\MyIFC.ifc", oOptions
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |