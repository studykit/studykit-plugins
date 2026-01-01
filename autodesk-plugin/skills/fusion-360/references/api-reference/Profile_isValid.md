# Profile.isValid Property

Parent Object: [Profile](Profile.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profile.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profile\_var" is a variable referencing a Profile object. |

"profile\_var" is a variable referencing a Profile object. ```` ``` #include <Fusion/Sketch/Profile.h>  // Get the value of the property. boolean propertyValue = profile_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |