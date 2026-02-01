# GeometricConstraints.addVertical

## Description

Demonstrates the GeometricConstraints.addVertical method.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
def demo_GeometricConstraints_addVertical(sketch: adsk.fusion.Sketch):
    # Create a sketch line.
    line = sketch.sketchCurves.sketchLines.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0),
                                                          adsk.core.Point3D.create(0, 10, 0))

    # Add a vertical constraint to the sketch line.
    constraints = sketch.geometricConstraints
    verticalConstraint = constraints.addVertical(line)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |