# Cone.radius Property

Parent Object: [Cone](Cone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cone.h>

## Description

Gets and sets the radius of the cone.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cone\_var" is a variable referencing a Cone object. |

"cone\_var" is a variable referencing a Cone object. ```` ``` #include <Core/Geometry/Cone.h>  // Get the value of the property. double propertyValue = cone_var->radius();  // Set the value of the property, where value_var is a double. bool returnValue = cone_var->radius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |