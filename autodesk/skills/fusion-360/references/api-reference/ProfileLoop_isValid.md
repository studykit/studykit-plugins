# ProfileLoop.isValid Property

Parent Object: [ProfileLoop](ProfileLoop.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileLoop.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileLoop\_var" is a variable referencing a ProfileLoop object. |

"profileLoop\_var" is a variable referencing a ProfileLoop object. ```` ``` #include <Fusion/Sketch/ProfileLoop.h>  // Get the value of the property. boolean propertyValue = profileLoop_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |