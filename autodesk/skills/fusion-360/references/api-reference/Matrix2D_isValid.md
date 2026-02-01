# Matrix2D.isValid Property

Parent Object: [Matrix2D](Matrix2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix2D.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix2D\_var" is a variable referencing a Matrix2D object. |

"matrix2D\_var" is a variable referencing a Matrix2D object. ```` ``` #include <Core/Geometry/Matrix2D.h>  // Get the value of the property. boolean propertyValue = matrix2D_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |