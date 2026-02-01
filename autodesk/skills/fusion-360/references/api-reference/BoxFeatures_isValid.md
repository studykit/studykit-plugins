# BoxFeatures.isValid Property

Parent Object: [BoxFeatures](BoxFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoxFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boxFeatures\_var" is a variable referencing a BoxFeatures object. |

"boxFeatures\_var" is a variable referencing a BoxFeatures object. ```` ``` #include <Fusion/Features/BoxFeatures.h>  // Get the value of the property. boolean propertyValue = boxFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |