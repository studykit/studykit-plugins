# SketchDimensions.AddEllipseMinorRadiusDimension

## Description

Demonstrates the SketchDimension.addEllipseMinorRadiusDimension method.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
def demo_Dimension_addEllipseMinorRadiusDimension(sketch: adsk.fusion.Sketch):
    centerPoint = adsk.core.Point3D.create(0, 0, 0)
    majorAxisPoint = adsk.core.Point3D.create(10, 0, 0)
    throughPoint = adsk.core.Point3D.create(5, 4, 0)

    # Create an ellipse and text point for parameters
    ellipse = sketch.sketchCurves.sketchEllipses.add(centerPoint, majorAxisPoint, throughPoint)
    textPoint = adsk.core.Point3D.create(12, 2, 0)

    # Create the ellipse
    dim = sketch.sketchDimensions
    minorRadiusDimension = dim.addEllipseMinorRadiusDimension(ellipse, textPoint)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |