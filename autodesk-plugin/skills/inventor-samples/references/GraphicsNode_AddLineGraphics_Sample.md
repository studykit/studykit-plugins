# Client Graphics - Line

## Description

This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub DrawCustomLines()
    Dim oDoc As Document
    Set oDoc = ThisApplication.ActiveDocument

    ' Set a reference to component definition of the active document.
    ' This assumes that a part or assembly document is active.
    Dim oCompDef As ComponentDefinition
    Set oCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Check to see if the test graphics data object already exists.
    ' If it does clean up by removing all associated of the client graphics
    ' from the document.  If it doesn't create it.
    On Error Resume Next
    Dim oGraphicsData As GraphicsDataSets
    Set oGraphicsData = oDoc.GraphicsDataSetsCollection.Item("SampleGraphicsID")
    If Err.Number = 0 Then
        On Error GoTo 0
        ' An existing client graphics object was successfully obtained so clean up.
        oGraphicsData.Delete
        oCompDef.ClientGraphicsCollection.Item("SampleGraphicsID").Delete

        ' update the display to see the results.
        ThisApplication.ActiveView.Update
    Else
        Err.Clear
        On Error GoTo 0

        ' Set a reference to the transient geometry object for user later.
        Dim oTransGeom As TransientGeometry
        Set oTransGeom = ThisApplication.TransientGeometry

        ' Create a graphics data set object.  This object contains all of the
        ' information used to define the graphics.
        Dim oDataSets As GraphicsDataSets
        Set oDataSets = oDoc.GraphicsDataSetsCollection.Add("SampleGraphicsID")

        ' Create a coordinate set.
        Dim oCoordSet As GraphicsCoordinateSet
        Set oCoordSet = oDataSets.CreateCoordinateSet(1)

        ' Create an array that contains coordinates that define a set
        ' of outwardly spiraling points.
        Dim oPointCoords(1 To 90) As Double
        Dim i As Long
        Dim dRadius As Double
        dRadius = 1
        Dim dAngle As Double
        For i = 0 To 29
            ' Define the X, Y, and Z components of the point.
            oPointCoords(i * 3 + 1) = dRadius * Cos(dAngle)
            oPointCoords(i * 3 + 2) = dRadius * Sin(dAngle)
            oPointCoords(i * 3 + 3) = i / 2

            ' Increment the angle and radius to create the spiral.
            dRadius = dRadius + 0.25
            dAngle = dAngle + (3.14159265358979 / 6)
        Next

        ' Assign the points into the coordinate set.
        Call oCoordSet.PutCoordinates(oPointCoords)

        ' Create the ClientGraphics object.
        Dim oClientGraphics As ClientGraphics
        Set oClientGraphics = oCompDef.ClientGraphicsCollection.Add("SampleGraphicsID")

        ' Create a new graphics node within the client graphics objects.
        Dim oLineNode As GraphicsNode
        Set oLineNode = oClientGraphics.AddNode(1)

        ' Create a LineGraphics object within the node.
        Dim oLineSet As LineGraphics
        Set oLineSet = oLineNode.AddLineGraphics

        ' Assign the coordinate set to the line graphics.
        oLineSet.CoordinateSet = oCoordSet

        ' Assign a color to the node using an existing appearance asset.
        Dim oAppearance As Asset
        Set oAppearance = oDoc.AppearanceAssets(1)

        oLineNode.Appearance = oAppearance

        ' Update the view to see the resulting spiral.
        ThisApplication.ActiveView.Update

        ' Create another graphics node for a line strip.
        Dim oLineStripNode As GraphicsNode
        Set oLineStripNode = oClientGraphics.AddNode(2)

        ' Create a LineStripGraphics object within the new node.
        Dim oLineStrip As LineStripGraphics
        Set oLineStrip = oLineStripNode.AddLineStripGraphics

        ' Assign the same coordinate set to the line strip.
        oLineStrip.CoordinateSet = oCoordSet

        ' Create a color set to use in defining a explicit color to the line strip.
        Dim oColorSet As GraphicsColorSet
        Set oColorSet = oDataSets.CreateColorSet(1)

        ' Add a single color to the set that is red.
        Call oColorSet.Add(1, 255, 0, 0)

        ' Assign the color set to the line strip.
        oLineStrip.ColorSet = oColorSet

        ' The two spirals are currently on top of each other so translate the
        ' new one in the x direction so they're side by side.
        Dim oMatrix As Matrix
        Set oMatrix = oLineStripNode.Transformation
        Call oMatrix.SetTranslation(oTransGeom.CreateVector(15, 0, 0))
        oLineStripNode.Transformation = oMatrix

        ' Update the view to see the resulting spiral.
        ThisApplication.ActiveView.Update
    End If
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |