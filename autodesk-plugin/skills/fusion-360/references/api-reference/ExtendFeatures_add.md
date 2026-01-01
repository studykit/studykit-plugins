# ExtendFeatures.add Method

Parent Object: [ExtendFeatures](ExtendFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeatures.h>

## Description

Creates a new extend feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeatures\_var" is a variable referencing an [ExtendFeatures](ExtendFeatures.htm) object.```` ``` returnValue = extendFeatures_var.add(input) ``` ```` |

"extendFeatures\_var" is a variable referencing an [ExtendFeatures](ExtendFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ExtendFeature](ExtendFeature.htm) | Returns the newly created ExtendFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ExtendFeatureInput](ExtendFeatureInput.htm) | An ExtendFeatureInput object that defines the desired extend feature. Use the createInput method to create a new ExtendFeatureInput object and then use methods on it (the ExtendFeatureInput object) to define the desired options for the extent feature. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [extendFeatures.add](extendFeatures_add_Sample.htm) | Demonstrates the extendFeatures.add method. To use this sample, have a design open that contains at least one surface body. When you run the sample, you will be prompted to select an open edge of the body. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |