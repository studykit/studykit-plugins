# Add a decal feature

## Description

This sample demonstrates the creation of a decal feature.

## Code Samples

* [VBA](#VBA)

Make sure that the path to the bmp file is valid before running the sample.

|  |
| --- |
| Copy Code |

```
Public Sub DecalFeature()
    ' ***Change path to point to the desired bmp file.
    Dim strImagePath As String
    strImagePath = "C:\Temp\Test.bmp"

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
    Set oCenter = oTransGeom.CreatePoint2d(0, 0)

    ' Create a sketch circle
    Dim oCircle As SketchCircle
    Set oCircle = oSketch.SketchCircles.AddByCenterRadius(oCenter, 1)

    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create a base extrusion 4 cm thick.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(1, kPositiveExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Create a new sketch on the Y-Z work plane.
    Dim oDecalSketch As PlanarSketch
    Set oDecalSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes(1))

    ' Create the placement point for the image.
    Dim oPoint As Point2d
    Set oPoint = oTransGeom.CreatePoint2d(0, 4)

    ' Add a sketch image
    Dim oSketchImage As SketchImage
    Set oSketchImage = oDecalSketch.SketchImages.Add(strImagePath, oPoint)

    ' Get the cylindrical face of the extrude
    Dim oFace As Face
    Set oFace = oExtrude.SideFaces.Item(1)

    ' Create a decal feature that wraps onto the cylindrical face.
    Dim oDecal As DecalFeature
    Set oDecal = oCompDef.Features.DecalFeatures.Add(oSketchImage, oFace, True)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |