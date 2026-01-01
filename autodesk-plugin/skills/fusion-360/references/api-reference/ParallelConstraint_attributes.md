# ParallelConstraint.attributes Property

Parent Object: [ParallelConstraint](ParallelConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ParallelConstraint.h>

## Description

Returns the collection of attributes associated with this geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parallelConstraint\_var" is a variable referencing a ParallelConstraint object. |

"parallelConstraint\_var" is a variable referencing a ParallelConstraint object. ```` ``` #include <Fusion/Sketch/ParallelConstraint.h>  // Get the value of the property. Ptr<Attributes> propertyValue = parallelConstraint_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |