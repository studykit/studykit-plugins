# Adding a new stitch (knit) feature

## Description

This sample demonstrates the creation of a stitch feature (known as the Knit feature in the API). The sample creates two work surfaces using surface extrusions and stitches them together.

## Code Samples

* [VBA](#VBA)

```
Sub StitchFeatureCreate()
    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane. Dim oSketch As PlanarSketch
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw two sketch lines that will be used as the
    ' open profiles for creating work surfaces.
    Dim oLineOne As SketchLine
    Set oLineOne = oSketch.SketchLines.AddByTwoPoints( _
                                oTransGeom.CreatePoint2d(0, 0), _
                                oTransGeom.CreatePoint2d(2, -2))

    Dim oLineTwo As SketchLine
    Set oLineTwo = oSketch.SketchLines.AddByTwoPoints( _
                                oTransGeom.CreatePoint2d(0, 0), _
                                oTransGeom.CreatePoint2d(-2, -2))

    ' Create a profile for the first extrude.
    Dim oProfileOne As Profile
    Set oProfileOne = oSketch.Profiles.AddForSurface(oLineOne)

    ' Create an surface extrusion 2 cm thick.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfileOne, kSurfaceOperation)
    Call oExtrudeDef.SetDistanceExtent(2, kNegativeExtentDirection)
    Dim oExtrudeOne As ExtrudeFeature
    Set oExtrudeOne = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Create a profile for the second extrude.
    Dim oProfileTwo As Profile
    Set oProfileTwo = oSketch.Profiles.AddForSurface(oLineTwo)

    ' Create an extrusion 2 cm thick.
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfileTwo, kSurfaceOperation)
    Call oExtrudeDef.SetDistanceExtent(2, kNegativeExtentDirection)
    Dim oExtrudeTwo As ExtrudeFeature
    Set oExtrudeTwo = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    Dim oSurfaces As ObjectCollection
    Set oSurfaces = ThisApplication.TransientObjects.CreateObjectCollection

    ' Since we know that the only work surfaces in the document
    ' are those created by the above extrusions, use those.
    oSurfaces.Add oCompDef.WorkSurfaces.Item(1)
    oSurfaces.Add oCompDef.WorkSurfaces.Item(2)

    ' Create a stitch (knit) feature by stitching
    ' together the two work surfaces created above.
    Dim oKnitFeature As KnitFeature
    Set oKnitFeature = oCompDef.Features.KnitFeatures.Add(oSurfaces)
End Sub
```
