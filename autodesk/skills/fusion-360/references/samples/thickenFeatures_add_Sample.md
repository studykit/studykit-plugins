# thickenFeatures.add

## Description

Demonstrates the thickenFeatures.add method.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
def demo_thickenFeatures_add(rootComp: adsk.fusion.Component):
    face = _ui.selectEntity('Select a face to thicken.', 'Faces').entity
    faces = adsk.core.ObjectCollection.create()
    faces.add(face)
    thickness = adsk.core.ValueInput.createByReal(1)
    isSymmetric = False
    operation = adsk.fusion.FeatureOperations.NewBodyFeatureOperation

    thickFeatures = rootComp.features.thickenFeatures
    input: adsk.fusion.ThickenFeatureInput = thickFeatures.createInput(faces, thickness, isSymmetric, operation)
    input.isChainSelection = True
    thickFeature = thickFeatures.add(input)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |