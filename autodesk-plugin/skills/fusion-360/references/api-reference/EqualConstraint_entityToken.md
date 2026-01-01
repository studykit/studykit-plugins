# EqualConstraint.entityToken Property

Parent Object: [EqualConstraint](EqualConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/EqualConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"equalConstraint\_var" is a variable referencing an EqualConstraint object.  ```` ``` # Get the value of the property. propertyValue = equalConstraint_var.entityToken ``` ```` |

"equalConstraint\_var" is a variable referencing an EqualConstraint object. ```` ``` #include <Fusion/Sketch/EqualConstraint.h>  // Get the value of the property. string propertyValue = equalConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |