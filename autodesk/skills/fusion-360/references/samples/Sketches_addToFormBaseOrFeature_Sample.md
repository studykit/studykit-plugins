# Sketches.addToBaseOrFormFeature

## Description

Demonstrates the Sketches.addToBaseOrFormFeature method.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
def demo_Sketches_addToBaseOrFeature(rootComp: adsk.fusion.Design.rootComponent):
    # Create a base feature
    baseFeats = rootComp.features.baseFeatures
    targetBaseOrFormFeature  = baseFeats.add()

    # To make changes to a base feature, it must be in an edit state.
    targetBaseOrFormFeature.startEdit()

    # Create a sketch in the base feature on the XY base plane.
    sketches = rootComp.sketches
    includeFaceEdges = True
    sketch = sketches.addToBaseOrFormFeature(rootComp.xYConstructionPlane, targetBaseOrFormFeature, includeFaceEdges)

    # Exit from the base Feature.
    targetBaseOrFormFeature.finishEdit()
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |