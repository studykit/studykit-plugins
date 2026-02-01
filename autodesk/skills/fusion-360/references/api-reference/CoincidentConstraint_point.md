# CoincidentConstraint.point Property

Parent Object: [CoincidentConstraint](CoincidentConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CoincidentConstraint.h>

## Description

Returns the sketch point that is constrained.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coincidentConstraint\_var" is a variable referencing a CoincidentConstraint object. |

"coincidentConstraint\_var" is a variable referencing a CoincidentConstraint object. ```` ``` #include <Fusion/Sketch/CoincidentConstraint.h>  // Get the value of the property. Ptr<SketchPoint> propertyValue = coincidentConstraint_var->point(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchPoint](SketchPoint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |