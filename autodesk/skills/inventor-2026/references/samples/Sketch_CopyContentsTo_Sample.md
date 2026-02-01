# Copy sketch contents

## Description

This sample shows how to copy the contents of one sketch to another.

## Code Samples

* [VBA](#VBA)

```
Public Sub CopySketch()
    Dim oCmdMgr As CommandManager
    Set oCmdMgr = ThisApplication.CommandManager

    Dim oSourceSketch As Sketch
    Set oSourceSketch = oCmdMgr.Pick(kSketchObjectFilter, "Select source sketch")

    Dim oTargetSketch As Sketch
    Set oTargetSketch = oCmdMgr.Pick(kSketchObjectFilter, "Select target sketch")

    Call oSourceSketch.CopyContentsTo(oTargetSketch)
End Sub
```
