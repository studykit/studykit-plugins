# Line2D.startPoint Property

Parent Object: [Line2D](Line2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Line2D.h>

## Description

Gets and sets the start point of the line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"line2D\_var" is a variable referencing a Line2D object. |

"line2D\_var" is a variable referencing a Line2D object. ```` ``` #include <Core/Geometry/Line2D.h>  // Get the value of the property. Ptr<Point2D> propertyValue = line2D_var->startPoint();  // Set the value of the property, where value_var is a Point2D. bool returnValue = line2D_var->startPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point2D](Point2D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |