# ParallelConstraint.parentSketch Property

Parent Object: [ParallelConstraint](ParallelConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ParallelConstraint.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parallelConstraint\_var" is a variable referencing a ParallelConstraint object. |

"parallelConstraint\_var" is a variable referencing a ParallelConstraint object. ```` ``` #include <Fusion/Sketch/ParallelConstraint.h>  // Get the value of the property. Ptr<Sketch> propertyValue = parallelConstraint_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |