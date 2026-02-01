# GeometricConstraint.entityToken Property

Parent Object: [GeometricConstraint](GeometricConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraint\_var" is a variable referencing a GeometricConstraint object.  ```` ``` # Get the value of the property. propertyValue = geometricConstraint_var.entityToken ``` ```` |

"geometricConstraint\_var" is a variable referencing a GeometricConstraint object. ```` ``` #include <Fusion/Sketch/GeometricConstraint.h>  // Get the value of the property. string propertyValue = geometricConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |