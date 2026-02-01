# Transient B-Rep Ruled Surface with Arc and Line

## Description

Demonstrate creating a transient ruled surface. This sample uses straight line segments for once section and an arc for the second. A part document must be open.

## Code Samples

* [VBA](#VBA)

To use this sample a part must be active.

```
Public Sub RuledSurf()
    ' Get the transient B-Rep and Geometry objects.
    Dim tBRep As TransientBRep
    Set tBRep = ThisApplication.TransientBRep

    Dim tg As TransientGeometry
    Set tg = ThisApplication.TransientGeometry

    ' Create a new surface body definition.
    Dim bodyDef As SurfaceBodyDefinition
    Set bodyDef = tBRep.CreateSurfaceBodyDefinition

    ' Add a lump, shell, and wire.
    Dim lumpDef As LumpDefinition
    Set lumpDef = bodyDef.LumpDefinitions.Add

    Dim shellDef As FaceShellDefinition
    Set shellDef = lumpDef.FaceShellDefinitions.Add

    Dim wireDef As WireDefinition
    Set wireDef = shellDef.WireDefinitions.Add

    ' Create coordinate points and use those to create vertex definitions.
    Dim pnts(2) As Point
    Set pnts(0) = tg.CreatePoint(0, 0, 0)
    Set pnts(1) = tg.CreatePoint(10, 3, 0)
    Set pnts(2) = tg.CreatePoint(20, 0, 0)

    Dim vertexDefs(2) As VertexDefinition
    Set vertexDefs(0) = bodyDef.VertexDefinitions.Add(pnts(0))
    Set vertexDefs(1) = bodyDef.VertexDefinitions.Add(pnts(1))
    Set vertexDefs(2) = bodyDef.VertexDefinitions.Add(pnts(2))

    ' Create two wire edges, passing through the three vertices.
    Call wireDef.WireEdgeDefinitions.Add(vertexDefs(0), vertexDefs(1), tg.CreateLineSegment(pnts(0), pnts(1)))
    Call wireDef.WireEdgeDefinitions.Add(vertexDefs(1), vertexDefs(2), tg.CreateLineSegment(pnts(1), pnts(2)))

    ' Create a second wire definition.
    Dim wireDef2 As WireDefinition
    Set wireDef2 = shellDef.WireDefinitions.Add

    ' Create coordinate points and use those to create vertex definitions.
    Set pnts(0) = tg.CreatePoint(-5, 0, 10)
    Set pnts(1) = tg.CreatePoint(10, 6, 10)
    Set pnts(2) = tg.CreatePoint(25, 0, 10)

    Set vertexDefs(0) = bodyDef.VertexDefinitions.Add(pnts(0))
    Set vertexDefs(1) = bodyDef.VertexDefinitions.Add(pnts(1))
    Set vertexDefs(2) = bodyDef.VertexDefinitions.Add(pnts(2))

    ' Create two edges, passing through the three vertices.
    Call wireDef2.WireEdgeDefinitions.Add(vertexDefs(0), vertexDefs(1), tg.CreateLineSegment(pnts(0), pnts(1)))
    Call wireDef2.WireEdgeDefinitions.Add(vertexDefs(1), vertexDefs(2), tg.CreateLineSegment(pnts(1), pnts(2)))

    ' Create a body using the defined wires.
    Dim errors As NameValueMap
    Set errors = ThisApplication.TransientObjects.CreateNameValueMap
    Dim body1 As SurfaceBody
    Set body1 = bodyDef.CreateTransientSurfaceBody(errors)

    ' Create a ruled surface between the two wire bodies.
    Dim ruled As SurfaceBody
    Set ruled = tBRep.CreateRuledSurface(body1.Wires.Item(1), body1.Wires.Item(2))

    ' Get the part component definition of the active document.
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.ActiveDocument
    Dim partDef As PartComponentDefinition
    Set partDef = partDoc.ComponentDefinition

    ' Create a base body feature of the transient body.
    Dim baseBody As NonParametricBaseFeature
    Set baseBody = partDef.Features.NonParametricBaseFeatures.Add(ruled)

    ' Change the result work surface so it's not translucent.
    baseBody.SurfaceBodies.Item(1).Parent.Translucent = False

    ThisApplication.ActiveView.Fit
End Sub
```
