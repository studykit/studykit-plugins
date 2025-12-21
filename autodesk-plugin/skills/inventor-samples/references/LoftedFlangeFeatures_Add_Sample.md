# Create sheet metal lofted flange feature

## Description

The following sample demonstrates the creation of a sheet metal lofted flange feature.

## Code Samples

* [VBA](#VBA)

```
Public Sub LoftedFeatureCreation()
    ' Create a new sheet metal document, using the default sheet metal template.
    Dim oSheetMetalDoc As PartDocument
    Set oSheetMetalDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                 ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject, , , "{9C464203-9BAE-11D3-8BAD-0060B0CE6BB4}"))

    ' Set a reference to the component definition.
    Dim oCompDef As SheetMetalComponentDefinition
    Set oCompDef = oSheetMetalDoc.ComponentDefinition

    ' Set a reference to the sheet metal features collection.
    Dim oSheetMetalFeatures As SheetMetalFeatures
    Set oSheetMetalFeatures = oCompDef.Features

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Create the first sketch on the X-Y work plane.
    Dim oSketch1 As PlanarSketch
    Set oSketch1 = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(3))

    ' Draw a 4cm x 3cm rectangle with the corner at (0,0)
    Dim oSketchLines As SketchEntitiesEnumerator
    Set oSketchLines = oSketch1.SketchLines.AddAsTwoPointRectangle( _
                                oTransGeom.CreatePoint2d(-2, -2), _
                                oTransGeom.CreatePoint2d(2, 2))

    ' Create a path.
    Dim oPath1 As Path
    Set oPath1 = oCompDef.Features.CreatePath(oSketchLines.Item(1))

    ' Create a workplane offset from the X-Y plane by 2 inches.
    Dim oWorkPlane As WorkPlane
    Set oWorkPlane = oCompDef.WorkPlanes.AddByPlaneAndOffset(oCompDef.WorkPlanes.Item(3), "2 in")
    oWorkPlane.Visible = False

    ' Create the second sketch on the new work plane.
    Dim oSketch2 As PlanarSketch
    Set oSketch2 = oCompDef.Sketches.Add(oWorkPlane)

    ' Draw a circle with center at (0,0) and radius 5.
    Dim oSketchCircle As SketchCircle
    Set oSketchCircle = oSketch2.SketchCircles.AddByCenterRadius(oTransGeom.CreatePoint2d(0, 0), 5)

    ' Create a path.
    Dim oPath2 As Path
    Set oPath2 = oCompDef.Features.CreatePath(oSketchCircle)

    Dim oLoftedFlangeDefinition As LoftedFlangeDefinition
    Set oLoftedFlangeDefinition = oSheetMetalFeatures.LoftedFlangeFeatures.CreateLoftedFlangeDefinition(oPath1, oPath2)

    ' Set the output type to press brake with a chord tolerance of .1
    Call oLoftedFlangeDefinition.SetOutputType(kPressBrakeChordToleranceLoftedFlange, "0.1 in")

    ' Create a lofted flange feature.
    Dim oLoftedFlangeFeature As LoftedFlangeFeature
    Set oLoftedFlangeFeature = oSheetMetalFeatures.LoftedFlangeFeatures.Add(oLoftedFlangeDefinition)

    ThisApplication.ActiveView.GoHome
End Sub
```
