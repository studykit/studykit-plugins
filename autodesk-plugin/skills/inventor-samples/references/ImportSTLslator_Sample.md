# Open an STL file using the STL Translator Sample

## Description

This sample demonstrates how open an STL file using the STL translator add-in.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Sub ImportFunc()
    ' Set STL translator's CLSID and STL file name.
    Dim strCLSID As String
    Dim strFileName As String
    strCLSld = "{81CA7D27-2DBE-4058-8188-9136F85FC859}"
    strFileName = "C:\Part1.stl"

    Dim oAddIns As ApplicationAddIns
    Set oAddIns = ThisApplication.ApplicationAddIns

    ' Find the Rhino translator, get the CLSID and activate it.
    Dim oTransAddIn As TranslatorAddIn
    Set oTransAddIn = oAddIns.ItemById(strCLSld)
    oTransAddIn.Activate

    ' Get the transient object and take it as a factory to produce other objects
    Dim transientObj As TransientObjects
    Set transientObj = ThisApplication.TransientObjects

    ' Prepare the first parameter for Open(), the file name
    Dim file As DataMedium
    Set file = transientObj.CreateDataMedium
    file.FileName = strFileName

    ' Prepare the second parameter for Open(), the open type.
    Dim context As TranslationContext
    Set context = transientObj.CreateTranslationContext
    context.Type = kDataDropIOMechanism

    ' Prepare the 3rd parameter for Open(), the options.
    Dim options As NameValueMap
    Set options = transientObj.CreateNameValueMap
    options.Value("SaveComponentDuringLoad") = False
    options.Value("SaveLocationIndex") = 0
    options.Value("ComponentDestFolder") = ""
    options.Value("ImportUnit") = 1
    options.Value("ImportColor") = True
    options.Value("ImportColorIndex") = 0

    ' Prepare the fourth parameter for Open(), the final document.
    Dim sourceObj As Object

    ' Open the STL file.
    oTransAddIn.Open file, context, options, sourceObj
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |