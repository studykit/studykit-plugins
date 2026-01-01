# CombineFeatures.isValid Property

Parent Object: [CombineFeatures](CombineFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeatures\_var" is a variable referencing a CombineFeatures object. |

"combineFeatures\_var" is a variable referencing a CombineFeatures object. ```` ``` #include <Fusion/Features/CombineFeatures.h>  // Get the value of the property. boolean propertyValue = combineFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |