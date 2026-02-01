# HorizontalConstraint.line Property

Parent Object: [HorizontalConstraint](HorizontalConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/HorizontalConstraint.h>

## Description

Returns the line being constrained.

## Syntax

* [Python](#Python)
* [C++](#C++)

"horizontalConstraint\_var" is a variable referencing a HorizontalConstraint object. |

"horizontalConstraint\_var" is a variable referencing a HorizontalConstraint object. ```` ``` #include <Fusion/Sketch/HorizontalConstraint.h>  // Get the value of the property. Ptr<SketchLine> propertyValue = horizontalConstraint_var->line(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchLine](SketchLine.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |