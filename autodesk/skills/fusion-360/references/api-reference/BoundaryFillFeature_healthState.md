# BoundaryFillFeature.healthState Property

Parent Object: [BoundaryFillFeature](BoundaryFillFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeature.h>

## Description

Returns the current health state of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object. |

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object. ```` ``` #include <Fusion/Features/BoundaryFillFeature.h>  // Get the value of the property. FeatureHealthStates propertyValue = boundaryFillFeature_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |