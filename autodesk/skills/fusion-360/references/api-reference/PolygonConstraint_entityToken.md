# PolygonConstraint.entityToken Property

Parent Object: [PolygonConstraint](PolygonConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PolygonConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polygonConstraint\_var" is a variable referencing a PolygonConstraint object.  ```` ``` # Get the value of the property. propertyValue = polygonConstraint_var.entityToken ``` ```` |

"polygonConstraint\_var" is a variable referencing a PolygonConstraint object. ```` ``` #include <Fusion/Sketch/PolygonConstraint.h>  // Get the value of the property. string propertyValue = polygonConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |