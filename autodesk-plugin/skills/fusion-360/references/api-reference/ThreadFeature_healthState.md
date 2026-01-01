# ThreadFeature.healthState Property

Parent Object: [ThreadFeature](ThreadFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeature.h>

## Description

Returns the current health state of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeature\_var" is a variable referencing a ThreadFeature object. |

"threadFeature\_var" is a variable referencing a ThreadFeature object. ```` ``` #include <Fusion/Features/ThreadFeature.h>  // Get the value of the property. FeatureHealthStates propertyValue = threadFeature_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |