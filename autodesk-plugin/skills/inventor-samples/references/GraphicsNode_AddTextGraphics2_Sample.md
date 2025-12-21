# Text Using Client Graphics (Multiple fonts and lines)

## Description

This sample demonstrates creating text using client graphics. It illustrates the more complex case of changes in font and more than one line.

## Code Samples

* [VBA](#VBA)

To run the sample have a part or assembly document open.

```
Public Sub ClientGraphicsTextMultipleFonts()
    ' Set a reference to the document.  This will work with
    ' either a part or assembly document.
    Dim oDoc As Document
    Set oDoc = ThisApplication.ActiveDocument

    ' Set a reference to the component definition.
    Dim oCompDef As ComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    ' Attempt to get the existing client graphics object.  If it exists
    ' delete it so the rest of the code can continue as if it never existed.
    Dim oClientGraphics As ClientGraphics
    On Error Resume Next
    Set oClientGraphics = oCompDef.ClientGraphicsCollection.Item("Text Test")
    If Err.Number = 0 Then
        oClientGraphics.Delete
    End If
    On Error GoTo 0
    ThisApplication.ActiveView.Update

    ' Create a new ClientGraphics object.
    Set oClientGraphics = oCompDef.ClientGraphicsCollection.Add("Text Test")

    ' Create a graphics node.
    Dim oNode As GraphicsNode
    Set oNode = oClientGraphics.AddNode(1)

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    Dim oModelAnchorPoint As Point
    Set oModelAnchorPoint = oTG.CreatePoint(50, 0, 0)

    ' Create several text graphics objects, one for each font change.  The anchor of the
    ' TextGraphics object defines the position of each text element relative to each other.
    ' Because they're all drawn with pixel scaling behavior these coordinates are in
    ' pixel space.  They all use the same point as input for the SetTransformBehavior call.
    ' This point is in model space and defines their anchor within the model.

    ' Draw the first character which is the diameter symbol.
    Dim oTextGraphics(1 To 4) As TextGraphics
    Set oTextGraphics(1) = oNode.AddTextGraphics
    oTextGraphics(1).Text = "n "

    ' Because this text will have pixel scaling behavior these coordinates are in pixel space.
    oTextGraphics(1).Anchor = oTG.CreatePoint(0, 0, 0)

    oTextGraphics(1).Font = "AIGDT"
    oTextGraphics(1).FontSize = 25
    oTextGraphics(1).HorizontalAlignment = kAlignTextLeft
    Call oTextGraphics(1).PutTextColor(0, 255, 255)
    oTextGraphics(1).VerticalAlignment = kAlignTextMiddle
    Call oTextGraphics(1).SetTransformBehavior(oModelAnchorPoint, kFrontFacingAndPixelScaling)
    Dim oBox As Box
    Set oBox = oTextGraphics(1).RangeBox

    ' Draw the next section of the string relative to the first section.
    Set oTextGraphics(2) = oNode.AddTextGraphics
    oTextGraphics(2).Text = "9.4 - 9.8"

    ' The range of the previous character is used to determine where to position
    ' the next string.  The range is returned in pixels.
    oTextGraphics(2).Anchor = oTG.CreatePoint(oModelAnchorPoint.X + oBox.MaxPoint.X, 0, 0)

    oTextGraphics(2).Font = "Arial"
    oTextGraphics(2).FontSize = 25
    oTextGraphics(2).HorizontalAlignment = kAlignTextLeft
    Call oTextGraphics(2).PutTextColor(0, 255, 255)
    oTextGraphics(2).VerticalAlignment = kAlignTextMiddle
    Call oTextGraphics(2).SetTransformBehavior(oModelAnchorPoint, kFrontFacingAndPixelScaling)

    ' Draw a depth symbol on the next line.
    Set oTextGraphics(3) = oNode.AddTextGraphics
    oTextGraphics(3).Text = "x "

    ' Using the range of the first text graphics determine the position for a string that
    ' is immediately below.  This defines the next line of text.
    oTextGraphics(3).Anchor = oTG.CreatePoint(oModelAnchorPoint.X + oBox.MinPoint.X, oBox.MinPoint.Y - ((oBox.MaxPoint.Y - oBox.MinPoint.Y) * 1.5), 0)
    oTextGraphics(3).Font = "AIGDT"
    oTextGraphics(3).FontSize = 25
    oTextGraphics(3).HorizontalAlignment = kAlignTextLeft
    Call oTextGraphics(3).PutTextColor(0, 255, 255)
    oTextGraphics(3).VerticalAlignment = kAlignTextMiddle
    Call oTextGraphics(3).SetTransformBehavior(oModelAnchorPoint, kFrontFacingAndPixelScaling)
    Set oBox = oTextGraphics(3).RangeBox

     ' Draw the last set of text.s
    Set oTextGraphics(4) = oNode.AddTextGraphics
    oTextGraphics(4).Text = "20"
    oTextGraphics(4).Anchor = oTG.CreatePoint(oModelAnchorPoint.X + oBox.MaxPoint.X, oTextGraphics(3).Anchor.Y, 0)
    oTextGraphics(4).Font = "Arial"
    oTextGraphics(4).FontSize = 25
    oTextGraphics(4).HorizontalAlignment = kAlignTextLeft
    Call oTextGraphics(4).PutTextColor(0, 255, 255)
    oTextGraphics(4).VerticalAlignment = kAlignTextMiddle
    Call oTextGraphics(4).SetTransformBehavior(oModelAnchorPoint, kFrontFacingAndPixelScaling)

    ' Update the view to see the text.
    ThisApplication.ActiveView.Update
End Sub
```
