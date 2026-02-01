# Vector3D.x Property

Parent Object: [Vector3D](Vector3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Vector3D.h>

## Description

The x value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"vector3D\_var" is a variable referencing a Vector3D object. |

"vector3D\_var" is a variable referencing a Vector3D object. ```` ``` #include <Core/Geometry/Vector3D.h>  // Get the value of the property. double propertyValue = vector3D_var->x();  // Set the value of the property, where value_var is a double. bool returnValue = vector3D_var->x(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |