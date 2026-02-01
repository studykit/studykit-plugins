# ChamferFeatures.isValid Property

Parent Object: [ChamferFeatures](ChamferFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatures\_var" is a variable referencing a ChamferFeatures object. |

"chamferFeatures\_var" is a variable referencing a ChamferFeatures object. ```` ``` #include <Fusion/Features/ChamferFeatures.h>  // Get the value of the property. boolean propertyValue = chamferFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |