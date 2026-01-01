# PerpendicularConstraint.parentSketch Property

Parent Object: [PerpendicularConstraint](PerpendicularConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PerpendicularConstraint.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"perpendicularConstraint\_var" is a variable referencing a PerpendicularConstraint object. |

"perpendicularConstraint\_var" is a variable referencing a PerpendicularConstraint object. ```` ``` #include <Fusion/Sketch/PerpendicularConstraint.h>  // Get the value of the property. Ptr<Sketch> propertyValue = perpendicularConstraint_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |