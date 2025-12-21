# Client graphics texture-based color mapping

## Description

This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors.

## Code Samples

* [VBA](#VBA)

To operate: 1. Open a part 2. Run Demo - it should show discrete bands moving across the model 3. Click on any of the other "convenience functions" and hit F5 to exercise them.

|  |
| --- |
| Copy Code |

```
Dim lastOffset As Double
Dim mapperType As Integer

'convenience "links"
Sub Demo()
    ThisApplication.ActiveView.DisplayMode = kWireframeRendering
    Call OffsetSurfaceBy(0#)
    Call UpdateValues(1 / 1.01, 0, 30)
    Call UpdateValues(1, -0.01, 20)
    Call UpdateValues(1, 0.01, 20)
    Call UpdateValues(1 / 1.01, 0, 50)
    Call UpdateValues(1, -0.01, 20)
    Call UpdateValues(1, 0.01, 20)
    Call UpdateValues(1 * 1.01, 0, 50)
End Sub

Sub narrowBands()
    Call UpdateValues(1 / 1.01, 0, 1)
End Sub

Sub widenBands()
    Call UpdateValues(1 * 1.01, 0, 1)
End Sub

Sub slideBandsUp()
    Call UpdateValues(1, 0.01, 1)
End Sub

Sub slideBandsDown()
    Call UpdateValues(1, -0.01, 1)
End Sub

Sub setContinuousMode()
    mapperType = 1
    Call OffsetSurfaceBy(0#)
End Sub

Sub setDiscreteMode()
    mapperType = 0
    Call OffsetSurfaceBy(0#)
End Sub

'internal functions
'randomly change colors in ColorMapper
Sub UpdateColors()
    Dim oDoc As Document
    Set oDoc = ThisApplication.ActiveDocument

    Dim oDataSets As GraphicsDataSets
    Set oDataSets = oDoc.GraphicsDataSetsCollection.Item("CG_Test")

    Dim oCompDef As ComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    Dim oClientGraphics As ClientGraphics
    Set oClientGraphics = oCompDef.ClientGraphicsCollection.Item("CG_Test")

    Dim oGraphicsNode As GraphicsNode
    Set oGraphicsNode = oClientGraphics.ItemById(100)

    Dim oTriangleSet As TriangleGraphics
    Set oTriangleSet = oGraphicsNode.Item(1)
    Dim oColorMapper As GraphicsColorMapper
    Set oColorMapper = oTriangleSet.ColorMapper

    For i = 1 To 100
        Dim cmColors() As Byte
        Call oColorMapper.GetColors(cmColors)
        For j = 0 To oColorMapper.ColorCount * 3 - 1
            cmColors(j) = 255 * Rnd() * i / 100#
        Next
        Call oColorMapper.PutColors(cmColors)
        ThisApplication.ActiveView.Update
    Next
End Sub

'change values in ColorMapper
Sub UpdateValues(factor As Double, offset As Double, count As Integer)
    Dim oDoc As Document
    Set oDoc = ThisApplication.ActiveDocument

    Dim oDataSets As GraphicsDataSets
    Set oDataSets = oDoc.GraphicsDataSetsCollection.Item("CG_Test")

    Dim oCompDef As ComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    Dim oClientGraphics As ClientGraphics
    Set oClientGraphics = oCompDef.ClientGraphicsCollection.Item("CG_Test")

    Dim oGraphicsNode As GraphicsNode
    Set oGraphicsNode = oClientGraphics.ItemById(100)

    Dim oTriangleSet As TriangleGraphics
    Set oTriangleSet = oGraphicsNode.Item(1)
    Dim oColorMapper As GraphicsColorMapper
    Set oColorMapper = oTriangleSet.ColorMapper

    For i = 1 To count
        Dim v() As Double
        Call oColorMapper.GetValues(v)
        Dim vMid As Double
        vMid = v(oColorMapper.ValueCount / 2)
        For j = 0 To oColorMapper.ValueCount - 1
            v(j) = (v(j) - vMid) * factor + vMid + offset * (v(oColorMapper.ValueCount - 1) - v(0))
        Next
        Call oColorMapper.PutValues(v)
        ThisApplication.ActiveView.Update
    Next
End Sub

Function min(a, b)
    min = a
    If (b < a) Then
        min = b
    End If
End Function

Function max(a, b)
    max = a
    If (b > a) Then
        max = b
    End If
End Function

'display part thickness by adding display of surfaces offset by given distance --
'wherever they stick through the part, it's thinner than that distance at that point
Public Sub OffsetSurfaceBy(offset As Double)
    ' Get the surface body from the active document.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument
    Dim oSurfBody As SurfaceBody
    Set oSurfBody = oPartDoc.ComponentDefinition.SurfaceBodies.Item(1)
    Set oSurfBody = oPartDoc.ComponentDefinitions.Item(1).SurfaceBodies.Item(1)

    ' Delete the graphics data set and client graphics, if they exist.
    Dim oDataSets As GraphicsDataSets
    On Error Resume Next
    Set oDataSets = oPartDoc.GraphicsDataSetsCollection.Item("CG_Test")
    If Err.Number = 0 Then
        oDataSets.Delete
        oPartDoc.ComponentDefinition.ClientGraphicsCollection.Item("CG_Test").Delete
        oSurfBody.Visible = True
        ThisApplication.ActiveView.Update
    End If
    On Error GoTo 0

'    If offset = 0 Then
'        Exit Sub
'    End If

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

    ' Offset vertices by given distance along anti-normals
    For i = 0 To (iVertexCount * 3 - 1)
        adVertexCoords(i) = adVertexCoords(i) - adNormalVectors(i) * offset
    Next

    ' Start a transaction.
    Dim oTrans As Transaction
    Set oTrans = ThisApplication.TransactionManager.StartTransaction(oPartDoc, "Z Height Colors")

    ' Create the graphics data sets collection.
    Set oDataSets = oPartDoc.GraphicsDataSetsCollection.Add("CG_Test")

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

    ' Allocate the array that will contain the color information.
    ' This array contains RGB values for each vertex.
    Dim abtColors() As Byte
    ReDim abtColors(0 To iVertexCount * 3 - 1) As Byte

    ' Load the array with color information for each vertex.
    For i = 0 To iVertexCount - 1
        ' Set the color information for the current vertex.
        ' currently, all vertices are a constant color, but ...
        abtColors(i * 3) = 200
        abtColors(i * 3 + 1) = 0
        abtColors(i * 3 + 2) = 0
    Next

    ' Create the color set and set it using the array of rgb values just created.
    Dim oGraphicsColorSet As GraphicsColorSet
    Set oGraphicsColorSet = oDataSets.CreateColorSet(4)
    Call oGraphicsColorSet.PutColors(abtColors)

    ' Create a scalar data texture coordinate set representing distance from origin
    Dim oTCSet As GraphicsTextureCoordinateSet
    Set oTCSet = oDataSets.CreateTextureCoordinateSet(5)
    Dim tc() As Double
    ReDim tc(1 To iVertexCount) As Double
    Dim tcMax As Double
    tcMax = 0
    Dim tcMin As Double
    tcMin = 1000000#
    For i = 1 To iVertexCount
        tc(i) = Sqr(adVertexCoords(3 * (i - 1)) * adVertexCoords(3 * (i - 1)) + adVertexCoords(3 * (i - 1) + 1) * adVertexCoords(3 * (i - 1) + 1) + adVertexCoords(3 * (i - 1) + 2) * adVertexCoords(3 * (i - 1) + 2))
        tcMin = min(tcMin, tc(i))
        tcMax = max(tcMax, tc(i))
    Next
    Call oTCSet.PutCoordinates(tc)

    ' Create the client graphics collection.
    Dim oClientGraphics As ClientGraphics
    Set oClientGraphics = oPartDoc.ComponentDefinition.ClientGraphicsCollection.Add("CG_Test")

    ' Create a graphics node.
    Dim oGraphicNode As GraphicsNode
    Set oGraphicNode = oClientGraphics.AddNode(100)

    ' Create the triangle graphics.
    Dim oTriangles As TriangleGraphics
    Set oTriangles = oGraphicNode.AddTriangleGraphics

    '============================================

    Dim oColorMapper As GraphicsColorMapper
    Set oColorMapper = oDataSets.CreateColorMapper

    '============================================

    'construct ColorMapper:
    '  black - red - orange - yellow - green - cyan - blue - magenta - black
    '      minV                          ...                        maxV
    Dim nColors As Integer
    nColors = 9

    Dim cmColors() As Byte
    ReDim cmColors(1 To nColors * 3) As Byte
    For i = 1 To nColors * 3
        cmColors(i) = 0
    Next
    'black
    cmColors(4) = 255       'red
    cmColors(7) = 255       'orange
    cmColors(7 + 1) = 125
    cmColors(10) = 255      'yellow
    cmColors(10 + 1) = 255
    cmColors(13 + 1) = 255  'green
    cmColors(16 + 1) = 255  'cyan
    cmColors(16 + 2) = 255
    cmColors(19 + 2) = 255  'blue
    cmColors(22) = 255      'magenta
    cmColors(22 + 2) = 255
    'black

    Dim nValues As Integer
    If (mapperType = 0) Then
        nValues = nColors - 1   'discrete value boundaries
    Else
        nValues = nColors       'continuous value points
    End If

    Dim cmValues() As Double
    ReDim cmValues(1 To nValues) As Double
    For i = 1 To nValues
        cmValues(i) = tcMin + (tcMax - tcMin) * (i - 1#) / (nValues - 1#)
    Next

    '============================================

    Call oColorMapper.PutColors(cmColors)
    Call oColorMapper.PutValues(cmValues)

    ' Set various properties of the triangle graphics.
    oTriangles.CoordinateSet = oGraphicsCoordSet
    oTriangles.CoordinateIndexSet = oGraphicsIndexSet
    oTriangles.NormalSet = oGraphicsNormalSet
    oTriangles.NormalBinding = kPerVertexNormals
    oTriangles.NormalIndexSet = oGraphicsIndexSet
'    oTriangles.ColorSet = oGraphicsColorSet
'    oTriangles.ColorBinding = kPerVertexColors
'    oTriangles.ColorIndexSet = oGraphicsIndexSet
    oTriangles.TextureCoordinateSet = oTCSet
    oTriangles.TextureCoordinateIndexSet = oGraphicsIndexSet
    oTriangles.ColorMapper = oColorMapper

    ' End the transaction.
    oTrans.End

    ' Update the view.
    ThisApplication.ActiveView.Update
End Sub

Public Sub increaseOffset()
    lastOffset = lastOffset * 1.1
    Dim offset As Double
    offset = lastOffset
    Call OffsetSurfaceBy(offset)
End Sub

Public Sub DecreaseOffset()
    lastOffset = lastOffset * 0.9
    Dim offset As Double
    offset = lastOffset
    Call OffsetSurfaceBy(offset)
End Sub

Public Sub OffsetSurface()
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    Dim lenunits As UnitsTypeEnum
    lenunits = oPartDoc.UnitsOfMeasure.LengthUnits
    Dim unitscale As Double
    Dim unitname As String
    If lenunits = kInchLengthUnits Then
        unitscale = 2.54
        unitname = "inches"
    Else
    If lenunits = kMillimeterLengthUnits Then
        unitscale = 0.1
        unitname = "millimeters"
    Else
    If lenunits = kCentimeterLengthUnits Then
        unitscale = 1#
        unitname = "centimeters"
    End If
    End If
    End If

    Dim offset As Double
    offset = 0
    On Error Resume Next
    offset = InputBox("Enter offset (in " + unitname + "):", "Offset", lastOffset / unitscale)
    On Error GoTo 0

    lastOffset = offset * unitscale

    Call OffsetSurfaceBy(lastOffset)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |