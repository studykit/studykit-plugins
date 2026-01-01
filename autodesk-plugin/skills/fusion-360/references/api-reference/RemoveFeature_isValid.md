# RemoveFeature.isValid Property

Parent Object: [RemoveFeature](RemoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RemoveFeature.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"removeFeature\_var" is a variable referencing a RemoveFeature object. |

"removeFeature\_var" is a variable referencing a RemoveFeature object. ```` ``` #include <Fusion/Features/RemoveFeature.h>  // Get the value of the property. boolean propertyValue = removeFeature_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |