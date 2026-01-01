# RuledSurfaceFeatureInput.targetBaseFeature Property

Parent Object: [RuledSurfaceFeatureInput](RuledSurfaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = ruledSurfaceFeatureInput_var.targetBaseFeature  # Set the value of the property. ruledSurfaceFeatureInput_var.targetBaseFeature = propertyValue ``` ```` |

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object. ```` ``` #include <Fusion/Features/RuledSurfaceFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = ruledSurfaceFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = ruledSurfaceFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |