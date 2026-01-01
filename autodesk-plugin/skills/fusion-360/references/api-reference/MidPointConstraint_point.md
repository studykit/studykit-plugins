# MidPointConstraint.point Property

Parent Object: [MidPointConstraint](MidPointConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/MidPointConstraint.h>

## Description

Returns the sketch point being constrained.

## Syntax

* [Python](#Python)
* [C++](#C++)

"midPointConstraint\_var" is a variable referencing a MidPointConstraint object. |

"midPointConstraint\_var" is a variable referencing a MidPointConstraint object. ```` ``` #include <Fusion/Sketch/MidPointConstraint.h>  // Get the value of the property. Ptr<SketchPoint> propertyValue = midPointConstraint_var->point(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchPoint](SketchPoint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |