# LoftFeatures.add Method

Parent Object: [LoftFeatures](LoftFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatures.h>

## Description

Creates a new loft feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatures\_var" is a variable referencing a [LoftFeatures](LoftFeatures.htm) object.```` ``` returnValue = loftFeatures_var.add(input) ``` ```` |

"loftFeatures\_var" is a variable referencing a [LoftFeatures](LoftFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LoftFeature](LoftFeature.htm) | Returns the newly created LoftFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [LoftFeatureInput](LoftFeatureInput.htm) | A LoftFeatureInput object that defines the desired loft feature. Use the createInput method to create a new LoftFeatureInput object and then use methods on it (the LoftFeatureInput object) to define the required input. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [loftFeatures.add](loftFeatures_add_Sample.htm) | Demonstrates the loftFeatures.add method. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |