# Edit profile of an extrude feature

## Description

This sample demonstrates editing the profile of an extrude feature.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub EditFeatureProfile()
    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
    ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    Dim oCenter As Point2d
    Set oCenter = oTransGeom.CreatePoint2d(-5, 0)

    ' Create a sketch circle
    Dim oCircle As SketchCircle
    Set oCircle = oSketch.SketchCircles.AddByCenterRadius(oCenter, 1)

    ' Create a profile based on the circle
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create a base extrusion 4 cm thick.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(4, kPositiveExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Draw a 4cm x 3cm rectangle with the corner at (0,0)
    Dim oRectangleLines As SketchEntitiesEnumerator
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
    oTransGeom.CreatePoint2d(0, 0), _
    oTransGeom.CreatePoint2d(4, 3))

    ' Add all the lines of the rectangle to an ObjectCollection
    Dim oPathSegments As ObjectCollection
    Set oPathSegments = ThisApplication.TransientObjects.CreateObjectCollection

    Dim oEntity As SketchEntity
    For Each oEntity In oRectangleLines
      oPathSegments.Add oEntity
    Next

    ' Create a profile that represents the newly created rectangle
    ' and excludes the original circle.
    Set oProfile = oSketch.Profiles.AddForSolid(False, oPathSegments)

    ' Set the new profile
    oExtrude.Definition.Profile = oProfile
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |