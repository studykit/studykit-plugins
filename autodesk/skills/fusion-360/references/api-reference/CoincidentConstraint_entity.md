# CoincidentConstraint.entity Property

Parent Object: [CoincidentConstraint](CoincidentConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CoincidentConstraint.h>

## Description

The sketch curve or point the point is constrained to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coincidentConstraint\_var" is a variable referencing a CoincidentConstraint object. |

"coincidentConstraint\_var" is a variable referencing a CoincidentConstraint object. ```` ``` #include <Fusion/Sketch/CoincidentConstraint.h>  // Get the value of the property. Ptr<SketchEntity> propertyValue = coincidentConstraint_var->entity(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchEntity](SketchEntity.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |