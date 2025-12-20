# Finish Feature Creation

## Description

This sample demonstrates how to create a finish feature.

## Code Samples

* [VBA](#VBA)

This sample demonstrates how to create a finish feature.

|  |
| --- |
| Copy Code |

```
Sub FinishFeatureSample()
    ' Create a new part document.
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
    Dim oExtrude1 As ExtrudeFeature
    Set oExtrude1 = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Get the top face of the extrusion to use for creating the new sketch.
    Dim oFrontFace As Face
    Set oFrontFace = oExtrude1.StartFaces.Item(1)

    Dim oGeometries As FaceCollection
    Set oGeometries = ThisApplication.TransientObjects.CreateFaceCollection

    oGeometries.Add oFrontFace

    Dim oFinishFeatures As FinishFeatures
    Set oFinishFeatures = oCompDef.Features.FinishFeatures

    Dim oAppearance As Asset
    ' Get an appearance asset from library: Autodesk Appearance Library
    ThisApplication.AssetLibraries("314DE259-5443-4621-BFBD-1730C6CC9AE9").AppearanceAssets("Red").CopyTo oPartDoc
    Set oAppearance = oPartDoc.AppearanceAssets.Item("Red")

    ' Create finish definition.
    Dim oFinishDef As FinishDefinition
    Set oFinishDef = oFinishFeatures.CreateFinishDefinition(oGeometries, FinishTypeEnum.kAppearanceFinishType, , oAppearance)

    ' Create finish feature.
    Dim oFinish As FinishFeature
    Set oFinish = oFinishFeatures.Add(oFinishDef)

End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |