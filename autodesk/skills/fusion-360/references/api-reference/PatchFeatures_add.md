# PatchFeatures.add Method

Parent Object: [PatchFeatures](PatchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatures.h>

## Description

Creates a new patch feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatures\_var" is a variable referencing a [PatchFeatures](PatchFeatures.htm) object.```` ``` returnValue = patchFeatures_var.add(input) ``` ```` |

"patchFeatures\_var" is a variable referencing a [PatchFeatures](PatchFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PatchFeature](PatchFeature.htm) | Returns the newly created PatchFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [PatchFeatureInput](PatchFeatureInput.htm) | A PatchFeatureInput object that defines the desired patch feature. Use the createInput method to create a new PatchFeatureInput object and then use methods on it (the PatchFeatureInput object) to define the patch feature. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [patchFeatures.add](patchFeatures_add_Sample.htm) | Demonstrates the patchFeatures.add method by creating a patch surface on the selected profile. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |