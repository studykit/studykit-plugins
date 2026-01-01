# ScaleFeature.healthState Property

Parent Object: [ScaleFeature](ScaleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeature.h>

## Description

Returns the current health state of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeature\_var" is a variable referencing a ScaleFeature object. |

"scaleFeature\_var" is a variable referencing a ScaleFeature object. ```` ``` #include <Fusion/Features/ScaleFeature.h>  // Get the value of the property. FeatureHealthStates propertyValue = scaleFeature_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |