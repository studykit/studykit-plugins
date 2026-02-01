# OffsetConstraint.parentCurves Property

Parent Object: [OffsetConstraint](OffsetConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/OffsetConstraint.h>

## Description

Returns an array of sketch curves that are the set of parent curves. Nothing should be assumed about the order in how the curves are returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetConstraint\_var" is a variable referencing an OffsetConstraint object. |

"offsetConstraint\_var" is a variable referencing an OffsetConstraint object. ```` ``` #include <Fusion/Sketch/OffsetConstraint.h>  // Get the value of the property. std::vector<Ptr<SketchCurve>> propertyValue = offsetConstraint_var->parentCurves(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [SketchCurve](SketchCurve.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |