# ScaleFeatures.createInput Method

Parent Object: [ScaleFeatures](ScaleFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatures.h>

## Description

Creates a ScaleFeatureInput object. Use properties and methods on this object to define the scale you want to create and then use the Add method, passing in the ScaleFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatures\_var" is a variable referencing a [ScaleFeatures](ScaleFeatures.htm) object.```` ``` returnValue = scaleFeatures_var.createInput(inputEntities, point, scaleFactor) ``` ```` |

"scaleFeatures\_var" is a variable referencing a [ScaleFeatures](ScaleFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ScaleFeatureInput](ScaleFeatureInput.htm) | Returns the newly created ScaleFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputEntities | [ObjectCollection](ObjectCollection.htm) | This collection can contain sketches, BRep bodies and T-Spline bodies in parametric modeling. It can contain sketches, BRep bodies, T-Spline bodies, mesh bodies, root component and occurrences in non-parametric modeling. |
| point | [Base](Base.htm) | Input a point as reference to scale. This can be a BRepVertex, a SketchPoint or a ConstructionPoint. |
| scaleFactor | [ValueInput](ValueInput.htm) | The ValueInput object that defines the scale factor for uniform scale. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [scaleFeatures.add](scaleFeatures_add_Sample.htm) | Demonstrates the creation a scale feature. |
| [Scale Feature API Sample](ScaleFeatureSample_Sample.htm) | Demonstrates creating a new scale feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |