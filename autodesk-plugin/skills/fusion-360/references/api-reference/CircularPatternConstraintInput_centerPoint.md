# CircularPatternConstraintInput.centerPoint Property

Parent Object: [CircularPatternConstraintInput](CircularPatternConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraintInput.h>

## Description

Gets and sets the sketch point that defines the center of the pattern.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternConstraintInput\_var" is a variable referencing a CircularPatternConstraintInput object. |

"circularPatternConstraintInput\_var" is a variable referencing a CircularPatternConstraintInput object. ```` ``` #include <Fusion/Sketch/CircularPatternConstraintInput.h>  // Get the value of the property. Ptr<SketchPoint> propertyValue = circularPatternConstraintInput_var->centerPoint();  // Set the value of the property, where value_var is a SketchPoint. bool returnValue = circularPatternConstraintInput_var->centerPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SketchPoint](SketchPoint.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |