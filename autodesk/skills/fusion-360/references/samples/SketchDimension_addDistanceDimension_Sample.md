# SketchDimensions.addDistanceDimension

## Description

Demonstrates the SketchDimension.addDistanceDimension method.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
def demo_Dimension_addDistanceDimension(sketch: adsk.fusion.Sketch):
    # Create points, orientation and text point for parameters
    pointOne = sketch.sketchPoints.add(adsk.core.Point3D.create(0, 0, 0))
    pointTwo = sketch.sketchPoints.add(adsk.core.Point3D.create(10, 10, 0))
    orientation = adsk.fusion.DimensionOrientations.AlignedDimensionOrientation
    textPoint = adsk.core.Point3D.create(5, 4, 0)

    # Create the circle based on the dimension
    dim = sketch.sketchDimensions
    distanceDimension = dim.addDistanceDimension(pointOne, pointTwo, orientation, textPoint)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |