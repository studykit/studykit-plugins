# TrimFeatures.add Method

Parent Object: [TrimFeatures](TrimFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeatures.h>

## Description

Creates a new trim feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeatures\_var" is a variable referencing a [TrimFeatures](TrimFeatures.htm) object.```` ``` returnValue = trimFeatures_var.add(input) ``` ```` |

"trimFeatures\_var" is a variable referencing a [TrimFeatures](TrimFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TrimFeature](TrimFeature.htm) | Returns the newly created TrimFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [TrimFeatureInput](TrimFeatureInput.htm) | A TrimFeatureInput object that defines the desired trim feature. Use the createInput method to create a new TrimFeatureInput object and then use methods on it (the TrimFeatureInput object) to define the trim feature. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [trimFeatures.add](trimFeatures_add_Sample.htm) | Demonstrates the trimFeatures.add method. |
| [Trim Feature API Sample](TrimFeatureSample_Sample.htm) | Demonstrates creating a new trim feature. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |