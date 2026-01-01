# TorusFeature.healthState Property

Parent Object: [TorusFeature](TorusFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TorusFeature.h>

## Description

Returns the current health state of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torusFeature\_var" is a variable referencing a TorusFeature object. |

"torusFeature\_var" is a variable referencing a TorusFeature object. ```` ``` #include <Fusion/Features/TorusFeature.h>  // Get the value of the property. FeatureHealthStates propertyValue = torusFeature_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |