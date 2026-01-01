# Defer sketch updates

## Description

This sample demonstrates the sketch defer update functionality.

## Code Samples

* [VBA](#VBA)

To run this sample, have a 2d sketch active. Choosing 'Yes' in the dialog popped up by this sample defers the sketch update and creates the circle (approximated by 500 lines) much faster.

```
Public Sub DeferSketchUpdate()
   ' Check to make sure a sketch is open.
   If Not Typeof ThisApplication.ActiveEditObject Is Sketch Then
      MsgBox "A sketch must be active."
      Exit Sub
   End If

   ' Set a reference to the active sketch.
   Dim oSketch As Sketch
   Set oSketch = ThisApplication.ActiveEditObject

   ' Set a reference to the transient geometry collection.
   Dim oTransGeom As TransientGeometry
   Set oTransGeom = ThisApplication.TransientGeometry

   Dim bDeferUpdatesSet As Boolean
   bDeferUpdatesSet = False

   If MsgBox("Suppress sketch solve?", vbYesNo) = vbYes Then
      ' Defer sketch updates
      oSketch.DeferUpdates = True
      bDeferUpdatesSet = True
   End If

   ' Draw a circle using 500 lines.
   Dim dRadius As Double
   dRadius = 2
   Dim dAngle As Double
   dAngle = 0
   Dim i As Long
   For i = 0 To 499
      Dim oPt1 As Point2d
      Set oPt1 = oTransGeom.CreatePoint2d(dRadius * Cos(dAngle), dRadius * Sin(dAngle))

      dAngle = dAngle + (3.14159265358979 / 250)

      Dim oPt2 As Point2d
      Set oPt2 = oTransGeom.CreatePoint2d(dRadius * Cos(dAngle), dRadius * Sin(dAngle))

      Dim oLine As SketchLine
      Set oLine = oSketch.SketchLines.AddByTwoPoints(oPt1, oPt2)

   Next

   If bDeferUpdatesSet = True Then
      ' Unset defer updates
      oSketch.DeferUpdates = False 'A full sketch solve occurs
   End If
End Sub
```
