# CoincidentToSurfaceConstraint.entityToken Property

Parent Object: [CoincidentToSurfaceConstraint](CoincidentToSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CoincidentToSurfaceConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coincidentToSurfaceConstraint\_var" is a variable referencing a CoincidentToSurfaceConstraint object.  ```` ``` # Get the value of the property. propertyValue = coincidentToSurfaceConstraint_var.entityToken ``` ```` |

"coincidentToSurfaceConstraint\_var" is a variable referencing a CoincidentToSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/CoincidentToSurfaceConstraint.h>  // Get the value of the property. string propertyValue = coincidentToSurfaceConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |