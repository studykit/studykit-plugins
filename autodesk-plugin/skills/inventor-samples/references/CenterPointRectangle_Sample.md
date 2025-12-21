# Create Centerpoint Rectangles

## Description

Creates a new sketch containing rectangles created using the two new center point rectangle commands.

## Code Samples

* [VBA](#VBA)

To use this sample a part must be active.

```
Public Sub SketchCreation()
    ' Get the active part document.
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.ActiveDocument
    Dim partDef As PartComponentDefinition
    Set partDef = partDoc.ComponentDefinition

    ' Create a new sketch.
    Dim sketch As PlanarSketch
    Set sketch = partDef.Sketches.Add(partDef.WorkPlanes.Item(3))

    Dim tg As TransientGeometry
    Set tg = ThisApplication.TransientGeometry

    ' Draw rectangles by center point.
    Call sketch.SketchLines.AddAsTwoPointCenteredRectangle(tg.CreatePoint2d(0, 0), tg.CreatePoint2d(8, 3))
    Call sketch.SketchLines.AddAsThreePointCenteredRectangle(tg.CreatePoint2d(20, 0), tg.CreatePoint2d(28, 3), tg.CreatePoint2d(24, 9))

    ThisApplication.ActiveView.Fit
End Sub
```
