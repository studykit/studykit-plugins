# reverseNormalFeatures.add

## Description

Demonstrates the reverseNormalFeatures.add method.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
def demo_reverseNormalFeatures_add(rootComp: adsk.fusion.Component):
    selection: adsk.fusion.BRepBodies = _ui.selectEntity('Select body to reverse normal.', 'Bodies').entity
    bodies = adsk.core.ObjectCollection.create()
    bodies.add(selection)

    reverseNormalFeatures = rootComp.features.reverseNormalFeatures
    reverseNormal = reverseNormalFeatures.add(bodies)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |