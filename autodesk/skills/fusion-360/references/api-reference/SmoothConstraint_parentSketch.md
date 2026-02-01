# SmoothConstraint.parentSketch Property

Parent Object: [SmoothConstraint](SmoothConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SmoothConstraint.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"smoothConstraint\_var" is a variable referencing a SmoothConstraint object. |

"smoothConstraint\_var" is a variable referencing a SmoothConstraint object. ```` ``` #include <Fusion/Sketch/SmoothConstraint.h>  // Get the value of the property. Ptr<Sketch> propertyValue = smoothConstraint_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |