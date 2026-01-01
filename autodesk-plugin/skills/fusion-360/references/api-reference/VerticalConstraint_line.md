# VerticalConstraint.line Property

Parent Object: [VerticalConstraint](VerticalConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/VerticalConstraint.h>

## Description

Returns the line being constrained.

## Syntax

* [Python](#Python)
* [C++](#C++)

"verticalConstraint\_var" is a variable referencing a VerticalConstraint object. |

"verticalConstraint\_var" is a variable referencing a VerticalConstraint object. ```` ``` #include <Fusion/Sketch/VerticalConstraint.h>  // Get the value of the property. Ptr<SketchLine> propertyValue = verticalConstraint_var->line(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchLine](SketchLine.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |