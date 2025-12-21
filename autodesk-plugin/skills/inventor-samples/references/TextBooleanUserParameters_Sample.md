# Text and Boolean user parameter creation

## Description

This sample demonstrates how to create Text and Boolean user parameter.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateTextBooleanUserParameter()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oUserParameters As UserParameters
    Set oUserParameters = oDoc.ComponentDefinition.Parameters.UserParameters

    Dim oTextParam As UserParameter
    Set oTextParam = oUserParameters.AddByValue("Printer_Name", "Inventor_3D_Printer1", kTextUnits)

    Dim oBooleanParam As UserParameter
    Set oBooleanParam = oUserParameters.AddByValue("Auto_Print", True, kBooleanUnits)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |