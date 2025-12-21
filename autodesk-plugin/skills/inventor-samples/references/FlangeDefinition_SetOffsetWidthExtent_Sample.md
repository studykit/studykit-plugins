# Creating flange features

## Description

Demonstrates creating flange features of various width extents. This creates a new document, creates a face feature and adds a flange feature on four edges.

## Code Samples

* [VBA](#VBA)

```
Public Sub FlangeWidthsCreation()
    ' Create a new sheet metal document.
    Dim sheetMetalDoc As PartDocument
    Set sheetMetalDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                        ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject, , , "{9C464203-9BAE-11D3-8BAD-0060B0CE6BB4}"))

    ' Get the sheet metal component definition.
    Dim smCompDef As SheetMetalComponentDefinition
    Set smCompDef = sheetMetalDoc.ComponentDefinition

    ' Create a sketch on the x-y plane.
    Dim sketch As PlanarSketch
    Set sketch = smCompDef.Sketches.Add(smCompDef.WorkPlanes.Item(3))

    Dim tg As TransientGeometry
    Set tg = ThisApplication.TransientGeometry

    ' Draw a rectangle.
    Call sketch.SketchLines.AddAsTwoPointRectangle(tg.CreatePoint2d(0, 0), tg.CreatePoint2d(25, 15))

    ' Create a profile.
    Dim profile As profile
    Set profile = sketch.Profiles.AddForSolid

    Dim smFeatures As SheetMetalFeatures
    Set smFeatures = smCompDef.Features

    ' Build up a face feature definition.
    Dim faceDef As FaceFeatureDefinition
    Set faceDef = smFeatures.FaceFeatures.CreateFaceFeatureDefinition(profile)

    ' Create a face feature.
    Dim faceFeature As faceFeature
    Set faceFeature = smFeatures.FaceFeatures.Add(faceDef)

    ' Get the "top" face.
    Dim topFace As face
    Set topFace = smCompDef.SurfaceBodies.Item(1).LocateUsingPoint(kFaceObject, tg.CreatePoint(5, 5, smCompDef.Thickness.Value))

    ' Create a collection containing the four edges.
    Dim edgeSet As EdgeCollection
    Set edgeSet = ThisApplication.TransientObjects.CreateEdgeCollection
    Dim i As Integer
    For i = 1 To 4
        Call edgeSet.Add(topFace.Edges.Item(i))
    Next

    ' Create the flange definition.
    Dim flangeDef As FlangeDefinition
    Set flangeDef = smFeatures.FlangeFeatures.CreateFlangeDefinition(edgeSet, "90", 6)

    ' Edit the definition to define a different width extent for each edge.
    For i = 1 To 4
        Dim faceEdge As Edge
        Set faceEdge = edgeSet.Item(i)
        Select Case i
            Case 1
                ' Do nothing and let it default to the edge extent.
            Case 2
                ' Edit the width extent to be centered.
                Call flangeDef.SetCenteredWidthExtent(faceEdge, 10)
            Case 3
                ' Edit the width extent to be offset as measured from the vertices of the edge.
                Call flangeDef.SetOffsetWidthExtent(faceEdge, faceEdge.StartVertex, 2, faceEdge.StopVertex, 5)
            Case 4
                ' Edit the width extent to be an offset width extent.
                Call flangeDef.SetWidthOffsetWidthExtent(faceEdge, 6, 2, faceEdge.StartVertex, True)
        End Select
    Next

    ' Create the flange.
    Call smFeatures.FlangeFeatures.Add(flangeDef)
End Sub
```
