# Save as IGES Translator Sample

## Description

This sample demonstrates how to save a IGES file using the IGES translator add-in.

## Code Samples

* [VBA](#VBA)

```
Public Sub ExportToIGES()
    ' Get the IGES translator Add-In.
    Dim oIGESTranslator As TranslatorAddIn
    Set oIGESTranslator = ThisApplication.ApplicationAddIns.ItemById("{90AF7F44-0C01-11D5-8E83-0010B541CD80}")

    If oIGESTranslator Is Nothing Then
        MsgBox "Could not access IGES translator."
        Exit Sub
    End If

    Dim oContext As TranslationContext
    Set oContext = ThisApplication.TransientObjects.CreateTranslationContext
    Dim oOptions As NameValueMap
    Set oOptions = ThisApplication.TransientObjects.CreateNameValueMap
    If oIGESTranslator.HasSaveCopyAsOptions(ThisApplication.ActiveDocument, oContext, oOptions) Then
        ' Set geometry type for wireframe.
        ' 0 = Surfaces, 1 = Solids, 2 = Wireframe
        oOptions.Value("GeometryType") = 1

        ' To set other translator values:
        ' oOptions.Value("SolidFaceType") = n
        ' 0 = NURBS, 1 = Analytic

        ' oOptions.Value("SurfaceType") = n
        ' 0 = 143(Bounded), 1 = 144(Trimmed)

        oContext.Type = kFileBrowseIOMechanism

        Dim oData As DataMedium
        Set oData = ThisApplication.TransientObjects.CreateDataMedium
        oData.FileName = "C:\Temptest.igs"

        Call oIGESTranslator.SaveCopyAs(ThisApplication.ActiveDocument, oContext, oOptions, oData)
    End If
End Sub
```
