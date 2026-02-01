# filletFeatures.add

## Description

Demonstrates the filletFeatures.add method.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
def demo_filletFeatures_add(rootComp: adsk.fusion.Component):
    # Have an edge selected.
    edge = _ui.selectEntity('Select an edge', 'Edges').entity
    edgesToFillet = adsk.core.ObjectCollection.create()

    # Define the required input.
    edgesToFillet.add(edge)
    filletFeatures = rootComp.features.filletFeatures
    input = filletFeatures.createInput()
    radius = adsk.core.ValueInput.createByReal(2)
    isTangentChain = True

    input.edgeSetInputs.addConstantRadiusEdgeSet(edgesToFillet, radius, isTangentChain)

    # Create the fillet.
    filletFeature = filletFeatures.add(input)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |