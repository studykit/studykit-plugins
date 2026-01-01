# Finding Bend Extent (Tangent) Edges

## Description

This sample demonstrates how to retrieve the bend extent edges (a.k.a. tangent edges) associated with the selected bend edge on a flat pattern.

## Code Samples

* [VBA](#VBA)

Before running the sample, activate a flat pattern and select a bend edge.

```
Sub BendExtentEdges()
    ' Check to make sure a flat pattern is open.
    If Not TypeOf ThisApplication.ActiveEditObject Is FlatPattern Then
        MsgBox "A flat pattern must be active."
        Exit Sub
    End If

    ' Set a reference to the active document.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active flat pattern.
    Dim oFlatPattern As FlatPattern
    Set oFlatPattern = ThisApplication.ActiveEditObject

    ' Check to make sure a bend edge is selected.
    If Not TypeOf oPartDoc.SelectSet(1) Is Edge Then
        MsgBox "A bend edge must be selected."
        Exit Sub
    End If

    Dim oBendEdge As Edge
    Set oBendEdge = oPartDoc.SelectSet(1)

    If Not IsBendEdge(oBendEdge, oFlatPattern) Then
        MsgBox "A bend edge must be selected."
        Exit Sub
    End If

    Dim oAllTangentEdges As Edges
    Set oAllTangentEdges = oFlatPattern.GetEdgesOfType(kTangentFlatPatternEdge)

    Dim MinimumDist As Double
    MinimumDist = 0

    ' Collect up tangent edges that are parallel and closest to the bend edge
    Dim oBendTangentEdges As ObjectCollection
    Set oBendTangentEdges = ThisApplication.TransientObjects.CreateObjectCollection

    Dim oEdge As Edge
    For Each oEdge In oAllTangentEdges
        ' Only interested in edges that are parallel to the bend edge
        If oBendEdge.Geometry.Direction.IsParallelTo(oEdge.Geometry.Direction, 0.0001) Then
            ' Eliminate any bend edges whose midpoint when projected onto
            ' the bend line is not within the length of the bend line.
            If IsWithinBendEdge(oBendEdge, oEdge) Then
                Dim dist As Double
                dist = ThisApplication.MeasureTools.GetMinimumDistance(oBendEdge, oEdge)
                If MinimumDist = 0 Then
                    oBendTangentEdges.Add oEdge
                    MinimumDist = dist
                ElseIf Abs(dist - MinimumDist) < 0.00001 Then
                    oBendTangentEdges.Add oEdge
                    MinimumDist = dist
                ElseIf dist < MinimumDist Then
                    ' Clear the collection
                    Dim oObject As Object
                    For Each oObject In oBendTangentEdges
                        oBendTangentEdges.RemoveByObject oObject
                    Next

                    oBendTangentEdges.Add oEdge
                    MinimumDist = dist
                End If
            End If
        End If
    Next

    ' Highlight tangent edges in blue.
    Dim oTangentHS As HighlightSet
    Set oTangentHS = oPartDoc.CreateHighlightSet
    oTangentHS.Color = ThisApplication.TransientObjects.CreateColor(255, 255, 0)

    Dim oBendTangentEdge As Edge
    For Each oBendTangentEdge In oBendTangentEdges
        oTangentHS.AddItem oBendTangentEdge
    Next

    MsgBox "Bend extent edges highlighted in yellow."
End Sub

Private Function IsWithinBendEdge(oBendEdge As Edge, TangentEdge As Edge) As Boolean
    Dim dPi As Double
    dPi = 4 * Atn(1)

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Determine the lengths of the sides of the triangle defined by the end points
    ' of the bend edge and the center point of the tangent edge.
    Dim oStartPoint As Point2d
    Set oStartPoint = oTG.CreatePoint2d(oBendEdge.StartVertex.Point.x, oBendEdge.StartVertex.Point.Y)
    Dim oEndPoint As Point2d
    Set oEndPoint = oTG.CreatePoint2d(oBendEdge.StopVertex.Point.x, oBendEdge.StopVertex.Point.Y)
    Dim oTangentPoint As Point2d
    Set oTangentPoint = oTG.CreatePoint2d((TangentEdge.StartVertex.Point.x + TangentEdge.StopVertex.Point.x) / 2, (TangentEdge.StartVertex.Point.Y + TangentEdge.StopVertex.Point.Y) / 2)
    Dim dBendLength As Double
    dBendLength = oStartPoint.DistanceTo(oEndPoint)
    Dim dStartLength As Double
    dStartLength = oStartPoint.DistanceTo(oTangentPoint)
    Dim dEndLength As Double
    dEndLength = oEndPoint.DistanceTo(oTangentPoint)

    ' Compute the angle from the start point to the tangent midpoint.
    Dim dStartAngle As Double
    dStartAngle = ArcCos((dStartLength ^ 2 + dBendLength ^ 2 - dEndLength ^ 2) / (2 * dStartLength * dBendLength))

    ' Check that it is less than 90 deg.
    If dStartAngle > dPi / 2 Then
        IsWithinBendEdge = False
        Exit Function
    End If

    ' Compute the angle from the end point to the tangent midpoint.
    Dim dEndAngle As Double
    dEndAngle = ArcCos((dEndLength ^ 2 + dBendLength ^ 2 - dStartLength ^ 2) / (2 * dEndLength * dBendLength))

    ' Check that it is less than 90 deg.
    If dEndAngle > dPi / 2 Then
        IsWithinBendEdge = False
        Exit Function
    End If

    IsWithinBendEdge = True
End Function

Private Function ArcCos(x As Double) As Double
    Dim dPi As Double
    dPi = 4 * Atn(1)

    If x = 1 Then
        ArcCos = 0
    ElseIf Abs((Abs(x) - 1)) < 0.000001 Then
        ArcCos = dPi
    Else
        ArcCos = Atn(-x / Sqr(-x * x + 1)) + 2 * (dPi / 4)
    End If
End Function

Private Function IsBendEdge(oEdge As Edge, oFlatPattern As FlatPattern) As Boolean
    ' Return False if the input edge is not a wire edge.
    Dim oWire As Wire
    Set oWire = oEdge.Wire

    If oWire Is Nothing Then
        IsBendEdge = False
        Exit Function
    End If

    Dim oAllBendEdges As EdgeCollection
    Set oAllBendEdges = ThisApplication.TransientObjects.CreateEdgeCollection

    Dim oTempEdge As Edge

    ' Get all Bend UP edges on top face
    Dim oTopFaceBendUpEdges As Edges
    Set oTopFaceBendUpEdges = oFlatPattern.GetEdgesOfType(kBendUpFlatPatternEdge, True)
    For Each oTempEdge In oTopFaceBendUpEdges
        oAllBendEdges.Add oTempEdge
    Next

    ' Get all Bend DOWN edges on top face
    Dim oTopFaceBendDownEdges As Edges
    Set oTopFaceBendDownEdges = oFlatPattern.GetEdgesOfType(kBendDownFlatPatternEdge, True)
    For Each oTempEdge In oTopFaceBendDownEdges
        oAllBendEdges.Add oTempEdge
    Next

    ' Get all Bend UP edges on bottom face
    Dim oBottomFaceBendUpEdges As Edges
    Set oBottomFaceBendUpEdges = oFlatPattern.GetEdgesOfType(kBendUpFlatPatternEdge, False)
    For Each oTempEdge In oBottomFaceBendUpEdges
        oAllBendEdges.Add oTempEdge
    Next

    ' Get all Bend DOWN edges on bottom face
    Dim oBottomFaceBendDownEdges As Edges
    Set oBottomFaceBendDownEdges = oFlatPattern.GetEdgesOfType(kBendDownFlatPatternEdge, False)
    For Each oTempEdge In oBottomFaceBendDownEdges
        oAllBendEdges.Add oTempEdge
    Next

     ' Check if the input edge is a bend edge
    For Each oTempEdge In oAllBendEdges
        If oTempEdge Is oEdge Then
            IsBendEdge = True
            Exit Function
        End If
    Next

    IsBendEdge = False
End Function
```
