# Matrix3D.objectType Property

Parent Object: [Matrix3D](Matrix3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix3D.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix3D\_var" is a variable referencing a Matrix3D object.  ```` ``` # Get the value of the property. propertyValue = matrix3D_var.objectType ``` ```` |

"matrix3D\_var" is a variable referencing a Matrix3D object. ```` ``` #include <Core/Geometry/Matrix3D.h>  // Get the value of the property. string propertyValue = matrix3D_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |