# HorizontalPointsConstraint.entityToken Property

Parent Object: [HorizontalPointsConstraint](HorizontalPointsConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/HorizontalPointsConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"horizontalPointsConstraint\_var" is a variable referencing a HorizontalPointsConstraint object.  ```` ``` # Get the value of the property. propertyValue = horizontalPointsConstraint_var.entityToken ``` ```` |

"horizontalPointsConstraint\_var" is a variable referencing a HorizontalPointsConstraint object. ```` ``` #include <Fusion/Sketch/HorizontalPointsConstraint.h>  // Get the value of the property. string propertyValue = horizontalPointsConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |