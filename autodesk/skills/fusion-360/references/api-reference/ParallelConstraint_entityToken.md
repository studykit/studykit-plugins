# ParallelConstraint.entityToken Property

Parent Object: [ParallelConstraint](ParallelConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ParallelConstraint.h>

## Description

Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parallelConstraint\_var" is a variable referencing a ParallelConstraint object.  ```` ``` # Get the value of the property. propertyValue = parallelConstraint_var.entityToken ``` ```` |

"parallelConstraint\_var" is a variable referencing a ParallelConstraint object. ```` ``` #include <Fusion/Sketch/ParallelConstraint.h>  // Get the value of the property. string propertyValue = parallelConstraint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |