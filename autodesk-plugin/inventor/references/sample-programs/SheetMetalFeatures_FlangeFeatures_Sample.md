# Create sheet metal face and flange features

## Description

This sample demonstrates the creation of sheet metal face and flange features.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub FaceAndFlangeFeatureCreation()
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

    ' Get the top face for creating the flange.
    ' We'll assume that the 6th face is the top face.
    Dim oFrontFace As Face
    Set oFrontFace = oFaceFeature.Faces.Item(6)

    ' Collect up all edges of the face
    Dim oEdgeCollection As EdgeCollection
    Set oEdgeCollection = ThisApplication.TransientObjects.CreateEdgeCollection

    Dim oEdge As Edge
    For Each oEdge In oFrontFace.Edges
        Call oEdgeCollection.Add(oEdge)
    Next

    Dim oFlangeDefinition As FlangeDefinition
    Set oFlangeDefinition = oSheetMetalFeatures.FlangeFeatures.CreateFlangeDefinition(oEdgeCollection, 3.14159 / 2, "2 in")

    ' Set the bend radius value
    oFlangeDefinition.BendRadius = oCompDef.BendRadius.Value * 2

    ' Create a flange feature
    Dim oFlangeFeature As FlangeFeature
    Set oFlangeFeature = oSheetMetalFeatures.FlangeFeatures.Add(oFlangeDefinition)

End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |