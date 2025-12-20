# Extrude Feature - Create Block with Pocket

## Description

This sample demonstrates creating a simple solid consisting a block with a pocket. It shows how to create a sketch plane at a specified orientation to existing geometry.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub DrawBlockWithPocket()
    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane.  Since it's being created on
    ' one of the base workplanes we know the orientation it will be created in
    ' and don't need to worry about controlling it.  Because of this we also
    ' know the origin of the sketch plane will be at (0,0,0) in model space.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw a 4cm x 3cm rectangle with the corner at (0,0)
    Dim oRectangleLines As SketchEntitiesEnumerator
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
                                oTransGeom.CreatePoint2d(0, 0), _
                                oTransGeom.CreatePoint2d(4, 3))

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

    ' Create a new sketch on this face, but use the method that allows you to
    ' control the orientation and orgin of the new sketch.
    Set oSketch = oCompDef.Sketches.AddWithOrientation(oFrontFace, _
                    oCompDef.WorkAxes.Item(1), True, True, oCompDef.WorkPoints(1))

    ' Determine where in sketch space the point (0.5,0.5,0) is.
    Dim oCorner As Point2d
    Set oCorner = oSketch.ModelToSketchSpace(oTransGeom.CreatePoint(0.5, 0.5, 0))

    ' Create the interior 3cm x 2cm rectangle for the pocket.
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
                oCorner, oTransGeom.CreatePoint2d(oCorner.X + 3, oCorner.Y + 2))

    ' Create a profile.
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create a pocket .25 cm deep.
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kCutOperation)
    Call oExtrudeDef.SetDistanceExtent(0.25, kNegativeExtentDirection)
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |