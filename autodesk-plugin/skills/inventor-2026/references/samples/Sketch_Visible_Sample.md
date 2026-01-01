# Set Sketch Visibility

## Description

This sample demonstrates setting the visibility of a sketch.

## Code Samples

* [VBA](#VBA)

To use this sample have a part document open that contains at least one sketch.

```
Public Sub ToggleSketchVisibility()
    ' Set a reference to the Sketches collection.  This assumes
    ' that a part document containing a sketch is active.
    Dim oSketches As PlanarSketches
    Set oSketches = ThisApplication.ActiveDocument.ComponentDefinition.Sketches

    ' Get whether the sketch visibility should be turned on or off.
    Dim bVisibleOn As Boolean
    If MsgBox("Do you want to turn all sketches on?", vbYesNo + vbQuestion) = vbYes Then
        bVisibleOn = True
    Else
        bVisibleOn = False
    End If

    ' Iterate through all of the sketches and set their visibility.
    Dim oSketch As PlanarSketch
    For Each oSketch In oSketches
        If bVisibleOn Then
            oSketch.Visible = True
        Else
            oSketch.Visible = False
        End If
    Next
End Sub
```
