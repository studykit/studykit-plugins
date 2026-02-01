# Polyline3D.points Property

Parent Object: [Polyline3D](Polyline3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Polyline3D.h>

## Description

Gets and sets the points that define the coordinates of the polyline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polyline3D\_var" is a variable referencing a Polyline3D object. |

"polyline3D\_var" is a variable referencing a Polyline3D object. ```` ``` #include <Core/Geometry/Polyline3D.h>  // Get the value of the property. std::vector<Ptr<Point3D>> propertyValue = polyline3D_var->points();  // Set the value of the property, where value_var is a Point3D. bool returnValue = polyline3D_var->points(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Point3D](Point3D.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |