# Circle2D.radius Property

Parent Object: [Circle2D](Circle2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Circle2D.h>

## Description

Gets and sets the radius of the circle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circle2D\_var" is a variable referencing a Circle2D object. |

"circle2D\_var" is a variable referencing a Circle2D object. ```` ``` #include <Core/Geometry/Circle2D.h>  // Get the value of the property. double propertyValue = circle2D_var->radius();  // Set the value of the property, where value_var is a double. bool returnValue = circle2D_var->radius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |