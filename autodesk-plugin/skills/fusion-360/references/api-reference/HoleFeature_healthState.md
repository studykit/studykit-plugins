# HoleFeature.healthState Property

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Returns the current health state of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a HoleFeature object. |

"holeFeature\_var" is a variable referencing a HoleFeature object. ```` ``` #include <Fusion/Features/HoleFeature.h>  // Get the value of the property. FeatureHealthStates propertyValue = holeFeature_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |