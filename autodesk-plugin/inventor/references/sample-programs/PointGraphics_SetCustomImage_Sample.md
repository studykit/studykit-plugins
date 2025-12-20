# Client graphics - image in point graphics

## Description

The following sample demonstrates creation of point client graphics with a custom image.

## Code Samples

* [VBA](#VBA)

The sample assumes that you've placed a MyImage.bmp in the C:\Temp\ directory.

|  |
| --- |
| Copy Code |

```
Public Sub ImageInPointClientGraphics()
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
        Dim oPointCoords(2) As Double
        oPointCoords(0) = 1
        oPointCoords(1) = 1
        oPointCoords(2) = 0

        ' Assign the points into the coordinate set.
        Call oCoordSet.PutCoordinates(oPointCoords)

        ' Create an image set
        Dim oImageSet As GraphicsImageSet
        Set oImageSet = oDataSets.CreateImageSet(2)

        Dim oImage As IPictureDisp
        Set oImage = LoadPicture("C:\Temp\MyImage.bmp")

        Call oImageSet.Add(1, oImage)

        ' Create the ClientGraphics object.
        Dim oClientGraphics As ClientGraphics
        Set oClientGraphics = oCompDef.ClientGraphicsCollection.Add("SampleGraphicsID")

        ' Create a new graphics node within the client graphics objects.
        Dim oPointNode As GraphicsNode
        Set oPointNode = oClientGraphics.AddNode(1)

        ' Create a PointGraphics object within the node.
        Dim oPointGraphics As PointGraphics
        Set oPointGraphics = oPointNode.AddPointGraphics

        ' Assign the coordinate set to the point graphics.
        oPointGraphics.CoordinateSet = oCoordSet

        ' Set a custom image
        Call oPointGraphics.SetCustomImage(oImageSet, 1)

        ' Update the view.
        ThisApplication.ActiveView.Update
    End If
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |