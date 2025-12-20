# Export to DWF

## Description

This sample demonstrates publishing of Inventor files in DWF format.

## Code Samples

* [VBA](#VBA)

To run this sample, the document to be published must be active. The DWF file is created as C:\temptest.DWF (this can be changed in the code below).

|  |
| --- |
| Copy Code |

```
Public Sub PublishDWF()
    ' Get the DWF translator Add-In.
    Dim DWFAddIn As TranslatorAddIn
    Set DWFAddIn = ThisApplication.ApplicationAddIns.ItemById("{0AC6FD95-2F4D-42CE-8BE0-8AEA580399E4}")

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
    If DWFAddIn.HasSaveCopyAsOptions(oDocument, oContext, oOptions) Then

        oOptions.Value("Launch_Viewer") = 1

        ' Other options...
        'oOptions.Value("Publish_All_Component_Props") = 1
        'oOptions.Value("Publish_All_Physical_Props") = 1
        'oOptions.Value("Password") = 0

        If Typeof oDocument Is DrawingDocument Then

            ' Drawing options
            oOptions.Value("Publish_Mode") = kCustomDWFPublish
            oOptions.Value("Publish_All_Sheets") = 0

            ' The specified sheets will be ignored if
            ' the option "Publish_All_Sheets" is True (1)
            Dim oSheets As NameValueMap
            Set oSheets = ThisApplication.TransientObjects.CreateNameValueMap

            ' Publish the first sheet AND its 3D model
            Dim oSheet1Options As NameValueMap
            Set oSheet1Options = ThisApplication.TransientObjects.CreateNameValueMap

            oSheet1Options.Add "Name", "Sheet:1"
            oSheet1Options.Add "3DModel", True
            oSheets.Value("Sheet1") = oSheet1Options

            ' Publish the third sheet but NOT its 3D model
            Dim oSheet3Options As NameValueMap
            Set oSheet3Options = ThisApplication.TransientObjects.CreateNameValueMap

            oSheet3Options.Add "Name", "Sheet3:3"
            oSheet3Options.Add "3DModel", False

            oSheets.Value("Sheet2") = oSheet3Options

            'Set the sheet options object in the oOptions NameValueMap
            oOptions.Value("Sheets") = oSheets
        End If

    End If

    'Set the destination file name
    oDataMedium.FileName = "c:\temptest.dwf"

    'Publish document.
    Call DWFAddIn.SaveCopyAs(oDocument, oContext, oOptions, oDataMedium)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |