# ReplaceFaceFeatureInput.targetBaseFeature Property

Parent Object: [ReplaceFaceFeatureInput](ReplaceFaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeatureInput\_var" is a variable referencing a ReplaceFaceFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = replaceFaceFeatureInput_var.targetBaseFeature  # Set the value of the property. replaceFaceFeatureInput_var.targetBaseFeature = propertyValue ``` ```` |

"replaceFaceFeatureInput\_var" is a variable referencing a ReplaceFaceFeatureInput object. ```` ``` #include <Fusion/Features/ReplaceFaceFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = replaceFaceFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = replaceFaceFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |