# Client Graphics - Vertex Color by Z Height

## Description

This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub ZHeightColors()
    ' Get the surface body from the active document.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument
    Dim oSurfBody As SurfaceBody
    Set oSurfBody = oPartDoc.ComponentDefinition.SurfaceBodies.Item(1)
    Set oSurfBody = oPartDoc.ComponentDefinitions.Item(1).SurfaceBodies.Item(1)

    ' Delete the graphics data set and client graphics, if they exist.
    Dim oDataSets As GraphicsDataSets
    On Error Resume Next
    Set oDataSets = oPartDoc.GraphicsDataSetsCollection.Item("MyTest")
    If Err.Number = 0 Then
        oDataSets.Delete
        oPartDoc.ComponentDefinition.ClientGraphicsCollection.Item("MyTest").Delete
        oSurfBody.Visible = True
        ThisApplication.ActiveView.Update
        Exit Sub
    End If
    On Error GoTo 0

    ' Determine the highest tolerance of the existing facet sets.
    Dim ToleranceCount As Long
    Dim ExistingTolerances() As Double
    Call oSurfBody.GetExistingFacetTolerances(ToleranceCount, ExistingTolerances)

    Dim i As Long
    Dim BestTolerance As Double
    For i = 0 To ToleranceCount - 1
        If i = 0 Then
            BestTolerance = ExistingTolerances(i)
        ElseIf ExistingTolerances(i) < BestTolerance Then
            BestTolerance = ExistingTolerances(i)
        End If
    Next

    ' Get a set of existing facets.
    Dim iVertexCount As Long
    Dim iFacetCount As Long
    Dim adVertexCoords() As Double
    Dim adNormalVectors() As Double
    Dim aiVertexIndices() As Long
    Call oSurfBody.GetExistingFacets(BestTolerance, iVertexCount, iFacetCount, _
                                    adVertexCoords, adNormalVectors, aiVertexIndices)

    ' Start a transaction.
    Dim oTrans As Transaction
    Set oTrans = ThisApplication.TransactionManager.StartTransaction(oPartDoc, "Z Height Colors")

    ' Create the graphics data sets collection.
    Set oDataSets = oPartDoc.GraphicsDataSetsCollection.Add("MyTest")

    ' Create the coordinate set and set it using the coordinates from the facets.
    Dim oGraphicsCoordSet As GraphicsCoordinateSet
    Set oGraphicsCoordSet = oDataSets.CreateCoordinateSet(1)
    Call oGraphicsCoordSet.PutCoordinates(adVertexCoords)

    ' Create the index set and set it using the indices from the facets.
    Dim oGraphicsIndexSet As GraphicsIndexSet
    Set oGraphicsIndexSet = oDataSets.CreateIndexSet(2)
    Call oGraphicsIndexSet.PutIndices(aiVertexIndices)

    ' Create the normal set and set it using the normals from the facets.
    Dim oGraphicsNormalSet As GraphicsNormalSet
    Set oGraphicsNormalSet = oDataSets.CreateNormalSet(3)
    Call oGraphicsNormalSet.PutNormals(adNormalVectors)

    ' Determine the min-max range of the body in Z.
    Dim dMinZ As Double
    dMinZ = oSurfBody.RangeBox.MinPoint.Z
    Dim dMaxZ As Double
    dMaxZ = oSurfBody.RangeBox.MaxPoint.Z
    Dim dHeightDifference As Double
    dHeightDifference = dMaxZ - dMinZ

    ' Allocate the array that will contain the color information.
    ' This array contains RGB values for each vertex.
    Dim abtColors() As Byte
    ReDim abtColors(0 To iVertexCount * 3 - 1) As Byte

    ' Load the array with color information for each vertex.
    For i = 0 To iVertexCount - 1
        ' Get the Z height of the current vertex.
        Dim dZValue As Double
        dZValue = adVertexCoords(i * 3 + 2)

        ' Set the color information for the current vertex.  It's computed by
        ' determining the percentage of the total Z range of the body this vertex
        ' is within.  A color between red and blue is computed based on this percentage.
        ' Blue is at the minimum Z and Red is at the maximum Z with blending between.
        abtColors(i * 3) = ((dZValue - dMinZ) / dHeightDifference) * 255
        abtColors(i * 3 + 1) = 0
        abtColors(i * 3 + 2) = ((dMaxZ - dZValue) / dHeightDifference) * 255
    Next

    ' Create the color set and set it using the array of rgb values just created.
    Dim oGraphicsColorSet As GraphicsColorSet
    Set oGraphicsColorSet = oDataSets.CreateColorSet(4)
    Call oGraphicsColorSet.PutColors(abtColors)

    ' Create the client graphics collection.
    Dim oClientGraphics As ClientGraphics
    Set oClientGraphics = oPartDoc.ComponentDefinition.ClientGraphicsCollection.Add("MyTest")

    ' Create a graphics node.
    Dim oGraphicNode As GraphicsNode
    Set oGraphicNode = oClientGraphics.AddNode(1)

    ' Create the triangle graphics.
    Dim oTriangles As TriangleGraphics
    Set oTriangles = oGraphicNode.AddTriangleGraphics

    ' Set various prroperties of the triangle graphics.
    oTriangles.CoordinateSet = oGraphicsCoordSet
    oTriangles.CoordinateIndexSet = oGraphicsIndexSet
    oTriangles.NormalSet = oGraphicsNormalSet
    oTriangles.NormalBinding = kPerVertexNormals
    oTriangles.NormalIndexSet = oGraphicsIndexSet
    oTriangles.ColorSet = oGraphicsColorSet
    oTriangles.ColorBinding = kPerVertexColors
    oTriangles.ColorIndexSet = oGraphicsIndexSet

    ' Turn off the display of the body.
    oSurfBody.Visible = False

    ' End the transaction.
    oTrans.End

    ' Update the view.
    ThisApplication.ActiveView.Update
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |