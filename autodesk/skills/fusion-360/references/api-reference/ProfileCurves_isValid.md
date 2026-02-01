# ProfileCurves.isValid Property

Parent Object: [ProfileCurves](ProfileCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileCurves.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileCurves\_var" is a variable referencing a ProfileCurves object. |

"profileCurves\_var" is a variable referencing a ProfileCurves object. ```` ``` #include <Fusion/Sketch/ProfileCurves.h>  // Get the value of the property. boolean propertyValue = profileCurves_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |