# Tapered Surface Using Offset Curve and Ruled Surface

## Description

This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface.

## Code Samples

* [VBA](#VBA)

To use this sample a part must be active.

|  |
| --- |
| Copy Code |

```
Public Sub TaperFace()
    Dim testFace As Face
    Set testFace = ThisApplication.CommandManager.Pick(kPartFacePlanarFilter, "Select a planar face")

    ' Get the transient B-Rep and geometry objects.
    Dim tBRep As TransientBRep
    Set tBRep = ThisApplication.TransientBRep
    Dim tg As TransientGeometry
    Set tg = ThisApplication.TransientGeometry

    ' Create the top-level objects needed to construct a wire.
    Dim bodyDef As SurfaceBodyDefinition
    Set bodyDef = tBRep.CreateSurfaceBodyDefinition

    Dim lumpDef As LumpDefinition
    Set lumpDef = bodyDef.LumpDefinitions.Add

    Dim shellDef As FaceShellDefinition
    Set shellDef = lumpDef.FaceShellDefinitions.Add

    Dim wireDef As WireDefinition
    Set wireDef = shellDef.WireDefinitions.Add

    ' ** Create a wire based on the outside loops of the selected face.

    ' Get the outer loop of the face.
    Dim outerLoop As EdgeLoop
    For Each outerLoop In testFace.EdgeLoops
        If outerLoop.IsOuterEdgeLoop Then
            Exit For
        End If
    Next

    ' Use the edge uses to step around the face.
    Dim lastVertexDef As VertexDefinition
    Set lastVertexDef = Nothing
    Dim coEdge As EdgeUse
    For Each coEdge In outerLoop.EdgeUses
        If lastVertexDef Is Nothing Then
            ' This is the first time through so get the starting vertex of the current edge use.
            If coEdge.IsOpposedToEdge Then
                Set lastVertexDef = bodyDef.VertexDefinitions.Add(coEdge.Edge.StopVertex.Point)
            Else
                Set lastVertexDef = bodyDef.VertexDefinitions.Add(coEdge.Edge.StartVertex.Point)
            End If
        End If

        ' Get the end vertex of the current edge use.
        Dim currentVertexDef As VertexDefinition
        If coEdge.IsOpposedToEdge Then
            Set currentVertexDef = bodyDef.VertexDefinitions.Add(coEdge.Edge.StartVertex.Point)
        Else
            Set currentVertexDef = bodyDef.VertexDefinitions.Add(coEdge.Edge.StopVertex.Point)
        End If

        ' If the geometry is an arc and the co-edge is opposed to the edge,
        ' the arc needs to be massaged so the start and end points are reversed.
        Dim geom As Object
        If coEdge.Edge.GeometryType = kCircularArcCurve And coEdge.IsOpposedToEdge Then
            Dim arc As Arc3d
            Set arc = coEdge.Edge.Geometry

            Dim center() As Double
            Dim axisVector() As Double
            Dim refVector() As Double
            Dim radius As Double
            Dim startAngle As Double
            Dim sweepAngle As Double
            Call arc.GetArcData(center, axisVector, refVector, radius, startAngle, sweepAngle)

            Set arc = tg.CreateArc3d(tg.CreatePoint(center(0), center(1), center(2)), _
                                     tg.CreateUnitVector(-axisVector(0), -axisVector(1), -axisVector(2)), _
                                     tg.CreateUnitVector(refVector(0), refVector(1), refVector(2)), _
                                     radius, startAngle + sweepAngle, sweepAngle)

            Set geom = arc
        Else
            Set geom = coEdge.Edge.Geometry
        End If

        ' Create a wire edge definition for the current edge.
        Call wireDef.WireEdgeDefinitions.Add(lastVertexDef, currentVertexDef, geom)

        ' Reset the last vertex to be the current vertex.
        Set lastVertexDef = currentVertexDef
    Next

    ' Create the wire body.
    Dim errors As NameValueMap
    Set errors = ThisApplication.TransientObjects.CreateNameValueMap
    Dim faceBody As SurfaceBody
    Set faceBody = bodyDef.CreateTransientSurfaceBody(errors)

    ' Draw the wire as client graphics to be able to visualize what's been calculated so far.
    ' This wire should overlay the selected face.
    Call DrawWire(ThisApplication.ActiveDocument.ComponentDefinition, faceBody.Wires.Item(1), True)
    MsgBox "Wire created for outer boundary of selected face."

    ' Copy the wire body and translate it along the normal of the face.
    Dim transBody As SurfaceBody
    Set transBody = tBRep.Copy(faceBody)

    Dim transMatrix As Matrix
    Set transMatrix = tg.CreateMatrix
    Dim faceNormal As Vector
    Set faceNormal = GetFaceNormal(testFace).AsVector
    Call faceNormal.ScaleBy(0.5)
    Call transMatrix.SetTranslation(faceNormal)
    Call tBRep.Transform(transBody, transMatrix)

    ' Draw the translated wire as client graphics to be able to visualize what's been calculated so far.
    Call DrawWire(ThisApplication.ActiveDocument.ComponentDefinition, transBody.Wires.Item(1), False)
    MsgBox "Copied and transformed wire created."

    ' Offset the transformed wire.
    Dim offsetWires As Wires
    Dim offsetDirection As UnitVector
    Set offsetWires = transBody.Wires.Item(1).OffsetPlanarWire(faceNormal.AsUnitVector, 0.25, kExtendCornerClosure)

    ' Draw the offset wire as client graphics to be able to visualize what's been calculated so far.
    Call DrawWire(ThisApplication.ActiveDocument.ComponentDefinition, offsetWires.Item(1), False)
    MsgBox "Offset of wire created."

    ' Creat a ruled surface between the original wire and the offset.
    Dim ruled As SurfaceBody
    Set ruled = tBRep.CreateRuledSurface(faceBody.Wires.Item(1), offsetWires.Item(1))

    ' Create a base body feature of the ruled surface.
    Dim partDef As PartComponentDefinition
    Set partDef = ThisApplication.ActiveDocument.ComponentDefinition
    Dim baseBody As NonParametricBaseFeature
    Set baseBody = partDef.Features.NonParametricBaseFeatures.Add(ruled)

    ' Change the result work surface so it's not translucent.
    baseBody.SurfaceBodies.Item(1).Parent.Translucent = False
    MsgBox "Ruled surface between wires created and base body created."

End Sub

' Utility function that given a face returns a normal.  This is only useful
' for planar faces, since they have a consistent normal anywhere on the face.
Private Function GetFaceNormal(InputFace As Face) As UnitVector
    Dim eval As SurfaceEvaluator
    Set eval = InputFace.Evaluator

    ' Get the center of the parametric range.
    Dim center(1) As Double
    center(0) = (eval.ParamRangeRect.MinPoint.X + eval.ParamRangeRect.MaxPoint.X) / 2
    center(1) = (eval.ParamRangeRect.MinPoint.y + eval.ParamRangeRect.MaxPoint.y) / 2

    ' Calculate the normal.
    Dim normal() As Double
    Call eval.GetNormal(center, normal)

    ' Create a unit vector to pass back the result.
    Set GetFaceNormal = ThisApplication.TransientGeometry.CreateUnitVector(normal(0), normal(1), normal(2))
End Function

' Utility function that draws a Wire as client graphics.
Private Sub DrawWire(partDef As PartComponentDefinition, WireToDisplay As Wire, ClearExisting As Boolean)
    Dim trans As Transaction
    Set trans = ThisApplication.TransactionManager.StartTransaction(partDef.Document, "Wire display")

    Dim graphics As ClientGraphics
    On Error Resume Next
    Set graphics = partDef.ClientGraphicsCollection.Item("WireTest")
    If Err Then
        Set graphics = partDef.ClientGraphicsCollection.Add("WireTest")
    Else
        If ClearExisting Then
            graphics.Delete
            Set graphics = partDef.ClientGraphicsCollection.Add("WireTest")
        End If
    End If

    Dim node As GraphicsNode
    Set node = graphics.AddNode(1)

    Dim e As Edge
    For Each e In WireToDisplay.Edges
        Call node.AddCurveGraphics(e.Geometry)
    Next
    ThisApplication.ActiveView.Update

    trans.End
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |