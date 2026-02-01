# LineParallelToPlanarSurfaceConstraint.entityToken Property

Parent Object: [LineParallelToPlanarSurfaceConstraint](LineParallelToPlanarSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/LineParallelToPlanarSurfaceConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"lineParallelToPlanarSurfaceConstraint\_var" is a variable referencing a LineParallelToPlanarSurfaceConstraint object.  ```` ``` # Get the value of the property. propertyValue = lineParallelToPlanarSurfaceConstraint_var.entityToken ``` ```` |

"lineParallelToPlanarSurfaceConstraint\_var" is a variable referencing a LineParallelToPlanarSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/LineParallelToPlanarSurfaceConstraint.h>  // Get the value of the property. string propertyValue = lineParallelToPlanarSurfaceConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |