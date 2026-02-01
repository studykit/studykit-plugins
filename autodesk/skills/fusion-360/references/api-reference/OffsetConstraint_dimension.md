# OffsetConstraint.dimension Property

Parent Object: [OffsetConstraint](OffsetConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/OffsetConstraint.h>

## Description

Returns the dimension controlling the offset distance. This can return null in the case where the dimension has been deleted. To change the offset distance you can use the parameter property of the returned dimension to get the parameter that controls the value and use properties on the parameter to change the value. This can return either a SketchOffsetCurvesDimension or a SketchOffsetDimension. A SketchOffsetCurvesDimension is created automatically when curves are offset but if it is deleted the offset can also be controlled by a SketchOffsetDimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetConstraint\_var" is a variable referencing an OffsetConstraint object. |

"offsetConstraint\_var" is a variable referencing an OffsetConstraint object. ```` ``` #include <Fusion/Sketch/OffsetConstraint.h>  // Get the value of the property. Ptr<SketchDimension> propertyValue = offsetConstraint_var->dimension(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchDimension](SketchDimension.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |