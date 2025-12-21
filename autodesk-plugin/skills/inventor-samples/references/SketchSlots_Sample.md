# Create slots in sketch.

## Description

This sample demonstrates several new methods to create sketch entities that represent slots. These are the equivalent to new sketch commands that were added in Inventor 2014.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateSlots()
    ' Create a new part.
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                  ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))
    Dim partDef As PartComponentDefinition
    Set partDef = partDoc.ComponentDefinition

    ' Create a 2D sketch on the X-Y plane.
    Dim sketch As PlanarSketch
    Set sketch = partDef.Sketches.Add(partDef.WorkPlanes.Item(3))

    Dim tg As TransientGeometry
    Set tg = ThisApplication.TransientGeometry

    Dim pi As Double
    pi = Atn(1) * 4

    Dim results As SketchEntitiesEnumerator
    Set results = sketch.AddArcSlotByCenterPointArc(tg.CreatePoint2d(0, 0), tg.CreatePoint2d(6, 0), pi / 2, 2)

    Set results = sketch.AddArcSlotByThreePointArc(tg.CreatePoint2d(15, 0), tg.CreatePoint2d(12.5, 2), _
                                                   tg.CreatePoint2d(10, 0), 2)

    Set results = sketch.AddStraightSlotByCenterToCenter(tg.CreatePoint2d(0, 10), tg.CreatePoint2d(6, 10), 2)

    Set results = sketch.AddStraightSlotByOverall(tg.CreatePoint2d(10, 10), tg.CreatePoint2d(16, 10), 2)

    ThisApplication.ActiveView.Fit
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |