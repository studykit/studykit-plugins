# Fillet Feature (All Rounds)

## Description

This sample demonstrates rounding all of the edges of a part.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateAllRoundsFillet()
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

    ' Declare an EdgeCollection object to pass in since it is a required argument,
    ' but since we're going to specify all rounds, we don't need to actually create
    ' the EdgeCollection or add any edges to it.
    Dim oEdges As EdgeCollection

    ' Create the fillet feature specifying to do all rounds.
    Dim oFillet As FilletFeature
    Set oFillet = oCompDef.Features.FilletFeatures.AddSimple(oEdges, 1, , True)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |