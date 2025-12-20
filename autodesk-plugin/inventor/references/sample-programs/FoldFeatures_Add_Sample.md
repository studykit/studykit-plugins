# Create sheet metal face and fold features

## Description

This sample demonstrates the creation of sheet metal face and fold features.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub FaceAndFoldFeatureCreation()
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

    ' Create a new sketch on the top face.
    Dim oFoldLineSketch As PlanarSketch
    Set oFoldLineSketch = oCompDef.Sketches.Add(oFrontFace)

    ' The end points of the sketch line must lie on an edge

    Dim oEdge1MidPoint As Point
    Set oEdge1MidPoint = oFrontFace.Edges(1).Geometry.MidPoint

    Dim oSketchPoint1 As Point2d
    Set oSketchPoint1 = oFoldLineSketch.ModelToSketchSpace(oEdge1MidPoint)

    Dim oEdge2MidPoint As Point
    Set oEdge2MidPoint = oFrontFace.Edges(3).Geometry.MidPoint

    Dim oSketchPoint2 As Point2d
    Set oSketchPoint2 = oFoldLineSketch.ModelToSketchSpace(oEdge2MidPoint)

    ' Create the fold line between the midpoint of two opposite edges on the face
    Dim oFoldLine As SketchLine
    Set oFoldLine = oFoldLineSketch.SketchLines.AddByTwoPoints(oSketchPoint1, oSketchPoint2)

    Dim oFoldDefinition As FoldDefinition
    Set oFoldDefinition = oSheetMetalFeatures.FoldFeatures.CreateFoldDefinition(oFoldLine, "60 deg")

    ' Create a fold feature
    Dim oFoldFeature As FoldFeature
    Set oFoldFeature = oSheetMetalFeatures.FoldFeatures.Add(oFoldDefinition)

    ThisApplication.ActiveView.GoHome

End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |