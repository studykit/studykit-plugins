# SketchArcs.addByThreePoints

## Description

Demonstrates the SketchArcs.addByThreePoints method.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
def demo_Arcs_addByThreePoints(sketch: adsk.fusion.Sketch):
    # Define three points
    startPoint = adsk.core.Point3D.create(0, 0, 0)
    alongPoint = adsk.core.Point3D.create(5, 0, 0)
    endPoint = adsk.core.Point3D.create(8, 7, 0)

    # Create an arc using three points along the arc.
    arcs = sketch.sketchCurves.sketchArcs
    arc = arcs.addByThreePoints(startPoint, alongPoint, endPoint)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |