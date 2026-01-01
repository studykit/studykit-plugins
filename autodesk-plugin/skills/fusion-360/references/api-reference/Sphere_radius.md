# Sphere.radius Property

Parent Object: [Sphere](Sphere.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Sphere.h>

## Description

Gets and sets the radius of the sphere.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sphere\_var" is a variable referencing a Sphere object. |

"sphere\_var" is a variable referencing a Sphere object. ```` ``` #include <Core/Geometry/Sphere.h>  // Get the value of the property. double propertyValue = sphere_var->radius();  // Set the value of the property, where value_var is a double. bool returnValue = sphere_var->radius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |