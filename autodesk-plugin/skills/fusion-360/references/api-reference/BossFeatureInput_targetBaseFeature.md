# BossFeatureInput.targetBaseFeature Property

Parent Object: [BossFeatureInput](BossFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureInput\_var" is a variable referencing a BossFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = bossFeatureInput_var.targetBaseFeature  # Set the value of the property. bossFeatureInput_var.targetBaseFeature = propertyValue ``` ```` |

"bossFeatureInput\_var" is a variable referencing a BossFeatureInput object. ```` ``` #include <Fusion/Plastic/BossFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = bossFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = bossFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |