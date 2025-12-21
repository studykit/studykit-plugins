# Export to DWG

## Description

This sample uses the DWG Translator Addin to publish to DWG.

## Code Samples

* [VBA](#VBA)

```
Public Sub PublishDWG()
    ' Get the DWG translator Add-In.
    Dim DWGAddIn As TranslatorAddIn
    Set DWGAddIn = ThisApplication.ApplicationAddIns.ItemById("{C24E3AC2-122E-11D5-8E91-0010B541CD80}")

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
    If DWGAddIn.HasSaveCopyAsOptions(oDocument, oContext, oOptions) Then

        Dim strIniFile As String
        strIniFile = "C:\tempDWGOut.ini"
        ' Create the name-value that specifies the ini file to use.
        oOptions.Value("Export_Acad_IniFile") = strIniFile
    End If

    'Set the destination file name
    oDataMedium.FileName = "c:\tempdwgout.dwg"

    'Publish document.
    Call DWGAddIn.SaveCopyAs(oDocument, oContext, oOptions, oDataMedium)
End Sub
```
