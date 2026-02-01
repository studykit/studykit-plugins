# VerticalConstraint.entityToken Property

Parent Object: [VerticalConstraint](VerticalConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/VerticalConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"verticalConstraint\_var" is a variable referencing a VerticalConstraint object.  ```` ``` # Get the value of the property. propertyValue = verticalConstraint_var.entityToken ``` ```` |

"verticalConstraint\_var" is a variable referencing a VerticalConstraint object. ```` ``` #include <Fusion/Sketch/VerticalConstraint.h>  // Get the value of the property. string propertyValue = verticalConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |