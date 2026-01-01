# ChamferFeatureInput.targetBaseFeature Property

Parent Object: [ChamferFeatureInput](ChamferFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatureInput\_var" is a variable referencing a ChamferFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = chamferFeatureInput_var.targetBaseFeature  # Set the value of the property. chamferFeatureInput_var.targetBaseFeature = propertyValue ``` ```` |

"chamferFeatureInput\_var" is a variable referencing a ChamferFeatureInput object. ```` ``` #include <Fusion/Features/ChamferFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = chamferFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = chamferFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |