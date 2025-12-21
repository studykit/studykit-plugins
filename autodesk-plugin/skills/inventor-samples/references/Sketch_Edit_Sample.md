# Sketch Open for Edit

## Description

This sample demonstrates opening a sketch for edit.

## Code Samples

* [VBA](#VBA)

To use this sample, have a part document open that contains a sketch named Sketch1.

```
Public Sub StartSketchEdit()
    ' Set a reference to the Sketches collection. This assumes
    ' that a part document containing a sketch is active.
    Dim oSketches As PlanarSketches
    Set oSketches = ThisApplication.ActiveDocument.ComponentDefinition.Sketches

    ' Get the sketch named "Sketch1".
    On Error Resume Next
    Dim oSketch As PlanarSketch
    Set oSketch = oSketches.Item("Sketch1")
    If Err Then
      MsgBox "A Sketch named ""Sketch1"" must exist."
      Exit Sub
    End If
    On Error GoTo 0

    ' Open the sketch for edit to allow the user to edit it.
    oSketch.Edit
End Sub
```
