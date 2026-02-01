# Sketch Delete

## Description

This sample demonstrates deleting a sketch.

## Code Samples

* [VBA](#VBA)

To use this sample, have a part document open that contains a sketch named Sketch1. The sketch cannot have any dependents, or the delete will fail.

```
Public Sub DeleteSketch()
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

    ' Check to see if the sketch has any dependents.
    If oSketch.Dependents.Count > 0 Then
      MsgBox "Cannot delete a sketch with dependents."
    Else
      ' Delete the sketch.
      oSketch.Delete
    End If
End Sub
```
