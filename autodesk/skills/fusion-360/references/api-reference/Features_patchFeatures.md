# Features.patchFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Patch features within the component and supports the creation of new Patch features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<PatchFeatures> propertyValue = features_var->patchFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [PatchFeatures](PatchFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [patchFeatures.add](patchFeatures_add_Sample.htm) | Demonstrates the patchFeatures.add method by creating a patch surface on the selected profile. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |