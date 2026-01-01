# FullRoundFilletFeatureInput.targetBaseFeature Property

Parent Object: [FullRoundFilletFeatureInput](FullRoundFilletFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FullRoundFilletFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fullRoundFilletFeatureInput\_var" is a variable referencing a FullRoundFilletFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = fullRoundFilletFeatureInput_var.targetBaseFeature  # Set the value of the property. fullRoundFilletFeatureInput_var.targetBaseFeature = propertyValue ``` ```` |

"fullRoundFilletFeatureInput\_var" is a variable referencing a FullRoundFilletFeatureInput object. ```` ``` #include <Fusion/Features/FullRoundFilletFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = fullRoundFilletFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = fullRoundFilletFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |