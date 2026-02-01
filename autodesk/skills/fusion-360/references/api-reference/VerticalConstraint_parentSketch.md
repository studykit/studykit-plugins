# VerticalConstraint.parentSketch Property

Parent Object: [VerticalConstraint](VerticalConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/VerticalConstraint.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"verticalConstraint\_var" is a variable referencing a VerticalConstraint object. |

"verticalConstraint\_var" is a variable referencing a VerticalConstraint object. ```` ``` #include <Fusion/Sketch/VerticalConstraint.h>  // Get the value of the property. Ptr<Sketch> propertyValue = verticalConstraint_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |