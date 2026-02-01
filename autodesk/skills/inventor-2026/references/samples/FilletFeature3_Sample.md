# Fillet Feature (Simple)

## Description

This sample demonstrates using the AddSimple method of the FilletFeatures collection to create a constant radius fillet.

## Code Samples

* [VBA](#VBA)

```
Public Sub CreateSimpleFillet()
    ' Create a new Part document.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                 ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Set a reference to the compdef.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a sketch on the xy work plane.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(3))

    ' Draw a rectangle.
    Call oSketch.SketchLines.AddAsTwoPointRectangle( _
                            ThisApplication.TransientGeometry.CreatePoint2d(-6, -4), _
                            ThisApplication.TransientGeometry.CreatePoint2d(6, 4))

    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create an extrusion.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(5, kSymmetricExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Define the set of edges that are for the start and end faces of the solid.
    Dim oEdges As EdgeCollection
    Set oEdges = ThisApplication.TransientObjects.CreateEdgeCollection

    Dim oEdge As Edge
    For Each oEdge In oExtrude.StartFaces.Item(1).Edges
        oEdges.Add oEdge
    Next

    For Each oEdge In oExtrude.EndFaces.Item(1).Edges
        oEdges.Add oEdge
    Next

    ' Create the fillet feature.
    Dim oFillet As FilletFeature
    Set oFillet = oCompDef.Features.FilletFeatures.AddSimple(oEdges, 1)
End Sub
```
