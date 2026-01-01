# ConstructionPoint.healthState Property

Parent Object: [ConstructionPoint](ConstructionPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPoint.h>

## Description

Returns the current health state of this construction point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPoint\_var" is a variable referencing a ConstructionPoint object. |

"constructionPoint\_var" is a variable referencing a ConstructionPoint object. ```` ``` #include <Fusion/Construction/ConstructionPoint.h>  // Get the value of the property. FeatureHealthStates propertyValue = constructionPoint_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Point API Sample](ConstructionPointSample_Sample.htm) | Demonstrates creating construction point by different ways |

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |