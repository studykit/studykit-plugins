# SketchTextInput.setAsFitOnPath

## Description

Demoonstrates the SketchTextInput.setAsFitOnPath method.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
def demo_SketchTextInput_setAsFitOnPath(sketch: adsk.fusion.Sketch):
    texts = sketch.sketchTexts
    input = texts.createInput2('Autodesk', 0.5)
    path = sketch.sketchCurves.sketchArcs.addByThreePoints(adsk.core.Point3D.create(-10, 0, 0),
                                                          adsk.core.Point3D.create(-5, 3, 0),
                                                          adsk.core.Point3D.create(0, 0, 0))
    isAbovePath = False

    input.setAsFitOnPath(path, isAbovePath)
    texts.add(input)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |