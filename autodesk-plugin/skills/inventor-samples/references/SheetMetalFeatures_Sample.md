# Create sheet metal face and cut features

## Description

This sample demonstrates the creation of sheet metal face and cut features.

## Code Samples

* [VBA](#VBA)

```
Public Sub FaceAndCutFeatureCreation()
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

    ' Create a new sketch on the X-Y work plane.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw a 4cm x 3cm rectangle with the corner at (0,0)
    Call oSketch.SketchLines.AddAsTwoPointRectangle( _
                                oTransGeom.CreatePoint2d(0, 0), _
                                oTransGeom.CreatePoint2d(4, 3))

    ' Create a profile.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    Dim oFaceFeatureDefinition As FaceFeatureDefinition
    Set oFaceFeatureDefinition = oSheetMetalFeatures.FaceFeatures.CreateFaceFeatureDefinition(oProfile)

    ' Create a face feature.
    Dim oFaceFeature As FaceFeature
    Set oFaceFeature = oSheetMetalFeatures.FaceFeatures.Add(oFaceFeatureDefinition)

    ' Get the top face for creating the new sketch.
    ' We'll assume that the 6th face is the top face.
    Dim oFrontFace As Face
    Set oFrontFace = oFaceFeature.Faces.Item(6)

    ' Create a new sketch on this face, but use the method that allows you to
    ' control the orientation and orgin of the new sketch.
    Set oSketch = oCompDef.Sketches.AddWithOrientation(oFrontFace, _
                    oCompDef.WorkAxes.Item(1), True, True, oCompDef.WorkPoints(1))

    ' Determine where in sketch space the point (1,0.75,0) is.
    Dim oCorner As Point2d
    Set oCorner = oSketch.ModelToSketchSpace(oTransGeom.CreatePoint(1, 0.75, 0))

    ' Create the interior 3cm x 2cm rectangle for the cut.
    Call oSketch.SketchLines.AddAsTwoPointRectangle( _
                oCorner, oTransGeom.CreatePoint2d(oCorner.X + 2, oCorner.Y + 1.5))

    ' Create a profile.
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create a cut definition object
    Dim oCutDefinition As CutDefinition
    Set oCutDefinition = oSheetMetalFeatures.CutFeatures.CreateCutDefinition(oProfile)

    ' Set extents to 'Through All'
    Call oCutDefinition.SetThroughAllExtent(kNegativeExtentDirection)

    ' Create the cut feature
    Dim oCutFeature As CutFeature
    Set oCutFeature = oSheetMetalFeatures.CutFeatures.Add(oCutDefinition)
End Sub
```
