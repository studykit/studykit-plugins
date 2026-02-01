# Point2D.x Property

Parent Object: [Point2D](Point2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Point2D.h>

## Description

Gets and sets the X coordinate of the point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"point2D\_var" is a variable referencing a Point2D object. |

"point2D\_var" is a variable referencing a Point2D object. ```` ``` #include <Core/Geometry/Point2D.h>  // Get the value of the property. double propertyValue = point2D_var->x();  // Set the value of the property, where value_var is a double. bool returnValue = point2D_var->x(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |