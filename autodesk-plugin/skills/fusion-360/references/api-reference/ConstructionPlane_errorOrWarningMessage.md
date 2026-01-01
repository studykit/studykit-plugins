# ConstructionPlane.errorOrWarningMessage Property

Parent Object: [ConstructionPlane](ConstructionPlane.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlane.h>

## Description

Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. |

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. ```` ``` #include <Fusion/Construction/ConstructionPlane.h>  // Get the value of the property. string propertyValue = constructionPlane_var->errorOrWarningMessage(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Plane API Sample](ConstructionPlaneSample_Sample.htm) | Demonstrates creating construction plane by different ways. |

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |