# Open a Catia file using the Catia Translator Sample

## Description

This sample demonstrates how open an Catia file using the Catia translator add-in.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CatiaImport()
    'Set CATIA V4 translator's CLSID and the file name (*.exp and *.dlv3).
    Dim strCLSID As String
    Dim strFileName As String
    strCLSID = "{C6ACD948-E1C5-4b5b-ADEE-3ED968F8CB1A}"
    strFileName = "C:\Hello.exp"

    Dim oAddIns As ApplicationAddIns
    Set oAddIns = ThisApplication.ApplicationAddIns

    ' find the translator and get CLSID and activate it
    Dim oTransAddIn As TranslatorAddIn
    Set oTransAddIn = oAddIns.ItemById(strCLSID)
    oTransAddIn.Activate

    ' get the transient object, take it as a factory to produce other objects
    Dim transientObj As TransientObjects
    Set transientObj = ThisApplication.TransientObjects

    ' prepare the 1st parameter for Open(), the file name
    Dim file As DataMedium
    Set file = transientObj.CreateDataMedium
    file.FileName = strFileName

    ' create an empty part
    Dim activeDoc As Document
    Set activeDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    ' prepare the 2nd parameter for Open()
    Dim context As TranslationContext
    Set context = transientObj.CreateTranslationContext
    context.Type = kFileBrowseIOMechanism
    ' this makes sure the imported stuff be inserted in the part doc created at the top
    context.OpenIntoExisting = activeDoc

    ' prepare the 3rd parameter for Open(), the options
    Dim options As NameValueMap
    Set options = transientObj.CreateNameValueMap
    options.Value("SaveComponentDuringLoad") = False
    options.Value("SaveLocationIndex") = 0
    options.Value("ComponentDestFolder") = ""
    options.Value("SaveAssemSeperateFolder") = False
    options.Value("AssemDestFolder") = ""
    options.Value("ImportSolid") = True
    options.Value("ImportSurface") = True
    options.Value("ImportWire") = True
    options.Value("ImportPoint") = True
    options.Value("ImportMeshes") = True
    options.Value("ImportAASP") = True
    options.Value("ImportAASPIndex") = 0
    options.Value("CreateSurfIndex") = 0
    options.Value("GroupNameIndex") = 0
    options.Value("GroupName") = ""
    options.Value("ImportUnit") = 0
    options.Value("CheckDuringLoad") = False
    options.Value("AutoStitchAndPromote") = False
    options.Value("AdvanceHealing") = False
    options.Value("NoShowExpModelList") = True

    ' open exp file to get the model count
    ' prepare the 4th parameter for Open(), the final document

    Dim sourceObj As Object
    oTransAddIn.Open file, context, options, sourceObj

    Dim nModelCount As Integer
    nModelCount = options.Value("ExpModelCount")

    ' open specified model in exp file
    Dim i As Integer
    For i = 0 To nModelCount - 1
        options.Value("ExpModeIndex") = i
        oTransAddIn.Open file, context, options, sourceObj
    Next i
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |