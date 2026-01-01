# LoftFeatureInput.targetBaseFeature Property

Parent Object: [LoftFeatureInput](LoftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = loftFeatureInput_var.targetBaseFeature  # Set the value of the property. loftFeatureInput_var.targetBaseFeature = propertyValue ``` ```` |

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. ```` ``` #include <Fusion/Features/LoftFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = loftFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = loftFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |