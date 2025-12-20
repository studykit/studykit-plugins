# Transient surface body creation

## Description

The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateRectangleFace()
    Dim oTransBRep As TransientBRep
    Set oTransBRep = ThisApplication.TransientBRep

    Dim oSurfaceBodyDef As SurfaceBodyDefinition
    Set oSurfaceBodyDef = oTransBRep.CreateSurfaceBodyDefinition

    ' Create a lump.
    Dim oLumpDef As LumpDefinition
    Set oLumpDef = oSurfaceBodyDef.LumpDefinitions.Add

    ' Create a shell.
    Dim oShell As FaceShellDefinition
    Set oShell = oLumpDef.FaceShellDefinitions.Add

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Create transient points representing the four corners.
    Dim oPoint1 As Point
    Set oPoint1 = oTG.CreatePoint(-1, -1, 1)
    Dim oPoint2 As Point
    Set oPoint2 = oTG.CreatePoint(1, -1, 1)
    Dim oPoint3 As Point
    Set oPoint3 = oTG.CreatePoint(1, 1, 1)
    Dim oPoint4 As Point
    Set oPoint4 = oTG.CreatePoint(-1, 1, 1)

    ' Create the Vertices.
    Dim oVertex1 As VertexDefinition
    Set oVertex1 = oSurfaceBodyDef.VertexDefinitions.Add(oPoint1)
    Dim oVertex2 As VertexDefinition
    Set oVertex2 = oSurfaceBodyDef.VertexDefinitions.Add(oPoint2)
    Dim oVertex3 As VertexDefinition
    Set oVertex3 = oSurfaceBodyDef.VertexDefinitions.Add(oPoint3)
    Dim oVertex4 As VertexDefinition
    Set oVertex4 = oSurfaceBodyDef.VertexDefinitions.Add(oPoint4)

    ' Create each of the edges, as defined by a line segment.
    Dim oLineSeg As LineSegment
    Set oLineSeg = oTG.CreateLineSegment(oPoint1, oPoint2)

    Dim oEdgeDef1 As EdgeDefinition
    Set oEdgeDef1 = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex1, oVertex2, oLineSeg)

    Set oLineSeg = oTG.CreateLineSegment(oPoint2, oPoint3)

    Dim oEdgeDef2 As EdgeDefinition
    Set oEdgeDef2 = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex2, oVertex3, oLineSeg)

    Set oLineSeg = oTG.CreateLineSegment(oPoint3, oPoint4)

    Dim oEdgeDef3 As EdgeDefinition
    Set oEdgeDef3 = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex3, oVertex4, oLineSeg)

    Set oLineSeg = oTG.CreateLineSegment(oPoint4, oPoint1)

    Dim oEdgeDef4 As EdgeDefinition
    Set oEdgeDef4 = oSurfaceBodyDef.EdgeDefinitions.Add(oVertex4, oVertex1, oLineSeg)

    ' Create the face as a planar face.
    Dim oFaceDef As FaceDefinition
    Set oFaceDef = oShell.FaceDefinitions.Add(oTG.CreatePlane( _
                                              oTG.CreatePoint(0, 0, 1), _
                                              oTG.CreateVector(0, 0, 1)), False)

    ' Create the loop.
    Dim oEdgeLoop As EdgeLoopDefinition
    Set oEdgeLoop = oFaceDef.EdgeLoopDefinitions.Add

    ' Define each of the edge uses of the loop using the previously defined edges.
    Call oEdgeLoop.EdgeUseDefinitions.Add(oEdgeDef1, False)
    Call oEdgeLoop.EdgeUseDefinitions.Add(oEdgeDef2, False)
    Call oEdgeLoop.EdgeUseDefinitions.Add(oEdgeDef3, False)
    Call oEdgeLoop.EdgeUseDefinitions.Add(oEdgeDef4, False)

    ' Create a transient body.
    Dim oErrors As NameValueMap
    Dim oNewBody As SurfaceBody
    Set oNewBody = oSurfaceBodyDef.CreateTransientSurfaceBody(oErrors)

    ' Create a non-parametric base feature based on the transient body.
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oDef As PartComponentDefinition
    Set oDef = oDoc.ComponentDefinition

    Dim oFeatureDef As NonParametricBaseFeatureDefinition
    Set oFeatureDef = oDef.Features.NonParametricBaseFeatures.CreateDefinition

    Dim oCollection As ObjectCollection
    Set oCollection = ThisApplication.TransientObjects.CreateObjectCollection

    oCollection.Add oNewBody

    oFeatureDef.BRepEntities = oCollection
    oFeatureDef.OutputType = kSurfaceOutputType

    Dim oBaseFeature As NonParametricBaseFeature
    Set oBaseFeature = oDef.Features.NonParametricBaseFeatures.AddByDefinition(oFeatureDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |