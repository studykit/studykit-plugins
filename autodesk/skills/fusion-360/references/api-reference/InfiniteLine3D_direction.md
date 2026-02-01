# InfiniteLine3D.direction Property

Parent Object: [InfiniteLine3D](InfiniteLine3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/InfiniteLine3D.h>

## Description

Gets and sets the direction of the line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"infiniteLine3D\_var" is a variable referencing an InfiniteLine3D object. |

"infiniteLine3D\_var" is a variable referencing an InfiniteLine3D object. ```` ``` #include <Core/Geometry/InfiniteLine3D.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = infiniteLine3D_var->direction();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = infiniteLine3D_var->direction(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |