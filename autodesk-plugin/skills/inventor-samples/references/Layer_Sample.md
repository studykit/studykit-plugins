# Moving sketch entities to a new layer

## Description

This sample demonstrates the creation of a new layer and moving sketch entities onto this newly created layer.

## Code Samples

* [VBA](#VBA)

To run the sample, have a drawing document open. After running the sample, select the 'Edit Layers' command in the toolbar and turn on the layer named Custom Sketch Circles.

```
Public Sub Layer()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    'Set a reference to the drawing view.
    Dim oDraftView As DrawingView
    Set oDraftView = oDrawDoc.ActiveSheet.DrawingViews.AddDraftView(1#, "My Draft View")

    ' Set a reference to the sketch of the created draft view.
    Dim oSketch As DrawingSketch
    Set oSketch = oDraftView.Sketches.Item(1)

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw four sketch lines that form a rectangle
    Call oSketch.SketchLines.AddAsTwoPointRectangle(oTransGeom.CreatePoint2d(10, 10), _
                                                oTransGeom.CreatePoint2d(30, 30))

    ' Draw four sketch circles
    Dim oSketchCircles(1 To 4) As SketchCircle
    Set oSketchCircles(1) = oSketch.SketchCircles.AddByCenterRadius(oTransGeom.CreatePoint2d(12, 12), 1.5)
    Set oSketchCircles(2) = oSketch.SketchCircles.AddByCenterRadius(oTransGeom.CreatePoint2d(28, 12), 1.5)
    Set oSketchCircles(3) = oSketch.SketchCircles.AddByCenterRadius(oTransGeom.CreatePoint2d(12, 28), 1.5)
    Set oSketchCircles(4) = oSketch.SketchCircles.AddByCenterRadius(oTransGeom.CreatePoint2d(28, 28), 1.5)

    ' Create a new layer (as a copy of the 'Sketch Geometry' layer)
    ' to put the sketch circles in.
    Dim oNewLayer As Layer
    Set oNewLayer = oDrawDoc.StylesManager.Layers.Item("Sketch Geometry (ANSI)").Copy("Custom Sketch Circles")

    ' Set the LineType on the new layer to 'dashed'.
    oNewLayer.LineType = kDashedLineType

    'Put all the sketch circles on this layer
    oSketchCircles(1).Layer = oNewLayer
    oSketchCircles(2).Layer = oNewLayer
    oSketchCircles(3).Layer = oNewLayer
    oSketchCircles(4).Layer = oNewLayer

    ' Turn off the new layer
    oNewLayer.Visible = False

    ' Exit from editing the sketch.
    oSketch.ExitEdit
End Sub
```
