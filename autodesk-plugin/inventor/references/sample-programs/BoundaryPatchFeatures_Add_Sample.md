# Delete Face, Boundary Patch and Stitch features

## Description

Demonstrates creating Face, Boundary Patch and Stitch features.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub BoundaryPatchFeature()
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

    ' Get the top face of the extrusion
    Dim oFrontFace As Face
    Set oFrontFace = oExtrude.StartFaces.Item(1)

    Dim oEdgeColl As EdgeCollection
    Set oEdgeColl = ThisApplication.TransientObjects.CreateEdgeCollection

    ' Collect up the edges to create boundary patch.
    Dim oEdge As Edge
    For Each oEdge In oFrontFace.Edges
        oEdgeColl.Add oEdge
    Next

    ' Create a Delete Face feature to delete the top face.
    Dim oFaceColl As FaceCollection
    Set oFaceColl = ThisApplication.TransientObjects.CreateFaceCollection
    Call oFaceColl.Add(oFrontFace)

    Dim oDeleteFace As DeleteFaceFeature
    Set oDeleteFace = oCompDef.Features.DeleteFaceFeatures.Add(oFaceColl)

    Dim oBoundaryPatchDef As BoundaryPatchDefinition
    Set oBoundaryPatchDef = oCompDef.Features.BoundaryPatchFeatures.CreateBoundaryPatchDefinition

    ' Create a boundary patch definition based on the edges of the deleted face.
    Call oBoundaryPatchDef.BoundaryPatchLoops.Add(oEdgeColl)

    ' Set the conditions on each edge to be tangent.
    For Each oEdge In oEdgeColl
        Call oBoundaryPatchDef.BoundaryPatchLoops.Item(1).SetBoundaryCondition(oEdge, kTangentBoundaryPatchCondition)
    Next

    ' Create the boundary patch feature based on the definition.
    Dim oBoundaryPatch As BoundaryPatchFeature
    Set oBoundaryPatch = oCompDef.Features.BoundaryPatchFeatures.Add(oBoundaryPatchDef)

    ' Stitch the boundary patch surface to the original body.
    Dim oSurfaceToStitch As ObjectCollection
    Set oSurfaceToStitch = ThisApplication.TransientObjects.CreateObjectCollection

    Call oSurfaceToStitch.Add(oBoundaryPatch.SurfaceBodies.Item(1))
    Call oSurfaceToStitch.Add(oCompDef.SurfaceBodies.Item(1))

    Dim oStitch As KnitFeature
    Set oStitch = oCompDef.Features.KnitFeatures.Add(oSurfaceToStitch)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |