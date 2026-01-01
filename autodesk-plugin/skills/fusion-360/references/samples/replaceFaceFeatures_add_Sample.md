# replaceFaceFeatures.add

## Description

Demonstrate the remove replaceFaceFeatures.add method.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
def demo_replaceFaceFeatures_add(rootComp: adsk.fusion.Component):
    sourceFace = _ui.selectEntity('Select a source face.', 'Faces').entity
    targetFace = _ui.selectEntity('Select a target face.', 'Faces').entity

    sourceFaces = adsk.core.ObjectCollection.create()
    sourceFaces.add(sourceFace)
    isTangentChain = False

    replaceFaceFeatures = rootComp.features.replaceFaceFeatures
    input = replaceFaceFeatures.createInput(sourceFaces, isTangentChain, targetFace)
    replaceFaceFeature = replaceFaceFeatures.add(input)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |