# Plane.isValid Property

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plane\_var" is a variable referencing a Plane object. |

"plane\_var" is a variable referencing a Plane object. ```` ``` #include <Core/Geometry/Plane.h>  // Get the value of the property. boolean propertyValue = plane_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |