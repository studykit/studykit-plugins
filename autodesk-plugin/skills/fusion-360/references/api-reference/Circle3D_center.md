# Circle3D.center Property

Parent Object: [Circle3D](Circle3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Circle3D.h>

## Description

Gets and sets the center position of the circle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circle3D\_var" is a variable referencing a Circle3D object. |

"circle3D\_var" is a variable referencing a Circle3D object. ```` ``` #include <Core/Geometry/Circle3D.h>  // Get the value of the property. Ptr<Point3D> propertyValue = circle3D_var->center();  // Set the value of the property, where value_var is a Point3D. bool returnValue = circle3D_var->center(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |