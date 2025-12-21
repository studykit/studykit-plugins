# Create Pattern Feature with PatternBoundarySetting Sample

## Description

This sample demonstrates how to create a rectangular pattern feature with boundary settings.

## Code Samples

* [VBA](#VBA)

This sample demonstrates how to create a rectangular pattern feature with boundary settings.

```
Public Sub CreatePatternBoundarySettingSample()
    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw a rectangle.
    Dim oRectangleLines As SketchEntitiesEnumerator
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
                                oTransGeom.CreatePoint2d(-10, -10), _
                                oTransGeom.CreatePoint2d(10, 10))

    ' Create a profile.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create a base extrusion 1cm thick.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(1, kNegativeExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Get the top face of the extrusion to use for creating the new sketch.
    Dim oFrontFace As Face
    Set oFrontFace = oExtrude.StartFaces.Item(1)

    ' Create a new sketch on this face.
    Set oSketch = oCompDef.Sketches.AddWithOrientation(oFrontFace, _
                    oCompDef.WorkAxes.Item(1), True, True, oCompDef.WorkPoints(1))

    ' Determine where in sketch space the point (0.5,0.5,0) is.
    Dim oCorner As Point2d
    Set oCorner = oTransGeom.CreatePoint2d(-9, 9)

    Dim oTriangle As SketchEntitiesEnumerator
    Set oTriangle = oSketch.SketchLines.AddAsPolygon(3, oCorner, oTransGeom.CreatePoint2d(-9.5, 9.5), True)

    ' Create a profile.
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create a cut feature.
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kCutOperation)
    Call oExtrudeDef.SetDistanceExtent(1, kNegativeExtentDirection)
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    Set oSketch = oCompDef.Sketches.AddWithOrientation(oFrontFace, _
                    oCompDef.WorkAxes.Item(1), True, True, oCompDef.WorkPoints(1))

    Call oSketch.SketchLines.AddAsTwoPointRectangle(oTransGeom.CreatePoint2d(-6.5, 8), oTransGeom.CreatePoint2d(8.5, -8))

    ' Use the cut feature as parent features for pattern feature.
    Dim oParentFeatures As ObjectCollection
    Set oParentFeatures = ThisApplication.TransientObjects.CreateObjectCollection
    oParentFeatures.Add oExtrude

    Dim oRectPatternDef As RectangularPatternFeatureDefinition
    Set oRectPatternDef = oCompDef.Features.RectangularPatternFeatures.CreateDefinition(oParentFeatures, oFrontFace.Edges(6), False, 6, "4 cm")
    oRectPatternDef.YDirectionEntity = oFrontFace.Edges(7)
    oRectPatternDef.YCount = 6
    oRectPatternDef.YSpacing = "3 cm"
    oRectPatternDef.NaturalYDirection = True

    ' Set the boundary settings for the pattern feature.
    Set oProfile = oSketch.Profiles.AddForSolid
    Dim oPatternBoundarySetting As PatternBoundarySetting
    Set oPatternBoundarySetting = oRectPatternDef.BoundarySetting
    Call oPatternBoundarySetting.SetBoundarySettingData(oProfile, kCentroidsInclusionType)

    ' Create rectangular pattern feature with boundary settings.
    Dim oRectPatternFeature As RectangularPatternFeature
    Set oRectPatternFeature = oCompDef.Features.RectangularPatternFeatures.AddByDefinition(oRectPatternDef)
End Sub
```
