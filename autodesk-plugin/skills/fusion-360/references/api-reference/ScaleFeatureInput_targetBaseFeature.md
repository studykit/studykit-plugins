# ScaleFeatureInput.targetBaseFeature Property

Parent Object: [ScaleFeatureInput](ScaleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatureInput\_var" is a variable referencing a ScaleFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = scaleFeatureInput_var.targetBaseFeature  # Set the value of the property. scaleFeatureInput_var.targetBaseFeature = propertyValue ``` ```` |

"scaleFeatureInput\_var" is a variable referencing a ScaleFeatureInput object. ```` ``` #include <Fusion/Features/ScaleFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = scaleFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = scaleFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |