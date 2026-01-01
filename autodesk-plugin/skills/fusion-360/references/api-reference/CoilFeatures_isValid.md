# CoilFeatures.isValid Property

Parent Object: [CoilFeatures](CoilFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeatures\_var" is a variable referencing a CoilFeatures object. |

"coilFeatures\_var" is a variable referencing a CoilFeatures object. ```` ``` #include <Fusion/Features/CoilFeatures.h>  // Get the value of the property. boolean propertyValue = coilFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |