# ExtrudeFeatureInput.targetBaseFeature Property

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = extrudeFeatureInput_var.targetBaseFeature  # Set the value of the property. extrudeFeatureInput_var.targetBaseFeature = propertyValue ``` ```` |

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object. ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = extrudeFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = extrudeFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BaseFeature Sample](BaseFeatureSample_Sample.htm) | Creates a new base feature. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |