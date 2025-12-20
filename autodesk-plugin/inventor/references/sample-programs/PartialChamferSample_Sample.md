# Partial Chamfer Sample

## Description

This sample demonstrates how to edit a chamfer feature to set the partial chamfer on a chamfered edge.

## Code Samples

* [VBA](#VBA)
* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Sub PartialChamferSample()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    Dim oSk As PlanarSketch
    Set oSk = oDoc.ComponentDefinition.Sketches.Add(oDoc.ComponentDefinition.WorkPlanes(3))

    Call oSk.SketchLines.AddAsTwoPointRectangle(oTG.CreatePoint2d(-5, -5), oTG.CreatePoint2d(5, 5))

    Dim oProfile As Profile
    Set oProfile = oSk.Profiles.AddForSolid

    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oDoc.ComponentDefinition.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kNewBodyOperation)

    Call oDoc.ComponentDefinition.Features.ExtrudeFeatures.Add(oExtrudeDef)

    Dim oEdges As EdgeCollection
    Set oEdges = ThisApplication.TransientObjects.CreateEdgeCollection

    oEdges.Add oDoc.ComponentDefinition.SurfaceBodies(1).Edges(1)

    Dim oChamfer As ChamferFeature
    Set oChamfer = oDoc.ComponentDefinition.Features.ChamferFeatures.AddUsingDistance(oEdges, 0.5, True)

    Dim oChamferDef As ChamferDefinition
    Set oChamferDef = oChamfer.Definition

    ' Rollback the End of Part node to be above the chamfer feature to edit it.
    Call oChamfer.SetEndOfPart(True)

    Dim oPartialChamferEdges As PartialChamferEdges
    Set oPartialChamferEdges = oChamferDef.PartialChamferEdges

    ' Set the partial chamfer edge.
    Call oPartialChamferEdges.Add(oDoc.ComponentDefinition.SurfaceBodies(1).Edges(1), 4, 3)

    ' After editing the feature, set it to be above the End of Part node.
    Call oChamfer.SetEndOfPart(False)
End Sub
```

|  |
| --- |
| Copy Code |

```
Sub PartialChamferSample()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    Dim oSk As PlanarSketch
    Set oSk = oDoc.ComponentDefinition.Sketches.Add(oDoc.ComponentDefinition.WorkPlanes(3))

    Call oSk.SketchLines.AddAsTwoPointRectangle(oTG.CreatePoint2d(-5, -5), oTG.CreatePoint2d(5, 5))

    Dim oProfile As Profile
    Set oProfile = oSk.Profiles.AddForSolid

    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oDoc.ComponentDefinition.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kNewBodyOperation)

    Call oDoc.ComponentDefinition.Features.ExtrudeFeatures.Add(oExtrudeDef)

    Dim oEdges As EdgeCollection
    Set oEdges = ThisApplication.TransientObjects.CreateEdgeCollection

    oEdges.Add oDoc.ComponentDefinition.SurfaceBodies(1).Edges(1)

    Dim oChamfer As ChamferFeature
    Set oChamfer = oDoc.ComponentDefinition.Features.ChamferFeatures.AddUsingDistance(oEdges, 0.5, True)

    Dim oChamferDef As ChamferDefinition
    Set oChamferDef = oChamfer.Definition

    ' Rollback the End of Part node to be above the chamfer feature to edit it.
    Call oChamfer.SetEndOfPart(True)

    Dim oPartialChamferEdges As PartialChamferEdges
    Set oPartialChamferEdges = oChamferDef.PartialChamferEdges

    ' Set the partial chamfer edge.
    Call oPartialChamferEdges.Add(oDoc.ComponentDefinition.SurfaceBodies(1).Edges(1), 4, 3)

    ' After editing the feature, set it to be above the End of Part node.
    Call oChamfer.SetEndOfPart(False)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |