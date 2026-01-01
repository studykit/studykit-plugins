# ConstructionAxis.healthState Property

Parent Object: [ConstructionAxis](ConstructionAxis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxis.h>

## Description

Returns the current health state of this construction axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxis\_var" is a variable referencing a ConstructionAxis object. |

"constructionAxis\_var" is a variable referencing a ConstructionAxis object. ```` ``` #include <Fusion/Construction/ConstructionAxis.h>  // Get the value of the property. FeatureHealthStates propertyValue = constructionAxis_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Axis API Sample](ConstructionAxisSample_Sample.htm) | Demonstrates creating construction axis in various ways. |

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |