# HorizontalPointsConstraint.parentSketch Property

Parent Object: [HorizontalPointsConstraint](HorizontalPointsConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/HorizontalPointsConstraint.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"horizontalPointsConstraint\_var" is a variable referencing a HorizontalPointsConstraint object. |

"horizontalPointsConstraint\_var" is a variable referencing a HorizontalPointsConstraint object. ```` ``` #include <Fusion/Sketch/HorizontalPointsConstraint.h>  // Get the value of the property. Ptr<Sketch> propertyValue = horizontalPointsConstraint_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |