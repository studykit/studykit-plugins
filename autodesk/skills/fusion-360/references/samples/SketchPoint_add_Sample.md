# SketchPoint.add

## Description

Demonstrates the SketchPoint.add method.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
def  demo_SketchPoint_add(sketch: adsk.fusion.Sketch):
    somePoint = adsk.core.Point3D.create(5, 4, 0)
    sketchPoints = sketch.sketchPoints
    point = sketchPoints.add(somePoint)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |