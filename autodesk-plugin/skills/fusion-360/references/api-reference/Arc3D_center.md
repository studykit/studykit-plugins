# Arc3D.center Property

Parent Object: [Arc3D](Arc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc3D.h>

## Description

Gets and sets the center position of the arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arc3D\_var" is a variable referencing an Arc3D object. |

"arc3D\_var" is a variable referencing an Arc3D object. ```` ``` #include <Core/Geometry/Arc3D.h>  // Get the value of the property. Ptr<Point3D> propertyValue = arc3D_var->center();  // Set the value of the property, where value_var is a Point3D. bool returnValue = arc3D_var->center(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |