# CoilFeature.errorOrWarningMessage Property

Parent Object: [CoilFeature](CoilFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeature.h>

## Description

Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeature\_var" is a variable referencing a CoilFeature object. |

"coilFeature\_var" is a variable referencing a CoilFeature object. ```` ``` #include <Fusion/Features/CoilFeature.h>  // Get the value of the property. string propertyValue = coilFeature_var->errorOrWarningMessage(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |