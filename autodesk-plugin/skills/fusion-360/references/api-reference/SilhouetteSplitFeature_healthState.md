# SilhouetteSplitFeature.healthState Property

Parent Object: [SilhouetteSplitFeature](SilhouetteSplitFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeature.h>

## Description

Returns the current health state of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeature\_var" is a variable referencing a SilhouetteSplitFeature object. |

"silhouetteSplitFeature\_var" is a variable referencing a SilhouetteSplitFeature object. ```` ``` #include <Fusion/Features/SilhouetteSplitFeature.h>  // Get the value of the property. FeatureHealthStates propertyValue = silhouetteSplitFeature_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |