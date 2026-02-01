# Sphere.isValid Property

Parent Object: [Sphere](Sphere.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Sphere.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sphere\_var" is a variable referencing a Sphere object. |

"sphere\_var" is a variable referencing a Sphere object. ```` ``` #include <Core/Geometry/Sphere.h>  // Get the value of the property. boolean propertyValue = sphere_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |