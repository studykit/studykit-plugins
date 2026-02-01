# PerpendicularConstraint.entityToken Property

Parent Object: [PerpendicularConstraint](PerpendicularConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PerpendicularConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"perpendicularConstraint\_var" is a variable referencing a PerpendicularConstraint object.  ```` ``` # Get the value of the property. propertyValue = perpendicularConstraint_var.entityToken ``` ```` |

"perpendicularConstraint\_var" is a variable referencing a PerpendicularConstraint object. ```` ``` #include <Fusion/Sketch/PerpendicularConstraint.h>  // Get the value of the property. string propertyValue = perpendicularConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |