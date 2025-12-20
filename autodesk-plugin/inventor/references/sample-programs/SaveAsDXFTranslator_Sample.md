# Save as DXF Translator Sample

## Description

This sample demonstrates how to save a DXF file using the DXF translator add-in.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub PublishDXF()
    ' Get the DXF translator Add-In.
    Dim DXFAddIn As TranslatorAddIn
    Set DXFAddIn = ThisApplication.ApplicationAddIns.ItemById("{C24E3AC4-122E-11D5-8E91-0010B541CD80}")

    'Set a reference to the active document (the document to be published).
    Dim oDocument As Document
    Set oDocument = ThisApplication.ActiveDocument

    Dim oContext As TranslationContext
    Set oContext = ThisApplication.TransientObjects.CreateTranslationContext
    oContext.Type = kFileBrowseIOMechanism

    ' Create a NameValueMap object
    Dim oOptions As NameValueMap
    Set oOptions = ThisApplication.TransientObjects.CreateNameValueMap

    ' Create a DataMedium object
    Dim oDataMedium As DataMedium
    Set oDataMedium = ThisApplication.TransientObjects.CreateDataMedium

    ' Check whether the translator has 'SaveCopyAs' options
    If DXFAddIn.HasSaveCopyAsOptions(oDocument, oContext, oOptions) Then
        Dim strIniFile As String
        strIniFile = "C:\temp\DXFOut.ini"

        ' Create the name-value that specifies the ini file to use.
        oOptions.Value("Export_Acad_IniFile") = strIniFile
    End If

    'Set the destination file name
    oDataMedium.FileName = "c:\temp\dxfout.dxf"

    'Publish document.
    Call DXFAddIn.SaveCopyAs(oDocument, oContext, oOptions, oDataMedium)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |