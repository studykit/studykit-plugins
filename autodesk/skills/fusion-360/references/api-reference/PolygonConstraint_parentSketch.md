# PolygonConstraint.parentSketch Property

Parent Object: [PolygonConstraint](PolygonConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PolygonConstraint.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polygonConstraint\_var" is a variable referencing a PolygonConstraint object. |

"polygonConstraint\_var" is a variable referencing a PolygonConstraint object. ```` ``` #include <Fusion/Sketch/PolygonConstraint.h>  // Get the value of the property. Ptr<Sketch> propertyValue = polygonConstraint_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |