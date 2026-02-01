# HoleFeatureInput.targetBaseFeature Property

Parent Object: [HoleFeatureInput](HoleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = holeFeatureInput_var.targetBaseFeature  # Set the value of the property. holeFeatureInput_var.targetBaseFeature = propertyValue ``` ```` |

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object. ```` ``` #include <Fusion/Features/HoleFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = holeFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = holeFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |