# Sketch fill region

## Description

This sample demonstrates the sketch fill functionality in drawing sketches.

## Code Samples

* [VBA](#VBA)

Have a drawing document open and run the sample.

```
Public Sub DrawingSketchFill()
    ' Set a reference to the active document. This assumes it
    ' is a drawing document.
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Create a sketch on the active sheet
    Dim oSketch As DrawingSketch
    Set oSketch = oDoc.ActiveSheet.Sketches.Add

    ' Put the sketch in edit mode
    oSketch.Edit

    ' Set a reference to the transient geometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Draw a circle in the sketch.
    Dim oCircle1 As SketchCircle
    Set oCircle1 = oSketch.SketchCircles.AddByCenterRadius(oTG.CreatePoint2d(10, 30), 2)

    ' Create a collection and add the circle.
    Dim oCollection1 As ObjectCollection
    Set oCollection1 = ThisApplication.TransientObjects.CreateObjectCollection
    oCollection1.Add oCircle1

    ' Create a profile from the first circle
    Dim oProfile1 As Profile
    Set oProfile1 = oSketch.Profiles.AddForSolid(False, oCollection1)

    ' Create a fill region based on the layer color.
    Call oSketch.SketchFillRegions.Add(oProfile1)

    ' Draw another circle in the sketch.
    Dim oCircle2 As SketchCircle
    Set oCircle2 = oSketch.SketchCircles.AddByCenterRadius(oTG.CreatePoint2d(30, 30), 2)

    ' Create a collection and add the circle.
    Dim oCollection2 As ObjectCollection
    Set oCollection2 = ThisApplication.TransientObjects.CreateObjectCollection
    oCollection2.Add oCircle2

    ' Create a profile from the second circle
    Dim oProfile2 As Profile
    Set oProfile2 = oSketch.Profiles.AddForSolid(False, oCollection2)

    ' Create a transient color object.
    Dim oColor As Color
    Set oColor = ThisApplication.TransientObjects.CreateColor(255, 0, 0) 'Red

    ' Create a fill region with an override color.
    Call oSketch.SketchFillRegions.Add(oProfile2, oColor)

    ' Exit from editing the sketch.
    oSketch.ExitEdit
End Sub
```
