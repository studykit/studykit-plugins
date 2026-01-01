# ConcentricConstraint.entityToken Property

Parent Object: [ConcentricConstraint](ConcentricConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ConcentricConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"concentricConstraint\_var" is a variable referencing a ConcentricConstraint object.  ```` ``` # Get the value of the property. propertyValue = concentricConstraint_var.entityToken ``` ```` |

"concentricConstraint\_var" is a variable referencing a ConcentricConstraint object. ```` ``` #include <Fusion/Sketch/ConcentricConstraint.h>  // Get the value of the property. string propertyValue = concentricConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |