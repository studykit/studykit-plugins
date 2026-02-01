# ChamferEdgeSets.isValid Property

Parent Object: [ChamferEdgeSets](ChamferEdgeSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferEdgeSets.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferEdgeSets\_var" is a variable referencing a ChamferEdgeSets object. |

"chamferEdgeSets\_var" is a variable referencing a ChamferEdgeSets object. ```` ``` #include <Fusion/Features/ChamferEdgeSets.h>  // Get the value of the property. boolean propertyValue = chamferEdgeSets_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |