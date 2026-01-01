# LineOnPlanarSurfaceConstraint.entityToken Property

Parent Object: [LineOnPlanarSurfaceConstraint](LineOnPlanarSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/LineOnPlanarSurfaceConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"lineOnPlanarSurfaceConstraint\_var" is a variable referencing a LineOnPlanarSurfaceConstraint object.  ```` ``` # Get the value of the property. propertyValue = lineOnPlanarSurfaceConstraint_var.entityToken ``` ```` |

"lineOnPlanarSurfaceConstraint\_var" is a variable referencing a LineOnPlanarSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/LineOnPlanarSurfaceConstraint.h>  // Get the value of the property. string propertyValue = lineOnPlanarSurfaceConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |