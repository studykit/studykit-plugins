# MidPointConstraint.entityToken Property

Parent Object: [MidPointConstraint](MidPointConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/MidPointConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"midPointConstraint\_var" is a variable referencing a MidPointConstraint object.  ```` ``` # Get the value of the property. propertyValue = midPointConstraint_var.entityToken ``` ```` |

"midPointConstraint\_var" is a variable referencing a MidPointConstraint object. ```` ``` #include <Fusion/Sketch/MidPointConstraint.h>  // Get the value of the property. string propertyValue = midPointConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |