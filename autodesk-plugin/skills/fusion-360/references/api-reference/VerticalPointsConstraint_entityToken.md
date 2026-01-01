# VerticalPointsConstraint.entityToken Property

Parent Object: [VerticalPointsConstraint](VerticalPointsConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/VerticalPointsConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"verticalPointsConstraint\_var" is a variable referencing a VerticalPointsConstraint object.  ```` ``` # Get the value of the property. propertyValue = verticalPointsConstraint_var.entityToken ``` ```` |

"verticalPointsConstraint\_var" is a variable referencing a VerticalPointsConstraint object. ```` ``` #include <Fusion/Sketch/VerticalPointsConstraint.h>  // Get the value of the property. string propertyValue = verticalPointsConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |