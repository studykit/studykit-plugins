# Line3D.startPoint Property

Parent Object: [Line3D](Line3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Line3D.h>

## Description

Gets and sets the start point of the line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"line3D\_var" is a variable referencing a Line3D object. |

"line3D\_var" is a variable referencing a Line3D object. ```` ``` #include <Core/Geometry/Line3D.h>  // Get the value of the property. Ptr<Point3D> propertyValue = line3D_var->startPoint();  // Set the value of the property, where value_var is a Point3D. bool returnValue = line3D_var->startPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |