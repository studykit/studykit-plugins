# ChamferEdgeSet.isValid Property

Parent Object: [ChamferEdgeSet](ChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferEdgeSet.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferEdgeSet\_var" is a variable referencing a ChamferEdgeSet object. |

"chamferEdgeSet\_var" is a variable referencing a ChamferEdgeSet object. ```` ``` #include <Fusion/Features/ChamferEdgeSet.h>  // Get the value of the property. boolean propertyValue = chamferEdgeSet_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |