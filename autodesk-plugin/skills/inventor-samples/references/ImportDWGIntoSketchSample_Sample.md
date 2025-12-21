# Import DWG into sketch

## Description

This sample demonstrates how to import DWG into sketch.

## Code Samples

* [VBA](#VBA)

```
Sub ImportDWGIntoSketch()
    ' Get the DWG translator.
    Dim oDWGTranslator As TranslatorAddIn
    Set oDWGTranslator = ThisApplication.ApplicationAddIns.ItemById("{C24E3AC2-122E-11D5-8E91-0010B541CD80}")

    Dim oDataMedium As DataMedium
    Set oDataMedium = ThisApplication.TransientObjects.CreateDataMedium

    ' Specify a DWG file to import it into sketch
    oDataMedium.FileName = "C:\Temp\abc.dwg"

    Dim oTranslationContext As TranslationContext
    Set oTranslationContext = ThisApplication.TransientObjects.CreateTranslationContext
    oTranslationContext.Type = kFileBrowseIOMechanism

    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    ' Get the sketch that the DWG will be imported into.
    Dim oSk As PlanarSketch
    Set oSk = oDoc.ComponentDefinition.Sketches.Add(oDoc.ComponentDefinition.WorkPlanes(3))

    ' Open the sketch for edit.
    oSk.Edit

    ' Specify the sketch to import the DWG into.
    oTranslationContext.OpenIntoExisting = oSk

    Dim oOptions As NameValueMap
    Set oOptions = ThisApplication.TransientObjects.CreateNameValueMap

    ' Specify the layers to import
    oOptions.Add "SelectedLayers", "0"
    oOptions.Add "InvertLayersSelection", True

    ' Specify the units
    oOptions.Add "FileUnits", "Centimeters"

    ' Set to constraint the end points.
    oOptions.Add "ConstrainEndPoints", True

    ' Do the translation.
    Call oDWGTranslator.Open(oDataMedium, oTranslationContext, oOptions, oDoc)
End Sub
```
