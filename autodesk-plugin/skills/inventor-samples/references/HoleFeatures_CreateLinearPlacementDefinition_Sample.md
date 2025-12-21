# Hole feature linear placement

## Description

This sample demonstrates the creation of a hole feature using the linear placement type.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub HoleFeatureLinearPlacement()
    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                 ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Create a square on the sketch.
    Call oSketch.SketchLines.AddAsTwoPointRectangle( _
                                        oTransGeom.CreatePoint2d(0, 0), _
                                        oTransGeom.CreatePoint2d(6, 6))

    ' Create the profile.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create an extrusion.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent("2 cm", kNegativeExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Get the start face of the extrude.
    Dim oFace As Face
    Set oFace = oExtrude.StartFaces(1)

    ' Get two adjacent edges on the start face.
    Dim oEdge1, oEdge2 As Edge
    Set oEdge1 = oFace.Edges(1)
    Set oEdge2 = oFace.Edges(2)

    ' Create a bias point for hole placement to place it at
    ' the expected location. This is the model point
    ' corresponding to the center of the square in the sketch.
    Dim oBiasPoint As Point
    Set oBiasPoint = oSketch.SketchToModelSpace(oTransGeom.CreatePoint2d(1.5, 1.5))

    ' Create the hole feature placement definition.
    Dim oLinearPlacementDef As LinearHolePlacementDefinition
    Set oLinearPlacementDef = oCompDef.Features.HoleFeatures.CreateLinearPlacementDefinition _
    (oFace, oEdge1, "2 cm", oEdge2, "2 cm", oBiasPoint)

    ' Create the hole feature.
    Call oCompDef.Features.HoleFeatures.AddDrilledByThroughAllExtent( _
                            oLinearPlacementDef, "1 cm", kPositiveExtentDirection)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |