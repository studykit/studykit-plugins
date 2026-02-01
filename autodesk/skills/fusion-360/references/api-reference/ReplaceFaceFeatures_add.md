# ReplaceFaceFeatures.add Method

Parent Object: [ReplaceFaceFeatures](ReplaceFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeatures.h>

## Description

Creates a new replace face feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeatures\_var" is a variable referencing a [ReplaceFaceFeatures](ReplaceFaceFeatures.htm) object.```` ``` returnValue = replaceFaceFeatures_var.add(input) ``` ```` |

"replaceFaceFeatures\_var" is a variable referencing a [ReplaceFaceFeatures](ReplaceFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ReplaceFaceFeature](ReplaceFaceFeature.htm) | Returns the newly created ReplaceFaceFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ReplaceFaceFeatureInput](ReplaceFaceFeatureInput.htm) | A ReplaceFaceFeatureInput object that defines the desired replace face. Use the createInput method to create a new ReplaceFaceFeatureInput object and then use methods on it (the ReplaceFaceFeatureInput object) to define the replace face. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [replaceFaceFeatures.add](replaceFaceFeatures_add_Sample.htm) | Demonstrate the remove replaceFaceFeatures.add method. |
| [ReplaceFace Feature](ReplaceFaceFeatureSample_Sample.htm) | Demonstrates creating a new replaceface feature. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |