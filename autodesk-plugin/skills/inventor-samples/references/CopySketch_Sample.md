# Copy a sketch

## Description

This sample demonstrates copying the contents of a sketch into another sketch via the API.

## Code Samples

* [VBA](#VBA)

Before running the sample, have a part document open that contains a sketch with some sketch entities in it.

|  |
| --- |
| Copy Code |

```
Public Sub CopySketch()
    ' Set a reference to the active document.
    ' This assumes a part document is active.
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Set a reference to the component definition.
    Dim oDef As PartComponentDefinition
    Set oDef = oDoc.ComponentDefinition

    ' Set a reference to the first sketch in the part.
    Dim oSketchToCopy As PlanarSketch
    Set oSketchToCopy = oDef.Sketches.Item(1)

    ' Select the sketch to copy.
    Call oDoc.SelectSet.Clear
    Call oDoc.SelectSet.Select(oSketchToCopy)

    ' Execute the copy command.
    Dim oCopyControlDef As ControlDefinition
    Set oCopyControlDef = ThisApplication.CommandManager.ControlDefinitions.Item("AppCopyCmd")
    oCopyControlDef.Execute

    ' Create a new sketch on the XY plane.
    Dim oNewSketch As PlanarSketch
    Set oNewSketch = oDef.Sketches.Add(oDef.WorkPlanes.Item(3))

    ' Put the sketch in edit mode.
    oNewSketch.Edit

    ' Execute the paste command.
    Dim oPasteControlDef As ControlDefinition
    Set oPasteControlDef = ThisApplication.CommandManager.ControlDefinitions.Item("AppPasteCmd")
    oPasteControlDef.Execute

    Dim oSketchEnts As ObjectCollection
    Set oSketchEnts = ThisApplication.TransientObjects.CreateObjectCollection

    Dim oSketchEnt As SketchEntity
    For Each oSketchEnt In oNewSketch.SketchEntities
        Call oSketchEnts.Add(oSketchEnt)
    Next

    ' Translate all sketch entities in the new sketch.
    Call oNewSketch.MoveSketchObjects(oSketchEnts, ThisApplication.TransientGeometry.CreateVector2d(1, 0))
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |