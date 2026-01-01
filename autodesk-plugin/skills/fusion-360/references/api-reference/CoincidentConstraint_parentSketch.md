# CoincidentConstraint.parentSketch Property

Parent Object: [CoincidentConstraint](CoincidentConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CoincidentConstraint.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coincidentConstraint\_var" is a variable referencing a CoincidentConstraint object. |

"coincidentConstraint\_var" is a variable referencing a CoincidentConstraint object. ```` ``` #include <Fusion/Sketch/CoincidentConstraint.h>  // Get the value of the property. Ptr<Sketch> propertyValue = coincidentConstraint_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |