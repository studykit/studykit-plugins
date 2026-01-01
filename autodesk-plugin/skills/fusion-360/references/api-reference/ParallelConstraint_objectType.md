# ParallelConstraint.objectType Property

Parent Object: [ParallelConstraint](ParallelConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ParallelConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parallelConstraint\_var" is a variable referencing a ParallelConstraint object.  ```` ``` # Get the value of the property. propertyValue = parallelConstraint_var.objectType ``` ```` |

"parallelConstraint\_var" is a variable referencing a ParallelConstraint object. ```` ``` #include <Fusion/Sketch/ParallelConstraint.h>  // Get the value of the property. string propertyValue = parallelConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |