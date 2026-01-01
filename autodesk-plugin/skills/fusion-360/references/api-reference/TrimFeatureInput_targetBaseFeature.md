# TrimFeatureInput.targetBaseFeature Property

Parent Object: [TrimFeatureInput](TrimFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeatureInput\_var" is a variable referencing a TrimFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = trimFeatureInput_var.targetBaseFeature  # Set the value of the property. trimFeatureInput_var.targetBaseFeature = propertyValue ``` ```` |

"trimFeatureInput\_var" is a variable referencing a TrimFeatureInput object. ```` ``` #include <Fusion/Features/TrimFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = trimFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = trimFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |