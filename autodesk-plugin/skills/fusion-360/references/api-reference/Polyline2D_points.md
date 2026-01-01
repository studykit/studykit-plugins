# Polyline2D.points Property

Parent Object: [Polyline2D](Polyline2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Polyline2D.h>

## Description

Gets and sets the points that define the coordinates of the polyline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polyline2D\_var" is a variable referencing a Polyline2D object. |

"polyline2D\_var" is a variable referencing a Polyline2D object. ```` ``` #include <Core/Geometry/Polyline2D.h>  // Get the value of the property. std::vector<Ptr<Point2D>> propertyValue = polyline2D_var->points();  // Set the value of the property, where value_var is a Point2D. bool returnValue = polyline2D_var->points(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Point2D](Point2D.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |