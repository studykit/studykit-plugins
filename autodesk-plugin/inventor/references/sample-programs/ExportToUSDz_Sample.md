# Export to USDz

## Description

This sample demonstrates how to export a part or assembly document to USDz format.

## Code Samples

* [VBA](#VBA)

This sample demonstrates how to export a part or assembly document to USDz format.

|  |
| --- |
| Copy Code |

```
Sub SaveToUSDz()
  Dim oAddin As TranslatorAddIn
  Set oAddin = ThisApplication.ApplicationAddIns.ItemById("{2F08D88C-E86A-490E-9059-DD97A44020AC}")

  Dim oContext As TranslationContext
  Set oContext = ThisApplication.TransientObjects.CreateTranslationContext()
  oContext.Type = kFileBrowseIOMechanism

  Dim oOptions As NameValueMap
  Set oOptions = ThisApplication.TransientObjects.CreateNameValueMap()

  Dim oData As DataMedium
  Set oData = ThisApplication.TransientObjects.CreateDataMedium()

  Dim outputFolderPath As String
  outputFolderPath = "C:\Temp\"
  oData.FileName = outputFolderPath + "USDz_output.usdz"

  Dim oDoc As Document
  Set oDoc = ThisApplication.ActiveDocument
  If oDoc.DocumentType = kAssemblyDocumentObject Or oDoc.DocumentType = kPartDocumentObject Then
    Call oAddin.SaveCopyAs(oDoc, oContext, oOptions, oData)
  End If
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |