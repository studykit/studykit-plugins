# SplitBodyFeatures.add Method

Parent Object: [SplitBodyFeatures](SplitBodyFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeatures.h>

## Description

Creates a new split body feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeatures\_var" is a variable referencing a [SplitBodyFeatures](SplitBodyFeatures.htm) object.```` ``` returnValue = splitBodyFeatures_var.add(input) ``` ```` |

"splitBodyFeatures\_var" is a variable referencing a [SplitBodyFeatures](SplitBodyFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SplitBodyFeature](SplitBodyFeature.htm) | Returns the newly created SplitBodyFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [SplitBodyFeatureInput](SplitBodyFeatureInput.htm) | A SplitBodyFeatureInput object that defines the desired split body feature. Use the createInput method to create a new SplitBodyFeatureInput object and then use methods on it (the SplitBodyFeatureInput object) to define the split body. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [splitBodyFeatures.add](splitBodyfeatures_add_Sample.htm) | Demonstrates the splitBodyFeatures.add method. |
| [Split Body Feature API Sample](SplitBodyFeatureSample_Sample.htm) | Demonstrates creating a new split body feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |