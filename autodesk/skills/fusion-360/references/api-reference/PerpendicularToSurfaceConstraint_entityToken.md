# PerpendicularToSurfaceConstraint.entityToken Property

Parent Object: [PerpendicularToSurfaceConstraint](PerpendicularToSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PerpendicularToSurfaceConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"perpendicularToSurfaceConstraint\_var" is a variable referencing a PerpendicularToSurfaceConstraint object.  ```` ``` # Get the value of the property. propertyValue = perpendicularToSurfaceConstraint_var.entityToken ``` ```` |

"perpendicularToSurfaceConstraint\_var" is a variable referencing a PerpendicularToSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/PerpendicularToSurfaceConstraint.h>  // Get the value of the property. string propertyValue = perpendicularToSurfaceConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |