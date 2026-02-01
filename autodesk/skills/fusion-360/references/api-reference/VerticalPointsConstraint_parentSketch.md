# VerticalPointsConstraint.parentSketch Property

Parent Object: [VerticalPointsConstraint](VerticalPointsConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/VerticalPointsConstraint.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"verticalPointsConstraint\_var" is a variable referencing a VerticalPointsConstraint object. |

"verticalPointsConstraint\_var" is a variable referencing a VerticalPointsConstraint object. ```` ``` #include <Fusion/Sketch/VerticalPointsConstraint.h>  // Get the value of the property. Ptr<Sketch> propertyValue = verticalPointsConstraint_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |