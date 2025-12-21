# Drawing Sketch Hatch Region Sample

## Description

This sample demonstrates how to create a sketch hatch region in drawing.

## Code Samples

* [VBA](#VBA)

```
Sub DrawingSketchHatchRegionSample()
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.Documents.Add(kDrawingDocumentObject)

    Dim oSketch As DrawingSketch
    Set oSketch = oDoc.ActiveSheet.Sketches.Add
    oSketch.Edit

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    Dim results As SketchEntitiesEnumerator
    Set results = oSketch.SketchLines.AddAsTwoPointRectangle(oTG.CreatePoint2d(10, 10), oTG.CreatePoint2d(15, 12))

    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    Dim oHatchPattern As DrawingHatchPattern
    Set oHatchPattern = oDoc.DrawingHatchPatternsManager.Item("ANSI 31")

    Dim oHatchRegion As SketchHatchRegion
    Set oHatchRegion = oSketch.SketchHatchRegions.Add(oProfile, oHatchPattern)

    oSketch.ExitEdit
End Sub
```
