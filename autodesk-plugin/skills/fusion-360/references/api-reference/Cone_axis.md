# Cone.axis Property

Parent Object: [Cone](Cone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cone.h>

## Description

Gets and sets the center axis (along the length) of the cone that defines its normal direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cone\_var" is a variable referencing a Cone object. |

"cone\_var" is a variable referencing a Cone object. ```` ``` #include <Core/Geometry/Cone.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = cone_var->axis();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = cone_var->axis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |