# PatchFeatureInput.targetBaseFeature Property

Parent Object: [PatchFeatureInput](PatchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = patchFeatureInput_var.targetBaseFeature  # Set the value of the property. patchFeatureInput_var.targetBaseFeature = propertyValue ``` ```` |

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object. ```` ``` #include <Fusion/Features/PatchFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = patchFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = patchFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |