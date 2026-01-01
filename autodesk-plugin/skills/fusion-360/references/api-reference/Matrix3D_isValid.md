# Matrix3D.isValid Property

Parent Object: [Matrix3D](Matrix3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix3D.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix3D\_var" is a variable referencing a Matrix3D object. |

"matrix3D\_var" is a variable referencing a Matrix3D object. ```` ``` #include <Core/Geometry/Matrix3D.h>  // Get the value of the property. boolean propertyValue = matrix3D_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |