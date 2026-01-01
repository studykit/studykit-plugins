# NurbsSurface.isValid Property

Parent Object: [NurbsSurface](NurbsSurface.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsSurface.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsSurface\_var" is a variable referencing a NurbsSurface object. |

"nurbsSurface\_var" is a variable referencing a NurbsSurface object. ```` ``` #include <Core/Geometry/NurbsSurface.h>  // Get the value of the property. boolean propertyValue = nurbsSurface_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |