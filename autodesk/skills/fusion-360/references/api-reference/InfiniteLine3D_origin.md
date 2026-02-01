# InfiniteLine3D.origin Property

Parent Object: [InfiniteLine3D](InfiniteLine3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/InfiniteLine3D.h>

## Description

Gets and sets the origin point of the line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"infiniteLine3D\_var" is a variable referencing an InfiniteLine3D object. |

"infiniteLine3D\_var" is a variable referencing an InfiniteLine3D object. ```` ``` #include <Core/Geometry/InfiniteLine3D.h>  // Get the value of the property. Ptr<Point3D> propertyValue = infiniteLine3D_var->origin();  // Set the value of the property, where value_var is a Point3D. bool returnValue = infiniteLine3D_var->origin(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |