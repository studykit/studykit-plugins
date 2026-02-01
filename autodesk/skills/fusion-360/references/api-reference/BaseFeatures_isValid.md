# BaseFeatures.isValid Property

Parent Object: [BaseFeatures](BaseFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BaseFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseFeatures\_var" is a variable referencing a BaseFeatures object. |

"baseFeatures\_var" is a variable referencing a BaseFeatures object. ```` ``` #include <Fusion/Features/BaseFeatures.h>  // Get the value of the property. boolean propertyValue = baseFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |