# CoilFeature.name Property

Parent Object: [CoilFeature](CoilFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeature.h>

## Description

Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeature\_var" is a variable referencing a CoilFeature object. |

"coilFeature\_var" is a variable referencing a CoilFeature object. ```` ``` #include <Fusion/Features/CoilFeature.h>  // Get the value of the property. string propertyValue = coilFeature_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = coilFeature_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |