# OffsetFeatures.isValid Property

Parent Object: [OffsetFeatures](OffsetFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeatures\_var" is a variable referencing an OffsetFeatures object. |

"offsetFeatures\_var" is a variable referencing an OffsetFeatures object. ```` ``` #include <Fusion/Features/OffsetFeatures.h>  // Get the value of the property. boolean propertyValue = offsetFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |