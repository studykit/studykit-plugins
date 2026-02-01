# Point3D.z Property

Parent Object: [Point3D](Point3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Point3D.h>

## Description

Gets and sets the Z coordinate of the point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"point3D\_var" is a variable referencing a Point3D object. |

"point3D\_var" is a variable referencing a Point3D object. ```` ``` #include <Core/Geometry/Point3D.h>  // Get the value of the property. double propertyValue = point3D_var->z();  // Set the value of the property, where value_var is a double. bool returnValue = point3D_var->z(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |