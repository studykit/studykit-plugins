# Cylinder.axis Property

Parent Object: [Cylinder](Cylinder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cylinder.h>

## Description

The center axis (along the length) of the cylinder that defines its normal direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinder\_var" is a variable referencing a Cylinder object. |

"cylinder\_var" is a variable referencing a Cylinder object. ```` ``` #include <Core/Geometry/Cylinder.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = cylinder_var->axis();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = cylinder_var->axis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |