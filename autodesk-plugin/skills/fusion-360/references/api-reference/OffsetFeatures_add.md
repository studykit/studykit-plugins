# OffsetFeatures.add Method

Parent Object: [OffsetFeatures](OffsetFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeatures.h>

## Description

Creates a new offset feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeatures\_var" is a variable referencing an [OffsetFeatures](OffsetFeatures.htm) object.```` ``` returnValue = offsetFeatures_var.add(input) ``` ```` |

"offsetFeatures\_var" is a variable referencing an [OffsetFeatures](OffsetFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OffsetFeature](OffsetFeature.htm) | Returns the newly created OffsetFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [OffsetFeatureInput](OffsetFeatureInput.htm) | A FeatureInput object that defines the desired offset feature. Use the createInput method to create a new OffsetFeatureInput object and then use methods on it (the OffsetFeatureInput object) to define the offset feature. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [offsetFeatures.add](offsetFeatures_add_Sample.htm) | Demonstrates the offsetFeatures.add method. This is the equivalent of the Offset command in the SURFACE tab. |
| [Offset Feature API Sample](OffsetFeatureSample_Sample.htm) | Demonstrates creating a new offset feature |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |