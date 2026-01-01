# ScaleFeatures.add Method

Parent Object: [ScaleFeatures](ScaleFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatures.h>

## Description

Creates a new scale feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatures\_var" is a variable referencing a [ScaleFeatures](ScaleFeatures.htm) object.```` ``` returnValue = scaleFeatures_var.add(input) ``` ```` |

"scaleFeatures\_var" is a variable referencing a [ScaleFeatures](ScaleFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ScaleFeature](ScaleFeature.htm) | Returns the newly created ScaleFeature object or null if the creation failed. Returns nothing in the case where the feature is non-parametric. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ScaleFeatureInput](ScaleFeatureInput.htm) | A ScaleFeatureInput object that defines the desired scale. Use the createInput method to create a new ScaleFeatureInput object and then use methods on it (the ScaleFeatureInput object) to define the scale. |

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