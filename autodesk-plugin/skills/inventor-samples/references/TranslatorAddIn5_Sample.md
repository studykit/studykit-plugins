# Export to STEP

## Description

This sample demonstrates exporting of Inventor files in STEP format.

## Code Samples

* [VBA](#VBA)

To run this sample, the document to be exported must be active. The STEP file is created as C:\temptest.stp (this can be changed in the code below).

```
Public Sub ExportToSTEP()
    ' Get the STEP translator Add-In.
    Dim oSTEPTranslator As TranslatorAddIn
    Set oSTEPTranslator = ThisApplication.ApplicationAddIns.ItemById("{90AF7F40-0C01-11D5-8E83-0010B541CD80}")

    If oSTEPTranslator Is Nothing Then
        MsgBox "Could not access STEP translator."
        Exit Sub
    End If

    Dim oContext As TranslationContext
    Set oContext = ThisApplication.TransientObjects.CreateTranslationContext
    Dim oOptions As NameValueMap
    Set oOptions = ThisApplication.TransientObjects.CreateNameValueMap
    If oSTEPTranslator.HasSaveCopyAsOptions(ThisApplication.ActiveDocument, oContext, oOptions) Then
        ' Set application protocol.
        ' 2 = AP 203 - Configuration Controlled Design
        ' 3 = AP 214 - Automotive Design
        oOptions.Value("ApplicationProtocolType") = 3

        ' Other options...
        'oOptions.Value("Author") = ""
        'oOptions.Value("Authorization") = ""
        'oOptions.Value("Description") = ""
        'oOptions.Value("Organization") = ""

        oContext.Type = kFileBrowseIOMechanism

        Dim oData As DataMedium
        Set oData = ThisApplication.TransientObjects.CreateDataMedium
        oData.FileName = "C:\temp\test.stp"

        Call oSTEPTranslator.SaveCopyAs(ThisApplication.ActiveDocument, oContext, oOptions, oData)
    End If
End Sub
```
