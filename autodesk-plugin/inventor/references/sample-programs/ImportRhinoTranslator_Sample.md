# Open Rhino Translator Sample

## Description

This sample demonstrates how to opening a Rhino file using the Rhino translator add-in.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Sub ImportRhino()
   ' Set Rhino translator’s CLSID and the Rhino file name.
   Dim strCLSID As String
   Dim strFileName As String
   strCLSld = "{2CB23BF0-E2AC-4b32-B0A1-1CC292AF6623}"

   ' Please set the full file name here, such as "C:\ETTI.3dm"
   strFileName = "ETTI.3dm"

   Dim oAddIns As ApplicationAddIns
   Set oAddIns = ThisApplication.ApplicationAddIns

   ' Find the Rhino translator, get the CLSID and activate it.
   Dim oPeTransAddIn As TranslatorAddIn
   Set oPeTransAddIn = oAddIns.ItemById(strCLSld)
   oPeTransAddIn.Activate

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
   options.Value("ImportSolid") = True
   options.Value("ImportSurface") = True
   options.Value("ImportWire") = True
   options.Value("ImportPoint") = False
   options.Value("CreateSurfIndex") = 1
   options.Value("GroupNameIndex") = 0
   options.Value("GroupName") = ""
   options.Value("CEGroupLevel") = 0
   options.Value("CEPrefixCk") = False
   options.Value("CEPrefixString") = ""
   options.Value("ImportUnit") = 0
   options.Value("CheckDuringLoad") = False
   options.Value("AutoStitchAndPromote") = True
   options.Value("AdvanceHealing") = False

   ' Prepare the fourth parameter for Open(), the final document.
   Dim sourceObj As Object

   ' Open the Rhino file.
   oPeTransAddIn.Open file, context, options, sourceObj
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |