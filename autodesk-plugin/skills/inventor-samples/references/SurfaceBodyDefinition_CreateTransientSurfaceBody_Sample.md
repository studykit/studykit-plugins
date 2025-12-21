# Transient solid body creation

## Description

The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part.

## Code Samples

* [VBA](#VBA)

```
Public Sub CreateBlock()
    Dim oTransBRep As TransientBRep
    Set oTransBRep = ThisApplication.TransientBRep

    Dim oSurfaceBodyDef As SurfaceBodyDefinition
    Set oSurfaceBodyDef = oTransBRep.CreateSurfaceBodyDefinition

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Create a lump.
    Dim oLumpDef As LumpDefinition
    Set oLumpDef = oSurfaceBodyDef.LumpDefinitions.Add

    ' Create a shell.
    Dim oShell As FaceShellDefinition
    Set oShell = oLumpDef.FaceShellDefinitions.Add

    ' Define the six planes of the box.
    Dim oPosX As Plane
    Dim oNegX As Plane
    Dim oPosY As Plane
    Dim oNegY As Plane
    Dim oPosZ As Plane
    Dim oNegZ As Plane
    Set oPosX = oTG.CreatePlane(oTG.CreatePoint(1, 0, 0), oTG.CreateVector(1, 0, 0))
    Set oNegX = oTG.CreatePlane(oTG.CreatePoint(-1, 0, 0), oTG.CreateVector(-1, 0, 0))
    Set oPosY = oTG.CreatePlane(oTG.CreatePoint(0, 1, 0), oTG.CreateVector(0, 1, 0))
    Set oNegY = oTG.CreatePlane(oTG.CreatePoint(0, -1, 0), oTG.CreateVector(0, -1, 0))
    Set oPosZ = oTG.CreatePlane(oTG.CreatePoint(0, 0, 1), oTG.CreateVector(0, 0, 1))
    Set oNegZ = oTG.CreatePlane(oTG.CreatePoint(0, 0, -1), oTG.CreateVector(0, 0, -1))

    ' Create the six faces.
    Dim oFaceDefPosX As FaceDefinition
    Dim oFaceDefNegX As FaceDefinition
    Dim oFaceDefPosY As FaceDefinition
    Dim oFaceDefNegY As FaceDefinition
    Dim oFaceDefPosZ As FaceDefinition
    Dim oFaceDefNegZ As FaceDefinition
    Set oFaceDefPosX = oShell.FaceDefinitions.Add(oPosX, False)
    Set oFaceDefNegX = oShell.FaceDefinitions.Add(oNegX, False)
    Set oFaceDefPosY = oShell.FaceDefinitions.Add(oPosY, False)
    Set oFaceDefNegY = oShell.FaceDefinitions.Add(oNegY, False)
    Set oFaceDefPosZ = oShell.FaceDefinitions.Add(oPosZ, False)
    Set oFaceDefNegZ = oShell.FaceDefinitions.Add(oNegZ, False)

    ' Create the vertices.
    Dim oVertex1 As VertexDefinition
    Dim oVertex2 As VertexDefinition
    Dim oVertex3 As VertexDefinition
    Dim oVertex4 As VertexDefinition
    Dim oVertex5 As VertexDefinition
    Dim oVertex6 As VertexDefinition
    Dim oVertex7 As VertexDefinition
    Dim oVertex8 As VertexDefinition
    Set oVertex1 = oSurfaceBodyDef.VertexDefinitions.Add(oTG.CreatePoint(1, 1, 1))
    Set oVertex2 = oSurfaceBodyDef.VertexDefinitions.Add(oTG.CreatePoint(1, 1, -1))
    Set oVertex3 = oSurfaceBodyDef.VertexDefinitions.Add(oTG.CreatePoint(-1, 1, -1))
    Set oVertex4 = oSurfaceBodyDef.VertexDefinitions.Add(oTG.CreatePoint(-1, 1, 1))
    Set oVertex5 = oSurfaceBodyDef.VertexDefinitions.Add(oTG.CreatePoint(1, -1, 1))
    Set oVertex6 = oSurfaceBodyDef.VertexDefinitions.Add(oTG.CreatePoint(1, -1, -1))
    Set oVertex7 = oSurfaceBodyDef.VertexDefinitions.Add(oTG.CreatePoint(-1, -1, -1))
    Set oVertex8 = oSurfaceBodyDef.VertexDefinitions.Add(oTG.CreatePoint(-1, -1, 1))

    ' Define the edges at intersections of the defined planes.
    Dim oEdgeDefPosXPosY As EdgeDefinition
    Dim oEdgeDefPosXNegZ As EdgeDefinition
    Dim oEdgeDefPosXNegY As EdgeDefinition
    Dim oEdgeDefPosXPosZ As EdgeDefinition
    Dim oEdgeDefNegXPosY As EdgeDefinition
    Dim oEdgeDefNegXNegZ As EdgeDefinition
    Dim oEdgeDefNegXNegY As EdgeDefinition
    Dim oEdgeDefNegXPosZ As EdgeDefinition
    Dim oEdgeDefPosYNegZ As EdgeDefinition
    Dim oEdgeDefPosYPosZ As EdgeDefinition
    Dim oEdgeDefNegYNegZ As EdgeDefinition
    Dim oEdgeDefNegYPosZ As EdgeDefinition
    Set oEdgeDefPosXPosY = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex1, oVertex2, oTG.CreateLineSegment(oVertex1.Position, oVertex2.Position))
    Set oEdgeDefPosXNegZ = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex2, oVertex6, oTG.CreateLineSegment(oVertex2.Position, oVertex6.Position))
    Set oEdgeDefPosXNegY = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex6, oVertex5, oTG.CreateLineSegment(oVertex6.Position, oVertex5.Position))
    Set oEdgeDefPosXPosZ = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex5, oVertex1, oTG.CreateLineSegment(oVertex5.Position, oVertex1.Position))
    Set oEdgeDefNegXPosY = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex4, oVertex3, oTG.CreateLineSegment(oVertex4.Position, oVertex3.Position))
    Set oEdgeDefNegXNegZ = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex3, oVertex7, oTG.CreateLineSegment(oVertex3.Position, oVertex7.Position))
    Set oEdgeDefNegXNegY = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex7, oVertex8, oTG.CreateLineSegment(oVertex7.Position, oVertex8.Position))
    Set oEdgeDefNegXPosZ = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex8, oVertex4, oTG.CreateLineSegment(oVertex8.Position, oVertex4.Position))
    Set oEdgeDefPosYNegZ = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex2, oVertex3, oTG.CreateLineSegment(oVertex2.Position, oVertex3.Position))
    Set oEdgeDefPosYPosZ = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex4, oVertex1, oTG.CreateLineSegment(oVertex4.Position, oVertex1.Position))
    Set oEdgeDefNegYNegZ = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex7, oVertex6, oTG.CreateLineSegment(oVertex7.Position, oVertex6.Position))
    Set oEdgeDefNegYPosZ = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex5, oVertex8, oTG.CreateLineSegment(oVertex5.Position, oVertex8.Position))

    ' Define the loops on the faces.
    Dim oPosXLoop As EdgeLoopDefinition
    Set oPosXLoop = oFaceDefPosX.EdgeLoopDefinitions.Add
    Call oPosXLoop.EdgeUseDefinitions.Add(oEdgeDefPosXPosY, True)
    Call oPosXLoop.EdgeUseDefinitions.Add(oEdgeDefPosXNegZ, True)
    Call oPosXLoop.EdgeUseDefinitions.Add(oEdgeDefPosXNegY, True)
    Call oPosXLoop.EdgeUseDefinitions.Add(oEdgeDefPosXPosZ, True)

    Dim oNegXLoop As EdgeLoopDefinition
    Set oNegXLoop = oFaceDefNegX.EdgeLoopDefinitions.Add
    Call oNegXLoop.EdgeUseDefinitions.Add(oEdgeDefNegXPosY, False)
    Call oNegXLoop.EdgeUseDefinitions.Add(oEdgeDefNegXNegZ, False)
    Call oNegXLoop.EdgeUseDefinitions.Add(oEdgeDefNegXNegY, False)
    Call oNegXLoop.EdgeUseDefinitions.Add(oEdgeDefNegXPosZ, False)

    Dim oPosYLoop As EdgeLoopDefinition
    Set oPosYLoop = oFaceDefPosY.EdgeLoopDefinitions.Add
    Call oPosYLoop.EdgeUseDefinitions.Add(oEdgeDefPosXPosY, False)
    Call oPosYLoop.EdgeUseDefinitions.Add(oEdgeDefPosYNegZ, False)
    Call oPosYLoop.EdgeUseDefinitions.Add(oEdgeDefNegXPosY, True)
    Call oPosYLoop.EdgeUseDefinitions.Add(oEdgeDefPosYPosZ, False)

    Dim oNegYLoop As EdgeLoopDefinition
    Set oNegYLoop = oFaceDefNegY.EdgeLoopDefinitions.Add
    Call oNegYLoop.EdgeUseDefinitions.Add(oEdgeDefPosXNegY, False)
    Call oNegYLoop.EdgeUseDefinitions.Add(oEdgeDefNegYPosZ, False)
    Call oNegYLoop.EdgeUseDefinitions.Add(oEdgeDefNegXNegY, True)
    Call oNegYLoop.EdgeUseDefinitions.Add(oEdgeDefNegYNegZ, False)

    Dim oPosZLoop As EdgeLoopDefinition
    Set oPosZLoop = oFaceDefPosZ.EdgeLoopDefinitions.Add
    Call oPosZLoop.EdgeUseDefinitions.Add(oEdgeDefNegXPosZ, True)
    Call oPosZLoop.EdgeUseDefinitions.Add(oEdgeDefNegYPosZ, True)
    Call oPosZLoop.EdgeUseDefinitions.Add(oEdgeDefPosXPosZ, False)
    Call oPosZLoop.EdgeUseDefinitions.Add(oEdgeDefPosYPosZ, True)

    Dim oNegZLoop As EdgeLoopDefinition
    Set oNegZLoop = oFaceDefNegZ.EdgeLoopDefinitions.Add
    Call oNegZLoop.EdgeUseDefinitions.Add(oEdgeDefNegXNegZ, True)
    Call oNegZLoop.EdgeUseDefinitions.Add(oEdgeDefNegYNegZ, True)
    Call oNegZLoop.EdgeUseDefinitions.Add(oEdgeDefPosXNegZ, False)
    Call oNegZLoop.EdgeUseDefinitions.Add(oEdgeDefPosYNegZ, True)

    ' Create a transient surface body.
    Dim oErrors As NameValueMap
    Dim oNewBody As SurfaceBody
    Set oNewBody = oSurfaceBodyDef.CreateTransientSurfaceBody(oErrors)

    ' Create client graphics to display the transient body.
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oDef As PartComponentDefinition
    Set oDef = oDoc.ComponentDefinition

    Dim oClientGraphics As ClientGraphics
    Set oClientGraphics = oDef.ClientGraphicsCollection.Add("Sample3DGraphicsID")

    ' Create a new graphics node within the client graphics objects.
    Dim oSurfacesNode As GraphicsNode
    Set oSurfacesNode = oClientGraphics.AddNode(1)

    ' Create client graphics based on the transient body
    Dim oSurfaceGraphics As SurfaceGraphics
    Set oSurfaceGraphics = oSurfacesNode.AddSurfaceGraphics(oNewBody)

    ' Update the view.
    ThisApplication.ActiveView.Update
End Sub
```
