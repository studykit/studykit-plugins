# OffsetConstraintInput.curves Property

Parent Object: [OffsetConstraintInput](OffsetConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/OffsetConstraintInput.h>

## Description

Gets and sets an array of SketchCurve objects that defines the connected curves that will be offset. The Sketch.FindConnectedCurves method is a convenient way to get this set of curves.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetConstraintInput\_var" is a variable referencing an OffsetConstraintInput object. |

"offsetConstraintInput\_var" is a variable referencing an OffsetConstraintInput object. ```` ``` #include <Fusion/Sketch/OffsetConstraintInput.h>  // Get the value of the property. std::vector<Ptr<SketchCurve>> propertyValue = offsetConstraintInput_var->curves();  // Set the value of the property, where value_var is a SketchCurve. bool returnValue = offsetConstraintInput_var->curves(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [SketchCurve](SketchCurve.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |