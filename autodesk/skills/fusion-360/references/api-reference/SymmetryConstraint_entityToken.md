# SymmetryConstraint.entityToken Property

Parent Object: [SymmetryConstraint](SymmetryConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SymmetryConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"symmetryConstraint\_var" is a variable referencing a SymmetryConstraint object.  ```` ``` # Get the value of the property. propertyValue = symmetryConstraint_var.entityToken ``` ```` |

"symmetryConstraint\_var" is a variable referencing a SymmetryConstraint object. ```` ``` #include <Fusion/Sketch/SymmetryConstraint.h>  // Get the value of the property. string propertyValue = symmetryConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |