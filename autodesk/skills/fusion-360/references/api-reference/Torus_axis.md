# Torus.axis Property

Parent Object: [Torus](Torus.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Torus.h>

## Description

Gets and sets the center axis of the torus.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torus\_var" is a variable referencing a Torus object. |

"torus\_var" is a variable referencing a Torus object. ```` ``` #include <Core/Geometry/Torus.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = torus_var->axis();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = torus_var->axis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |