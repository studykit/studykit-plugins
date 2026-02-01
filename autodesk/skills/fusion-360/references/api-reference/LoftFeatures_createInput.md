# LoftFeatures.createInput Method

Parent Object: [LoftFeatures](LoftFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatures.h>

## Description

Creates a LoftFeatureInput object. Use properties and methods on the returned LoftFeatureInput object to provide the required input to create a loft feature. The LoftFeatureInput object can then be used as input to the add method to create the loft feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatures\_var" is a variable referencing a [LoftFeatures](LoftFeatures.htm) object.```` ``` returnValue = loftFeatures_var.createInput(operation) ``` ```` |

"loftFeatures\_var" is a variable referencing a [LoftFeatures](LoftFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LoftFeatureInput](LoftFeatureInput.htm) | Returns the newly created LoftFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| operation | [FeatureOperations](FeatureOperations.htm) | The feature operation to perform. |

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