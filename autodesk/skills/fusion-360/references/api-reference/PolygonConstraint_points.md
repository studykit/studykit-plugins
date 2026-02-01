# PolygonConstraint.points Property

Parent Object: [PolygonConstraint](PolygonConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PolygonConstraint.h>

## Description

Returns the sketch points that define the vertices of the polygon. The sketch lines that draw the shape of the polygon can be obtained from the points.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polygonConstraint\_var" is a variable referencing a PolygonConstraint object. |

"polygonConstraint\_var" is a variable referencing a PolygonConstraint object. ```` ``` #include <Fusion/Sketch/PolygonConstraint.h>  // Get the value of the property. std::vector<Ptr<SketchPoint>> propertyValue = polygonConstraint_var->points(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [SketchPoint](SketchPoint.htm).

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |