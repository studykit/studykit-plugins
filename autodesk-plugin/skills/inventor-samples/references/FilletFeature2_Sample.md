# Fillet Feature (Complex)

## Description

This sample demonstrates creating a complex fillet. The result in this case has several different constant radii fillets and two edges that use variable radius, with one of these having a different radius defined along the edge.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateFilletComplex()
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
    Dim oEnts As SketchEntitiesEnumerator
    Set oEnts = oSketch.SketchLines.AddAsTwoPointRectangle( _
                            ThisApplication.TransientGeometry.CreatePoint2d(-6, -4), _
                            ThisApplication.TransientGeometry.CreatePoint2d(6, 4))

    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create an extrusion.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(8, kSymmetricExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Create an EdgeCollection object to use for inputting the edges for fillets.
    Dim oEdgeCollection As EdgeCollection
    Set oEdgeCollection = ThisApplication.TransientObjects.CreateEdgeCollection

    ' Add all of the edges of the start face to the edge collection.
    Dim oEdge As Edge
    For Each oEdge In oExtrude.StartFaces.Item(1).Edges
        oEdgeCollection.Add oEdge
    Next

    ' Obtain a FilletDefinition object to use in defining the various inputs to create the fillet.
    Dim oFilletDef As FilletDefinition
    Set oFilletDef = oCompDef.Features.FilletFeatures.CreateFilletDefinition

    ' Create the first edge set.
    Call oFilletDef.AddConstantRadiusEdgeSet(oEdgeCollection, 1.5)

    ' Reinitialize the edge collection.
    Set oEdgeCollection = ThisApplication.TransientObjects.CreateEdgeCollection

    ' Add all of the edges of the end face to the edge collection.
    For Each oEdge In oExtrude.EndFaces.Item(1).Edges
        oEdgeCollection.Add oEdge
    Next

    ' Create the first edge set.
    Call oFilletDef.AddConstantRadiusEdgeSet(oEdgeCollection, 1)

    ' Find the edges that go between the start and end faces by checking to
    ' see if they're parallel to the Z axis.
    Dim oZVector As UnitVector
    Set oZVector = ThisApplication.TransientGeometry.CreateUnitVector(0, 0, 1)
    Dim oSideEdges(1 To 4) As Edge
    Dim EdgeCount As Long
    EdgeCount = 0
    For Each oEdge In oCompDef.SurfaceBodies.Item(1).Edges
        ' In this case we know all the edges are linear.
        Dim oLine As LineSegment
        Set oLine = oEdge.Geometry

        If oLine.Direction.IsParallelTo(oZVector) Then
            EdgeCount = EdgeCount + 1
            Set oSideEdges(EdgeCount) = oEdge
        End If
    Next

    ' Add the first two edges to a constant radius edge set.
    Set oEdgeCollection = ThisApplication.TransientObjects.CreateEdgeCollection
    oEdgeCollection.Add oSideEdges(1)
    oEdgeCollection.Add oSideEdges(2)
    Call oFilletDef.AddConstantRadiusEdgeSet(oEdgeCollection, 0.5)

    ' Create a variable radius edge set for the third edge.
    Set oEdgeCollection = ThisApplication.TransientObjects.CreateEdgeCollection
    oEdgeCollection.Add oSideEdges(3)
    Call oFilletDef.AddVariableRadiusEdgeSet(oEdgeCollection, 1, 2)

    ' Create a variable radius edge with a different internal radius for the fourth edge.
    Set oEdgeCollection = ThisApplication.TransientObjects.CreateEdgeCollection
    oEdgeCollection.Add oSideEdges(4)
    Dim oVarRadiusEdgeSet As FilletVariableRadiusEdgeSet
    Set oVarRadiusEdgeSet = oFilletDef.AddVariableRadiusEdgeSet(oEdgeCollection, 0.5, 1.5)
    Call oVarRadiusEdgeSet.AddIntermediateRadius(oSideEdges(4), 3, 0.5)

    Dim oFillet As FilletFeature
    Set oFillet = oCompDef.Features.FilletFeatures.Add(oFilletDef, False)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |