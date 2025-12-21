# Publish FlatPattern to STEP

## Description

This sample demonstrates how to save a FlatPattern file using the STEP translator add-in.

## Code Samples

* [VBA](#VBA)

This sample demonstrates how to save a FlatPattern file using the STEP translator add-in.

|  |
| --- |
| Copy Code |

```
Sub ExportFlatPatternToSTEP()
    'Set a reference to the active document (the document to be published).
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oCompDef As SheetMetalComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    If oCompDef.HasFlatPattern = False Then
        oCompDef.Unfold
    End If

    Dim oFlatPattern As FlatPattern
    Set oFlatPattern = oCompDef.FlatPattern

    Dim oSTEPTranslator As TranslatorAddIn
    Set oSTEPTranslator = ThisApplication.ApplicationAddIns.ItemById("{90AF7F40-0C01-11D5-8E83-0010B541CD80}")

    Dim oContext As TranslationContext
    Set oContext = ThisApplication.TransientObjects.CreateTranslationContext

    Dim oOptions As NameValueMap
    Set oOptions = ThisApplication.TransientObjects.CreateNameValueMap

    If oSTEPTranslator.HasSaveCopyAsOptions(oFlatPattern, oContext, oOptions) Then
        ' Set application protocol.
        ' 2 = AP 203 - Configuration Controlled Design
        ' 3 = AP 214 - Automotive Design
        oOptions.Value("ApplicationProtocolType") = 3
        ' Other options...
        'oOptions.Value("Author") = ""
        'oOptions.Value("Authorization") = ""
        'oOptions.Value("Description") = ""
        'oOptions.Value("Organization") = ""

        oContext.Type = IOMechanismEnum.kFileBrowseIOMechanism

        Dim oData As DataMedium
        Set oData = ThisApplication.TransientObjects.CreateDataMedium
        oData.FileName = oDoc.FullFileName & ".stp"
    Call oSTEPTranslator.SaveCopyAs(oFlatPattern, oContext, oOptions, oData)
    End If
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |