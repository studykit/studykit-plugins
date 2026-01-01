# BoundingBox2D.minPoint Property

Parent Object: [BoundingBox2D](BoundingBox2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox2D.h>

## Description

Gets and sets the minimum point of the box.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundingBox2D\_var" is a variable referencing a BoundingBox2D object. |

"boundingBox2D\_var" is a variable referencing a BoundingBox2D object. ```` ``` #include <Core/Geometry/BoundingBox2D.h>  // Get the value of the property. Ptr<Point2D> propertyValue = boundingBox2D_var->minPoint();  // Set the value of the property, where value_var is a Point2D. bool returnValue = boundingBox2D_var->minPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point2D](Point2D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |