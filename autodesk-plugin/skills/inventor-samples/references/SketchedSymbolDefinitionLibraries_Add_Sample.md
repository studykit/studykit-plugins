# Sketched Symbol Definition Library Creation

## Description

This sample demonstrates how to create a sketched symbol definition and save it to the SketchedSymbolDefinitionLibrary, and then add the sketched symbol definition from the SketchedSymbolDefinitionLibrary to another drawing document.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Sub SketchSymbolDefinitionLibrarySample()
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.Documents.Add(kDrawingDocumentObject)

    Dim oSymbolLib As SketchedSymbolDefinitionLibrary
    Dim oSymbolLibs As SketchedSymbolDefinitionLibraries

    Set oSymbolLibs = oDoc.SketchedSymbolDefinitions.SketchedSymbolDefinitionLibraries

    On Error Resume Next
    Set oSymbolLib = oSymbolLibs.Item("MySymbolLib")

    If oSymbolLib Is Nothing Then
        Set oSymbolLib = oSymbolLibs.Add("MySymbolLib")
    End If

    On Error GoTo 0

    ' Create a new sketched symbol definition.
    Dim oSymbolDef As SketchedSymbolDefinition
    Set oSymbolDef = oDoc.SketchedSymbolDefinitions.Add("CircleSymbol")

    Dim oSketch As DrawingSketch
    Call oSymbolDef.Edit(oSketch)

    Dim oCenter As Point2d
    Set oCenter = ThisApplication.TransientGeometry.CreatePoint2d(12, 12)

    Call oSketch.SketchCircles.AddByCenterRadius(oCenter, 0.5)

    Call oSymbolDef.ExitEdit(True)

    ' Save the above sketched symbol definition to library.
    Call oSymbolDef.SaveToLibrary(oSymbolLib, , , True)

    ' Sync the sketched symbol definition from the library to another drawing document
    Dim oNewDoc As DrawingDocument
    Set oNewDoc = ThisApplication.Documents.Add(kDrawingDocumentObject)

    Dim oNewSymbolDef As SketchedSymbolDefinition
    Set oNewSymbolDef = oNewDoc.SketchedSymbolDefinitions.AddFromLibrary(oSymbolLib, "CircleSymbol")

    ' Create a sketched symbol bases on the synced sketched symbol definition from library.
    Call oNewDoc.Sheets(1).SketchedSymbols.Add(oNewSymbolDef, ThisApplication.TransientGeometry.CreatePoint2d(12, 12))
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |